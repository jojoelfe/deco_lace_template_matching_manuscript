from re import sub
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import latexipy as lp
import mrcfile
from mpl_toolkits.axes_grid1 import make_axes_locatable


mip_filename = "/scratch/bern/elferich/the_special_micrograph_and_lamella/CF4-g1_00185_-20.0_186_0_scaled_mip_186_0.mrc"
with mrcfile.open(mip_filename) as mrc:
    mip = mrc.data
subarea = mip[0,1196:1696,1785:2285]


lp.latexify()
with lp.figure("initial_map_match",size=lp.figure_size(ratio=0.6666,doc_width_pt=500),tight_layout=True):
    #plt.rcParams['figure.constrained_layout.use'] = True
    #fig, (axCenter,axright) = plt.subplots(1,2)
    axCenter = plt.subplot2grid((4, 6), (1, 0), colspan=3,rowspan=3)
    axvert = plt.subplot2grid((4, 6), (1, 3), colspan=1,rowspan=3)
    axhoriz = plt.subplot2grid((4, 6), (0, 0), colspan=3,rowspan=1)

    sumvertical = np.max(subarea, 0)
    xvert = range(np.shape(subarea)[1])

    sumhoriz = np.max(subarea, 1)
    yhoriz = range(np.shape(subarea)[0])

    #divider = make_axes_locatable(axCenter)
    #axvert = divider.append_axes('right', size='30%', pad=0.1)
    #axhoriz = divider.append_axes('top', size='30%', pad=0.1)

    axCenter.imshow(subarea,cmap="Greys", origin='lower')
    axCenter.xaxis.set_visible(False)
    axCenter.yaxis.set_visible(False)
    axhoriz.plot(xvert, sumvertical)
    axvert.plot(sumhoriz, yhoriz)

    axhoriz.margins(x=0)
    axhoriz.axes.xaxis.set_visible(False)
    axhoriz.set_yticks([6,8,10])
    axhoriz.set_ylabel("2DTM SNR")
    axvert.margins(y=0)
    axvert.axes.yaxis.set_visible(False)
    axvert.set_xticks([6,8,10])
    axvert.set_xlabel("2DTM SNR")

    # Create a Rectangle patch
    rect = patches.Rectangle((60, 40), 20, 20, linewidth=1, edgecolor='r', facecolor='none')
    rect2 = patches.Rectangle((333, 156), 20, 20, linewidth=1, edgecolor='b', facecolor='none')
    # Add the patch to the Axes
    axCenter.add_patch(rect)
    axCenter.add_patch(rect2)

    ax3d1 = plt.subplot2grid((4, 6), (0, 4),colspan=2,rowspan=2, projection='3d')

    subsubarea = subarea[40:60,60:80]
    X, Y = np.meshgrid(range(20),range(20))
    ax3d1.plot_surface(X,Y,Z=subsubarea, rstride=1, cstride=1,
                    cmap='viridis', edgecolor='none')
    ax3d1.set_zlabel('2DTM SNR')
    ax3d1.set_zticks([6,8,10])
    ax3d1.w_xaxis.line.set_color("red")
    ax3d1.w_yaxis.line.set_color("red")
    ax3d1.set_xticklabels([])
    ax3d1.set_yticklabels([])

    ax3d2 = plt.subplot2grid((4, 6), (2, 4),colspan=2,rowspan=2, projection='3d')

    subsubarea = subarea[156:176,333:353]
    X, Y = np.meshgrid(range(20),range(20))
    ax3d2.plot_surface(X,Y,Z=subsubarea, rstride=1, cstride=1,
                    cmap='viridis', edgecolor='none')
    ax3d2.set_zlabel('2DTM SNR')
    ax3d2.set_zticks([6,8,10])
    ax3d2.w_xaxis.line.set_color("blue")
    ax3d2.w_yaxis.line.set_color("blue")
    ax3d2.set_xticklabels([])
    ax3d2.set_yticklabels([])