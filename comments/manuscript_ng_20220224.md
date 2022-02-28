This manuscript was automatically generated on February 21, 2022.

## Authors

-   **Johannes Elferich** ![ORCID
    icon](media/image1.png){width="0.16666666666666666in"
    height="0.16666666666666666in"}
    [0000-0002-9911-706X](https://orcid.org/0000-0002-9911-706X) ·
    ![GitHub icon](media/image2.png){width="0.16666666666666666in"
    height="0.16666666666666666in"}
    [jojoelfe](https://github.com/jojoelfe) RNA Therapeutic Institute,
    UMass Chan Medical School; HHMI

-   **Nikolaus Grigorieff** ![ORCID
    icon](media/image1.png){width="0.16666666666666666in"
    height="0.16666666666666666in"}
    [0000-0002-1506-909X](https://orcid.org/0000-0002-1506-909X) ·
    ![GitHub icon](media/image2.png){width="0.16666666666666666in"
    height="0.16666666666666666in"}
    [nikogrigorieff](https://github.com/nikogrigorieff) RNA Therapeutic
    Institute, UMass Chan Medical School; HHMI

## Abstract

Localization of biomolecules inside a cell is an important goal of
biological imaging. Fluorescence microscopy can localize biomolecules
inside whole cells and tissues, but its ability to count biomolecules
and accuracy of the spatial coordinates is limited by the wavelength of
visible light. Cryo-electron microscopy (cryo-EM) provides highly
accurate position and orientation information of biomolecules but is
often confined to small fields of view inside a cell, limiting
biological context. In this study we use a new data-acquisition scheme
called "Beam-Imageshift for Large Area Cryo-Electron microscopy"
(BILACE) to collect high-resolution cryo-EM data over entire sections
(100 -- 200 nm thick lamellae) of neutrophil-like mouse cells,
representing roughly 1% of the total cellular volume. We use 2D template
matching (2DTM) to determine localization and orientation of the large
ribosomal subunit in these sections, detect bound small ribosomal
subunit, and assign ribosomes to polysomes based on their relative
orientations to each other. These data provide "maps" of translational
activity across sections of mammalian cells. This new high-throughput
cryo-EM data collection approach, together with 2DTM, will advance
visual proteomics and complement other single-cell "omics" techniques,
such as flow-cytometry and single-cell sequencing.

## Introduction

A major goal in understanding cellular processes is the knowledge of the
amounts, location, interactions, and conformations of biomolecules
inside the cell. This knowledge can be obtained by approaches broadly
divided into label- and label-free techniques. In label-dependent
techniques a probe is physically attached to a molecule of interest that
is able to detected with a high signal-to-noise signal, such as a
fluorescent molecule. In label-free techniques the physical properties
of molecules themselves are used for detection. An example for this is
proteomics using mass-spectrometry \[[1](#ref-tSXIKPl7)\]. The advantage
of label-free techniques is that they can provide information over
thousands of molecules, while label-techniques offer highly specific
information for a few molecules. Especially spatial information can
often only be achieved using label-dependent techniques, such as
fluorescence microscopy \[[2](#ref-VBmW7Aot)\].

Cryo-electron microscopy has the potential to directly visualize the
arrangement of atoms that compose biomolecules inside of cells, thereby
allowing label-free detection with high spatial accuracy. This has been
called "visual proteomics" \[[3](#ref-tGQ6TSUo)\]. Since cryo-EM
requires thin samples (\<500nm), imaging of biomolecules inside cells is
restricted to small organisms, thin regions of cells, or samples that
have been suitably thinned. Thinning can be achieved either by
mechanical sectioning \[[4](#ref-g8QavfwP)\] or by milling using a
focused ion beam (FIB) \[[5](#ref-16IhS1Nc4)\]. This complex workflow
leads to a low throughput of cryo-EM imaging of cells and is further
limited by the fact that at the required magnifications, typical fields
of view (FOV) are very small compared to mammalian cells, and the FOV
achieved by label-techniques such as fluorescence light microscopy. The
predominant cryo-EM technique for the localization of biomolecules of
defined size and shape inside cells is cryo-electron tomography
\[[6](#ref-Rksh2dxu)\]. However, the requirement of a tilt series at
every imaged location and subsequent image alignment, severely limits
the throughput for molecular localization.

An alternative approach is to identify molecules by their structural
"fingerprint" in single projection using "2D template-matching" (2DTM)
\[[7](#ref-Ynb3IP6I),[8](#ref-18KGpXYPE),[9](#ref-10bXZuF3G)\]. In this
method a 3D model of a biomolecule is used as a template to find 2D
projections that match the molecules visible in the electron
micrographs. This method requires a projection search on a fine angular
grid, and the projections are used to find local cross-correlation peaks
with the micrograph. Since the location of a biomolecule in the
z-direction causes predictable aberrations to the projection image, this
method can be used to calculate complete 3D coordinates and orientations
of a biomolecule in a cellular sample \[[8](#ref-18KGpXYPE)\].

Hematopoiesis is the process of generating the various cell types of the
blood in the bone marrow. Dysregulation of this process results in
diseases like leukemia. Understanding how hematopoietic stem and
progenitor cells are programmed to differentiate to the appropriate cell
type would provide new insight into how hematopoiesis can be
misregulated. Of special interest is the regulation of translation
during hematopoiesis. This is exemplified by the observation that
genetic defects in the ribosome machinery often lead to hematopoietic
disease \[[10](#ref-gRoY21jY)\]. As such, direct quantification of
ribosome location, number and conformational states could lead to new
insight into hematopoietic disease \[[11](#ref-KAJ7221k)\].

Here we apply 2D-template matching of ribosomes to cryo-FIB milled
neutrophil-like murine cells \[[12](#ref-1B9Vt9eYu)\]. To increase the
amount of collected data and to provide unbiased sampling of the whole
lamella, we devised a new data-acquisition scheme, Defocus-corrected
large area cryo-electron microscopy (DeCo-LACE). We characterize
aberration cause by the used large beam-image shifts and highly focused
beams and find that they can be adequately corrected to enable ribosome
detection by 2DTM. The resulting data provide a description of ribosome
distribution in the whole lamellae, which represent roughly 2% of the
cellular volume. We find highly heterogeneous density of ribosome within
the cell and can identify discrete clusters of presumably
translationally active ribosomes, by testing for the presence of the
small ribosomal subunit. The high accuracy of location and orientation
of each detected ribosome also allows us to cluster ribosome molecules
into potential polysomes. Analysis of the throughput in this method
suggests that for the foreseeable future computation will be the
bottleneck for visual proteomics.

## Materials and Methods

### Grid preparation

ER-HoxA9 cells were maintained in RPMI supplemented with 10% FBS,
penicillin/streptomycin, SCF, and estrogen \[[12](#ref-1B9Vt9eYu)\] at
37C and 5% CO2. 120h prior to grid freezing cells were washed twice in
PBS and cultured in the same medium, except without estrogen.
Differentiation was verified by staining with Hoechst-dye and insepction
of nuclear morphology. Cells were then counted and diluted to 1\^106
cells/ml. Grids ( either 200 mesh copper grids, with a sillicone-oxide
and 2um holes with a 2um spacing or 200 mesh gold grids with a thin gold
film and 2 um holes in 2um sapcing) were glow-discharged from both sides
using a ... for ... . 3.5 ul of cells suspension was added to grids on
the thin-film side and grids were automatically blotted from the
back-side using a GP2 cryoplunger (Leica) for ... s and rapidly plunged
into liquid ethane at -185C.

### FIB-milling

Grids were loaded into a Acquilos 2 FIB/SEM microscope with a stage
cooled to -190C. Grids were sputter-coated with platinum for 15s at 45
mA and then coated with a layer of platinum-precursor by openin the
GIS-valve for 45s. An overview of the grid was created by montaging SEM
images and isolated cells at the center of gridsquares were selected for
FB-milling. Lamella were generated automatically using the AutoTEM
software, resulting in 6-8 um wide lamella with 150-200 um thickness as
determined by FIB-imaging of the lamella edge.

### Data collection

Grids were loaded into a Krios Titam TEM operated at 300 keV. The
microscope was setup with a cross-grating grid on the stageby setting
the beam-diameter to 900 nm, resulting in the beam being completely
visible in the camera. To establish fringe-free conditions, the "Fine
eucentric" procedure of serialEM was used to move a square of the
cross-grating grid to the eucentric position of the microscope. The
effective defocus was then set to 2 um, using the "autofocus" routine of
serialEM. The objective focus of the microscope was changed until no
fringes were visible. The stage was then moved in Z until images had a
apparent defocus of 2 um. The differnce in stage Z-position between the
eucentric and fringe-free conditions was calculate d and noted to move
other areas into fringe-free condition.

Low magnification montages were used to find lamella and lamella that
were sufficiently thin and free of contamination were selected for
automated data collection. The corners of the lamella were manually
annotated in SerialEM and translated into Beam-Imageshift values using
SerialEm calibration. A hexagonal patter of beam-imageshift positions
was calculated that covered the area between he four corners in a
serpentine way, with a sqrt(3) \* 400 nm horizontal spacing and 800 nm
vertical spacing. Exposures were then taking at each position with a 30
e/A total dose. After each exposure that defocus was estimated using the
ctffind function of SerialEM and the focus for th next exposure was
corrected by the difference between the estimated focus and the desired
defocus of 800 um. Also after each exposure the deviation of the beam
from the center of the camera was measured and corrected using the
"CenterBeamFrom IMage" command of SerialEM.

After datacollection a 20s exposure at 2250x magnification of the
lamella at 200um defocus was taken for visualization purposes.

### Data pre-processing

Movies were gain-corrected and motion-corrected using a custom version
of unblur. To avoid influence of the beam-edge on motion-correction only
a quarter of the movie in the center of the camera was considered for
calculation of the estimated motion. After movie frames were aligned and
summed a mask for the illuminated area was calculated by lowpass
filtering the image at ... A, thresholding the image at 10% of the
maximal value and then lowpass filtering the mask at ... A. This mask
was then used to replace un-illuminated area with gaussian noise, with
the same mean and standard deviation as the illuminated area. The
contrast-transfer function (CTF) was estimated using ctffind, searching
between 0.02 and 2 um defocus.

### Template matching

The search template was generated from the cryo-EM structure of the
mouse large ribosomal subunit (PDB 6SWA). The ... subunit was deleted
from the model and the simulate program of the cisTEM suite was used to
calculate an density map from the atomic coordinates. The match_template
program was used to search for this template in the preprocessed images,
using 1.5 deg angular step in out-of-plane angles and 1.0 deg in-plane.
21 defocus planes in 200nm steps centered around the defocus estimates
by ctffind were searches. Matches were defined as peaks above a
threshold calulated according to .. .(7.75 for most images).

### Data analysis

## Results

### 2D-Template matching can be used to find ribosomal subunits in cryo-FIB thinned lamella of mammalian cells

To test whether we could detect individual ribosomes in mammalian cells
we prepared cryo-lamella of mouse neutrophil-like cells.
Low-magnification images of these lamellas clearly shows cellular
features consistent with a neutrophil-like phenotype, mainly a segmented
nucleus and a plethora of membrane-organelles, corresponding to the
granules and secretory vesicles of neutrophils. We then proceeded to
acquire micrographs on this lamella with a defocus of 0.5-1.0 um, 30
e/A2/s exposure and 1.5 A pixelsize. We manually selected multiple
locations in the lamella and focused using standard low-dose techniques,
i.e. by first ensuring correct focus by imaging a sacrifical area. The
resoluting micrographs showed no signs of crystalline ice and had
thon-rings to resolution, indicating successfull vitrification.

We used an atomic model of the 60S mouse ribosomal subunit (6SWA) for 2D
template matching. In a subset of images the distribution of
cross-correlation scores significantly exceeded the distribution
expected from non-signifcant matching(Figure 1B). In the resulting
scaled maximum-intensity maps, clear peaks with SNR thresholds up to 10
were apparent (Figure 1C). By using the criterion described by for
thresholding potential matches we found that in images of cytosolic
ompartments we found evidence of 10-500 ribosomes in the imaged areas.
Notably we found no matches in images that were taken in the nuclear
compartment. In the cytosolic areas we found a drastically different
number of matches, In somer areas we found only \~ 50 matches er image
area, corresponding to a concentration of..., while in another area we
found more than 500 matches, corresponding to a concentration of ... .

### cryo-EMILIA for 2D imaging of whole lamella

In order to obtain high-resolution data for complete lamella we used a
new approach for data collection. This approach uses three key
strategies: (1) ensures that every electron that exposes the sample is
collected on the camera (2) uses beam-image shift to precisely and
quickly raster the surface of the lamella and (3) uses a focusing
strategy that does not rely on a sacrificial area.

To ensure that every electron exposing the sample was captured by the
detector, we focused the electron beam so that the entire beam was
placed on the detector. During canonical low-dose imaging the microscope
is configured so that the focal plan is identical to the eucentric plane
of the specimen stage. This leaves the C2 aperture out of focus,
resulting in ripples at the edge of the beam (Figure 2B). While these
ripples are low-resolution features that might not interfere with 2D
template matching, which is designed to be robust to low-resolution
noise, we also tested collecting data under a condition where the C2
aperture is in focus (Figure 2C).

We then centered a lamella under the electron beam and used beam-image
shift of the microscope to systematically raster the whole surface of
the lamella in a hexagonal pattern. Instead of focusing in a sacrificial
area, we determined the defocus after every exposure using a routine
implemented in SerialEM modeled after CTFFind. The focus was then
adjusted based on the difference between desired and measured defocus.
Since we used a serpentine pattern for data collection every exposure is
close to the previous exposure making drastic changes in the defocus
unlikely. Furthermore we started our acquisition pattern on the platinum
deposition edge, so the initial exposure where the defocus was not yet
adjusted did not contain any biologically relevant information.

We used this strategy to collect data on 8 lamella, 4 using the
eucentric focus condition and 4 using the fringe-free condition. We were
able to highly consistently collect data with a defocus of 8 um (Figure
2D), both in the eucentric focus and fringe-free focus condition.
Together with the nominal defocus of the microscope this data results in
a topological map of the lamella. To ensure that data was collected
consistently, we mapped defocus values as a function of the applied
Beam-image shift (Figure 2E). This demonstrated that the defocus was
consistent over the lamella, with outliers only at isolated images and
in images containing contamination. We also plotted the measure
objective astigmatism of the lamella and found that it varies with the
applied Beam-image shift, become more astigmatic mostly due to
beam-image shift in the X direction. While approaches exist to correct
this during the data-collection, we opted to not use these mechanism for
these early experiments and instead rely on computational correction of
these aberrations in order to characterize them.

### 2D-Template matching of cryo-EMILIA data reveals ribosome distribution

We developed customized preprocessing protocol to images obtained by
cryo-EMILIA to enable their use for 2D-template matching. First we
restricted calculation of cross-correlation coefficients between
individual movie frames to the central portion of the image to prevent
artifacts from the beam edges on estimation of motion. Then we
calculated a mask that defined the illuminated area of the micrographs
and used it to fill non-illumated areas with gaussian noise, matching
mean and standard deviation to the illuminated signal (Figure 3A). The
so processed images were suitable for 2D-template matching and we were
able to obtained matches with the same model used for the data in Figure
1.

### Quantitative analysis of translation activity

## Discussion

-   Elizabeth Wright and Grant Jensen Montage tomography papers

-   Waffle method for higher throughput, automation of fib-milling

-   Throughput and bottlenecks

-   Visual proteomics

-   Granules containing ribosomes?

-   Threshold implications (no matches on most images)

## Figures

![Figure 1: Template matching of ribosomal large subunits in fib-milled
neutrophil like cells](media/image3.png){width="6.5in"
height="4.199437882764655in"}

Figure 1: Template matching of ribosomal large subunits in fib-milled
neutrophil like cells

![Figure 2: This is an
example-figurern](media/image4.png){width="6.291666666666667in"
height="3.9270833333333335in"}

Figure 2: This is an example-figurern

![Figure 3: This is an example-figurern](media/image5.png){width="6.5in"
height="3.510744750656168in"}

Figure 3: This is an example-figurern

![Figure 4: This is an
example-figurern](media/image6.png){width="6.302083333333333in"
height="3.9270833333333335in"}

Figure 4: This is an example-figurern

![Figure 5: This is an
example-figurern](media/image7.png){width="6.302083333333333in"
height="3.9270833333333335in"}

Figure 5: This is an example-figurern

![Figure 6: This is an example-figurern](media/image8.png){width="6.5in"
height="3.9929866579177604in"}

Figure 6: This is an example-figurern

![Figure 7: This is an
example-figurern](media/image9.png){width="6.291666666666667in"
height="3.9270833333333335in"}

Figure 7: This is an example-figurern

## References

[]{#ref-tSXIKPl7 .anchor}1. **Label-free, normalized quantification of
complex mass spectrometry data for proteomic analysis** Noelle M
Griffin, Jingyi Yu, Fred Long, Phil Oh, Sabrina Shore, Yan Li, Jim A
Koziol, Jan E Schnitzer *Nature Biotechnology* (2010-01)
<https://doi.org/fshgnc> DOI:
[10.1038/nbt.1592](https://doi.org/10.1038/nbt.1592) · PMID:
[20010810](https://www.ncbi.nlm.nih.gov/pubmed/20010810) · PMCID:
[PMC2805705](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2805705)

[]{#ref-VBmW7Aot .anchor}2. **Fluorescence microscopy** Jeff W Lichtman,
José-Angel Conchello *Nature Methods* (2005-11-18)
<https://doi.org/bbpg4n> DOI:
[10.1038/nmeth817](https://doi.org/10.1038/nmeth817) · PMID:
[16299476](https://www.ncbi.nlm.nih.gov/pubmed/16299476)

[]{#ref-tGQ6TSUo .anchor}3. **A visual approach to proteomics** Stephan
Nickell, Christine Kofler, Andrew P Leis, Wolfgang Baumeister *Nature
Reviews Molecular Cell Biology* (2006-02-15) <https://doi.org/d6d5mq>
DOI: [10.1038/nrm1861](https://doi.org/10.1038/nrm1861) · PMID:
[16482091](https://www.ncbi.nlm.nih.gov/pubmed/16482091)

[]{#ref-g8QavfwP .anchor}4. **Electron microscopy of frozen hydrated
sections of vitreous ice and vitrified biological samples** AW McDowall,
J-J Chang, R Freeman, J Lepault, CA Walter, J Dubochet *Journal of
Microscopy* (1983-07) <https://doi.org/bdnzmv> DOI:
[10.1111/j.1365-2818.1983.tb04225.x](https://doi.org/10.1111/j.1365-2818.1983.tb04225.x)
· PMID: [6350598](https://www.ncbi.nlm.nih.gov/pubmed/6350598)

[]{#ref-16IhS1Nc4 .anchor}5. **Opening windows into the cell:
focused-ion-beam milling for cryo-electron tomography** Elizabeth Villa,
Miroslava Schaffer, Jürgen M Plitzko, Wolfgang Baumeister *Current
Opinion in Structural Biology* (2013-10) <https://doi.org/f537jp> DOI:
[10.1016/j.sbi.2013.08.006](https://doi.org/10.1016/j.sbi.2013.08.006) ·
PMID: [24090931](https://www.ncbi.nlm.nih.gov/pubmed/24090931)

[]{#ref-Rksh2dxu .anchor}6. **Electron tomography of cells** Lu Gan,
Grant J Jensen *Quarterly Reviews of Biophysics* (2011-11-15)
<https://doi.org/czj9hr> DOI:
[10.1017/s0033583511000102](https://doi.org/10.1017/s0033583511000102) ·
PMID: [22082691](https://www.ncbi.nlm.nih.gov/pubmed/22082691)

[]{#ref-Ynb3IP6I .anchor}7. **Single-protein detection in crowded
molecular environments in cryo-EM images** JPeter Rickgauer, Nikolaus
Grigorieff, Winfried Denk *eLife* (2017-05-03) <https://doi.org/gnq4q4>
DOI: [10.7554/elife.25648](https://doi.org/10.7554/elife.25648) · PMID:
[28467302](https://www.ncbi.nlm.nih.gov/pubmed/28467302) · PMCID:
[PMC5453696](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5453696)

[]{#ref-18KGpXYPE .anchor}8. **Label-free single-instance protein
detection in vitrified cells** JPeter Rickgauer, Heejun Choi, Jennifer
Lippincott-Schwartz, Winfried Denk *Cold Spring Harbor Laboratory*
(2020-04-24) <https://doi.org/gpbjfd> DOI:
[10.1101/2020.04.22.053868](https://doi.org/10.1101/2020.04.22.053868)

[]{#ref-10bXZuF3G .anchor}9. **Locating macromolecular assemblies in
cells by 2D template matching with cisTEM** Bronwyn A Lucas, Benjamin A
Himes, Liang Xue, Timothy Grant, Julia Mahamid, Nikolaus Grigorieff
*eLife* (2021-06-11) <https://doi.org/gkkc49> DOI:
[10.7554/elife.68946](https://doi.org/10.7554/elife.68946) · PMID:
[34114559](https://www.ncbi.nlm.nih.gov/pubmed/34114559) · PMCID:
[PMC8219381](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8219381)

[]{#ref-gRoY21jY .anchor}10. **Hallmarks of ribosomopathies** Kim R
Kampen, Sergey O Sulima, Stijn Vereecke, Kim De Keersmaecker *Nucleic
Acids Research* (2019-07-27) <https://doi.org/gpbjfm> DOI:
[10.1093/nar/gkz637](https://doi.org/10.1093/nar/gkz637) · PMID:
[31350888](https://www.ncbi.nlm.nih.gov/pubmed/31350888) · PMCID:
[PMC7026650](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7026650)

[]{#ref-KAJ7221k .anchor}11. **Diagnostic and prognostic implications of
ribosomal protein transcript expression patterns in human cancers**
James M Dolezal, Arie P Dash, Edward V Prochownik *BMC Cancer*
(2018-03-12) <https://doi.org/gc87j9> DOI:
[10.1186/s12885-018-4178-z](https://doi.org/10.1186/s12885-018-4178-z) ·
PMID: [29530001](https://www.ncbi.nlm.nih.gov/pubmed/29530001) · PMCID:
[PMC5848553](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5848553)

[]{#ref-1B9Vt9eYu .anchor}12. **Inhibition of Dihydroorotate
Dehydrogenase Overcomes Differentiation Blockade in Acute Myeloid
Leukemia** David B Sykes, Youmna S Kfoury, François E Mercier, Mathias J
Wawer, Jason M Law, Mark K Haynes, Timothy A Lewis, Amir Schajnovitz,
Esha Jain, Dongjun Lee, ... David T Scadden *Cell* (2016-09)
<https://doi.org/f3r5jr> DOI:
[10.1016/j.cell.2016.08.057](https://doi.org/10.1016/j.cell.2016.08.057)
· PMID: [27641501](https://www.ncbi.nlm.nih.gov/pubmed/27641501) ·
PMCID:
[PMC7360335](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7360335)
