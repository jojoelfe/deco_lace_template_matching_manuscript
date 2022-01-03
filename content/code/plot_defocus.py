import matplotlib.pyplot as plt
import sqlite3
import pandas as pd
import os

dataset = "/scratch/bern/elferich/ER_Hox_120h_20211029_g1_l1/ER_Hox_120h_20211029_g1_l1.db"


con = sqlite3.connect(dataset)


df1 = pd.read_sql_query(f"SELECT IMAGE_ASSET_ID,IMAGE_ASSETS. FILENAME, MOVIE_ASSETS.FILENAME as movie_filename, CTF_ESTIMATION_ID ,IMAGE_ASSETS.PIXEL_SIZE as image_pixel_size, MOVIE_ASSETS.PIXEL_SIZE as movie_pixel_size, IMAGE_ASSETS.X_SIZE, IMAGE_ASSETS.Y_SIZE  FROM IMAGE_ASSETS INNER JOIN MOVIE_ASSETS ON MOVIE_ASSETS.MOVIE_ASSET_ID == IMAGE_ASSETS.PARENT_MOVIE_ID", con)
df2 = pd.read_sql_query("SELECT CTF_ESTIMATION_ID,DEFOCUS1,DEFOCUS2,DEFOCUS_ANGLE,OUTPUT_DIAGNOSTIC_FILE,SCORE, DETECTED_RING_RESOLUTION FROM ESTIMATED_CTF_PARAMETERS",con)
selected_micrographs = pd.merge(df1,df2,on="CTF_ESTIMATION_ID")

plt.hist([(m["DEFOCUS1"]+m["DEFOCUS2"])/2 for i,m in selected_micrographs.iterrows() if m['SCORE']>0.05])