import matplotlib.pyplot as plt
import latexipy as lp
import utils
import starfile
from pathlib import Path
import numpy as np
from scipy.stats import mannwhitneyu

bis_scores = []

for dataset, name in utils.dataset_info:
    assembled_directory = Path("/scratch/bern/elferich/deco_lace_manuscript_processing/assemble/")
    data  =  starfile.read(assembled_directory / f"{name}_assembled_matches.star")
    bis_scores.append((data[data["display"]]["tile_image_shift_x"],data[data["display"]]["tile_image_shift_y"],data[data["display"]]["peak_value"]))


lp.latexify()

with lp.figure("num_matches_vs_bis",size=lp.figure_size(ratio=0.6,doc_width_pt=500),tight_layout=False):
    fig, axs = plt.subplots(1,2,sharey=True,constrained_layout=True)
    axs[0].hexbin(np.concatenate([bis_scores[i][0] for i in range(4)]),np.concatenate([bis_scores[i][1] for i in range(4)]),gridsize=20,bins='log',cmap='viridis')
    hb = axs[1].hexbin(np.concatenate([bis_scores[i][0] for i in range(5,8)]),np.concatenate([bis_scores[i][1] for i in range(5,8)]),gridsize=20,bins='log',cmap='viridis')
    axs[0].axis('scaled')
    axs[1].axis('scaled')
    axs[0].set_xlabel("Beam image-shift X [µm]")
    axs[1].set_xlabel("Beam image-shift X [µm]")
    axs[0].set_ylabel("Beam image-shift Y [µm]")
    axs[0].set_title("Eucentric Focus")
    axs[1].set_title("Fringe-free Focus")
    axs[0].set_xlim(-6,6)
    axs[0].set_ylim(-10,8)
    axs[1].set_xlim(-6,6)
    axs[1].set_ylim(-10,8)

    cb = fig.colorbar(hb, ax=axs[1], label='Detected targets')
