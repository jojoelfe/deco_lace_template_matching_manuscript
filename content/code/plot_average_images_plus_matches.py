import matplotlib.pyplot as plt
import numpy as np
import latexipy as lp
import json
from pathlib import Path
import logging
from rich.logging import RichHandler
import mrcfile

FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)
loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
for logger in loggers:
    logger.setLevel(logging.INFO)

import utils

intensity = {}
gain_average = {}
all_average = {}
selected_micrographs = {}

exclude = {
    "euc_lamella1": [49,82,86,89,126,130],
    "euc_lamella2": [59,61,62,81],
    "euc_lamella3": [49,61,78],
    "euc_lamella4": [25],
    "fff_lamella1": [2,23,24,33,34],
    "fff_lamella2": [7,8,9,521,522,523,524,543,544,545,546],
    "fff_lamella3": [8,9,10,11,39,515,516,519,520],
    "fff_lamella4": [7,13]

}

output_dir = Path("/scratch/bern/elferich/deco_lace_manuscript_processing/averages/")
output_dir.mkdir(exist_ok=True, parents=True)
max_x = {}
max_y = {}
for dataset, dataset_name in utils.dataset_info:
    logging.info(dataset)
    selected_micrographs[dataset] = utils.get_data_from_db(dataset)
    with open(Path(dataset).stem +"_thickness.json","r") as fp:
        thickness_data = json.load(fp)
    selected_micrographs[dataset]["thickness"] = 0
    for i, micrograph in selected_micrographs[dataset].iterrows():
        if micrograph['movie_filename'] in thickness_data:
            selected_micrographs[dataset].loc[i,"thickness"] = thickness_data[micrograph['movie_filename']]
    if dataset_name.startswith("euc"):
        selected_micrographs[dataset] = selected_micrographs[dataset].loc[
            (selected_micrographs[dataset]['X_SIZE'] > 3200) &
            (selected_micrographs[dataset]['X_SIZE'] < 3360) &
            (selected_micrographs[dataset]['Y_SIZE'] > 3200) &
            (selected_micrographs[dataset]['Y_SIZE'] < 3360)]
    if dataset_name.startswith("fff"):
        selected_micrographs[dataset] = selected_micrographs[dataset].loc[
            (selected_micrographs[dataset]['X_SIZE'] > 3350) &
            (selected_micrographs[dataset]['X_SIZE'] < 3510) &
            (selected_micrographs[dataset]['Y_SIZE'] > 3320) &
            (selected_micrographs[dataset]['Y_SIZE'] < 3480)]
    max_xsize = selected_micrographs[dataset]['X_SIZE'].max() + 1
    max_ysize = selected_micrographs[dataset]['Y_SIZE'].max() + 1 
    max_x[dataset_name] = max_xsize
    max_y[dataset_name] = max_ysize
    gain_average[dataset] = np.zeros((max_ysize,max_xsize))
    all_average[dataset] = np.zeros((max_ysize,max_xsize))
    logging.info(f"Average image has shape {gain_average[dataset].shape}")

    gain_counter = 0
    for i, micrograph in selected_micrographs[dataset].iterrows():
        filename = micrograph['FILENAME']
        mask_filename = filename.replace(".mrc","_mask.mrc")
        with mrcfile.open(filename) as mrc:
            data = mrc.data[0].copy()
        with mrcfile.open(mask_filename) as mrc:
            mask_data = mrc.data[0].copy()
            mask_data.dtype = np.uint8
            mask_data = mask_data/255.0
        
        x_offset =int( (max_xsize-data.shape[1])/2)
        y_offset = int((max_ysize-data.shape[0])/2)
        
        if dataset_name.startswith("euc"):
            threshold = 0.305
            mask_threshold = 8300000
        if dataset_name.startswith("fff"):
            threshold = 0.29
            mask_threshold = 9000000
        if micrograph['thickness'] > threshold and np.sum(mask_data) > mask_threshold and i not in exclude[dataset_name]:
            gain_counter += 1
            gain_average[dataset][y_offset:y_offset+data.shape[0],
                                    x_offset:x_offset+data.shape[1]] += data
            with mrcfile.new(output_dir / f"diag_{dataset_name}_av_{i:03}.mrc", overwrite=True) as mrc:
                mrc.set_data(data)
            print(f"diag_{dataset_name}_av_{i:03}.mrc",np.mean(data),np.sum(mask_data))
        data *= mask_data
        all_average[dataset][y_offset:y_offset+data.shape[0],
                                x_offset:x_offset+data.shape[1]] += data
        
    logger.info(f"{gain_counter} micrographs are in the gain reference")
    with mrcfile.new(output_dir / f"{dataset_name}_av.mrc", overwrite=True) as mrc:
        mrc.set_data(np.float32(all_average[dataset]))
    with mrcfile.new(output_dir / f"{dataset_name}_av_gain.mrc", overwrite=True) as mrc:
        mrc.set_data(np.float32(gain_average[dataset]))

