import matplotlib.pyplot as plt
import latexipy as lp
import utils
import numpy as np
import napari
import mrcfile
from pathlib import Path
from skimage.transform import rescale, resize, downscale_local_mean

IS_to_camera = np.array([13374,  6053.4,  6394.1,  -13172])
IS_to_camera.shape = (2,2)

#orig_x_size = 5120
scaled_x_size = 1200.0

load_cached_images = True

def get_scaled_filename(filename):
    p = Path(filename)
    return p.parent.joinpath("Scaled").joinpath(p.name)

def initial_assembly(expand_data, IS_to_camera):
    for item in expand_data.iterrows():
        image_shift = np.array([item[1]["IMAGE_SHIFT_X"],item[1]["IMAGE_SHIFT_Y"]])
        shift_in_camera_pixels = np.dot(IS_to_camera,image_shift)
        largest_size = np.max([item[1]["X_SIZE"],item[1]["Y_SIZE"]])
        shift_in_image_pixel = (shift_in_camera_pixels / (item[1]["image_pixel_size"]/(item[1]["movie_pixel_size"])))
        expand_data.loc[item[0],"image_shift_pixel_x"] = shift_in_image_pixel[0]
        expand_data.loc[item[0],"image_shift_pixel_y"] = shift_in_image_pixel[1]

def get_corners(x,y,radius):
    return [[x+radius,y+radius],[x-radius,y+radius],[x-radius,y-radius],[x+radius,y-radius]]

def get_range(data):
    min_shift_x = np.min(data.loc[:,"image_shift_pixel_x"]) - 4000
    min_shift_y = np.min(data.loc[:,"image_shift_pixel_y"]) - 4000
    max_shift_x = np.max(data.loc[:,"image_shift_pixel_x"]/4) + 1000
    max_shift_y = np.max(data.loc[:,"image_shift_pixel_y"]/4) + 1000
    max_image_x = np.max(data.loc[:,"X_SIZE"]/4)
    max_image_y = np.max(data.loc[:,"Y_SIZE"]/4)
    return (min_shift_x,min_shift_y)

