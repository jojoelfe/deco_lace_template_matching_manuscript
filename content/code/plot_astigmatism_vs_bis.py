import matplotlib.pyplot as plt
import numpy as np
import latexipy as lp


import utils

defocus = []

lp.latexify()

for dataset, name in utils.dataset_info:
    selected_micrographs = utils.get_data_from_db(dataset)
    defocus = [[m["DEFOCUS1"]-m["DEFOCUS2"],m['IMAGE_SHIFT_X'],m['IMAGE_SHIFT_Y']] for i,m in selected_micrographs.iterrows() if m['SCORE']>0.05 and m['DETECTED_RING_RESOLUTION'] < 15]



    with lp.figure(f"defocus_astigmatism_vs_bs_plot_{name}",size=lp.figure_size(ratio=1.0,doc_width_pt=250),tight_layout=True):
        cm = plt.cm.get_cmap('viridis')
        data_euc = np.array(defocus,dtype=float)
        if name.startswith("euc"):
            s = 9
        else:
            s = 11
        sc = plt.scatter(data_euc[:,1],data_euc[:,2],c=data_euc[:,0], cmap=cm,vmin=0000,vmax=3000,marker='H',s=s)
        plt.axis('scaled')
        plt.xlabel("Beam-Image Shift X [µm]")
        plt.ylabel("Beam-Image Shift Y [µm]")
        plt.xlim(-6,6)
        plt.ylim(-10,8)

        #plt.colorbar(sc, shrink=1.0,label="Defocus [Å]")
for dataset, name in utils.dataset_info[-1:]:
    selected_micrographs = utils.get_data_from_db(dataset)
    defocus = [[m["DEFOCUS1"]-m["DEFOCUS2"],m['IMAGE_SHIFT_X'],m['IMAGE_SHIFT_Y']] for i,m in selected_micrographs.iterrows() if m['SCORE']>0.05 and m['DETECTED_RING_RESOLUTION'] < 15]



    with lp.figure(f"defocus_astigmatism_vs_bs_plot_colorbar",size=lp.figure_size(ratio=2.5,doc_width_pt=100),tight_layout=True):
        cm = plt.cm.get_cmap('viridis')
        data_euc = np.array(defocus,dtype=float)
        if name.startswith("euc"):
            s = 8
        else:
            s = 10
        sc = plt.scatter(data_euc[:,1],data_euc[:,2],c=data_euc[:,0], cmap=cm,vmin=0000,vmax=3000,marker='H',s=s)
        plt.axis('scaled')
        plt.xlabel("Beam-Image Shift X [µm]")
        plt.ylabel("Beam-Image Shift Y [µm]")
        plt.xlim(-7,7)
        plt.ylim(-11,9)
        plt.gca().set_visible(False)
        plt.colorbar(sc, shrink=1.0,label="Astigmatism [Å]")


