import matplotlib.pyplot as plt
import latexipy as lp
import utils
import starfile
from pathlib import Path
from mpl_toolkits.axes_grid1 import make_axes_locatable

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
    fig, ax = plt.subplots()
    hb = ax.hexbin(phis, thetas, bins='log', cmap="viridis", gridsize=20)
    ax.set(xlim=(0, 180), ylim=(0, 180))
    ax.set_xlabel('$\phi$ (rlnAngleRot, deg)')
    ax.set_xticks(range(0, 181, 45))
    ax.set_ylabel('$\\theta$ (rlnAngleTilt, deg)')
    ax.set_yticks(range(0, 181, 45))
    ax.set_title("Ribosome orientation distribution")
    fig.gca().set_aspect('equal', adjustable='box')
    divider = make_axes_locatable(ax)
    cax = divider.append_axes('right', size='5%', pad=0.1)
    cb = fig.colorbar(hb, ax=ax, cax=cax)
    cb.set_label('Number of particles')
    fig.tight_layout()
    
