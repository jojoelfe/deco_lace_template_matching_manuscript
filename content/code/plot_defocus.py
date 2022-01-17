import matplotlib.pyplot as plt
import latexipy as lp
import utils

defocus = []

for dataset in utils.datasets:
    
    selected_micrographs = utils.get_data_from_db(dataset)
    defocus.append([(m["DEFOCUS1"]+m["DEFOCUS2"])/2 for i,m in selected_micrographs.iterrows() if m['SCORE']>0.05 and m['DETECTED_RING_RESOLUTION'] < 15])

lp.latexify()
with lp.figure("defocusplot"):
    flierprops = dict(marker='o', markerfacecolor='grey', markeredgecolor='grey', markersize=2, linestyle='none')
    fig, axs = plt.subplots(1,2,sharey=True)
    axs[0].boxplot(defocus[0:4],flierprops=flierprops)
    axs[1].boxplot(defocus[4:8],flierprops=flierprops)
    axs[0].set_title("Eucentric Focus")
    axs[1].set_title("Fringe-free Focus")
    axs[0].set_xlabel("Lamella")
    axs[1].set_xlabel("Lamella")
    axs[0].set_ylabel("Defocus [Å]")
    axs[0].set_yticks([0,4000,8000,12000,16000,20000])

