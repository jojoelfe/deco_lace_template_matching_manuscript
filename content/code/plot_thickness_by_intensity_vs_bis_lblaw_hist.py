import matplotlib.pyplot as plt
import numpy as np
import latexipy as lp
import json
from pathlib import Path


import utils
defocus = []

thicknesses = np.array([])

lp.latexify()

for dataset, name in utils.dataset_info[:]:
    selected_micrographs = utils.get_data_from_db(dataset)
    with open(Path(dataset).stem +"_thickness.json","r") as fp:
        thickness_data = json.load(fp)
    defocus = [[thickness_data[m['movie_filename']],m['IMAGE_SHIFT_X'],m['IMAGE_SHIFT_Y']] for i,m in selected_micrographs.iterrows() if m['movie_filename'] in thickness_data ]

    data_euc = np.array(defocus,dtype=float)
    # Average all values over 0.3 in data_euc[:,0]
    if name.startswith("euc"):
        thresh = 0.3
    else:
        thresh = 0.28
    average = np.mean(data_euc[data_euc[:,0]>thresh,0])
    
    data_euc[:,0] = - np.log(data_euc[:,0]/average) * 322
    print(data_euc[:,0])
    thicknesses = np.append(thicknesses,data_euc[:,0])
    #plt.hist(data_euc[:,0],bins=100,color='k',alpha=0.5)

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
    with lp.figure(f"thickness_by_intensity_vs_bs_plo_lblaw_hist",size=lp.figure_size(ratio=1.0,doc_width_pt=250),tight_layout=True):
        plt.hist(thicknesses,bins=100,color='k',alpha=0.5,range=[70,300])

