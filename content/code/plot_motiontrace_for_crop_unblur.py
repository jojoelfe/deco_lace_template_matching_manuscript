from re import sub
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import latexipy as lp
import mrcfile
import pandas as pd
import contextlib
import sqlite3
from mpl_toolkits.axes_grid1 import make_axes_locatable


lp.latexify()

def plot(df,name):
    with lp.figure(f"crop_unblur_motiontrace_{name}",size=lp.figure_size(ratio=0.667,doc_width_pt=300),tight_layout=True):
       plt.plot(df["FRAME_NUMBER"],df["X_SHIFT"],label="X")
       plt.plot(df["FRAME_NUMBER"],df["Y_SHIFT"],label="Y")

       plt.xlim(0,32)
       plt.ylim(-10,29)

       plt.xlabel("Frame")
       plt.ylabel("Shift [Å]")

       plt.legend()
       

  
database = "/scratch/bern/elferich/ER_HoxB8_undiff_spot/ER_HoxB8_undiff_spot.db"

with contextlib.closing(sqlite3.connect(database)) as con:
    df = pd.read_sql_query("SELECT * FROM MOVIE_ALIGNMENT_PARAMETERS_1420",con)

plot(df,"initial")

with contextlib.closing(sqlite3.connect(database)) as con:
    df = pd.read_sql_query("SELECT * FROM MOVIE_ALIGNMENT_PARAMETERS_1959",con)

plot(df,"cropped")

with contextlib.closing(sqlite3.connect(database)) as con:
    df = pd.read_sql_query("SELECT * FROM MOVIE_ALIGNMENT_PARAMETERS_1965",con)

plot(df,"final")