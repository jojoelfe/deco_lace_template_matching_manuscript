import matplotlib.pyplot as plt
import latexipy as lp
import utils
import starfile
from pathlib import Path
import numpy as np
from scipy.stats import mannwhitneyu

scores = []

for dataset, name in utils.dataset_info:
    assembled_directory = Path("/scratch/bern/elferich/deco_lace_manuscript_processing/assemble/")
    data  =  starfile.read(assembled_directory / f"{name}_assembled_matches.star")
    scores.append(data[data["display"]]["peak_value"])

# Combine scores into a single numpy array
a = np.concatenate(scores[0:4])
b = np.concatenate(scores[4:8])

res = mannwhitneyu(scores[0],scores[1])
print(res.statistic / (len(scores[0])*len(scores[1])))

res = mannwhitneyu(a,b)
print(res.statistic / (len(a)*len(b)))

lp.latexify()

with lp.figure("scores_plot",tight_layout=False):
    flierprops = dict(marker='o', markerfacecolor='grey', markeredgecolor='grey', markersize=2, linestyle='none')

    fig, axs = plt.subplots(1,2,sharey=True,constrained_layout=True)
    axs[0].boxplot(scores[0:4],flierprops=flierprops)
    axs[1].boxplot(scores[4:8],flierprops=flierprops)
    axs[0].set_title(f"Eucentric Focus \n M = {np.median(np.concatenate(scores[0:4])):.1f}")
    axs[1].set_title(f"Fringe-free Focus \n M = {np.median(np.concatenate(scores[4:8])):.1f}")
    axs[0].set_xlabel("Lamella")
    axs[1].set_xlabel("Lamella")
    axs[0].set_ylabel("2DTM SNR")
    axs[0].set_xticks([1,2,3,4])
    axs[1].set_xticks([1,2,3,4])
    axs[0].set_ylim(4.0,16.5)
    axs[1].set_ylim(4.0,16.5)

    pos = np.arange(4) + 1
    upper_labels = [f"n={len(s)}\nM={np.median(s):.1f}" for s in scores[0:4]]
    weights = ['bold', 'semibold']
    for tick, label in zip(range(4), axs[0].get_xticklabels()):
        k = tick % 2
        axs[0].text(pos[tick], .88, upper_labels[tick],
                transform=axs[0].get_xaxis_transform(),
                horizontalalignment='center', size='xx-small',
                )
    
    pos = np.arange(4) + 1
    upper_labels = [f"n={len(s)}\nM={np.median(s):.1f}" for s in scores[4:8]]
    weights = ['bold', 'semibold']
    for tick, label in zip(range(4), axs[1].get_xticklabels()):
        k = tick % 2
        axs[1].text(pos[tick], .88, upper_labels[tick],
                transform=axs[1].get_xaxis_transform(),
                horizontalalignment='center', size='xx-small',
                )
#
