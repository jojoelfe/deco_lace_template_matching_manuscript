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
from skimage import filters
from functools import partial
from scipy.ndimage import binary_erosion
import json

ver = "_t2"
FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)
loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
for logger in loggers:
    logger.setLevel(logging.INFO)

def calculate_crosscorrelations(tile_data,num_proc=20,erode_mask=0):
    logger = logging.getLogger("ref_mon")

    points = np.array([(a["tile_x_offset"]/a["tile_pixel_size"],a["tile_y_offset"]/a["tile_pixel_size"]) for i,a in tile_data.iterrows()])
    kd_tree = KDTree(points)

    pairs = kd_tree.query_pairs(r=3000)
    row_pairs = [(tile_data.iloc[a[0]],tile_data.iloc[a[1]]) for a in pairs]
    logger.info(f"There are {len(points)} tiles and {len(pairs)} pairs")
    pool = multiprocessing.Pool(processes=num_proc)
    shifts = pool.map(partial(determine_shift_by_cc,erode_mask=erode_mask), row_pairs)
    pool.close()
    pool.join()
    shifts = pd.DataFrame([a for a in shifts if a is not None])
    return(shifts)

def determine_shift_by_cc(doubled,diagnostic=False,erode_mask=0):
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
            reference = filters.butterworth(reference,cutoff_frequency_ratio=0.02,order=4.0, high_pass=False)
    with mrcfile.open(im2["tile_filename"]) as mrc: 
            moving = np.copy(mrc.data[0])
            if diagnostic:
                axs[2][0].imshow(moving,cmap="Greys_r")
            moving = filters.butterworth(moving,cutoff_frequency_ratio=0.02,order=4.0, high_pass=False)

    if diagnostic:
        axs[2][1].imshow(moving,cmap="Greys_r")
    diff = (im2['image_shift_pixel_x']-im1['image_shift_pixel_x'],im2['image_shift_pixel_y']-im1['image_shift_pixel_y'])
    tform = transform.SimilarityTransform(translation=(diff[0],diff[1])).inverse
    moving = transform.warp(moving,tform,output_shape=reference.shape)

    if diagnostic:

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
    if erode_mask > 0:
        reference_mask = reference_mask > 0.5
        moving_mask = moving_mask > 0.5
        reference_mask = binary_erosion(reference_mask,iterations=erode_mask)
        moving_mask = binary_erosion(moving_mask,iterations=erode_mask)

    moving_mask = transform.warp(moving_mask,tform,output_shape=reference_mask.shape)
    mask =  np.minimum(reference_mask,moving_mask) > 0.9
    if np.sum(mask) < 100:
        return None
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
                                   overlap_ratio=0.1)

    # Generalize to the average of multiple equal maxima
    maxima = np.stack(np.nonzero(xcorr == xcorr.max()), axis=1)
    center = np.mean(maxima, axis=0)
    shift = center - np.array(reference.shape) + 1
    shift = -shift
    if diagnostic:
        
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
    with np.errstate(all='raise'):
        try:
            ratio = np.sum(reference)/np.sum(moving)
        except:
            ratio = 1
           
    return(
        {"shift_x":diff[0]+shift[1],
         "shift_y":diff[1]+shift[0],
         "initial_area":np.sum(mask),
         "max_cc":xcorr.max(),
         "add_shift":np.linalg.norm(shift),
         "int_ratio":ratio,
         "image_1":im1["tile_filename"],
         "image_2":im2["tile_filename"]})
    
       

def pair_and_shift_quality_control(tile_data,shifts):
    good_shifts=shifts[(shifts["add_shift"] < 500) & (shifts["initial_area"] > 200000)]
    tile_data["include_in_refined"] = False
    for i,shift in good_shifts.iterrows():
        tile_data.loc[shift["image_1"],"include_in_refined"] = True
        tile_data.loc[shift["image_2"],"include_in_refined"] = True
    
    logger = logging.getLogger("refmon")
    logger.info(f"{np.sum(tile_data['include_in_refined'] == False)} tiles have no connection")

    return(good_shifts)

def residuals(is_pixel,index_image_1,index_image_2,shifts):
    distance = (is_pixel[index_image_2]-is_pixel[index_image_1])-shifts
    return(distance)



