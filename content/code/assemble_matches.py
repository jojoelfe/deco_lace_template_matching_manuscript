import starfile
import utils
from pathlib import Path


montage_directory = Path("/scratch/bern/elferich/deco_lace_manuscript_processing/initial_assembly/")
refine_directory = Path("/scratch/bern/elferich/deco_lace_manuscript_processing/lamella_refine/")
assembled_directory = Path("/scratch/bern/elferich/deco_lace_manuscript_processing/assemble/")
assembled_directory.mkdir(exist_ok=True,parents=True)
for (database, name) in utils.dataset_info:
    print(name)
    montage_info = starfile.read(montage_directory / f"{name}.star")
    refine_info = starfile.read(refine_directory / f"{name}_refine.star")
    print(len(refine_info.index))
    # Make sure both sides use image 0
    montage_info["tiles"]["tile_filename"] = montage_info["tiles"]["tile_filename"].apply(lambda x: x.replace("_1.mrc","_0.mrc"))
    refine_info["image_filename"] = refine_info["image_filename"].apply(lambda x: x.replace("_1.mrc","_0.mrc"))

    # Join the two dataframes
    info = montage_info["tiles"].merge(refine_info, how="right", left_on="tile_filename", right_on="image_filename")
    #print(info.loc[0])
    info["tile_x"] = info["x"]
    info["tile_y"] = info["y"]
    info["x"] = info["tile_x"] + info["tile_x_offset"]
    info["y"] = info["tile_y"] + info["tile_y_offset"]
    info["image_filename"] = montage_info["montage"]["montage_filename"].loc[0]
    print(info["template_filename"].unique())
    print(info["image_filename"].unique())
    # Write the new starfile
    starfile.write(info, assembled_directory / f"{name}_assembled_matches.star",overwrite=True)
