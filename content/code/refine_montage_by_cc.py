from pyexpat.errors import XML_ERROR_INCORRECT_ENCODING
import numpy as np
import starfile
from scipy.spatial import KDTree
import multiprocessing
from skimage.registration._masked_phase_cross_correlation import cross_correlate_masked
import mrcfile
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
import pycistem
import numpy as np
from pathlib import Path
import utils
from skimage import transform
from scipy import optimize
import logging
from rich.logging import RichHandler
import pandas as pd
import assemble_montage_utils


FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)


def calculate_crosscorrelations(tile_data,num_proc=20):
    logger = logging.getLogger("ref_mon")

    points = np.array([(a["tile_x_offset"]/a["tile_pixel_size"],a["tile_y_offset"]/a["tile_pixel_size"]) for i,a in tile_data.iterrows()])
    kd_tree = KDTree(points)

    pairs = kd_tree.query_pairs(r=3000)
    row_pairs = [(tile_data.iloc[a[0]],tile_data.iloc[a[1]]) for a in pairs]
    logger.info(f"There are {len(points)} tiles and {len(pairs)} pairs")
    pool = multiprocessing.Pool(processes=num_proc)
    shifts = pool.map(determine_shift_by_cc, row_pairs)
    pool.close()
    pool.join()
    shifts = np.array(shifts)
    pairs=np.array(list(pairs))
    return((pairs,shifts))

def determine_shift_by_cc(doubled,diagnostic=False):
    # Given the infow of two images, calculate the refined relative shifts by crosscorrelation return
    im1, im2 = doubled
    im1["image_shift_pixel_x"] = im1["tile_x_offset"]/im1["tile_pixel_size"]
    im1["image_shift_pixel_y"] = im1["tile_y_offset"]/im1["tile_pixel_size"]
    im2["image_shift_pixel_x"] = im2["tile_x_offset"]/im2["tile_pixel_size"]
    im2["image_shift_pixel_y"] = im2["tile_y_offset"]/im2["tile_pixel_size"]

    if diagnostic:
        fig, axs = plt.subplots(4,4,figsize=(15,15))
    with mrcfile.open(im1["tile_filename"]) as mrc: 
            reference = np.copy(mrc.data[0])
    with mrcfile.open(im2["tile_filename"]) as mrc: 
            moving = np.copy(mrc.data[0])
    if diagnostic:
        axs[2][1].imshow(moving,cmap="Greys_r")
    diff = (im2['image_shift_pixel_x']-im1['image_shift_pixel_x'],im2['image_shift_pixel_y']-im1['image_shift_pixel_y'])
    tform = transform.SimilarityTransform(translation=(diff[0],diff[1])).inverse
    moving = transform.warp(moving,tform,output_shape=reference.shape)

    if diagnostic:
        print(diff)
        axs[0][0].imshow(reference,cmap="Greys_r")
        axs[0][1].imshow(moving,cmap="Greys_r")
 
    with mrcfile.open(im1["tile_mask_filename"]) as mrc: 
            reference_mask = np.copy(mrc.data[0])
            reference_mask.dtype = np.uint8
            reference_mask = reference_mask/255.0
    with mrcfile.open(im2["tile_mask_filename"]) as mrc: 
            moving_mask = np.copy(mrc.data[0])
            moving_mask.dtype = np.uint8
            moving_mask = moving_mask/255.0
    moving_mask = transform.warp(moving_mask,tform,output_shape=reference_mask.shape)
    mask =  np.minimum(reference_mask,moving_mask) > 0.9
    reference*= mask
    moving *= mask 
    if diagnostic:
        axs[0][2].imshow(reference,cmap="Greys_r")
        axs[0][3].imshow(moving,cmap="Greys_r")
    #shift = phase_cross_correlation(reference, moving,reference_mask=mask,moving_mask=mask)
    xcorr = cross_correlate_masked(moving, reference,
                                   mask, mask ,
                                   axes=tuple(range(moving.ndim)),
                                   mode='full',
                                   overlap_ratio=0.5)

    # Generalize to the average of multiple equal maxima
    maxima = np.stack(np.nonzero(xcorr == xcorr.max()), axis=1)
    center = np.mean(maxima, axis=0)
    shift = center - np.array(reference.shape) + 1
    shift = -shift
    if diagnostic:
        print(shift)
        axs[1][0].imshow(reference+moving,cmap="Greys_r")
        axs[1][1].imshow(reference+ndi.shift(moving,shift),cmap="Greys_r")
        axs[1][2].imshow(reference+ndi.shift(moving,(-shift[0],-shift[1])),cmap="Greys_r")
        axs[1][3].imshow(reference+ndi.shift(moving,(shift[0],-shift[1])),cmap="Greys_r")

        axs[2][2].imshow(xcorr)
        # Get random 10 character string
        import random
        import string
        random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        plt.savefig("diag/"+random_string+".png")
    return(np.array([(diff[0]+shift[1],
                      diff[1]+shift[0],
                     np.sum(mask),
                     xcorr.max(),
                     np.linalg.norm(shift),
                     np.sum(reference)/np.sum(moving))],
                    dtype=[('shift_x','f4'),
                           ('shift_y','f4'),
                           ('initial_area','f4'),
                           ('max_cc','f4'),
                           ('add_shift','f4'),
                           ('int_ratio','f4')]))

