import matplotlib.pyplot as plt
import latexipy as lp
import utils
import numpy as np
import napari
import mrcfile
from pathlib import Path
from skimage.transform import rescale, resize, downscale_local_mean
from skimage import io

import plot_acquisition_utils 
import utils


load_cached_images = False


selected_micrographs = utils.get_data_from_db(utils.datasets[0])
selected_micrographs = selected_micrographs[40:1020]
print(utils.datasets[0])
print(len(selected_micrographs))
plot_acquisition_utils.initial_assembly(selected_micrographs,IS_to_camera=plot_acquisition_utils.IS_to_camera)



directory = Path("/scratch/bern/elferich/decolace_manuscript_processing/initial_assembly/")
directory.mkdir(parents=True,exist_ok=True)

image_cache_filename = directory / 'euc_lamella1_cache.npz'
if load_cached_images:
    load = np.load(image_cache_filename)
    assemb = load["image"]
    mask = load["mask"]
    matches = load["matches"]
else:
    (assemb, mask, matches) = plot_acquisition_utils.plot_montage(selected_micrographs,[i for i in range(2,1010)])
    np.savez_compressed(image_cache_filename,matches=matches,mask=mask,image=assemb)
    corr = assemb/mask
    io.imsave(directory / 'euc_lamella1_image.tif',corr/np.max(corr),plugin='pil')


exit()
centers = [get_corners(m['IMAGE_SHIFT_X']*150,m['IMAGE_SHIFT_Y']*150,36) for i,m in selected_micrographs.iterrows()]
#assemb=np.zeros((100,100))
scale = 0.15 * crop_by
viewer = napari.view_image(assemb/mask,contrast_limits=(0,10),interpolation='bilinear',scale=(scale,scale))
viewer.add_image(mask,contrast_limits=(0,10),interpolation='bilinear',scale=(scale,scale))
viewer.add_image(matches,contrast_limits=(0,100000),interpolation='bilinear',blending='additive',colormap='red' ,scale=(scale,scale))

radius = 250
min_shift_x, min_shift_y = get_range(selected_micrographs)
data = [[[(row["image_shift_pixel_y"]-min_shift_y+row['ORIGINAL_Y_SIZE']//2)*0.15+radius,(row["image_shift_pixel_x"]-min_shift_x+row['ORIGINAL_X_SIZE']//2)*0.15+radius],
         [(row["image_shift_pixel_y"]-min_shift_y+row['ORIGINAL_Y_SIZE']//2)*0.15-radius,(row["image_shift_pixel_x"]-min_shift_x+row['ORIGINAL_X_SIZE']//2)*0.15+radius],
         [(row["image_shift_pixel_y"]-min_shift_y+row['ORIGINAL_Y_SIZE']//2)*0.15-radius,(row["image_shift_pixel_x"]-min_shift_x+row['ORIGINAL_X_SIZE']//2)*0.15-radius],
         [(row["image_shift_pixel_y"]-min_shift_y+row['ORIGINAL_Y_SIZE']//2)*0.15+radius,(row["image_shift_pixel_x"]-min_shift_x+row['ORIGINAL_X_SIZE']//2)*0.15-radius]] for i, row in selected_micrographs.iterrows()]
viewer.add_shapes(data,shape_type='ellipse',face_color='transparent',edge_color="red",edge_width=15)
napari.run()