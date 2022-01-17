import matplotlib.pyplot as plt
import numpy as np
import latexipy as lp
import json
from pathlib import Path


import utils

intensity = []
dataset = utils.datasets[0]
selected_micrographs = utils.get_data_from_db(dataset)
with open(Path(dataset).stem +"_thickness.json","r") as fp:
    thickness_data = json.load(fp)
intensity = [[thickness_data[m['movie_filename']],m['IMAGE_SHIFT_X'],m['IMAGE_SHIFT_Y']] for i,m in selected_micrographs.iterrows()]



lp.latexify()
with lp.figure("thickness_by_intensity_vs_bs_plot",size=lp.figure_size(ratio=0.5,doc_width_pt=500),tight_layout=False):
    cm = plt.cm.get_cmap('viridis')
    fig, axs = plt.subplots(1,2,sharey=True,constrained_layout=True)
    #data_euc = np.array(defocus[0],dtype=float)
    #axs[0].scatter(data_euc[:,1],data_euc[:,2],c=data_euc[:,0], cmap=cm,vmin=0,vmax=3000)
    data_ff = np.array(intensity,dtype=float)
    sc = axs[1].scatter(data_ff[:,1],data_ff[:,2],c=data_ff[:,0], cmap=cm,vmin=0.1,vmax=0.25)

    axs[0].set_xlabel("Image Shift X [µm]")
    axs[1].set_xlabel("Image Shift X [µm]")
    axs[0].set_ylabel("Image Shift Y [µm]")
    axs[0].set_title("Eucentric Focus")
    axs[1].set_title("Fringe-Free Focus")

    fig.colorbar(sc, ax=axs[1], shrink=1.0,label="Astigmatism [Å]")

