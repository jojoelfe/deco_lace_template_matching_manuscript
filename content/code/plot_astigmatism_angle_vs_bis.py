import matplotlib.pyplot as plt
import sqlite3
import pandas as pd
import os
import contextlib
import numpy as np

import datasets

defocus = []

for dataset in datasets.datasets:
    print(dataset)
    with contextlib.closing(sqlite3.connect(dataset)) as con:

        df1 = pd.read_sql_query(f"SELECT IMAGE_ASSET_ID,MOVIE_ASSET_ID,IMAGE_ASSETS.FILENAME, MOVIE_ASSETS.FILENAME as movie_filename, CTF_ESTIMATION_ID ,IMAGE_ASSETS.PIXEL_SIZE as image_pixel_size, MOVIE_ASSETS.PIXEL_SIZE as movie_pixel_size, IMAGE_ASSETS.X_SIZE, IMAGE_ASSETS.Y_SIZE  FROM IMAGE_ASSETS INNER JOIN MOVIE_ASSETS ON MOVIE_ASSETS.MOVIE_ASSET_ID == IMAGE_ASSETS.PARENT_MOVIE_ID", con)
        df2 = pd.read_sql_query("SELECT CTF_ESTIMATION_ID,DEFOCUS1,DEFOCUS2,DEFOCUS_ANGLE,OUTPUT_DIAGNOSTIC_FILE,SCORE, DETECTED_RING_RESOLUTION FROM ESTIMATED_CTF_PARAMETERS",con)
        selected_micrographs = pd.merge(df1,df2,on="CTF_ESTIMATION_ID")
        df3 = pd.read_sql_query(f"SELECT MOVIE_ASSET_ID,IMAGE_SHIFT_X, IMAGE_SHIFT_Y FROM MOVIE_ASSETS_METADATA",con)
        selected_micrographs = pd.merge(selected_micrographs,df3,on="MOVIE_ASSET_ID")

        defocus.append([[m["DEFOCUS_ANGLE"],m['IMAGE_SHIFT_X'],m['IMAGE_SHIFT_Y']] for i,m in selected_micrographs.iterrows() if m['SCORE']>0.05])

print(defocus)
fig, axs = plt.subplots(2, 4,sharex=True,sharey=True)
for i,la in enumerate(defocus):
    data = np.array(la,dtype=float)

    axs.flat[i].scatter(data[:,1],data[:,2],c=data[:,0], cmap='viridis')
plt.xlabel("BIS X")
plt.ylabel("BIS Y")

import tikzplotlib

tikzplotlib.save("../graphics/approach/defocusplot.tex")