def pair_and_shift_quality_control(tile_data,pairs,shifts):
    points = np.array([(a["tile_x_offset"]/a["tile_pixel_size"],a["tile_y_offset"]/a["tile_pixel_size"]) for i,a in tile_data.iterrows()])
    good_shifts=shifts[(shifts["add_shift"] < 200) & (shifts["initial_area"] > 200000)]
    good_pairs=pairs[np.array((shifts["add_shift"] < 200) & (shifts["initial_area"] > 200000))[:,0]]
    tile_data["include_in_refined"] = np.array([i in good_pairs for i in range(len(points))])
    return((good_pairs,good_shifts))

def residuals(is_pixel,pairs,shifts):
    is_pixel = is_pixel.reshape(int(len(is_pixel)/2),2)
    distance = []
    for i,pair in enumerate(pairs):
        distance.append((is_pixel[pair[1]][0] - is_pixel[pair[0]][0])-shifts[i][0])
        distance.append((is_pixel[pair[1]][1] - is_pixel[pair[0]][1])-shifts[i][1])
    return(np.array(distance))

def residual_intensity(intensity_correction,pairs,shifts):
    distance = []
    for i,pair in enumerate(pairs):
        existing_ratio = shifts[i][5]
        existing_ratio *= intensity_correction[pair[0]]
        existing_ratio /= intensity_correction[pair[1]]
        distance.append(1.0-existing_ratio)
    return(np.array(distance))

def calculate_refined_image_shifts(tile_data,pairs,shifts): 
    is_pixel = np.array([(a["tile_x_offset"]/a["tile_pixel_size"],a["tile_y_offset"]/a["tile_pixel_size"]) for i,a in tile_data.iterrows()])
    res = optimize.least_squares(residuals,x0=is_pixel.flatten(),args=(pairs,shifts))
    new_positions = res.x.reshape(int(len(res.x)/2),2)
    tile_data["tile_x_offset_original"] = tile_data["tile_x_offset"]
    tile_data["tile_y_offset_original"] = tile_data["tile_y_offset"]
    tile_data["tile_x_offset"] = [a[0] for a in new_positions]
    tile_data["tile_x_offset"] *= tile_data["tile_pixel_size"]
    tile_data["tile_y_offset"] = [a[1] for a in new_positions]
    tile_data["tile_y_offset"] *= tile_data["tile_pixel_size"]
    
logger = logging.getLogger("ref_mon")
pycistem.set_cistem_path("/groups/elferich/cisTEM/build/refine_template_tests_Intel-gpu-debug/src/")
input_directory = Path("/scratch/bern/elferich/deco_lace_manuscript_processing/initial_assembly/")
output_directory = Path("/scratch/bern/elferich/deco_lace_manuscript_processing/refined_assembly/")
output_directory.mkdir(exist_ok=True,parents=True)
for (database, name) in utils.dataset_info[-1:]:
    logger.info(f"Working on {name}")
    montage_data = starfile.read(input_directory/f"{name}.star")
    tile_data = montage_data["tiles"]
    #tile_data = tile_data[35:50].copy()
    pairs, shifts = calculate_crosscorrelations(tile_data,num_proc=20)
    pairs, shifts = pair_and_shift_quality_control(tile_data,pairs,shifts)
    logger.info(f"{len(shifts)} are good")
    shifts_df = pd.DataFrame(shifts)
    shifts_df["image_1"] = [tile_data.iloc[a[0]]["tile_filename"] for a in pairs]
    shifts_df["image_2"] = [tile_data.iloc[a[1]]["tile_filename"] for a in pairs]
    starfile.write(shifts_df,output_directory/f"{name}_shifts.star",overwrite=True)
    logger.info(f"Doing lstsquares")
    calculate_refined_image_shifts(tile_data,pairs,shifts)
    binning = montage_data["montage"]["montage_binning"].loc[0]
    max_image_x = np.max(tile_data.loc[:,"tile_x_size"]/binning)
    max_image_y = np.max(tile_data.loc[:,"tile_y_size"]/binning)
    min_shift_x = np.min(tile_data.loc[:,"tile_x_offset"]/tile_data.loc[:,"tile_pixel_size"]/binning) - 2 * binning
    min_shift_y = np.min(tile_data.loc[:,"tile_y_offset"]/tile_data.loc[:,"tile_pixel_size"]/binning) - 2 * binning
    max_shift_x = np.max(tile_data.loc[:,"tile_x_offset"]/tile_data.loc[:,"tile_pixel_size"]/binning) + max_image_x + 2 * binning
    max_shift_y = np.max(tile_data.loc[:,"tile_y_offset"]/tile_data.loc[:,"tile_pixel_size"]/binning) + max_image_y + 2 * binning
    # Correct tile shift
    tile_data["tile_x_offset"] -= min_shift_x * tile_data["tile_pixel_size"] * binning
    tile_data["tile_y_offset"] -= min_shift_y * tile_data["tile_pixel_size"] * binning

    # Decide on dimensions of montage

    montage_y_size = int(max_shift_y-min_shift_y)
    montage_x_size = int(max_shift_x-min_shift_x)
    montage_pixel_size = tile_data['tile_pixel_size'].iloc[0] * binning

    montage_data["montage"].loc[0] =  {
        'montage_filename': str(output_directory/f"{name}") + "_montage.tif",
        'matches_montage_filename': str(output_directory/f"{name}")+"_matches_montage.tif",
        'montage_pixel_size': montage_pixel_size,
        'montage_binning': binning,
        'montage_x_size': montage_x_size,
        'montage_y_size': montage_y_size,
    }
    results = {
        "montage": montage_data["montage"],
        "tiles": tile_data
    }
    starfile.write(results,output_directory/f"{name}.star",overwrite=True)
    assemble_montage_utils.create_montage(results)