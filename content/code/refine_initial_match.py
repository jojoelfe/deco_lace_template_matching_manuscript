import pycistem
import numpy as np
from pathlib import Path


pycistem.set_cistem_path("/groups/elferich/cisTEM/build/refine_template_tests_Intel-gpu-debug/src/")

pa = pycistem.programs.refine_template.parameters_from_database("/scratch/bern/elferich/ER_HoxB8_96h/ER_HoxB8_96h.db",
                                                                     186,
                                                                     template_match_id=4,
                                                                     wanted_threshold=7.76,
                                                                     input_reconstruction="/groups/elferich/mammalian_ribosome_structures/6swa_simulate_bfsca1_5.mrc",)
print(pa)
res_my = pycistem.programs.refine_template.run([pa],num_procs=1)


directory = Path("/scratch/bern/elferich/decolace_manuscript_processing/initial_matching/")
directory.mkdir(parents=True,exist_ok=True)

pycistem.programs.refine_template.write_starfile(res_my, str(directory / "506_matches.star"))
 