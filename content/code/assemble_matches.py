from numpy import byte
import starfile
import utils
from pathlib import Path
import mrcfile
import numpy as np


montage_directory = Path("/scratch/bern/elferich/deco_lace_manuscript_processing/refined_assembly/")
refine_directory = Path("/scratch/bern/elferich/deco_lace_manuscript_processing/lamella_refine/")
assembled_directory = Path("/scratch/bern/elferich/deco_lace_manuscript_processing/assemble/")
assembled_directory.mkdir(exist_ok=True,parents=True)
for (database, name) in utils.dataset_info[5:6]:
    print(name)
    montage_info = starfile.read(montage_directory / f"{name}.star")
    refine_info = starfile.read(refine_directory / f"{name}_refine.star")
    print(len(refine_info.index))
    print(len(montage_info["tiles"].index))
    # Make sure both sides use image 0
    montage_info["tiles"]["tile_filename"] = montage_info["tiles"]["tile_filename"].apply(lambda x: x.replace("_1.mrc","_0.mrc"))
    refine_info["image_filename"] = refine_info["image_filename"].apply(lambda x: x.replace("_1.mrc","_0.mrc"))
    montage_info["tiles"]["tile_filename"] = montage_info["tiles"]["tile_filename"].apply(lambda x: x.replace("_2.mrc","_0.mrc"))
    refine_info["image_filename"] = refine_info["image_filename"].apply(lambda x: x.replace("_2.mrc","_0.mrc"))
    montage_info["tiles"]["tile_filename"] = montage_info["tiles"]["tile_filename"].apply(lambda x: x.replace("_3.mrc","_0.mrc"))
    refine_info["image_filename"] = refine_info["image_filename"].apply(lambda x: x.replace("_3.mrc","_0.mrc"))
    # Join the two dataframes
    info = montage_info["tiles"].merge(refine_info, how="inner", left_on="tile_filename", right_on="image_filename")
    print(len(info.index))
    #print(info.loc[0])
    info["tile_x"] = info["x"]
    info["tile_y"] = info["y"]
    info["x"] = info["tile_x"] + info["tile_x_offset"]
    info["y"] = info["tile_y"] + info["tile_y_offset"]
    info["image_filename"] = montage_info["montage"]["montage_filename"].loc[0]
    info["pixel_size"] = montage_info["montage"]["montage_pixel_size"].loc[0]
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
    info["defocus"] += microscope_focus_correction * 10000
    # Write the new starfile
    starfile.write(info, assembled_directory / f"{name}_assembled_matches.star",overwrite=True)
