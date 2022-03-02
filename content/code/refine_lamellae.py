import pycistem
import numpy as np
from pathlib import Path
import utils


pycistem.set_cistem_path("/groups/elferich/cisTEM/build/refine_template_tests_Intel-gpu-debug/src/")

for (database, name) in utils.dataset_info[7:]:
    pa = []
    results = utils.get_tm_data_from_db(database)
    for i, row in results.iterrows():
        pa.append(pycistem.programs.refine_template.parameters_from_database(database,
                                                                        row["IMAGE_ASSET_ID"],
                                                                        template_match_id=row["TEMPLATE_MATCH_JOB_ID"],
                                                                        wanted_threshold=7.75,
                                                                        input_reconstruction="/groups/elferich/mammalian_ribosome_structures/6swa_simulate_bfsca1_5.mrc",))
    print(name)
    print(len(pa))
    print(pa[0])
    res_my = pycistem.programs.refine_template.run(pa,num_procs=20,num_threads=3)


    directory = Path("/scratch/bern/elferich/deco_lace_manuscript_processing/lamella_refine/")
    directory.mkdir(parents=True,exist_ok=True)

    pycistem.programs.refine_template.write_starfile(res_my, str(directory / f"{name}_refine.star"))
    