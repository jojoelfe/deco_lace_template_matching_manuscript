import matplotlib.pyplot as plt
import numpy as np
import latexipy as lp
import json
from pathlib import Path
import logging
from rich.logging import RichHandler
import mrcfile
import starfile
import matplotlib

FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)
loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
for logger in loggers:
    logger.setLevel(logging.INFO)

import utils

refine_input_dir = Path("/scratch/bern/elferich/deco_lace_manuscript_processing/assemble/")
average_input_dir = Path("/scratch/bern/elferich/deco_lace_manuscript_processing/averages/")
image = {}
matches = {}
for dataset, dataset_name in utils.dataset_info:
    logger.info(dataset_name)
    matches[dataset] = starfile.read(refine_input_dir / f"{dataset_name}_assembled_matches.star")
    if dataset_name.startswith("euc"):
        matches[dataset] = matches[dataset].loc[
                (matches[dataset]['tile_x_size'] > 3200) &
                (matches[dataset]['tile_x_size'] < 3360) &
                (matches[dataset]['tile_y_size'] > 3200) &
                (matches[dataset]['tile_y_size'] < 3360)]
    else:
        matches[dataset] = matches[dataset].loc[
                (matches[dataset]['tile_x_size'] > 3350) &
                (matches[dataset]['tile_x_size'] < 3510) &
                (matches[dataset]['tile_y_size'] > 3320) &
                (matches[dataset]['tile_y_size'] < 3480)]
    with mrcfile.open(average_input_dir / f"{dataset_name}_av.mrc") as mrc:
        image[dataset] = mrc.data.copy()
    u = dataset
    




lp.latexify()
with lp.figure("micrograph_with_matches",size=lp.figure_size(ratio=0.4,doc_width_pt=1000),tight_layout=False):
    fig, axs = plt.subplots(2,4,sharey=True,sharex=True,constrained_layout=True)
    axs = axs.flatten()
    for i, dataset in enumerate(utils.datasets):

        axs[i].set_title(utils.dataset_names[i])
        axs[i].imshow(image[dataset],cmap="gray")
        colormap = plt.cm.viridis #or any other colormap
        normalize = matplotlib.colors.Normalize(vmin=7, vmax=10)
        print(len(matches[dataset]["tile_x"]/1.5))
        s = axs[i].scatter(matches[dataset]["tile_x"]/1.5,matches[dataset]["tile_y"]/1.5,s=1,c=matches[dataset]["peak_value"],cmap=colormap,norm=normalize)
    plt.colorbar(s)

