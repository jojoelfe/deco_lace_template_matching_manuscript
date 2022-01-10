import matplotlib.pyplot as plt
import sqlite3
import pandas as pd
import os
import contextlib

datasets = ["/scratch/bern/elferich/ER_Hox_120h_20211029_g1_l1/ER_Hox_120h_20211029_g1_l1.db",
            "/scratch/bern/elferich/ER_Hox_120h_20211029_g1_l2/ER_Hox_120h_20211029_g1_l2.db",
            "/scratch/bern/elferich/ER_Hox_120h_20211029_g2_l3/ER_Hox_120h_20211029_g2_l3.db",
            "/scratch/bern/elferich/ER_Hox_120h_202111029_g2_l4/ER_Hox_120h_202111029_g2_l4.db"]
astig_angle = []

for dataset in datasets:
    print(dataset)
    with contextlib.closing(sqlite3.connect(dataset)) as con:

        df1 = pd.read_sql_query(f"SELECT IMAGE_ASSET_ID,IMAGE_ASSETS. FILENAME, MOVIE_ASSETS.FILENAME as movie_filename, CTF_ESTIMATION_ID ,IMAGE_ASSETS.PIXEL_SIZE as image_pixel_size, MOVIE_ASSETS.PIXEL_SIZE as movie_pixel_size, IMAGE_ASSETS.X_SIZE, IMAGE_ASSETS.Y_SIZE  FROM IMAGE_ASSETS INNER JOIN MOVIE_ASSETS ON MOVIE_ASSETS.MOVIE_ASSET_ID == IMAGE_ASSETS.PARENT_MOVIE_ID", con)
        df2 = pd.read_sql_query("SELECT CTF_ESTIMATION_ID,DEFOCUS1,DEFOCUS2,DEFOCUS_ANGLE,OUTPUT_DIAGNOSTIC_FILE,SCORE, DETECTED_RING_RESOLUTION FROM ESTIMATED_CTF_PARAMETERS",con)
        selected_micrographs = pd.merge(df1,df2,on="CTF_ESTIMATION_ID")

        astig_angle.append([(m["DEFOCUS_ANGLE"]) for i,m in selected_micrographs.iterrows() if m['SCORE']>0.05])

plt.boxplot(astig_angle)
plt.xlabel("Lamella")
plt.ylabel("Astigmatism [A]")

import tikzplotlib

tikzplotlib.save("../graphics/approach/defocusplot.tex")