def plot_montage(data,to_show):
    min_shift_x = np.min(data.loc[:,"image_shift_pixel_x"]/4) - 1000
    min_shift_y = np.min(data.loc[:,"image_shift_pixel_y"]/4) - 1000
    max_shift_x = np.max(data.loc[:,"image_shift_pixel_x"]/4) + 1000
    max_shift_y = np.max(data.loc[:,"image_shift_pixel_y"]/4) + 1000
    max_image_x = np.max(data.loc[:,"X_SIZE"]/4)
    max_image_y = np.max(data.loc[:,"Y_SIZE"]/4)

    big = np.zeros((int(max_shift_y-min_shift_y+max_image_y),int(max_shift_x-min_shift_x+max_image_x)))
    mask = np.zeros((int(max_shift_y-min_shift_y+max_image_y),int(max_shift_x-min_shift_x+max_image_x)))
    matches = np.zeros((int(max_shift_y-min_shift_y+max_image_y),int(max_shift_x-min_shift_x+max_image_x)))
    for i, image in data.iterrows():
        if image[0] not in to_show:
            continue
        with mrcfile.open(image['FILENAME'][:-6]+"_0.mrc") as mrc: 
            image_data = np.copy(np.flip(mrc.data[0],axis=0))
            image_data = resize(image_data, (image_data.shape[0] // 4, image_data.shape[1] // 4),anti_aliasing=True)
        
        with mrcfile.open(image['FILENAME'][:-6]+"_1_mask.mrc") as mrc: 
            mask_data = np.copy(np.flip(mrc.data[0],axis=0))
            mask_data.dtype = np.uint8
        
        (y,x) = image_data.shape
        mask_float = mask_data/255.0
        mask_resized = resize(mask_float, (y,x),anti_aliasing=True) 
        image_data *= mask_resized

        crop_x = (image["ORIGINAL_X_SIZE"] - image["X_SIZE"]) / 2
        crop_y = (image["ORIGINAL_Y_SIZE"] - image["Y_SIZE"]) / 2

        crop_center_x = image["CROP_CENTER_X"] 
        crop_center_y = image["CROP_CENTER_Y"] 
        insert_point_x = image["image_shift_pixel_x"] + crop_x + crop_center_x
        insert_point_y = image["image_shift_pixel_y"] + crop_y - crop_center_y
        insert_point_x /= 4
        insert_point_y /= 4
        insert_point_x -= min_shift_x
        insert_point_y -= min_shift_y
        big[int(insert_point_y):int(insert_point_y+y),
            int(insert_point_x):int(insert_point_x+x)] += image_data
        mask[int(insert_point_y):int(insert_point_y+y),
            int(insert_point_x):int(insert_point_x+x)] += mask_resized
        mask[mask < 0.1] = 1.0
        matches_dir = Path(image['FILENAME']).parent.parent / 'TemplateMatching' 
        matches_filenames = list(matches_dir.glob(Path(image['FILENAME'][:-6]).name +"*plotted_result*.mrc"))
        if len(matches_filenames) > 0:
            with mrcfile.open(matches_filenames[-1]) as mrc: 
                match_data = np.copy(np.flip(mrc.data[0],axis=0))
                match_data = resize(match_data, (image_data.shape[0], image_data.shape[1]),anti_aliasing=True)
            matches[int(insert_point_y):int(insert_point_y+y),
                int(insert_point_x):int(insert_point_x+x)] += match_data    
    return(big,mask,matches)





selected_micrographs = utils.get_data_from_db(utils.datasets[4])
print(utils.datasets[4])
print(len(selected_micrographs))
initial_assembly(selected_micrographs,IS_to_camera=IS_to_camera)


image_cache_filename = '/scratch/bern/elferich/napari_' + Path(utils.datasets[4]).stem + '_cache.npz'
if load_cached_images:
    load = np.load(image_cache_filename)
    assemb = load["image"]
    mask = load["mask"]
    matches = load["matches"]
else:
    (assemb, mask, matches) = plot_montage(selected_micrographs,[i for i,r in selected_micrographs.iterrows()])
    np.savez_compressed('/scratch/bern/elferich/napari_lamella5',matches=matches,mask=mask,image=assemb)

centers = [get_corners(m['IMAGE_SHIFT_X']*150,m['IMAGE_SHIFT_Y']*150,36) for i,m in selected_micrographs.iterrows()]
#assemb=np.zeros((100,100))
viewer = napari.view_image(assemb,contrast_limits=(0,10),interpolation='bilinear',scale=(0.6,0.6))
viewer.add_image(mask,contrast_limits=(0,10),interpolation='bilinear',scale=(0.6,0.6))
viewer.add_image(matches,contrast_limits=(0,100000),interpolation='bilinear',blending='additive',colormap='red' ,scale=(0.6,0.6))

radius = 250
min_shift_x, min_shift_y = get_range(selected_micrographs)
data = [[[(row["image_shift_pixel_y"]-min_shift_y+row['ORIGINAL_Y_SIZE']//2)*0.15+radius,(row["image_shift_pixel_x"]-min_shift_x+row['ORIGINAL_X_SIZE']//2)*0.15+radius],
         [(row["image_shift_pixel_y"]-min_shift_y+row['ORIGINAL_Y_SIZE']//2)*0.15-radius,(row["image_shift_pixel_x"]-min_shift_x+row['ORIGINAL_X_SIZE']//2)*0.15+radius],
         [(row["image_shift_pixel_y"]-min_shift_y+row['ORIGINAL_Y_SIZE']//2)*0.15-radius,(row["image_shift_pixel_x"]-min_shift_x+row['ORIGINAL_X_SIZE']//2)*0.15-radius],
         [(row["image_shift_pixel_y"]-min_shift_y+row['ORIGINAL_Y_SIZE']//2)*0.15+radius,(row["image_shift_pixel_x"]-min_shift_x+row['ORIGINAL_X_SIZE']//2)*0.15-radius]] for i, row in selected_micrographs.iterrows()]
viewer.add_shapes(data,shape_type='ellipse',face_color='transparent',edge_color="red",edge_width=15)
napari.run()