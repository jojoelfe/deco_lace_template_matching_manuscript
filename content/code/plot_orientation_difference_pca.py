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



distances = [300,400,500,600,700,500]
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
  rot0 = Rotation.from_euler('ZYZ', -angle1, degrees=True)
  rot1 = Rotation.from_euler('ZYZ', -angle2, degrees=True)
  # Convert to quaternions
  q0 = Quaternion([rot0.as_quat()[3], rot0.as_quat()[0], rot0.as_quat()[1], rot0.as_quat()[2]])
  q1 = Quaternion([rot1.as_quat()[3], rot1.as_quat()[0], rot1.as_quat()[1], rot1.as_quat()[2]])
  # rotation that converts q1 into q0
  return q1 * q0.inverse

# Test using FFF_Lamella4 image s_lam_00173

for dataset, name in utils.dataset_info:
    assembled_directory = Path("/scratch/bern/elferich/deco_lace_manuscript_processing/assemble/")
    print(assembled_directory / f"{name}_assembled_matches.star")
    data  =  starfile.read(assembled_directory / f"{name}_assembled_matches.star")
    
    # Ensure tile_filename contains s_lam_0173
    # data = data[data["tile_filename"].str.contains("s_lam_00173")]
    #data["image_filename"] = data["tile_filename"]
    #data["pixel_size"] = 1.5
    #data["x"] = data["tile_x"]
    #data["y"] = data["tile_y"]
    #starfile.write(data, "test.star",overwrite=True)
    coordinates = np.stack((data["x"].to_numpy(), data["y"].to_numpy(), data["defocus"].to_numpy()),axis=1)
    euler_angles = np.stack((data["phi"].to_numpy(), data["theta"].to_numpy(), data["psi"].to_numpy()),axis=1)
    
    tree = KDTree(coordinates)
    for i, distance in enumerate(distances):
        pairs = tree.query_pairs(r=distance)
        for pair in pairs:
            rotation = calculate_quaternion_rotation(euler_angles[pair[0]], euler_angles[pair[1]])
            axis = rotation.axis
            if axis[2] < 0:
                axis = -axis
            rotations[i].append(axis)
            diffs[i].append(calculate_quaternion_distance(euler_angles[pair[0]], euler_angles[pair[1]]))
        
       
    



#lp.latexify()
#with lp.figure("orientation_diff_pca",tight_layout=True,size=lp.figure_size(ratio=1.0,doc_width_pt=750)):
if True:
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    distance = distances[-1]
    i = -1
    rotations[i] = np.array(rotations[i])
    diffs[i] = np.array(diffs[i])
    print(rotations[i].shape)
    ax.scatter(rotations[i][:,0],rotations[i][:,1],rotations[i][:,2],s=0.1)
    ax.set_title(f"Up to  {distances[i]}A")
    plt.show()
        #fmt_cyl = ".cylinder %f %f %f %f %f %f %f\n"
    with open(f"test_{distance}.bild", "w") as f:
      for r in rotations[i]:
        r*=250
        f.write(f".sphere {r[0]} {r[1]} {r[2]} 1.3\n")
   
    #axs[1].bar(range(1,5),num_matches[4:8], align='center', color='grey', edgecolor='black', linewidth=0.5)
    #axs[0].set_title("Eucentric Focus")
    
