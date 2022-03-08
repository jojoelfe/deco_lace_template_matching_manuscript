import pycistem
import numpy as np
from pathlib import Path
import utils


pycistem.set_cistem_path("/groups/elferich/cisTEM/build/refine_template_tests_Intel-gpu-debug/src/")

for (database, name) in utils.dataset_info:
    directory = Path("/scratch/bern/elferich/deco_lace_manuscript_processing/lamella_match/")
    directory.mkdir(parents=True,exist_ok=True)
    pycistem.database.write_match_template_to_starfile(database,directory / f"{name}_match.star",overwrite=True,switch_phi_psi=True)