from re import sub
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import latexipy as lp
import mrcfile
from mpl_toolkits.axes_grid1 import make_axes_locatable


lp.latexify()

def plot(mip,subarea,name):
    with lp.figure(f"crop_unblur_mip_{name}",size=lp.figure_size(ratio=0.6667,doc_width_pt=300),tight_layout=True):
        #fig, (axCenter,axright) = plt.subplots(1,2)
        axCenter = plt.subplot2grid((2, 2), (0, 0), colspan=2,rowspan=2)
        
        sumvertical = np.max(subarea, 0)
        xvert = range(np.shape(subarea)[1])

        sumhoriz = np.max(subarea, 1)
        yhoriz = range(np.shape(subarea)[0])

        divider = make_axes_locatable(axCenter)
        axvert = divider.append_axes('right', size='30%', pad=0.1)
        axhoriz = divider.append_axes('top', size='30%', pad=0.1)

        axCenter.imshow(subarea,cmap="Greys", origin='lower',vmin=4.0,vmax=8.0)
        axhoriz.plot(xvert, sumvertical)
        axvert.plot(sumhoriz, yhoriz)

        axhoriz.margins(x=0)
        axhoriz.axes.xaxis.set_visible(False)
        axhoriz.set_yticks([6,8,10])
        axvert.margins(y=0)
        axvert.axes.yaxis.set_visible(False)
        axvert.set_xticks([6,8,10])

  

mip_filename = "/scratch/bern/elferich/ER_HoxB8_undiff_spot/Assets/TemplateMatching/s_record_00192_0.0_1420_6_scaled_mip_1420_1.mrc"
with mrcfile.open(mip_filename) as mrc:
    mip = mrc.data
subarea = mip[0,1800:2200,3020:3500]

plot(mip,subarea,"final_alignment")

mip_filename = "/scratch/bern/elferich/ER_HoxB8_undiff_spot/Assets/TemplateMatching/s_record_00192_0.0_trunc_gain_1959_0_scaled_mip_1959_0.mrc"
with mrcfile.open(mip_filename) as mrc:
    mip = mrc.data
subarea = mip[0,900:1300,1750:2250]

plot(mip,subarea,"cropped_alignment")

mip_filename = "/scratch/bern/elferich/ER_HoxB8_undiff_spot/Assets/TemplateMatching/s_record_00192_0.0_1420_0_scaled_mip_1420_0.mrc"
with mrcfile.open(mip_filename) as mrc:
    mip = mrc.data
subarea = mip[0,1800:2200,3020:3500]

plot(mip,subarea,"initial_alignment")