max_x_fff = max([max_x[k] for k in max_x if k.startswith("fff")])
max_y_fff = max([max_y[k] for k in max_y if k.startswith("fff")])
gain = np.zeros((max_y_fff,max_x_fff))
for dataset, dataset_name in utils.dataset_info:
    
    if dataset_name.startswith("fff"):
        with mrcfile.open(output_dir / f"{dataset_name}_av_gain.mrc") as mrc:
            data = mrc.data
        x_offset =int( (max_x_fff-data.shape[1])/2)
        y_offset = int((max_y_fff-data.shape[0])/2)
        gain[y_offset:y_offset+data.shape[0],x_offset:x_offset+data.shape[1]] += data
gain /= gain.mean()
with mrcfile.new(output_dir / f"fff_gain.mrc", overwrite=True) as mrc:
    mrc.set_data(np.float32(gain))
    

lp.latexify()
with lp.figure("averaged_images",size=lp.figure_size(ratio=0.5,doc_width_pt=500),tight_layout=False):
    fig, axs = plt.subplots(2,4,sharey=True,sharex=True,constrained_layout=True)
    axs = axs.flatten()
    for i, dataset in enumerate(utils.datasets):

        axs[i].imshow(all_average[dataset],cmap='gray')
        axs[i].set_title(utils.dataset_names[i])

lp.latexify()
with lp.figure("gain_averaged_images",size=lp.figure_size(ratio=0.5,doc_width_pt=500),tight_layout=False):
    fig, axs = plt.subplots(2,4,sharey=True,sharex=True,constrained_layout=True)
    axs = axs.flatten()
    for i, dataset in enumerate(utils.datasets):

        axs[i].imshow(gain_average[dataset],cmap='gray')
        axs[i].set_title(utils.dataset_names[i])

lp.latexify()
with lp.figure("intensity_histogram",size=lp.figure_size(ratio=0.5,doc_width_pt=500),tight_layout=False):
    cm = plt.cm.get_cmap('viridis')
    fig, axs = plt.subplots(2,4,sharey=True,sharex=True,constrained_layout=True)
    axs = axs.flatten()
    for i, dataset in enumerate(utils.datasets):

        axs[i].hist(selected_micrographs[dataset]["thickness"],bins=100,alpha=0.5)
        axs[i].set_title(utils.dataset_names[i])

lp.latexify()
with lp.figure("xsize_histograms",size=lp.figure_size(ratio=0.5,doc_width_pt=500),tight_layout=False):
    cm = plt.cm.get_cmap('viridis')
    fig, axs = plt.subplots(2,4,sharey=True,sharex=True,constrained_layout=True)
    axs = axs.flatten()
    for i, dataset in enumerate(utils.datasets):

        axs[i].hist(selected_micrographs[dataset]["X_SIZE"],bins=100,alpha=0.5)
        axs[i].set_title(f"{utils.dataset_names[i]} ")

lp.latexify()
with lp.figure("ysize_histograms",size=lp.figure_size(ratio=0.5,doc_width_pt=500),tight_layout=False):
    cm = plt.cm.get_cmap('viridis')
    fig, axs = plt.subplots(2,4,sharey=True,sharex=True,constrained_layout=True)
    axs = axs.flatten()
    for i, dataset in enumerate(utils.datasets):

        axs[i].hist(selected_micrographs[dataset]["Y_SIZE"],bins=100,alpha=0.5)
        axs[i].set_title(f"{utils.dataset_names[i]} ")


