import matplotlib.pyplot as plt
import latexipy as lp
import utils
import numpy as np
from pathlib import Path
from skimage.transform import rescale, resize, downscale_local_mean
from skimage import io

import assemble_montage_utils as assemble_montage_utils 
import utils


load_cached_images = False


directory = Path("/scratch/bern/elferich/deco_lace_manuscript_processing/initial_assembly/")
directory.mkdir(parents=True,exist_ok=True)

selected_micrographs = utils.get_data_from_db(utils.datasets[1])
selected_micrographs = selected_micrographs[5:-2]

print(utils.datasets[1])
print(len(selected_micrographs))
metadata = assemble_montage_utils.create_metadata(selected_micrographs,
                                       IS_to_camera=assemble_montage_utils.IS_to_camera,
                                       output_base=str(directory / 'euc_lamella2'))
#assemble_montage_utils.create_montage(metadata)
exit()
