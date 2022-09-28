import matplotlib.pyplot as plt
import latexipy as lp
import utils
import starfile
from pathlib import Path
import numpy as np
from scipy.stats import mannwhitneyu
import json

#bis_scores = []
#
#for dataset, name in utils.dataset_info:
#    assembled_directory = Path("/scratch/bern/elferich/deco_lace_manuscript_processing/assemble/")
#    data  =  starfile.read(assembled_directory / f"{name}_assembled_matches.star")
#    bis_scores.append((data[data["display"]]["tile_image_shift_x"],data[data["display"]]["tile_image_shift_y"],data[data["display"]]["peak_value"]))

lp.latexify()
thickness = []
match_range = []
for dataset, name in utils.dataset_info[:]:
    assembled_directory = Path("/scratch/bern/elferich/deco_lace_manuscript_processing/assemble/")
    data  =  starfile.read(assembled_directory / f"{name}_assembled_matches.star")

    selected_micrographs = data[data["display"]]["tile_movie_filename"].unique()

    
    
    
    with open(Path(dataset).stem +"_thickness.json","r") as fp:
        thickness_data = json.load(fp)
    thicknesses = np.array(list(thickness_data.values()),dtype=float)
    print(thicknesses)
    # Average all values over 0.3 in data_euc[:,0]
    if name.startswith("euc"):
        thresh = 0.3
    else:
        thresh = 0.28
    print(thresh)
    average = np.mean(thicknesses[thicknesses>thresh])
    print(average)
    for m in selected_micrographs:
        thickness.append(- np.log(thickness_data[m]/average) * 322)
        hits = data[data["display"] & (data["tile_movie_filename"] == m)]
        z_positions = hits["defocus"]
        # get 90% percentile range of z positions
        match_range.append((np.percentile(z_positions,90) - np.percentile(z_positions,10))/10)
        #range = (np.max(z_positions) - np.min(z_positions)) / 10
        #match_range.append(range)
with lp.figure(f"matchrange_vs_thickness_plot",size=lp.figure_size(ratio=1.0,doc_width_pt=250),tight_layout=True):
    plt.scatter(thickness,match_range,s=0.5)
    # Ensure that the axes are equal
    plt.gca().set_aspect('equal', adjustable='box')
    # Set range of axes
    plt.xlim(0,300)
    plt.ylim(0,300)
    plt.xlabel("Thickness (nm)")
    plt.ylabel("Match range (nm)")
    # Draw line of equality
    plt.plot([0,300],[0,300],color="black",linestyle="--")
    # PLot line 50 nm lower
    plt.plot([0,300],[-70,230],color="red",linestyle=":")

        