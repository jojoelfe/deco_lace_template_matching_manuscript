from curses import meta
from selectors import EpollSelector
import matplotlib.pyplot as plt
import latexipy as lp
import numpy as np
import mrcfile
from pathlib import Path
from skimage.transform import resize
from skimage import io
import pandas as pd
import starfile
from skimage.util import img_as_uint
import json
from scipy.ndimage import binary_erosion

IS_to_camera = np.array([13374,  6053.4,  6394.1,  -13172])
IS_to_camera.shape = (2,2)



def create_metadata(expand_data, IS_to_camera, output_base, binning=10, image_suffix="_0.mrc", mask_suffix ="_0_mask.mrc"):
    
    result_montage = pd.DataFrame({
        'montage_filename': pd.Series(dtype='string'),
        'matches_montage_filename': pd.Series(dtype='string'),
        'montage_pixel_size': pd.Series(dtype='float'),
        'montage_binning': pd.Series(dtype='float'),
        'montage_x_size': pd.Series(dtype='int'),
        'montage_y_size': pd.Series(dtype='int'),
    })

    result_tiles = pd.DataFrame({
        'tile_filename': pd.Series(dtype='object'),
        'tile_movie_filename': pd.Series(dtype='object'),
        'tile_x_offset': pd.Series(dtype='int'),
        'tile_y_offset': pd.Series(dtype='int'),
        'tile_pixel_size': pd.Series(dtype='float'),
        'tile_x_size': pd.Series(dtype='int'),
        'tile_y_size': pd.Series(dtype='int'),
        'tile_orig_x_size': pd.Series(dtype='int'),
        'tile_orig_y_size': pd.Series(dtype='int'),
        'tile_x_crop_center': pd.Series(dtype='int'),
        'tile_y_crop_center': pd.Series(dtype='int'),
        'tile_mask_filename': pd.Series(dtype='object'),
        'tile_plotted_result_filename': pd.Series(dtype='object'),
        'tile_image_shift_x': pd.Series(dtype='float'),
        'tile_image_shift_y': pd.Series(dtype='float'),
        'tile_microscope_focus': pd.Series(dtype='float'),
        'tile_defocus': pd.Series(dtype='float'),
    })


    for i, item in expand_data.iterrows():

        # Initially convert image shift to unbinned pixels
        image_shift = np.array([item["IMAGE_SHIFT_X"],item["IMAGE_SHIFT_Y"]])
        shift_in_camera_pixels = np.dot(IS_to_camera,image_shift)
        shift_in_image_pixel = (shift_in_camera_pixels / (item["image_pixel_size"]/(item["movie_pixel_size"])))
        crop_x = (item["ORIGINAL_X_SIZE"] - item["X_SIZE"]) / 2
        crop_y = (item["ORIGINAL_Y_SIZE"] - item["Y_SIZE"]) / 2
        crop_center_x = item["CROP_CENTER_X"] 
        crop_center_y = item["CROP_CENTER_Y"] 
        expand_data.loc[i,"image_shift_pixel_x"] = shift_in_image_pixel[0] + crop_x + crop_center_x
        expand_data.loc[i,"image_shift_pixel_y"] = - shift_in_image_pixel[1] + crop_y - crop_center_y
        
    
    # Get the range of the shifts taking binning into account
    max_image_x = np.max(expand_data.loc[:,"X_SIZE"]/binning)
    max_image_y = np.max(expand_data.loc[:,"Y_SIZE"]/binning)
    min_shift_x = np.min(expand_data.loc[:,"image_shift_pixel_x"]/binning) - 2 * binning
    min_shift_y = np.min(expand_data.loc[:,"image_shift_pixel_y"]/binning) - 2 * binning
    max_shift_x = np.max(expand_data.loc[:,"image_shift_pixel_x"]/binning) + max_image_x + 2 * binning
    max_shift_y = np.max(expand_data.loc[:,"image_shift_pixel_y"]/binning) + max_image_y + 2 * binning

    # Decide on dimensions of montage

    montage_y_size = int(max_shift_y-min_shift_y)
    montage_x_size = int(max_shift_x-min_shift_x)
    montage_pixel_size = expand_data['image_pixel_size'].iloc[0] * binning

    result_montage.loc[0] =  {
        'montage_filename': output_base + "_montage.tif",
        'matches_montage_filename': output_base+"_matches_montage.tif",
        'montage_pixel_size': montage_pixel_size,
        'montage_binning': binning,
        'montage_x_size': montage_x_size,
        'montage_y_size': montage_y_size,
    }
    
    # No iterate again, to setup the required data
    for i, item in expand_data.iterrows():
        new_entry = {}
        #print(item['FILENAME'])
        new_entry['tile_filename'] = item['FILENAME'][:-6]+image_suffix
        new_entry['tile_movie_filename'] = item['movie_filename']
        new_entry['tile_mask_filename'] = item['FILENAME'][:-6]+mask_suffix
        new_entry['tile_pixel_size'] = item['image_pixel_size']
        new_entry['tile_x_size'] = item['X_SIZE']
        new_entry['tile_y_size'] = item['Y_SIZE']
        new_entry['tile_orig_x_size'] = item['ORIGINAL_X_SIZE']
        new_entry['tile_orig_y_size'] = item['ORIGINAL_Y_SIZE']
        new_entry['tile_x_crop_center'] = item['CROP_CENTER_X']
        new_entry['tile_y_crop_center'] = item['CROP_CENTER_Y']
        new_entry['tile_image_shift_x'] = item['IMAGE_SHIFT_X']
        new_entry['tile_image_shift_y'] = item['IMAGE_SHIFT_Y']
        new_entry['tile_microscope_focus'] = json.loads(item['CONTENT_JSON'])["Defocus"]
        new_entry['tile_defocus'] = (item['DEFOCUS1'] + item['DEFOCUS2'])/2
        matches_dir = Path(item['FILENAME']).parent.parent / 'TemplateMatching' 
        #print(Path(item['FILENAME'][:-6]).name +"*plotted_result*.mrc")
        matches_filenames = list(matches_dir.glob(Path(item['FILENAME'][:-6]).name +"*plotted_result*.mrc"))
        #print(matches_filenames)
        if len(matches_filenames) > 0:
            new_entry['tile_plotted_result_filename'] = str(matches_filenames[0])
        else:
            new_entry['tile_plotted_result_filename'] = "None"
        # Calulate the offset
        insert_point_x = item["image_shift_pixel_x"] 
        insert_point_y = item["image_shift_pixel_y"]
        insert_point_x /= binning
        insert_point_y /= binning
        insert_point_x -= min_shift_x
        insert_point_y -= min_shift_y

        new_entry['tile_x_offset'] = insert_point_x * montage_pixel_size
        new_entry['tile_y_offset'] = insert_point_y * montage_pixel_size
        
        result_tiles.loc[len(result_tiles.index)] = new_entry

    results = {
        "montage": result_montage,
        "tiles": result_tiles
    }
    print(result_montage.shape)
    starfile.write(results, output_base + ".star",overwrite=True)

    return(results)

