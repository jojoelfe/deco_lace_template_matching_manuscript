import matplotlib.pyplot as plt
import latexipy as lp
import utils
import starfile
from pathlib import Path
import numpy as np
from scipy.stats import mannwhitneyu
import json
from vedo import *
import utils as ut
#bis_scores = []
#
#for dataset, name in utils.dataset_info:
#    assembled_directory = Path("/scratch/bern/elferich/deco_lace_manuscript_processing/assemble/")
#    data  =  starfile.read(assembled_directory / f"{name}_assembled_matches.star")
#    bis_scores.append((data[data["display"]]["tile_image_shift_x"],data[data["display"]]["tile_image_shift_y"],data[data["display"]]["peak_value"]))


for dataset, name in ut.dataset_info[:]:
    plt = Plotter()
    assembled_directory = Path("/scratch/bern/elferich/deco_lace_manuscript_processing/assemble/")
    datan  =  starfile.read(assembled_directory / f"{name}_assembled_matches.star")
    x = datan[datan["display"]]["x"]
    y = datan[datan["display"]]["y"]
    z = datan[datan["display"]]["defocus"]
    data = np.stack((x,y,z), axis=1)
    plt += Points(data, r=10, c="yellow")
    plane = fitPlane(data).c("green4")  # fit a plane
    print("Plane Fit normal =", plane.normal)
    # Calculate angle from normal in degrees
    angle = np.arccos(plane.normal[2]) * 180 / np.pi
    print("Angle from normal =", angle)




    plt += [plane, __doc__]

    plt.show(axes=1).close()

        