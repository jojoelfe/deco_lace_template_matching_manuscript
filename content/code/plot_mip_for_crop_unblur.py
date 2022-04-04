from re import sub
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import latexipy as lp
import mrcfile
from mpl_toolkits.axes_grid1 import make_axes_locatable


mip_filename = "/scratch/bern/elferich/ER_Hox_undiff_spot/"
with mrcfile.open(mip_filename) as mrc:
    mip = mrc.data
subarea = mip[0,1196:1696,1785:2285]


lp.latexify()
with lp.figure("initial_map_match",size=lp.figure_size(ratio=0.6667,doc_width_pt=500),tight_layout=True):
    #fig, (axCenter,axright) = plt.subplots(1,2)
    axCenter = plt.subplot2grid((2, 3), (0, 0), colspan=2,rowspan=2)
    
    sumvertical = np.max(subarea, 0)
    xvert = range(np.shape(subarea)[1])

    sumhoriz = np.max(subarea, 1)
    yhoriz = range(np.shape(subarea)[0])

    divider = make_axes_locatable(axCenter)
    axvert = divider.append_axes('right', size='30%', pad=0.1)
    axhoriz = divider.append_axes('top', size='30%', pad=0.1)

    axCenter.imshow(subarea,cmap="Greys", origin='lower')
    axhoriz.plot(xvert, sumvertical)
    axvert.plot(sumhoriz, yhoriz)

    axhoriz.margins(x=0)
    axhoriz.axes.xaxis.set_visible(False)
    axhoriz.set_yticks([6,8,10])
    axvert.margins(y=0)
    axvert.axes.yaxis.set_visible(False)
    axvert.set_xticks([6,8,10])

    # Create a Rectangle patch
    rect = patches.Rectangle((60, 40), 20, 20, linewidth=1, edgecolor='r', facecolor='none')
    rect2 = patches.Rectangle((333, 156), 20, 20, linewidth=1, edgecolor='b', facecolor='none')
    # Add the patch to the Axes
    axCenter.add_patch(rect)
    axCenter.add_patch(rect2)

    ax3d1 = plt.subplot2grid((2, 3), (0, 2), projection='3d')

    subsubarea = subarea[40:60,60:80]
    X, Y = np.meshgrid(range(20),range(20))
    ax3d1.plot_surface(X,Y,Z=subsubarea, rstride=1, cstride=1,
                    cmap='viridis', edgecolor='none')

    ax3d2 = plt.subplot2grid((2, 3), (1, 2), projection='3d')

    subsubarea = subarea[156:176,333:353]
    X, Y = np.meshgrid(range(20),range(20))
    ax3d2.plot_surface(X,Y,Z=subsubarea, rstride=1, cstride=1,
                    cmap='viridis', edgecolor='none')