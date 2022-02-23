import pandas as pd
import contextlib
import sqlite3
import numpy as np

datasets = ["/scratch/bern/elferich/ER_Hox_120h_20211029_g1_l1/ER_Hox_120h_20211029_g1_l1.db",
            "/scratch/bern/elferich/ER_Hox_120h_20211029_g1_l2/ER_Hox_120h_20211029_g1_l2.db",
            "/scratch/bern/elferich/ER_Hox_120h_20211029_g2_l3/ER_Hox_120h_20211029_g2_l3.db",
            "/scratch/bern/elferich/ER_Hox_120h_202111029_g2_l4/ER_Hox_120h_202111029_g2_l4.db",
            "/scratch/bern/elferich/R_Hox_120h_20211108_g2_l1/R_Hox_120h_20211108_g2_l1.db",
            "/scratch/bern/elferich/ER_Hox_120h_20211108_g2_l2/ER_Hox_120h_20211108_g2_l2.db",
            "/scratch/bern/elferich/ER_Hox_120h_20211108_g2_l3/ER_Hox_120h_20211108_g2_l3.db",
            "/scratch/bern/elferich/ER_Hox_120h_20211108_g2_l4/ER_Hox_120h_20211108_g2_l4.db"]

def get_data_from_db(dataset,get_movement=False):
    with contextlib.closing(sqlite3.connect(dataset)) as con:

        df1 = pd.read_sql_query(f"SELECT IMAGE_ASSET_ID,MOVIE_ASSET_ID,IMAGE_ASSETS.FILENAME, MOVIE_ASSETS.FILENAME as movie_filename, CTF_ESTIMATION_ID , ALIGNMENT_ID, IMAGE_ASSETS.PIXEL_SIZE as image_pixel_size, MOVIE_ASSETS.PIXEL_SIZE as movie_pixel_size, IMAGE_ASSETS.X_SIZE, IMAGE_ASSETS.Y_SIZE, IMAGE_ASSETS.ORIGINAL_X_SIZE, IMAGE_ASSETS.ORIGINAL_Y_SIZE, IMAGE_ASSETS.CROP_CENTER_X, IMAGE_ASSETS.CROP_CENTER_Y  FROM IMAGE_ASSETS INNER JOIN MOVIE_ASSETS ON MOVIE_ASSETS.MOVIE_ASSET_ID == IMAGE_ASSETS.PARENT_MOVIE_ID", con)
        df2 = pd.read_sql_query("SELECT CTF_ESTIMATION_ID,DEFOCUS1,DEFOCUS2,DEFOCUS_ANGLE,OUTPUT_DIAGNOSTIC_FILE,SCORE, DETECTED_RING_RESOLUTION FROM ESTIMATED_CTF_PARAMETERS",con)
        selected_micrographs = pd.merge(df1,df2,on="CTF_ESTIMATION_ID")
        df3 = pd.read_sql_query(f"SELECT MOVIE_ASSET_ID,IMAGE_SHIFT_X, IMAGE_SHIFT_Y FROM MOVIE_ASSETS_METADATA",con)
        selected_micrographs = pd.merge(selected_micrographs,df3,on="MOVIE_ASSET_ID")
        selected_micrographs["TOTAL_MOVEMENT"] = 0
        if get_movement:
            prev_shift = None
            for i, row in selected_micrographs.iterrows():
                df4 = pd.read_sql_query(f"SELECT FRAME_NUMBER, X_SHIFT, Y_SHIFT FROM MOVIE_ALIGNMENT_PARAMETERS_{row['ALIGNMENT_ID']}",con)
                total_movement = 0
                for j, mrow in df4.iterrows():
                    if prev_shift is None:
                        prev_shift = np.array([mrow["X_SHIFT"],mrow["Y_SHIFT"]])
                        continue
                    movement = np.linalg.norm(prev_shift-np.array([mrow["X_SHIFT"],mrow["Y_SHIFT"]]))
                    total_movement += movement
                    prev_shift = np.array([mrow["X_SHIFT"],mrow["Y_SHIFT"]])
                selected_micrographs.at[i,'TOTAL_MOVEMENT'] = total_movement
    return(selected_micrographs)