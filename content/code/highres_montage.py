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



logger = logging.getLogger("ref_mon")
pycistem.set_cistem_path("/groups/elferich/cisTEM/build/refine_template_tests_Intel-gpu-debug/src/")
input_directory = Path("/scratch/bern/elferich/deco_lace_manuscript_processing/refined_assembly_it2/")
output_directory = Path("/scratch/bern/elferich/deco_lace_manuscript_processing/refined_assembly_it2/")
output_directory.mkdir(exist_ok=True,parents=True)
for (database, name) in utils.dataset_info[:]:
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
    
    logger.info(f"Writing out refined montage")
    binning = 5
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
        'montage_filename': str(output_directory/f"{name}") + f"_montage{ver}_highres.tif",
        'matches_montage_filename': str(output_directory/f"{name}")+f"_matches_montage{ver}_highres.tif",
        'montage_pixel_size': montage_pixel_size,
        'montage_binning': binning,
        'montage_x_size': montage_x_size,
        'montage_y_size': montage_y_size,
    }
    results = {
        "montage": montage_data["montage"],
        "tiles": tile_data
    }
    if name.startswith("euc"):
        gain = "/scratch/bern/elferich/deco_lace_manuscript_processing/averages/euc_gain.mrc"
    if name.startswith("fff"):
        gain = "/scratch/bern/elferich/deco_lace_manuscript_processing/averages/fff_gain.mrc"
    starfile.write(results,output_directory/f"{name}{ver}_highres.star",overwrite=True)

    assemble_montage_utils.create_montage_bin_after(results,erode_mask=erode_mask+50,gain=gain,blend=False,gain_mult=0.5)