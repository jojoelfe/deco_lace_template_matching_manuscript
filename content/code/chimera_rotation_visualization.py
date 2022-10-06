from chimerax.geometry import Place, Places, translation, quaternion_rotation, rotation
from chimerax.core.commands import run
import starfile
import numpy as np
from scipy.spatial import KDTree
from chimerax.std_commands.measure_rotation import measure_rotation
from chimerax.markers import MarkerSet, create_link
from pathlib import Path


datasets = ["/scratch/bern/elferich/ER_Hox_120h_20211029_g1_l1/ER_Hox_120h_20211029_g1_l1.db",
            "/scratch/bern/elferich/ER_Hox_120h_20211029_g1_l2/ER_Hox_120h_20211029_g1_l2.db",
            "/scratch/bern/elferich/ER_Hox_120h_20211029_g2_l3/ER_Hox_120h_20211029_g2_l3.db",
            "/scratch/bern/elferich/ER_Hox_120h_202111029_g2_l4/ER_Hox_120h_202111029_g2_l4.db",
            "/scratch/bern/elferich/R_Hox_120h_20211108_g2_l1/R_Hox_120h_20211108_g2_l1.db",
            "/scratch/bern/elferich/ER_Hox_120h_20211108_g2_l2/ER_Hox_120h_20211108_g2_l2.db",
            "/scratch/bern/elferich/ER_Hox_120h_20211108_g2_l3/ER_Hox_120h_20211108_g2_l3.db",
            "/scratch/bern/elferich/ER_Hox_120h_20211108_g2_l4/ER_Hox_120h_20211108_g2_l4.db"]

dataset_names = ["euc_lamella1",
                 "euc_lamella2",
                 "euc_lamella3",
                 "euc_lamella4",
                 "fff_lamella1",
                 "fff_lamella2",
                 "fff_lamella3",
                 "fff_lamella4"]

dataset_info = [(dataset,dataset_names[i]) for i,dataset in enumerate(datasets)]

sel1 = run(session,"open /groups/elferich/mammalian_ribosome_structures/6swa_simulate_bfsca1_5.mrc")
for v in sel1:
    o1 = v
sel2 = run(session,"open /groups/elferich/mammalian_ribosome_structures/6swa_simulate_bfsca1_5.mrc")
for v in sel2:
    o2 = v
mset1 = MarkerSet(session, 'rotation points up to 200')
mset2 = MarkerSet(session, 'rotation points 200 to 4000')
mset3 = MarkerSet(session, 'rotation points 400 to 800')
#mset4 = MarkerSet(session, 'rotation points 2000 to 4000')
for dataset, name in dataset_info:
    assembled_directory = Path("/scratch/bern/elferich/deco_lace_manuscript_processing/assemble/")
    print(assembled_directory / f"{name}_assembled_matches.star")
    data  =  starfile.read(assembled_directory / f"{name}_assembled_matches.star")

    coordinates = np.stack((data["x"].to_numpy(), data["y"].to_numpy(), data["defocus"].to_numpy()),axis=1)
    euler_angles = np.stack((data["phi"].to_numpy(), data["theta"].to_numpy(), data["psi"].to_numpy()),axis=1)

    origin_transform = translation(-0.5 *
                                        np.array([384,384,384]) * 1.5
                                        )

    tree = KDTree(coordinates)
    pairs = tree.query_pairs(r=800)

    
    for pair in pairs:
        t1 =   rotation(np.array((0, 0, 1)), euler_angles[pair[0]][2])  * rotation(np.array((0, 1, 0)), euler_angles[pair[0]][1])  * rotation(np.array((0, 0, 1)), euler_angles[pair[0]][0])  
        o1.scene_position = translation((0,0,0))
        t2 =  t1.inverse() * rotation(np.array((0, 0, 1)), euler_angles[pair[1]][2])  * rotation(np.array((0, 1, 0)), euler_angles[pair[1]][1])  * rotation(np.array((0, 0, 1)), euler_angles[pair[1]][0])  
        o2.scene_position = t2
        res = measure_rotation(session, o2, o1, color = (210, 100, 100, 255),show_axis=False)
        axis_vec = res.rotation_axis_and_angle()[0]
        if np.linalg.norm(coordinates[pair[0]] - coordinates[pair[1]]) < 200:
            mset1.create_marker(axis_vec*250, (210, 100, 100, 255),1.0)
            mset1.create_marker(axis_vec*-250,  (210, 100, 100, 255),1.0)
        elif np.linalg.norm(coordinates[pair[0]] - coordinates[pair[1]]) < 400:
            mset2.create_marker(axis_vec*250,  (210, 100, 100, 255),1.0)
            mset2.create_marker(axis_vec*-250,  (210, 100, 100, 255),1.0)
        elif np.linalg.norm(coordinates[pair[0]] - coordinates[pair[1]]) < 800:
            mset3.create_marker(axis_vec*250,  (210, 100, 100, 255),1.0)
            mset3.create_marker(axis_vec*-250, (210, 100, 100, 255),1.0)
        
o1.scene_position = origin_transform
session.models.add([mset1])
session.models.add([mset2])
session.models.add([mset3])
# Result:
#Position of 6swa_simulate_bfsca1_5.mrc #1 relative to 6swa_simulate_bfsca1_5.mrc #2 coordinates:
#Matrix rotation and translation
#0.40550293 -0.82542968 -0.39272536 522.04381036
#0.87639470 0.22895687 0.42368748 -152.36324671
#-0.25980705 -0.51598894 0.81624488 276.35071750
#Axis -0.48224278 -0.06821380 0.87337780
#Axis point 447.02158284 310.49378687 0.00000000
#Rotation angle (degrees) 76.97640190
#Shift along axis 0.00000000
#
#Position of 6swa_simulate_bfsca1_5.mrc #1 relative to 6swa_simulate_bfsca1_5.mrc #2 coordinates:
#Matrix rotation and translation
#0.40550293 -0.82542968 -0.39272536 0.00000000
#0.87639470 0.22895687 0.42368748 -0.00000000
#-0.25980705 -0.51598894 0.81624488 0.00000000
#Axis -0.48224278 -0.06821380 0.87337780
#Axis point 0.00000000 0.00000000 0.00000000
#Rotation angle (degrees) 76.97640190
#Shift along axis 0.00000000
#
#executed chimera_rotation_test.py

# This shows that I can the axis vector is in the original reference frame