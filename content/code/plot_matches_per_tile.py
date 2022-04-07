import matplotlib.pyplot as plt
import latexipy as lp
import utils
import starfile
from pathlib import Path
import numpy as np

matches_per_tile = []

for dataset, name in utils.dataset_info:
    assembled_directory = Path("/scratch/bern/elferich/deco_lace_manuscript_processing/assemble/")
    data  =  starfile.read(assembled_directory / f"{name}_assembled_matches.star")
    #Count occurence of tile_filename in data
    counts = data["tile_filename"].value_counts()
    counts = counts[counts > 1]
    matches_per_tile.append(counts)

lp.latexify()
with lp.figure("matches_per_tile_plot",tight_layout=False):
    flierprops = dict(marker='o', markerfacecolor='grey', markeredgecolor='grey', markersize=2, linestyle='none')

    fig, axs = plt.subplots(1,2,sharey=True,constrained_layout=True)
    bp1 = axs[0].boxplot(matches_per_tile[0:4],flierprops=flierprops)
    bp2 = axs[1].boxplot(matches_per_tile[4:8],flierprops=flierprops)
    axs[0].set_title("Eucentric Focus")
    axs[1].set_title("Fringe-free Focus")
    axs[0].set_xlabel("Lamella")
    axs[1].set_xlabel("Lamella")
    axs[0].set_ylabel("Matches per tile")
    axs[0].set_xticks([1,2,3,4])
    axs[1].set_xticks([1,2,3,4])
    axs[0].set_ylim(0,100)

    pos = np.arange(4) + 1
    upper_labels = [f"n={len(s)}" for s in matches_per_tile[0:4]]
    weights = ['bold', 'semibold']
    for tick, label in zip(range(4), axs[0].get_xticklabels()):
        k = tick % 2
        axs[0].text(pos[tick], .92, upper_labels[tick],
                transform=axs[0].get_xaxis_transform(),
                horizontalalignment='center', size='x-small',
                )
    upper_labels = [f"n={len(s)}" for s in matches_per_tile[4:8]]
    weights = ['bold', 'semibold']
    for tick, label in zip(range(4), axs[1].get_xticklabels()):
        k = tick % 2
        axs[1].text(pos[tick], .92, upper_labels[tick],
                transform=axs[1].get_xaxis_transform(),
                horizontalalignment='center', size='x-small',
                )

