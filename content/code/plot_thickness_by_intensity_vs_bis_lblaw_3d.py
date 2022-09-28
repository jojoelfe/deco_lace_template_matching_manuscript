import matplotlib.pyplot as plt
import numpy as np
import latexipy as lp
import json
from pathlib import Path
from vedo import *
settings.defaultFont = "Theemim"
settings.useParallelProjection = True
import utils
defocus = []

lp.latexify()

for dataset, name in utils.dataset_info[:1]:
    selected_micrographs = utils.get_data_from_db(dataset)
    with open(Path(dataset).stem +"_thickness.json","r") as fp:
        thickness_data = json.load(fp)
    defocus = [[thickness_data[m['movie_filename']],m['IMAGE_SHIFT_X'],m['IMAGE_SHIFT_Y']] for i,m in selected_micrographs.iterrows() if m['movie_filename'] in thickness_data ]

    with lp.figure(f"thickness_by_intensity_vs_bs_plot_{name}_lblawxx",size=lp.figure_size(ratio=1.0,doc_width_pt=250),tight_layout=True):
        cm = plt.cm.get_cmap('viridis')
        data_euc = np.array(defocus,dtype=float)
        # Average all values over 0.3 in data_euc[:,0]
        if name.startswith("euc"):
            thresh = 0.3
        else:
            thresh = 0.28
        average = np.mean(data_euc[data_euc[:,0]>thresh,0])
        
        data_euc[:,0] = - np.log(data_euc[:,0]/average) * 322
        print(data_euc[:,0])
        #plt.hist(data_euc[:,0],bins=100,color='k',alpha=0.5)
        # iterate over data points in data_euc
        cols = colorMap(data_euc[:,0], "RdYlBu",vmin=0,vmax=300)

        items = []
        k = 0
        for i in range(len(data_euc[:,0])):
            hexa = Circle([data_euc[i,1],data_euc[i,2]], r=0.15, res=6)
            col = cols[i]
            if data_euc[i,0] > 300:
                continue
            hbar = hexa.extrude(data_euc[i,0]/100) # create the hex bar
            hbar.lighting("default").flat().c(col)
            #txt = Text3D(precision(val,3), [x,y,z], s=.12, justify='center', c='k')
            items += [hbar]
            k += 1

        show(items, axes=dict(xtitle="Beam-Image Shift X [µm]",
                              ytitle="Beam-Image Shift Y [µm]",
                              ztitle="Thickness [x10 nm]"))



        if False:
            if name.startswith("euc"):
                s = 9
            else:
                s = 11
            sc = plt.scatter(data_euc[:,1],data_euc[:,2],c=data_euc[:,0], cmap=cm,vmin=10,vmax=300.0,marker='H',s=s)
            
            plt.axis('scaled')
            plt.xlabel("Beam-Image Shift X [µm]")
            plt.ylabel("Beam-Image Shift Y [µm]")
            plt.xlim(-6,6)
            plt.ylim(-10,8)

exit()
for dataset, name in utils.dataset_info[:1]:
    selected_micrographs = utils.get_data_from_db(dataset)
    with open(Path(dataset).stem +"_thickness.json","r") as fp:
        thickness_data = json.load(fp)
    defocus = [[thickness_data[m['movie_filename']],m['IMAGE_SHIFT_X'],m['IMAGE_SHIFT_Y']] for i,m in selected_micrographs.iterrows() if m['movie_filename'] in thickness_data ]

    with lp.figure(f"thickness_by_intensity_vs_bs_plot_colorbar_lblaw",size=lp.figure_size(ratio=2.5,doc_width_pt=100),tight_layout=True):
        cm = plt.cm.get_cmap('viridis')
        data_euc = np.array(defocus,dtype=float)
        average = np.mean(data_euc[data_euc[:,0]>0.3,0])
        
        data_euc[:,0] = - np.log(data_euc[:,0]/average) * 322.0
        if name.startswith("euc"):
            s = 9
        else:
            s = 11
        sc = plt.scatter(data_euc[:,1],data_euc[:,2],c=data_euc[:,0], cmap=cm,vmin=10,vmax=300.0,marker='H',s=s)
        
        plt.axis('scaled')
        plt.xlabel("Beam-Image Shift X [µm]")
        plt.ylabel("Beam-Image Shift Y [µm]")
        plt.xlim(-6,6)
        plt.ylim(-10,8)
        plt.gca().set_visible(False)
        plt.colorbar(sc, shrink=1.0,label="Thickness [nm]")
