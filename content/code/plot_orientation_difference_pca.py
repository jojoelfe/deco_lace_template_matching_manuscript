import matplotlib.pyplot as plt
import latexipy as lp
import utils
import starfile
from pathlib import Path
from scipy.spatial import KDTree
import numpy as np
from pyquaternion import Quaternion 
from scipy.spatial.transform import Rotation
from sklearn.decomposition import PCA


distances = [300,400,500,600,700,800]
rotations = []
diffs = []
distance_data = []
for i, distance in enumerate(distances):
    rotations.append([])
    diffs.append([])
    distance_data.append([])

def calculate_quaternion_distance(angle1, angle2):
  rot0 = Rotation.from_euler('zyz', angle1, degrees=True)
  rot1 = Rotation.from_euler('zyz', angle2, degrees=True)
  # Convert to quaternions
  q0 = Quaternion(rot0.as_quat())
  q1 = Quaternion(rot1.as_quat())
  # distance
  return Quaternion.absolute_distance(q0, q1)

def calculate_quaternion_rotation(angle1, angle2):
  rot0 = Rotation.from_euler('zyz', angle1, degrees=True)
  rot1 = Rotation.from_euler('zyz', angle2, degrees=True)
  # Convert to quaternions
  q0 = Quaternion(rot0.as_quat())
  q1 = Quaternion(rot1.as_quat())
  # rotation that converts q1 into q0
  return q1 * q0.inverse

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
            rotation = calculate_quaternion_rotation(euler_angles[pair[0]], euler_angles[pair[1]])
            rotations[i].append(rotation.axis)
            diffs[i].append(calculate_quaternion_distance(euler_angles[pair[0]], euler_angles[pair[1]]))
        
       
    



lp.latexify()
with lp.figure("orientation_diff_pca",tight_layout=True,size=lp.figure_size(ratio=1.0,doc_width_pt=750)):
    fig, axs = plt.subplots(2,3,sharey=False)
    for i, distance in enumerate(distances):
        rotations[i] = np.array(rotations[i])
        diffs[i] = np.array(diffs[i])
        print(rotations[i].shape)
        axs.flatten()[i].scatter(rotations[i][:,0],rotations[i][:,1],s=0.1)
        axs.flatten()[i].set_title(f"Up to  {distances[i]}A")

        #fmt_cyl = ".cylinder %f %f %f %f %f %f %f\n"
        #with open(f"test_{distance}.bild", "w") as f:
        #    for r in rotations[i]:
        #        r*=150
        #        f.write(f".sphere {r[0]} {r[1]} {r[2]} 1.3\n")
   
    #axs[1].bar(range(1,5),num_matches[4:8], align='center', color='grey', edgecolor='black', linewidth=0.5)
    #axs[0].set_title("Eucentric Focus")
    
