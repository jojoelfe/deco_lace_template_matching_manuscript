import matplotlib.pyplot as plt
import latexipy as lp
import utils
import starfile
from pathlib import Path

phis = []
thetas = []
psis = []

for dataset, name in utils.dataset_info:
    assembled_directory = Path("/scratch/bern/elferich/deco_lace_manuscript_processing/assemble/")
    data  =  starfile.read(assembled_directory / f"{name}_assembled_matches.star")
    phis += data[data["display"]]["phi"].tolist()
    thetas += data[data["display"]]["theta"].tolist()
    psis += data[data["display"]]["psi"].tolist()

lp.latexify()
with lp.figure("orientation_dist",tight_layout=True):
    fig, axs = plt.subplots(1,3,sharey=True)
    axs[0].hist(phis, bins=100, color='grey', edgecolor='black', linewidth=0.5)
    axs[0].set_title("Phi")
    axs[1].hist(thetas, bins=100, color='grey', edgecolor='black', linewidth=0.5)
    axs[1].set_title("Theta")
    axs[2].hist(psis, bins=100, color='grey', edgecolor='black', linewidth=0.5)
    axs[2].set_title("Psi")
    #axs[1].bar(range(1,5),num_matches[4:8], align='center', color='grey', edgecolor='black', linewidth=0.5)
    #axs[0].set_title("Eucentric Focus")
    
