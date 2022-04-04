import matplotlib.pyplot as plt
import numpy as np
import latexipy as lp


import utils

defocus = []
lp.latexify()
for dataset, name in utils.dataset_info:
    selected_micrographs = utils.get_data_from_db(dataset,get_movement=True)
    defocus = [[m["TOTAL_MOVEMENT"],m['IMAGE_SHIFT_X'],m['IMAGE_SHIFT_Y']] for i,m in selected_micrographs.iterrows()]



    with lp.figure(f"movement_vs_bs_plot_{name}",size=lp.figure_size(ratio=1.0,doc_width_pt=250),tight_layout=True):
        cm = plt.cm.get_cmap('viridis')
        data_euc = np.array(defocus,dtype=float)
        sc =plt.scatter(data_euc[:,1],data_euc[:,2],c=data_euc[:,0], cmap=cm,vmin=0,vmax=50)
       
        plt.xlabel("Image Shift X [µm]")
        plt.ylabel("Image Shift Y [µm]")
        plt.xlim(-6,6)
        plt.ylim(-10,8)
        #fig.colorbar(sc, ax=axs[1], shrink=1.0,label="Total movement [Å]")

for dataset, name in utils.dataset_info[-1:]:
    selected_micrographs = utils.get_data_from_db(dataset,get_movement=True)
    defocus = [[m["TOTAL_MOVEMENT"],m['IMAGE_SHIFT_X'],m['IMAGE_SHIFT_Y']] for i,m in selected_micrographs.iterrows()]



    with lp.figure(f"movement_vs_bs_plot_colorbar",size=lp.figure_size(ratio=2.5,doc_width_pt=100),tight_layout=True):
        cm = plt.cm.get_cmap('viridis')
        data_euc = np.array(defocus,dtype=float)
        sc =plt.scatter(data_euc[:,1],data_euc[:,2],c=data_euc[:,0], cmap=cm,vmin=0,vmax=50)
       
        plt.xlabel("Image Shift X [µm]")
        plt.ylabel("Image Shift Y [µm]")
        plt.xlim(-6,6)
        plt.ylim(-10,8)
        plt.gca().set_visible(False)
        plt.colorbar(sc, ax=axs[1], shrink=1.0,label="Total movement [Å]")