def calculate_refined_image_shifts(tile_data,shifts): 
    initial_pixel_coordinates = np.array([(a["tile_x_offset"]/a["tile_pixel_size"],a["tile_y_offset"]/a["tile_pixel_size"]) for i,a in tile_data.iterrows()])

    indices_image1 = np.array([np.repeat([tile_data.index.get_loc(shift["image_1"]) for i,shift in shifts.iterrows()],2),np.tile([0,1],len(shifts)) ])
    indices_image1 = np.ravel_multi_index(indices_image1,initial_pixel_coordinates.shape)
    indices_image2 = np.array([np.repeat([tile_data.index.get_loc(shift["image_2"]) for i,shift in shifts.iterrows()],2),np.tile([0,1],len(shifts)) ])
    indices_image2 = np.ravel_multi_index(indices_image2,initial_pixel_coordinates.shape)
    shifts_array = shifts[['shift_x','shift_y']].to_numpy().flatten()
    initial_pixel_coordinates = initial_pixel_coordinates.flatten()

    res = optimize.least_squares(residuals,x0=initial_pixel_coordinates,bounds=(initial_pixel_coordinates-5000,initial_pixel_coordinates+5000), args=(indices_image1,indices_image2,shifts_array))
    new_positions = res.x.reshape(int(len(res.x)/2),2)
    tile_data["tile_x_offset_original"] = tile_data["tile_x_offset"]
    tile_data["tile_y_offset_original"] = tile_data["tile_y_offset"]
    tile_data["tile_x_offset"] = [a[0] for a in new_positions]
    tile_data["tile_x_offset"] *= tile_data["tile_pixel_size"]
    tile_data["tile_y_offset"] = [a[1] for a in new_positions]
    tile_data["tile_y_offset"] *= tile_data["tile_pixel_size"]

def residual_intensity(intensity_correction,shifts,indices_image_1,indices_image_2):
    distance = 1.0 - (np.array(shifts["int_ratio"]) * intensity_correction[indices_image_1]) / (intensity_correction[indices_image_2])
    return(distance)

def calculate_refined_intensity(tile_data,shifts):
    intensity_correction = np.array([1.0 for i in range(len(tile_data))])
    min_cor = np.array([0.2 for i in range(len(tile_data))])
    max_cor = np.array([5.0 for i in range(len(tile_data))])
    indices_image_1 = np.array([tile_data.index.get_loc(shift["image_1"]) for i,shift in shifts.iterrows()])
    indices_image_2 = np.array([tile_data.index.get_loc(shift["image_2"]) for i,shift in shifts.iterrows()])

    res = optimize.least_squares(residual_intensity,x0=intensity_correction,bounds=(min_cor,max_cor),args=(shifts,indices_image_1,indices_image_2))
    tile_data["tile_intensity_correction"] = res.x

logger = logging.getLogger("ref_mon")
pycistem.set_cistem_path("/groups/elferich/cisTEM/build/refine_template_tests_Intel-gpu-debug/src/")
input_directory = Path("/scratch/bern/elferich/deco_lace_manuscript_processing/refined_assembly/")
output_directory = Path("/scratch/bern/elferich/deco_lace_manuscript_processing/refined_assembly_it2/")
output_directory.mkdir(exist_ok=True,parents=True)
for (database, name) in utils.dataset_info:
    logger.info(f"Working on {name}")
    montage_data = starfile.read(input_directory/f"{name}{ver}.star")
    tile_data = montage_data["tiles"]
    # Set index of tile_data to tile_file_name
    tile_data["filename_index"] = tile_data["tile_filename"]
    tile_data.set_index("filename_index",inplace=True)
    #tile_data = tile_data[235:295].copy()
    tile_data = tile_data[tile_data["include_in_refined"] == True].copy()
    erode_mask = 0 
    if name.startswith("euc"):
        erode_mask = 100
        logger.info("Eroding mask by 130 pixels")
    else: 
        erode_mask = 50
        logger.info("Eroding mask by 90 pixels")
    shifts = calculate_crosscorrelations(tile_data,num_proc=20,erode_mask=erode_mask)
    starfile.write(shifts,output_directory/f"{name}_shifts{ver}.star",overwrite=True)
    #shifts = starfile.read(output_directory/f"{name}_shifts.star")
    shifts = pair_and_shift_quality_control(tile_data,shifts)
    tile_data = tile_data[tile_data["include_in_refined"] == True].copy()
    logger.info(f"{len(shifts)} are good")
    
    logger.info(f"Doing lstsquares for positions")
    calculate_refined_image_shifts(tile_data,shifts)
    logger.info(f"Doing lstsquares for intensity")
    calculate_refined_intensity(tile_data,shifts)
    logger.info(f"Writing out refined montage")
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
        'montage_filename': str(output_directory/f"{name}") + f"_montage{ver}.tif",
        'matches_montage_filename': str(output_directory/f"{name}")+f"_matches_montage{ver}.tif",
        'montage_pixel_size': montage_pixel_size,
        'montage_binning': binning,
        'montage_x_size': montage_x_size,
        'montage_y_size': montage_y_size,
    }
    results = {
        "montage": montage_data["montage"],
        "tiles": tile_data
    }
    starfile.write(results,output_directory/f"{name}{ver}.star",overwrite=True)
    if name.startswith("euc"):
        gain = "/scratch/bern/elferich/deco_lace_manuscript_processing/averages/euc_gain.mrc"
    if name.startswith("fff"):
        gain = "/scratch/bern/elferich/deco_lace_manuscript_processing/averages/fff_gain.mrc"

    assemble_montage_utils.create_montage_bin_after(results,erode_mask=erode_mask+50,gain=gain,blend=False,gain_mult=0.5)