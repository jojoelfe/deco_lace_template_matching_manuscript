import matplotlib.pyplot as plt
import latexipy as lp
import utils
import starfile
from pathlib import Path
from scipy.spatial import KDTree
import numpy as np
from pyquaternion import Quaternion 
from scipy.spatial.transform import Rotation


distances = [300,400,500,600,700,800]
diffs = []
for i, distance in enumerate(distances):
    diffs.append([])

def calculate_quaternion_distance(angle1, angle2):
  rot0 = Rotation.from_euler('zyz', angle1, degrees=True)
  rot1 = Rotation.from_euler('zyz', angle2, degrees=True)
  # Convert to quaternions
  q0 = Quaternion(rot0.as_quat())
  q1 = Quaternion(rot1.as_quat())
  # distance
  return Quaternion.absolute_distance(q0, q1)

for dataset, name in utils.dataset_info:
    assembled_directory = Path("/scratch/bern/elferich/deco_lace_manuscript_processing/assemble/")
    data  =  starfile.read(assembled_directory / f"{name}_assembled_matches.star")
    coordinates = np.stack((data["x"].to_numpy(), data["y"].to_numpy(), data["defocus"].to_numpy()),axis=1)
    euler_angles = np.stack((data["phi"].to_numpy(), data["theta"].to_numpy(), data["psi"].to_numpy()),axis=1)
    tree = KDTree(coordinates)
    for i, distance in enumerate(distances):
        pairs = tree.query_pairs(r=distance)
        print(len(pairs))
        for pair in pairs:
            #print(pair)
            diffs[i].append(calculate_quaternion_distance(euler_angles[pair[0]], euler_angles[pair[1]]))
        
    



lp.latexify()
with lp.figure("orientation_diff_dist",tight_layout=True):
    fig, axs = plt.subplots(2,3,sharey=False)
    for i, distance in enumerate(distances):
        axs.flatten()[i].hist(diffs[i], bins=100, color='grey', edgecolor='black', linewidth=0.5)
        axs.flatten()[i].set_title(f"Up to  {distances[i]}A")
   
    #axs[1].bar(range(1,5),num_matches[4:8], align='center', color='grey', edgecolor='black', linewidth=0.5)
    #axs[0].set_title("Eucentric Focus")
    
