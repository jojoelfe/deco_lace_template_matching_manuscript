import pycistem, asyncio

lamella = [
    (98, "fff_lamella1.mrc"),
    (99, "fff_lamella2.mrc"),
    (100, "fff_lamella3.mrc"),
    (101, "fff_lamella4.mrc"),
    (83, "euc_lamella1.mrc"),
    (82,"euc_lamella2.mrc"),
    (81,"euc_lamella3.mrc"),
    (80,"euc_lamella4.mrc")
]
for l in lamella:
    p = pycistem.programs.apply_ctf.parameters_from_database("/scratch/bern/elferich/views/views.db",l[0],l[1],
        apply_wiener_filter=True,
        wiener_filter_falloff_frequency = 720.0,
        wiener_filter_falloff_fudge_factor = 0.9,
        wiener_filter_scale_fudge_factor = 0.4,
        wiener_filter_high_pass_radius= 200.0)
    print(p)
    pycistem.set_cistem_path("/groups/elferich/cisTEM/build/fowl_template_matching_Intel-gpu-debug/src/")
    asyncio.run(pycistem.programs.apply_ctf.run(p))