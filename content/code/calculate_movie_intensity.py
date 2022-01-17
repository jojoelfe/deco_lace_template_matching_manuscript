import matplotlib.pyplot as plt
import latexipy as lp
import utils
from tifffile import imread
from tqdm import tqdm
import numpy as np
import json
from pathlib import Path

defocus = []


selected_micrographs = utils.get_data_from_db(utils.datasets[0])

data = {}
for dataset in utils.datasets[1:]:
    selected_micrographs = utils.get_data_from_db(dataset)

    for i, row in tqdm(selected_micrographs.iterrows()):
        movie_data = imread(row['movie_filename'])
        data[row['movie_filename']] = np.mean(movie_data[:,3000:5184,4000:7520])
        with open(Path(dataset).stem +"_thickness.json","w") as fp:
            json.dump(data,fp)


