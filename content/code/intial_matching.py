import configparser
import glob
import numpy as np

navfile = "/scratch/bern/elferich/the_special_micrograph_and_lamella/nav.nav"

with open(navfile, 'r') as f:
    nav_string = '[header]\n' + f.read()
nav = configparser.ConfigParser()
nav.read_string(nav_string)

mdoc_files = "/scratch/bern/elferich/the_special_micrograph_and_lamella/*.tif.mdoc"

for mdoc_file in glob.glob(mdoc_files):
    #print(mdoc_file)
    with open(mdoc_file, 'r') as f:
        mdoc_string = '[header]\n' + f.read()
    mdoc = configparser.ConfigParser()
    mdoc.read_string(mdoc_string)
    for section in nav:
        if "StageXYZ" not in nav[section]:
            continue
        nav_position = np.array(nav[section]["StageXYZ"].split(' '),dtype=float)[0:2]
        #print(nav_position)
        mdoc_position = np.array(mdoc["FrameSet = 0"]["StagePosition"].split(' '),dtype=float)
        #print(mdoc_position)\
        distance = np.linalg.norm(nav_position-mdoc_position)
        if distance < 0.3:
            #print(distance)
            print(str(nav[section]["DrawnID"]))

