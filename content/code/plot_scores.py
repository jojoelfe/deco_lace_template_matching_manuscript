import matplotlib.pyplot as plt
import latexipy as lp
import utils
import starfile
from pathlib import Path

scores = []

for dataset, name in utils.dataset_info:
    assembled_directory = Path("/scratch/bern/elferich/deco_lace_manuscript_processing/assemble/")
    data  =  starfile.read(assembled_directory / f"{name}_assembled_matches.star")
    scores.append(data[data["display"]]["peak_value"])

lp.latexify()
with lp.figure("scores_plot",tight_layout=False):
    flierprops = dict(marker='o', markerfacecolor='grey', markeredgecolor='grey', markersize=2, linestyle='none')

    fig, axs = plt.subplots(1,2,sharey=True,constrained_layout=True)
    axs[0].boxplot(scores[0:4],flierprops=flierprops)
    axs[1].boxplot(scores[4:8],flierprops=flierprops)
    axs[0].set_title("Eucentric Focus")
    axs[1].set_title("Fringe-free Focus")
    axs[0].set_xlabel("Lamella")
    axs[1].set_xlabel("Lamella")
    axs[0].set_ylabel("Peak height")
    axs[0].set_xticks([1,2,3,4])
    axs[1].set_xticks([1,2,3,4])