def create_montage(metadata ):

    montage_info = metadata['montage'].iloc[0]

    montage_dimensions = (montage_info['montage_y_size'], montage_info['montage_x_size'])

    big = np.zeros(montage_dimensions,dtype=float)
    mask = np.zeros(montage_dimensions,dtype=float)
    matches = np.zeros(montage_dimensions,dtype=float)

    tile_info = metadata['tiles']

    for i, tile in tile_info.iterrows():
        
        with mrcfile.open(tile['tile_filename']) as mrc: 
            tile_data = np.copy(mrc.data[0])
            tile_dimensions = (int(tile_data.shape[0]// montage_info['montage_binning']),int(tile_data.shape[1]// montage_info['montage_binning']))
            
            tile_data = resize(tile_data,tile_dimensions,anti_aliasing=True)
        
        with mrcfile.open(tile['tile_mask_filename']) as mrc: 
            mask_data = np.copy(mrc.data[0])
            mask_data.dtype = np.uint8
        
        
        mask_float = mask_data/255.0
        mask_resized = resize(mask_float, tile_dimensions,anti_aliasing=True) 
        tile_data *= mask_resized


        montage_pixel_size = montage_info['montage_pixel_size']
        insertion_slice= (
            slice(int(tile['tile_y_offset'] / montage_pixel_size),int(tile['tile_y_offset']/ montage_pixel_size)+tile_dimensions[0]),
            slice(int(tile['tile_x_offset'] / montage_pixel_size),int(tile['tile_x_offset']/ montage_pixel_size)+tile_dimensions[1])
        )
        
        big[insertion_slice] += tile_data
        mask[insertion_slice] += mask_resized
        
        
        if str(tile['tile_plotted_result_filename']) != "None":
            with mrcfile.open(tile['tile_plotted_result_filename']) as mrc: 
                match_data = np.copy(mrc.data[0])
                if np.max(match_data) > 300000:
                    print(i)
                    print(tile['tile_filename'])
                    print(np.max(match_data))
                match_data = resize(match_data, tile_dimensions,anti_aliasing=True)
                match_data *= mask_resized
            matches[insertion_slice] += match_data   

    mask[mask < 0.1] = 1.0 
    big /= mask
    big /= np.max(big)
    matches /= np.max(matches)
    io.imsave(montage_info['montage_filename'],img_as_uint(big),plugin='tifffile')
    io.imsave(montage_info['matches_montage_filename'],img_as_uint(matches),plugin='tifffile')

def create_montage_bin_after(metadata,erode_mask=0,gain=None,blend=True,gain_mult=1.0 ):

    montage_info = metadata['montage'].iloc[0]
    if gain is not None:
        with mrcfile.open(gain) as mrc:
            gain_data = mrc.data.copy()
        gain_data[gain_data < 0.5] = 1.0
        gain_data *= gain_mult
    else:
        gain_data = None
    montage_dimensions = (montage_info['montage_y_size']*montage_info['montage_binning'], montage_info['montage_x_size']*montage_info['montage_binning'])
    montage_binned_dimension = (montage_info['montage_y_size'], montage_info['montage_x_size'])
    big = np.zeros(montage_dimensions,dtype=float)
    mask = np.zeros(montage_dimensions,dtype=float)
    matches = np.zeros(montage_dimensions,dtype=float)

    tile_info = metadata['tiles']

    for i, tile in tile_info.iterrows():
        
        with mrcfile.open(tile['tile_filename']) as mrc: 
            tile_data = np.copy(mrc.data[0])
            tile_dimensions = (int(tile_data.shape[0]),int(tile_data.shape[1]))
            tile_data *= tile["tile_intensity_correction"]
            #tile_data = resize(tile_data,tile_dimensions,anti_aliasing=True)
        if tile_data.shape[1] > gain_data.shape[1] or tile_data.shape[0] > gain_data.shape[0]:
            print("Skipping tile as it is larger than the gain")
            continue
        x_offset = (gain_data.shape[1]-tile_data.shape[1])//2
        y_offset = (gain_data.shape[0]-tile_data.shape[0])//2
        print(tile_data.mean())
        
        pers_gain = gain_data[y_offset:y_offset+tile_data.shape[0],x_offset:x_offset+tile_data.shape[1]]
        print(pers_gain.mean())
        tile_data /= pers_gain
        print(tile_data.mean())
        print(tile_data.dtype)
        print(pers_gain.dtype)
        with mrcfile.open(tile['tile_mask_filename']) as mrc: 
            mask_data = np.copy(mrc.data[0])
            mask_data.dtype = np.uint8
        
        
        mask_float = mask_data/255.0
        #mask_resized = resize(mask_float, tile_dimensions,anti_aliasing=True) 
        if erode_mask > 0:
            mask_float = binary_erosion(mask_float>0.5,iterations=erode_mask)
            mask_float = 1.0 * mask_float

        tile_data *= mask_float


        montage_pixel_size = montage_info['montage_pixel_size']
        insertion_slice= (
            slice(int(tile['tile_y_offset'] / tile['tile_pixel_size']),int(tile['tile_y_offset']/ tile['tile_pixel_size'])+tile_dimensions[0]),
            slice(int(tile['tile_x_offset'] / tile['tile_pixel_size']),int(tile['tile_x_offset']/ tile['tile_pixel_size'])+tile_dimensions[1])
        )

        existing_mask = 1.0 - mask[insertion_slice]
        if not blend:
            tile_data *= existing_mask
            mask_float *= existing_mask
        
        big[insertion_slice] += tile_data
        mask[insertion_slice] += mask_float
        
        
        if str(tile['tile_plotted_result_filename']) != "None":
            with mrcfile.open(tile['tile_plotted_result_filename']) as mrc: 
                match_data = np.copy(mrc.data[0])
                if np.max(match_data) > 300000:
                    print(i)
                    print(tile['tile_filename'])
                    print(np.max(match_data))
                #match_data = resize(match_data, tile_dimensions,anti_aliasing=True)
                match_data *= mask_float
            matches[insertion_slice] += match_data   

    mask[mask < 0.1] = 1.0 
    if blend:
        big /= mask
    big /= np.max(big)
    matches /= np.max(matches)
    big = resize(big,montage_binned_dimension,anti_aliasing=True)
    matches = resize(matches,montage_binned_dimension,anti_aliasing=True)
    io.imsave(montage_info['montage_filename'],img_as_uint(big),plugin='tifffile')
    io.imsave(montage_info['matches_montage_filename'],img_as_uint(matches),plugin='tifffile')


