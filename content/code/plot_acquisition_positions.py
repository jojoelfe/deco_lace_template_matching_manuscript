import matplotlib.pyplot as plt
import latexipy as lp
import utils
import numpy as np
import napari
import mrcfile
from pathlib import Path

IS_to_camera = np.array([13374,  6053.4,  6394.1,  -13172])
IS_to_camera.shape = (2,2)

orig_x_size = 5120
scaled_x_size = 1200.0

def get_scaled_filename(filename):
    p = Path(filename)
    return p.parent.joinpath("Scaled").joinpath(p.name)

def initial_assembly(expand_data, IS_to_camera):
    for item in expand_data.iterrows():
        image_shift = np.array([item[1]["IMAGE_SHIFT_X"],item[1]["IMAGE_SHIFT_Y"]])
        shift_in_camera_pixels = np.dot(IS_to_camera,image_shift)
        shift_in_image_pixel = (shift_in_camera_pixels / (item[1]["image_pixel_size"]/(item[1]["movie_pixel_size"]))) / (orig_x_size/scaled_x_size)
        expand_data.loc[item[0],"image_shift_pixel_x"] = shift_in_image_pixel[0]
        expand_data.loc[item[0],"image_shift_pixel_y"] = shift_in_image_pixel[1]

def get_corners(x,y,radius):
    return [[x+radius,y+radius],[x-radius,y+radius],[x-radius,y-radius],[x+radius,y-radius]]

def plot_montage(data,to_show):
    min_shift_x = np.min(data.loc[:,"image_shift_pixel_x"])
    min_shift_y = np.min(data.loc[:,"image_shift_pixel_y"])
    max_shift_x = np.max(data.loc[:,"image_shift_pixel_x"])
    max_shift_y = np.max(data.loc[:,"image_shift_pixel_y"])
    image_x = 1200
    image_y = 852

    big = np.zeros((int(max_shift_y-min_shift_y+image_y),int(max_shift_x-min_shift_x+image_x)))
    for image in data.iterrows():
        if image[0] not in to_show:
            continue
        with mrcfile.open(get_scaled_filename(image[1]['FILENAME'])) as mrc: 
            image_data = np.copy(np.flip(mrc.data[0],axis=0))
        
        xx,yy  = np.meshgrid(np.arange(image_data.shape[1]),np.arange(image_data.shape[0]))
        mask =  (((xx-600)**2 + (yy-425)**2) < 400**2)
        image_data *= mask
        big[int(image[1]["image_shift_pixel_y"]-min_shift_y):int(image[1]["image_shift_pixel_y"]+image_y-min_shift_y),int(image[1]["image_shift_pixel_x"]-min_shift_x):int(image[1]["image_shift_pixel_x"]-min_shift_x+image_x)] += image_data
    return(big)





selected_micrographs = utils.get_data_from_db(utils.datasets[0])

initial_assembly(selected_micrographs,IS_to_camera=IS_to_camera)

assemb = plot_montage(selected_micrographs,[i for i,r in selected_micrographs.iterrows()])
print(assemb.shape)
#centers = [get_corners(m['IMAGE_SHIFT_X']*150,m['IMAGE_SHIFT_Y']*150,36) for i,m in selected_micrographs.iterrows()]

viewer = napari.view_image(assemb,contrast_limits=(0,10),interpolation='bilinear')

napari.run()