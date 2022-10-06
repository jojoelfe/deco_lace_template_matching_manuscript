from chimerax.geometry import Place, Places, translation, quaternion_rotation, rotation
from chimerax.core.commands import run
import starfile
import numpy as np
from scipy.spatial import KDTree, cKDTree
from chimerax.std_commands.measure_rotation import measure_rotation
from chimerax.markers import MarkerSet, create_link
from pathlib import Path
from healpy import pix2ang


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
mset1 = MarkerSet(session, 'rotation points up to 300')
mset2 = MarkerSet(session, 'rotation points 300 to 4000')
mset3 = MarkerSet(session, 'rotation points 400 to 800')
mset4 = MarkerSet(session, 'rotation points 800 to 1600')
axis_vecs_1 = []
axis_vecs_2 = []
axis_vecs_3 = []
axis_vecs_4 = []
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
    pairs = tree.query_pairs(r=1600)

    
    for pair in pairs:
        t1 =   rotation(np.array((0, 0, 1)), -euler_angles[pair[0]][2])  * rotation(np.array((0, 1, 0)), -euler_angles[pair[0]][1])  * rotation(np.array((0, 0, 1)), -euler_angles[pair[0]][0])  
        #o1.scene_position = translation((0,0,0))
        t2 =  t1.inverse() * rotation(np.array((0, 0, 1)), -euler_angles[pair[1]][2])  * rotation(np.array((0, 1, 0)), -euler_angles[pair[1]][1])  * rotation(np.array((0, 0, 1)), -euler_angles[pair[1]][0])  
        #o2.scene_position = t2
        #res = measure_rotation(session, o2, o1, color = (210, 100, 100,
        #255),show_axis=False)
        res = translation((0,0,0)) * t2
        axis_vec = res.rotation_axis_and_angle()[0]
        
        if np.linalg.norm(coordinates[pair[0]] - coordinates[pair[1]]) < 300:
            mset1.create_marker(axis_vec*250, (210, 100, 100, 255),1.0)
            mset1.create_marker(axis_vec*-250,  (210, 100, 100, 255),1.0)
            axis_vecs_1.append(axis_vec)
        elif np.linalg.norm(coordinates[pair[0]] - coordinates[pair[1]]) < 400:
            mset2.create_marker(axis_vec*250,  (210, 100, 100, 255),1.0)
            mset2.create_marker(axis_vec*-250,  (210, 100, 100, 255),1.0)
            axis_vecs_2.append(axis_vec)
        elif np.linalg.norm(coordinates[pair[0]] - coordinates[pair[1]]) < 600:
            mset3.create_marker(axis_vec*250,  (210, 100, 100, 255),1.0)
            mset3.create_marker(axis_vec*-250, (210, 100, 100, 255),1.0)
            axis_vecs_3.append(axis_vec)
        elif np.linalg.norm(coordinates[pair[0]] - coordinates[pair[1]]) < 800:
            mset4.create_marker(axis_vec*250,  (210, 100, 100, 255),1.0)
            mset4.create_marker(axis_vec*-250, (210, 100, 100, 255),1.0)
            axis_vecs_4.append(axis_vec)
        
o1.scene_position = origin_transform
session.models.add([mset1])
session.models.add([mset2])
session.models.add([mset3])
session.models.add([mset4])

for i, axis_vecs in enumerate([axis_vecs_1, axis_vecs_2, axis_vecs_3, axis_vecs_4]):
    heightscale=0.3
    widthscale=0.5
    nside = 2**4
    angular_sampling = np.sqrt(3 / np.pi) * 60 / nside
    theta, phi = pix2ang(nside, np.arange(12 * nside ** 2))
    phi = np.pi - phi
    hp = np.column_stack((np.sin(theta) * np.cos(phi),
                            np.sin(theta) * np.sin(phi),
                            np.cos(theta)))
    kdtree = cKDTree(hp)
    #st = np.sin(np.deg2rad(df[star.Relion.ANGLETILT]))
    #ct = np.cos(np.deg2rad(df[star.Relion.ANGLETILT]))
    #sp = np.sin(np.deg2rad(df[star.Relion.ANGLEROT]))
    #cp = np.cos(np.deg2rad(df[star.Relion.ANGLEROT]))
    #ptcls = np.column_stack((st * cp, st * sp, ct)) I need to create ptcls
    ptcls = np.array(axis_vecs)
    _, idx = kdtree.query(ptcls)
    cnts = np.bincount(idx, minlength=theta.size)
    frac = cnts / np.max(cnts).astype(np.float64)
    mu = np.mean(frac)
    sigma = np.std(frac)
    print("%.0f (%.2f%%) +/- %.1f (%.2f%%) particles per bin" %
        (np.mean(cnts), mu, np.std(cnts), sigma))
    color_scale = (frac - mu) / sigma
    color_scale[color_scale > 5] = 5
    color_scale[color_scale < -1] = -1
    color_scale /= 6
    color_scale += 1 / 6.
    imin = np.argmin(cnts)
    imax = np.argmax(cnts)
    print("Min %d particles (%.2f%%); color %f,0,%f" %
        (cnts[imin], frac[imin] * 100, color_scale[imin], 1 - color_scale[imin]))
    print("Max %d particles (%.2f%%); color %f,0,%f" %
        (cnts[imax], frac[imax] * 100, color_scale[imax], 1 - color_scale[imax]))
    r = 250
    rp = np.reshape(r + r * frac * heightscale, (-1, 1))
    base1 = hp * r
    base2 = hp * rp
    base1 = base1[:, [0, 1, 2]] + np.array([r]*3)
    base2 = base2[:, [0, 1, 2]] + np.array([r]*3)
    height = np.squeeze(np.abs(rp - r))
    idx = np.where(height >= 0.01)[0]
    width = widthscale * np.pi * r * angular_sampling / 360
    bild = np.hstack((base1, base2, np.ones((base1.shape[0], 1)) * width))
    fmt_color = ".color %f 0 %f\n"
    fmt_cyl = ".cylinder %f %f %f %f %f %f %f\n"
    with open(f"/tmp/test{i+1}.bild", "w") as f:
        for i in idx:
            f.write(fmt_color % (color_scale[i], 1 - color_scale[i]))
            f.write(fmt_cyl % tuple(bild[i]))