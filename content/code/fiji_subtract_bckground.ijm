filename = getArgument();

open('/scratch/bern/elferich/deco_lace_manuscript_processing/views/' + filename);
run("Subtract Background...", "rolling=200 light");
saveAs("Tiff", '/scratch/bern/elferich/deco_lace_manuscript_processing/views/sub200_' + filename);
