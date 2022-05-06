from numpy import byte
import starfile
import utils
from pathlib import Path
import mrcfile
import numpy as np


annot_directory = Path("/scratch/bern/elferich/deco_lace_manuscript_processing/nucleus_annotation/")
refine_directory = Path("/scratch/bern/elferich/deco_lace_manuscript_processing/lamella_refine/")

num_tiles = 0 
num_matches = 0
num_cellmatches = 0
for (database, name) in utils.dataset_info:
    print(annot_directory / f"{name}_tiles.star")
    montage_info = starfile.read(annot_directory / f"{name}_tiles.star")
    refine_info = starfile.read(refine_directory / f"{name}_refine.star")
    print(len(refine_info.index))
    print(len(montage_info.index))
    # Make sure both sides use image 0
    montage_info["tile_filename"] = montage_info["tile_filename"].apply(lambda x: x.replace("_1.mrc","_0.mrc"))
    refine_info["image_filename"] = refine_info["image_filename"].apply(lambda x: x.replace("_1.mrc","_0.mrc"))
    montage_info["tile_filename"] = montage_info["tile_filename"].apply(lambda x: x.replace("_2.mrc","_0.mrc"))
    refine_info["image_filename"] = refine_info["image_filename"].apply(lambda x: x.replace("_2.mrc","_0.mrc"))
    montage_info["tile_filename"] = montage_info["tile_filename"].apply(lambda x: x.replace("_3.mrc","_0.mrc"))
    refine_info["image_filename"] = refine_info["image_filename"].apply(lambda x: x.replace("_3.mrc","_0.mrc"))
    # Join the two dataframes
    info = montage_info.merge(refine_info, how="inner", left_on="tile_filename", right_on="image_filename")
    print(len(info.index))
    #print(info.loc[0])
    info["tile_x"] = info["x"]
    info["tile_y"] = info["y"]
    info["x"] = info["tile_x"] + info["tile_x_offset"]
    info["y"] = info["tile_y"] + info["tile_y_offset"]
    info["image_filename"] = "whocares"
    info["pixel_size"] = 1.5
    print(info["template_filename"].unique())
    print(info["image_filename"].unique())

    info["mask_value"] = 0.0
    info["display"] = False
    #Check the value of the mask at each match
    for mask_filename in info["tile_mask_filename"].unique():
        # Open mask and convert to 0-1 floats
        if mask_filename == None: 
            continue
        with mrcfile.open(mask_filename) as mask:
            mask_data = np.copy(mask.data[0])
            mask_data.dtype = np.uint8
            mask_float = mask_data/255.0
    #    
        peak_indices = info.loc[info["tile_mask_filename"] == mask_filename].index.tolist()
        for i in peak_indices:
            try:
                info.loc[i,"mask_value"] = mask_float[int(info.loc[i,"tile_y"]/info.loc[i,"tile_pixel_size"]),int(info.loc[i,"tile_x"]/info.loc[i,"tile_pixel_size"])]
            except IndexError:
                info.loc[i,"mask_value"] = 0
            if info.loc[i,"mask_value"] > 0.7:
                info.loc[i,"display"] = True
    # Correct for defocus and nominal focus
    median_defocus = info["tile_defocus"].median()
    median_microscope_focus = info["tile_microscope_focus"].median()
    defocus_correction = info["tile_defocus"] - median_defocus
    microscope_focus_correction = info["tile_microscope_focus"] - median_microscope_focus
    info["defocus"] += defocus_correction
    info["defocus"] = microscope_focus_correction * 10000 + info["defocus"]
    print("res")
    print(info.groupby("tile_filename").count())
    print(info.groupby("tile_filename").agg({"display": "sum"}))
    num_tiles += len(montage_info.index)
    num_matches += len(info.index)
    num_cellmatches += len(info.loc[info["mask_value"] > 0.7].index)
    # Write the new starfile
    #starfile.write(info, assembled_directory / f"{name}_assembled_matches.star",overwrite=True)

print(f"Overall:\n{num_tiles} tiles\n{num_matches} matches\n{num_cellmatches} cell matches")