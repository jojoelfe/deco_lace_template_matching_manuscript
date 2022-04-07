import matplotlib.pyplot as plt
import latexipy as lp
import utils
import starfile
from pathlib import Path

num_matches = []

for dataset, name in utils.dataset_info:
    assembled_directory = Path("/scratch/bern/elferich/deco_lace_manuscript_processing/assemble/")
    data  =  starfile.read(assembled_directory / f"{name}_assembled_matches.star")
    num_matches.append(len(data[data["display"]]))

lp.latexify()
with lp.figure("num_matches_plot",tight_layout=True):
    fig, axs = plt.subplots(1,2,sharey=True)
    axs[0].bar(range(1,5),num_matches[0:4], align='center', color='grey', edgecolor='black', linewidth=0.5)
    axs[1].bar(range(1,5),num_matches[4:8], align='center', color='grey', edgecolor='black', linewidth=0.5)
    axs[0].set_title("Eucentric Focus")
    axs[1].set_title("Fringe-free Focus")
    axs[0].set_xlabel("Lamella")
    axs[1].set_xlabel("Lamella")
    axs[0].set_ylabel("# Matches")
    axs[0].set_xticks([1,2,3,4])
    axs[1].set_xticks([1,2,3,4])
    plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
