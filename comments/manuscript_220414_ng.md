This manuscript was automatically generated on April 14, 2022.

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
    icon](media/image3.png){width="0.16666666666666666in"
    height="0.16666666666666666in"}
    [0000-0002-1506-909X](https://orcid.org/0000-0002-1506-909X) ·
    ![GitHub icon](media/image4.png){width="0.16666666666666666in"
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
called "Defocus-Corrected Large-Area cryo-EM" (DeCo-LACE) to collect
high-resolution cryo-EM data over entire sections (100 -- 200 nm thick
lamellae) of neutrophil-like mouse cells, representing 1% - 2% of the
total cellular volume. We use 2D template matching (2DTM) to determine
localization and orientation of the large ribosomal subunit in these
sections, detect bound small ribosomal subunits and assign ribosomes to
polysomes based on their relative orientations to each other. These data
provide "maps" of translational activity across sections of mammalian
cells. This new high-throughput cryo-EM data collection approach
together with 2DTM will advance visual proteomics and complement other
single-cell "omics" techniques, such as flow-cytometry and single-cell
sequencing.

## Introduction

A major goal in understanding cellular processes is the knowledge of the
amounts, location, interactions, and conformations of biomolecules
inside the cell. This knowledge can be obtained by approaches broadly
divided into label- and label-free techniques. In label-dependent
techniques a probe is physically attached to a molecule of interest that
is able to be detected by its strong signal, such as a fluorescent
molecule. In label-free techniques, the physical properties of molecules
themselves are used for detection. An example for this is proteomics
using mass-spectrometry \[[1](#ref-tsxikpl7)\]. The advantage of
label-free techniques is that they can provide information over
thousands of molecules, while label-dependent techniques offer highly
specific information for a few molecules. Especially spatial information
can often only be achieved using label-dependent techniques, such as
fluorescence microscopy \[[2](#ref-VBmW7Aot)\].

Cryo-electron microscopy (cryo-EM) has the potential to directly
visualize the arrangement of atoms that compose biomolecules inside of
cells, thereby allowing label-free detection with high spatial accuracy.
This has been called "visual proteomics" \[[3](#ref-tGQ6TSUo)\]. Since
cryo-EM requires thin samples (\<500nm), imaging of biomolecules inside
cells is restricted to small organisms, thin regions of cells, or
samples that have been suitably thinned. Thinning can be achieved either
by mechanical sectioning \[[4](#ref-g8QavfwP)\] or by milling using a
focused ion beam (FIB) \[[5](#ref-16IhS1Nc4)\]. This complex workflow
leads to a low throughput of cryo-EM imaging of cells and is further
limited by the fact that at the required magnifications, typical fields
of view (FOV) are very small compared to mammalian cells, and the FOV
achieved by label-dependent techniques such as fluorescence light
microscopy. The predominant cryo-EM technique for the localization of
biomolecules of defined size and shape inside cells is cryo-electron
tomography \[[6](#ref-Rksh2dxu)\]. However, the requirement of a tilt
series at every imaged location and subsequent image alignment, severely
limits the throughput for molecular localization.

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
of a biomolecule in a cellular sample \[[8](#ref-18KGpXYPE)\]

Hematopoiesis is the process of generating the various cell types of the
blood in the bone marrow. Dysregulation of the process results in
diseases like leukemia. Understanding how hematopoietic stem and
progenitor cells are programmed to differentiate to the appropriate cell
type would be provide new insight how hematopoiesis can be misregulated.
Of special interest is the regulation of translation during
hematopoiesis. This is exemplified by the observation that genetic
defects in the ribosome machinery often leads to hematopoietic
disease\[[10](#ref-gRoY21jY)\]. As such direct quantification of
ribosome location, number and conformational states could lead to new
insight into hematopoietic disease \[[11](#ref-KAJ7221k)\].

Here we apply 2DTM of ribosomes to cryo-FIB milled neutrophil-like
murine cells \[[12](#ref-KAJ7221k)\]. To increase the amount of
collected data and to provide unbiased sampling of the whole lamella, we
devised a new data-acquisition scheme, Defocus-corrected large area
cryo-electron microscopy (DeCo-LACE). We characterize aberration cause
by the large image shifts and highly focused beams used to scan the
sample and find that they can be adequately corrected to enable ribosome
detection by 2DTM. The resulting data provide a description of ribosome
distribution in an entire lamellae, which represent roughly 2% of the
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

ER-HoxA9 cells were maintained in RPMI medium supplemented with 10% FBS,
penicillin/streptomycin, SCF, and estrogen \[[12](#ref-KAJ7221k)\] at
37C and 5% CO2. 120 h prior to grid preparation, cells were washed twice
in PBS and cultured in the same medium except without estrogen.
Differentiation was verified by staining with Hoechst-dye and inspection
of nuclear morphology. Cells were then counted and diluted to
$1 \cdot 10^{6}$ cells/ml. Grids (either 200 mesh copper grids, with a
sillicone-oxide and 2 µm holes with a 2 µm spacing or 200 mesh gold
grids with a thin gold film and 2 µm holes in 2 µm spacing) were
glow-discharged from both sides using a 15 mA for 45 s. 3.5 µl of cell
suspension was added to grids on the thin-film side and grids were
blotted from the back side using a GP2 cryoplunger (Leica) for 8 s and
rapidly plunged into liquid ethane at -185 °C.

### FIB-milling

Grids were loaded into an Acquilos 2 FIB/SEM (Thermo Fisher) microscope
with a stage cooled to -190 °C. Grids were sputter-coated with platinum
for 15 s at 45 mA and then coated with a layer of platinum-precursor by
opening the GIS-valve for 45 s. An overview of the grid was created by
montaging SEM images and isolated cells at the center of gridsquares
were selected for FIB-milling. Lamellae were generated automatically
using the AutoTEM software (Thermo Fisher), with the following
parameters:

-   Milling angle: 20°

```{=html}
<!-- -->
```
-   Rough milling: 3.2 µm thickness, 0.5nA current

```{=html}
<!-- -->
```
-   Medium milling: 1.8 µm thickness, 0.3nA current, 1.0° overtilt

```{=html}
<!-- -->
```
-   Fine milling: 1.0 µm tchickness, 0.1nA current, 0.5° overtilt

```{=html}
<!-- -->
```
-   Finer milling: 700 nm thickness, 0.1nA curent, 0.2° overtilt

```{=html}
<!-- -->
```
-   Polish 1: 450nm thickness, 50 pA current

```{=html}
<!-- -->
```
-   Polish 2: 200nm thickness, 30 pA current

This resulted in 6-8 μm wide lamellae with 150-250 nm thickness as
determined by FIB-imaging of the lamellae edges.

### Data collection

Grids were loaded into a Titan Krios TEM (Thermo Fisher) operated at 300
keV, and equipped with a BioQuantum energy filter (Gatan) and K3 camera
(Gatan). The microscope was aligned using a cross-grating grid on the
stage. Prior to each session we carefully performed the Image/Beam
calibration in nanoprobe. Then we set the magnification to a pixel size
of 1.76Å and condensed the beam to \~ 900nm diameter, resulting in the
beam being completely visible on the camera. To establish fringe-free
conditions, the "Fine eucentric" procedure of SerialEM was used to move
a square of the cross-grating grid to the eucentric position of the
microscope. The effective defocus was then set to 2 μm, using the
"autofocus" routine of SerialEM. The objective focus of the microscope
was changed until no fringes were visible. The stage was then moved in Z
until images had an apparent defocus of 2 μm. The difference in stage
Z-position between the eucentric and fringe-free conditions was used to
move other areas into fringe-free condition.

Low magnification montages were used to find lamellae, and lamellae that
were sufficiently thin and free of contamination were selected for
automated data collection. Overview images of each lamella were taken at
2250x magnification (39 Å pixel-size). The corners of the lamella in the
overview image were manually annotated in SerialEM and translated into
beam image shift values using SerialEM calibration. A hexagonal pattern
of image shift positions was calculated that covered the area between
the four corners in a serpentine way, with a sqrt(3) \* 400 nm
horizontal spacing and 800 nm vertical spacing. Exposures were taken at
each position with a 30 e^-^/Å${}^{2}$ total dose. After each exposure
the defocus was estimated using the ctffind function of SerialEM and the
focus for the next exposure was corrected by the difference between the
estimated focus and the desired defocus of 800 nm. Furthermore, after
each exposure the deviation of the beam from the center of the camera
was measured and corrected using the "CenterBeamFromImage" command of
SerialEM.

After data collection, a 20s exposure at 2250x magnification of the
lamella at 200 μm defocus was taken for visualization purposes. A python
script implementing this procedure is available at \[Link to repo\].

### Data pre-processing

To avoid influence of the beam edge on motion-correction, only a quarter
of the movie in the center of the camera was considered for calculation
of the estimated motion. After movie frames were aligned and summed a
mask for the illuminated area was calculated by lowpass filtering the
image with a 100-Å cutoff, thresholding the image at 10% of the maximal
value and then lowpass filtering the mask with a 100-Å cutoff to smooth
the mask edges. This mask was then used to select un-illuminated areas
in the image and fill the pixels with Gaussian noise, with the same mean
and standard deviation as the illuminated area. A custom version of the
unblur program \[cite\] implementing this procedure is available at
\[link to decolace branch\]. The contrast-transfer function (CTF) was
estimated using ctffind, searching between 0.02 and 2 μm defocus.

### 2DTM

The search template was generated from the cryo-EM structure of the
mouse large ribosomal subunit (PDB 6SWA) using the cryo-EM simulator
implemented in *cis*TEM \[cite\]. The atomic coordinates corresponding
to subunit Epb1 were deleted from the model and the simulator was used
to calculate a density map from the atomic coordinates. The
match_template program \[cite\] was used to search for this template in
the movie-aligned, exposure-filtered and masked images, using a 1.5°
angular step in out-of-plane angles and 1.0° in-plane. 11 defocus planes
in 20 nm steps centered around the ctffind defocus estimates were
searched. Targets were defined as detected when their matches with a
template produced peaks with a signal-to-noise ratio (SNR) above a
threshold of 7.75, which was chosen based on the
one-false-positive-per-tile criterion \[cite\].

### DeCo-LACE data processing

An overview of the data analysis pipeline is shown in Fig.
[6](#fig:deco_lace_workflow). Initial coordinates of each tile $i$,
$\text{c}_{init,i}$ were derived from the beam image shift of the tile,
$BIS_{i}$, and the ISToCamera matrix $IC$:

$\text{c}_{init,i} = IC \cdot BIS_{i}$

To refine the montage, a list of overlapping tile pairs
$\left| \text{c}_{i} - \text{c}_{j} \right| < 900\text{nm}$ were
compiled and the offsets $\text{o}_{i,j} = \text{c}_{i} - \text{c}_{j}$
were refined by using a masked cross-correlation of the overlap region
as implemented in the scikit-image package \[cite\]. Refined coordinates
were then derived by least-squares minimization of the new offsets and
tile positions:

$\min\sum_{pairs}^{}\left( \text{o}_{refined,i,j} - \left( \text{c}_{i} - \text{c}_{j} \right) \right)^{2}$

using the scipy package \[cite\]. This refinement was repeated once more
to arrive at the final tile alignment.

The x,y coordinates of target $n$ detected by 2DTM in the tile $i$,
$\text{m}_{n,i}^{\text{T}}$, was transformed into the montage frame by
adding the coordinate of the tile.

$\text{m}_{n}^{\text{M}} = \text{m}_{n,i}^{\text{T}} + \text{c}_{i}$

The z coordinate of each target was calculated as the sum of the defocus
offset for the target, the estimated defocus of the tile, and the
nominal defocus of the microscope when the tile was acquired. The python
scripts used for data processing are available under \[repolink\].

## Results

### 2DTM detects large ribosomal subunits in cryo-FIB lamellae of mammalian cells

To test whether we could detect individual ribosomes in mammalian cells
we prepared cryo-lamellae of mouse neutrophil-like cells.
Low-magnification images of these lamellae clearly shows cellular
features consistent with a neutrophil-like phenotype, mainly a segmented
nucleus and a plethora of membrane-organelles, corresponding to the
granules and secretory vesicles of neutrophils (Fig.
[1](#fig:initmatching)A). We then proceeded to acquire micrographs on
these lamellae with a defocus of 0.5-1.0 μm, 30 e^-^/Å2/s exposure and
1.5 Å pixel size. We manually selected multiple locations in the
lamellae and acquired micrographs using standard low-dose techniques
where focusing is performed on a sacrificial area. The resulting
micrographs showed smooth bilayered membranes and no signs of
crystalline ice (Fig. [1](#fig:initmatching)C,D), indicating successful
vitrification.

We used an atomic model of the 60S mouse ribosomal subunit (6SWA) for
2DTM. In a subset of images the distribution of cross-correlation scores
significantly exceeded the distribution expected images devoid of
detectable targets. In the resulting scaled maximum-intensity
projections (MIPs), clear peaks with SNR values up to 10 were apparent
(Fig. [S1](#fig:initmatching2)A). Using a threshold criterion to select
significant targets (see Methods) we found that in images of cytosolic
compartments there were 10-500 ribosomes in the imaged areas (Fig.
[1](#fig:initmatching)B-E). Notably, we found no targets in areas
corresponding to the nucleus (Fig. [1](#fig:initmatching)B) or
mitochondria (Fig. [1](#fig:initmatching)D). In the cytoplasm we found a
highly variable number of targets, only \~ 50 in some areas (Fig.
[1](#fig:initmatching)E) and up to 500 in others (Fig.
[1](#fig:initmatching)C). This is a ten-fold difference in local
ribosome concentration, highlighting the importance of imaging larger
areas of a lamella to gain a complete picture of target distributions.
We therefore set out to collect cryo-EM data for 2DTM from mammalian
cell lamellae in a high-throughput unbiased fashion.

### DECO-LACE for 2D imaging of whole lamellae

In order to obtain high-resolution data from complete lamellae, we used
a new approach for data collection. This approach uses three key
strategies: (1) every electron that exposes a fresh area of the sample
is collected on the camera (2) image shift is used to precisely and
quickly raster the surface of a lamella and (3) focusing without using a
sacrificial area (Fig. [2](#fig:approach)A).

To ensure that every electron exposing a fresh area of the sample is
captured by the detector, we adjusted the electron beam size to be
entirely contained by the detector area. During canonical low-dose
imaging the microscope is configured so that the focal plane is
identical to the eucentric plane of the specimen stage. This leaves the
C2 aperture out of focus, resulting in ripples at the edge of the beam
(Fig. [2](#fig:approach)D). While these ripples are low-resolution
features that likely do not interfere with 2DTM \[cite\], we also tested
data collection under conditions where the C2 aperture is in focus
("fringe-free", Fig. [2](#fig:approach)E).

We then centered a lamella on the optical axis of the microscope and
used the image shift controls of the microscope to systematically scan
the whole surface of the lamella in a hexagonal pattern (Fig.
[2](#fig:approach)A,C). Instead of focusing on a sacrificial area, we
determined the defocus from every exposure after it was taken. The
defocus was then adjusted based on the difference between desired and
measured defocus (Fig. [2](#fig:approach)B). Since we used a serpentine
pattern for data collection, every exposure was close to the previous
exposure, making large changes in the defocus unlikely. Furthermore, we
started our acquisition pattern on the platinum deposition edge to make
sure that the initial exposure where the defocus was not yet adjusted
did not contain any biologically relevant information.

We used this strategy to collect data on eight lamellae, four using the
eucentric focus condition, hereafter referred to as Lamella~EUC~, and
four using the fringe-free condition, hereafter referred to as
Lamella~FFF~(Fig. [S2](#fig:lamella_images)). We were able to collect
data with a highly consistent defocus of 800nm (Fig.
[2](#fig:approach)F), both in the eucentric focus and fringe-free focus
condition. To ensure that data were collected consistently, we mapped
defocus values as a function of the applied image shift (Fig.
[S3](#fig:lamella_spatial_info)A). This demonstrated that the defocus
was consistent across a lamella, with rare outliers and in images
containing contamination. We also plotted the measured objective
astigmatism of each lamella and found that it varies with the applied
image shift, becoming more astigmatic mostly due to image shift in the X
direction (Fig. [S3](#fig:lamella_spatial_info)B). While approaches
exist to correct for this during the data collection \[cite\], we opted
to not use these approaches in our initial experiments. We reasoned that
because 2DTM depends on high-resolution information, this would be an
excellent test of how much these aberration affect imaging.

We assembled the tile micrographs into a montage using the image-shift
values and the SerialEM calibration followed by cross-correlation based
refinement (see Methods). In the resulting montages the same cellular
features visible in the overview images are apparent (Fig.
[S3](#fig:lamella_spatial_info)G-J), however due to the high
magnification and low defocus many more details, such as the membrane
bilayer seperation can be observed. For montages collected using the
eucentric condition, there are clearly visible fringes at the edges
between the tiles, which are absent in the fringe-free focus montages.
In our analysis below, we show that these fringes do not impede target
detection by 2DTM, making them primarily an aesthetic issue. We also
note that the serpentine tiling pattern is visible in the montages,
which we believe is due to the non-linear behaviour of the K3 camera
(see Dicussion).

The montages show membrane vesicles and granules with highly variable
sizes and density. We found furthermore that a substantial number of
granules with a high density seemed to contain a membrane-enclosed
inclusion with density similar to the surrounding cytosol (Fig.
\[TODO\]). \[Describe measurements\]

### 2DTM of DeCo-LACE data reveals ribosome distribution in cellular cross-sections

In our initial attempts of using 2DTM on micrographs acquired with the
DeCo-LACE protocol, we did not observe any SNR peaks above threshold
using the large subunit of the mouse ribosome (Fig.
[S4](#fig:crop_unblur)A). We reasoned that the edges of the beam might
interfere with motion-correction of the movies as they represent strong
low-resolution features that do not move with the sample. When we
cropped the movie frames to exclude the beam edges the estimated amount
of motion increased (Fig. [S4](#fig:crop_unblur)B), consistent with
successful tracking of sample motion. Furthermore, in the
motion-corrected average we could identify significant SNR peaks (Fig.
[S4](#fig:crop_unblur)B), confirming to high sensitivity of 2DTM to the
presents of high-resolution signal preserved in the images by the motion
correction. To streamline data processing, we implemented a function in
unblur to consider only defined central area of a movie for estimation
of sample motion, while still averaging the complete movie frames (Fig.
[S4](#fig:crop_unblur)B). Using this approach, we motion-corrected all
tiles in the eight lamellae and found consistently total motion below 1
Å per frame (Fig. [S5](#fig:lamella_motion_thickness) A). In some
lamellae we found increased motion in the lamella center, which
indicates areas of variable mechanical stability within FIB-milled
lamellae. In some micrographs we also observed that the beam edges gave
rise to artifacts in the MIP and numerous false-positive detections at
the edge of the illuminated area (Fig. TODO). A similar phenomenon was
observed on isolated "hot" pixels in unilluminated areas. To overcome
this issue we implemented a function in unblur to replace unillluminated
areas in the micrograph with Gaussian noise (see Methods), with mean and
standard deviation matching the illuminated portion of the micrograph
(Fig. TODO). Together, these pre-processing steps enabled us to perform
2DTM on all tiles of the eight lamellae.

We used the refined tile positions to calculate the positions of the
detected LSUs in the lamellae (Fig. [4](#fig:matching_euc) A, Fig.
[5](#fig:matching_fff) A). Overlaying these positions of the lamellae
montages reveal ribosome distribution throughout the FIB-milled slices
of individual cells. Organelles like the nucleus and mitochondria only
showed sporadic targets detected with low SNRs, consistent with the
estimated false-positive rate on one per tile. For each detected target
we also calculated the Z positions from the individual estimated defocus
and defocus offset for each tile. When viewed from the side the ribosome
positions therefore show the slight tilts of the lamellae relative to
the microscope frame of reference (Fig. [4](#fig:matching_euc) B, Fig.
[5](#fig:matching_fff) B). Furthermore, the side views indicated that
lamellae were thinner at the leading edge. Indeed, when we plotted the
transmitted beam intensities in individual tiles as a function of image
shift we observed substantially higher intensities at the leading edge,
which in energy-filtered TEM indicates a thinner sample \[cite\]. Even
though we prepared the lamellae with the "overtilt" approach \[cite\],
this means that ribosome densities across the lamellae can be skewed by
a change in thickness, and better sample preparation methods are needed
to generate more even samples.

Close inspection of the ribosome positions in the lamellae revealed
several interesting features. Ribosomes could be seen associating with
membranes, in patterns reminiscent of the rough endoplasmic reticulum
(Fig. [4](#fig:matching_euc) C, Fig. [5](#fig:matching_fff) C) or the
outer nuclear membrane (Fig. [4](#fig:matching_euc) D). We also observed
ribosomes forming ring-like structures (Fig. [4](#fig:matching_euc) E),
potentially indicating circularized mRNAs \[cite\]. While ribosomes were
for the most part excluded from the numerous granules observed in the
cytoplasm, in some cases we observed clusters of ribosomes in low
density inclusions in double-membraned granules described earlier (Fig.
[4](#fig:matching_euc) F, Fig. [5](#fig:matching_fff) D,E). It is, in
principle, possible that these targets are situated above or below the
imaged granules, since the granule positions in Z cannot be determined
using 2D projections. However, in the case of Fig.
[5](#fig:matching_fff) E, the detected ribosomes span the whole lamella
in the Z direction, while positions above or below a granule would
result in ribosomes situated exlusively at the top or bottom of the
lamella. This conclusive evidence of ribosomes in inclusions is
consistent with the earlier hypothesis that the inclusions are of
cytoplasmic origin.

Between the eight lamellae we found different number of detected targets
(Fig. [3](#fig:matching_stat) A). Lamella~EUC~ 1 has in the most
targets, but also has the largest surface area and contained cytoplasm
from two cells. Lamella~FFF~ 4 had the fewest detected targets, but this
particular lamella was dominated by a circular section of the nucleus,
with only small pockets of cytoplasm (Fig. [S2](#fig:lamella_images)).
In an attempt to normalize for these differences in lamella surface
area, we compared the number of detected targets per tile in tiles that
contained more than one target, which should exclude tiles with
non-cytosolic content (Fig. [3](#fig:matching_stat) B). While this
measure had less variablity, there were still differences. Lamella~EUC~
4 had not only the fewest targets, but also the lowest density, which
could be due to lamella being thinnest, or due to a section of the cells
with a lower concentration of ribosomes. Lamella~FFF~ 3 had a
substantially higher number of ribosomes per tile. Since all of these
lamellae were made from identical cells under identical conditions, this
underscores the necessity to collect data from large numbers of lamellae
to capture the inherent variability. When comparing the distribution of
scores between lamellae, we found them to be fairly comparable with a
median of \[todo get values, test\]. Lamella~EUC~ 1 had slightly lower
scores compared to the rest, potentially due to its large size and
connected mechanical instability during imaging. Overall, we did not
observe differences in the number or SNR of detected targets between
eucentric or fringe-free illumination conditions that were bigger than
the observed inter-lamella variability.

Since the SNR values of 2DTM are highly sensitive to image quality, we
reasoned we could use them to verify that DeCo-LACE does not introduce a
systematic loss of image quality. We considered non-parallel
illumination introduced by the unusually condensed beam and
uncharacterized aberrations near the beam periphery. When plotting the
SNR values of detected targets in all eight lamellae as a function of
their location in the tiles, we found uniformly high SNR values
throughout the illuminated areas for both eucentric and fringe-free
focus illumination, demonstrating that both illumination schemed are
suitable for DeCo-LACE.

We also wondered whether large image shifts would lead aberration due to
the astigmatism or beam tilt \[cite\]. \[TODO plot scores vs BIS, euc vs
fff\]

### Computation is the bottleneck of visual proteomics

As described above, the variability of lamellae, both in terms of
experimental parameters including area, thickness and mechanical
stability, and in terms of biology, such as selection of cell type and
location of the section within the cell, requires the collection orders
of magnitude more data to draw quantitative and statistically relevant
conclusions about the number and location of molecules under different
experimental conditions. The samples used were prepared in two 24 h
sessions on a FIB/SEM instrument, and imaging was performed during
another two 24h session on the TEM microscope. Inspections of the
timestamps of the raw data files revealed that the milling time per
lamella was \~30 minutes and TEM imaging was accomplished in \~10
seconds per tile or 90 minutes for a \~ 6x6 μm lamella. Processing of
the data, however, took substantially longer. Specifically, 2DTM of all
tiles took approximately one week per lamella on 32 A100 GPUs.
Computation is therefore a bottleneck in our current workflow, and
further optimizations of the algorithm may be necessary increase
throughput. Alternatively, this bottleneck could be reduced by
increasing the number of processing units.

## Discussion

-   Elizabeth Wright and Grant Jensen Montage tomography papers

```{=html}
<!-- -->
```
-   Waffle method for higher throughput, automation of fib-milling

```{=html}
<!-- -->
```
-   Throughput and bottlenecks

```{=html}
<!-- -->
```
-   lamella mechanical properties, radiation damage, other ways to to
    thin?

```{=html}
<!-- -->
```
-   eucentric vs fringe free illumination

```{=html}
<!-- -->
```
-   Visual proteomics

```{=html}
<!-- -->
```
-   Granules containing ribosomes?

```{=html}
<!-- -->
```
-   Threshold implications (no detected targets in most images)

```{=html}
<!-- -->
```
-   K3 not linear

## Figures

![Figure 1: 2D template matching of the large subunit of the ribosome in
fib-milled neutrophil-like cells (A) Overview image of the lamella.
Major cellular regions are labeled, as Nucleus (Nuc), Mitochondria (M),
and granular cytoplasm (GrCyt). FOVs where high-magnification images for
template matching where acquired are indicated as boxes with the number
of matches indicated on the bottom right. FOVs displayed in Panels B-E
are color-coded. (B-E) FOVs with projection of ribosome LSU matches
shown in green. (B) Perinuclear region, the only matches are in the
cytoplasmic half. (C) Cytoplasmic region with high density of ribosomes
(D) Mitochondrium, as expected there are only matches in the cytoplasmic
region (E) Cytoplasm, with low density of
ribosomes.](media/image5.png){width="6.5in"
height="3.4208333333333334in"}

Figure 1: 2D template matching of the large subunit of the ribosome in
fib-milled neutrophil-like cells. (A) Overview image of the lamella.
Major cellular regions are labeled, as Nucleus (Nuc), Mitochondria (M),
and granular cytoplasm (GrCyt). FOVs where high-magnification images for
template matching where acquired are indicated as boxes with the number
of detected targets indicated on the bottom right. FOVs displayed in
Panels B-E are color-coded. (B-E) FOVs with projection of detected
ribosome LSUs shown in green. (B) Perinuclear region, the only detected
targets are in the cytoplasmic half. (C) Cytoplasmic region with high
density of ribosomes. (D) Mitochondrium, as expected there are only
targets in the cytoplasmic region. (E) Cytoplasm, with low density of
ribosomes.

![Figure S1: 2D template matching of the large subunit of the ribosome
in fib-milled neutrophil-like cells (A) Maximum intensity projection
cross-correlation map of micrograph shown in Figure 1 (B+C) 3D plot of
MIP regions indicated by color boxes in Panel
A](media/image6.png){width="6.5in" height="4.501388888888889in"}

Figure S1: 2D template matching of the large subunit of the ribosome in
fib-milled neutrophil-like cells. (A) Maximum intensity projection (MIP)
of micrograph shown in Figure [1](#fig:initmatching). (B+C) 3D plot of
MIP regions indicated by color boxes in Panel A

![Figure 2: DeCo-LACE approach (A) Graphic demonstrating the
data-collection strategy for DeCo-LACE. The electron beam is condensed
to a diameter D\_{Beam} that allows captured of the whole illuminated
area on the camera. Beam-image shift along X and Y (BIS_X,\$BIS_Y) is
used to raster the whole lamella (B) Diagram of the collection algorithm
(C) Example overview image of a lamella with the designated acquisition
positions and the used beam diameter indicated with red circles (D+E)
Representative micrographs takne with a condensed beam at eucentric
focus (D) or fringe-free focus (E) (F) Boxplot of defocus measured by
ctffind of micrographs taken by the DeCo-LACE approach on 4 lamella
images at eucentric focus and 4 lamella imaged with fringe-free focus.
(F+G) Lamella overview images of lamella imaged at eucentric focus (F)
Overview image taken at low magnification (40Å pixel size) (G) Overview
created by montaging high magnification images taken with the DeCo-LACE
approach (1.5Å pixelsize) (H+I) Lamella overview images of lamella
imaged at fringe-free focus (H) Overview image taken at low
magnification (40Å pixel size) (I) Overview created by montaging high
magnification images taken with the DeCo-LACE approach (1.5Å
pixelsize)](media/image7.png){width="6.5in"
height="6.513888888888889in"}

Figure 2: DeCo-LACE approach. (A) Graphic demonstrating the
data-collection strategy for DeCo-LACE. The electron beam is condensed
to a diameter $D_{Beam}$ that allows captured of the whole illuminated
area on the camera. Beam image shift along X and Y
($BIS_{X}$,\$$BIS_{Y}$) is used to scan the whole lamella. (B) Diagram
of the collection algorithm. (C) Example overview image of a lamella
with the designated acquisition positions and the used beam diameter
indicated with red circles. (D+E) Representative micrographs takne with
a condensed beam at eucentric focus (D) or fringe-free focus (E). (F)
Boxplot of defocus measured by ctffind of micrographs taken by the
DeCo-LACE approach on four lamella images at eucentric focus and four
lamella imaged with fringe-free focus. (F+G) Lamella overview images of
lamella imaged at eucentric focus. (F) Overview image taken at low
magnification (40Å pixel size). (G) Overview created by montaging high
magnification images taken with the DeCo-LACE approach (1.5Å pixelsize).
(H+I) Lamella overview images of lamella imaged at fringe-free focus.
(H) Overview image taken at low magnification (40Å pixel size). (I)
Overview created by montaging high magnification images taken with the
DeCo-LACE approach (1.5Å pixelsize)

![Figure S2: Overview images of lamellae imaged using the DeCo-LACE
approach taken at low-magnification](media/image8.png){width="6.5in"
height="3.3875in"}

Figure S2: Overview images of lamellae imaged using the DeCo-LACE
approach taken at low-magnification

![Figure S3: Defocus estimation of individual tiles of DeCo-LACE
montages (A) Defocus values of individual micrographs taken using the
DeCo-LACE approach plotted as a function of the Beam-Image-Shift values.
(B) Defocus astigmatism of individual micrographs taken using the
DeCo-LACE approach plotted as a function of the Beam-Image-Shift
values.](media/image9.png){width="6.5in" height="6.940277777777778in"}

Figure S3: Defocus estimation of individual tiles of DeCo-LACE montages.
(A) Defocus values of individual micrographs taken using the DeCo-LACE
approach plotted as a function of the beam image-shift values. (B)
Defocus astigmatism of individual micrographs taken using the DeCo-LACE
approach plotted as a function of the image-shift values.

![Figure S4: Motion correction of movies with condensed beams. At the
top of each panel is an average of the movie that was motion-corrected
with a red dashed box indicating the region that was used to estimate
shifts. Below is a graph indicating the estimated shifts of the
individual frames of the movie. Below this is the MIP of 2DTM using the
large subunit of the mouse ribosome. (A) Motion correction of the whole
movie (B) Notion correction of a cropped region of the movie that
eliminates the beam edges (C) Motion correction of the whole movie,
using only hte cropped region to estimate the
shifts](media/image10.png){width="6.5in" height="4.3590277777777775in"}

Figure S4: Motion correction of movies with condensed beams. At the top
of each panel is an average of the movie that was motion-corrected with
a red dashed box indicating the region that was used to estimate shifts.
Below is a graph indicating the estimated shifts of the individual
frames of the movie. Below this is the MIP of 2DTM using the large
subunit of the mouse ribosome. (A) Motion correction of the whole movie.
(B) Notion correction of a cropped region of the movie that eliminates
the beam edges. (C) Motion correction of the whole movie, using only the
central region to estimate the shifts

![Figure S5: Motion correction of individual tiles imaged using the
DeCo-LACE approach (A) Total estimated motion of individual micrographs
taken using the DeCo-LACE approach plotted as a function of the
Beam-Image-Shift values. (B) Electron intensity of individual
micrographs taken using the DeCo-LACE approach plotted as a function of
the Beam-Image-Shift values.](media/image11.png){width="6.5in"
height="6.940277777777778in"}

Figure S5: Motion correction of individual tiles imaged using the
DeCo-LACE approach. (A) Total estimated motion of individual micrographs
taken using the DeCo-LACE approach plotted as a function of the beam
image-shift values. (B) Electron intensity of individual micrographs
taken using the DeCo-LACE approach plotted as a function of the
image-shift values.

![Figure 3: Statistics of 2DTM on lamella imaged using DeCo-LACE (A)
Number of matches of each lamella (B) Distribution of matches per tile
in each lamella. Only tiles with two or more matches were included (C)
Distribution of SNRs in each lamella (D) For each lamella an average of
all tiles is shown. Overlaid is a scatterplot of all matches in these
tiles according to their in-tile coordinates. Scatterplot is color
according to the SNR. There are no matches in the top circle-circle
intersection due to radiation damage from previous
exposures.](media/image12.png){width="6.5in"
height="4.295833333333333in"}

Figure 3: Statistics of 2DTM on lamella imaged using DeCo-LACE. (A)
Number of detected targets in each lamella. (B) Distribution of targets
per tile in each lamella. Only tiles with two or more targets were
included. (C) Distribution of SNRs in each lamella. (D) For each lamella
an average of all tiles is shown. Overlaid is a scatterplot of all
detected targets in these tiles according to their in-tile coordinates.
Scatterplot is color according to the detection SNR. There are no
detected targets in the top circle-circle intersection due to radiation
damage from previous exposures.

![Figure 4: Template matching in lamella imaged using the DeCo-LACE
approach at eucentric focus (A) Montage of Lamella\_\\textrm{EUC} 1
overlaid with matches according to their montage coordinates (B) Side
view of matches in the lamella, such that the direction of the electron
beam is horizontal. (C-F) Magnified area of panel A showing rough ER
with associated ribosomes(C), outer nuclear membrane with associated
ribosomes (D), ribsomes arranged in a circular fashion(E), ribosomes
enclosed in a less electron dense inclusion in a
granule(F).](media/image13.png){width="6.5in" height="4.79375in"}

Figure 4: Template matching in lamella imaged using the DeCo-LACE
approach at eucentric focus. (A) Montage of Lamella${}_{\text{EUC}}$ 1
overlaid with detected targets according to their montage coordinates.
(B) Side view of targets in the lamella, such that the direction of the
electron beam is horizontal. (C-F) Magnified area of panel A showing
rough ER with associated ribosomes (C), outer nuclear membrane with
associated ribosomes (D), ribsomes arranged in a circular fashion(E),
ribosomes enclosed in a less electron dense inclusion in a granule (F).

![Figure 5: Template matching in lamella imaged using the DeCo-LACE
approach at fringe-free focus (A) Montage of Lamella\_\\textrm{FFF} 4
overlaid with matches according to their montage coordinates (B) Side
view of matches in the lamella, such that the direction of the electron
beam is horizontal. (C-E) Magnified area of panel A showing rough ER
with associated ribosomes(C) and ribosomes enclosed in a less electron
dense inclusion in a granule(D,E). (F) Side view of panel E with
ribosomes situated inside the granule colored accoding to SNR and other
ribosomes colored in grey.](media/image14.png){width="6.5in"
height="4.79375in"}

Figure 5: Template matching in lamella imaged using the DeCo-LACE
approach at fringe-free focus. (A) Montage of Lamella${}_{\text{FFF}}$ 4
overlaid with detected targets according to their montage coordinates.
(B) Side view of targets in the lamella, such that the direction of the
electron beam is horizontal. (C-E) Magnified area of panel A showing
rough ER with associated ribosomes (C) and ribosomes enclosed in a less
electron dense inclusion in a granule (D,E). (F) Side view of panel E
with ribosomes situated inside the granule colored accoding to SNR and
other ribosomes colored in grey.

![Figure 6: Workflow of DeCo-LACE
processing](media/image15.png){width="6.5in" height="6.5in"}

Figure 6: Workflow of DeCo-LACE processing

## References

1\. **Label-free, normalized quantification of complex mass spectrometry
data for proteomic analysis** Noelle M Griffin, Jingyi Yu, Fred Long,
Phil Oh, Sabrina Shore, Yan Li, Jim A Koziol, Jan E Schnitzer *Nature
Biotechnology* (2010-01) <https://doi.org/fshgnc> DOI:
[10.1038/nbt.1592](https://doi.org/10.1038/nbt.1592) · PMID:
[20010810](https://www.ncbi.nlm.nih.gov/pubmed/20010810) · PMCID:
[PMC2805705](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2805705)

[]{#ref-tsxikpl7 .anchor}2. **Fluorescence microscopy** Jeff W Lichtman,
José-Angel Conchello *Nature Methods* (2005-11-18)
<https://doi.org/bbpg4n> DOI:
[10.1038/nmeth817](https://doi.org/10.1038/nmeth817) · PMID:
[16299476](https://www.ncbi.nlm.nih.gov/pubmed/16299476)

[]{#ref-VBmW7Aot .anchor}3. **A visual approach to proteomics** Stephan
Nickell, Christine Kofler, Andrew P Leis, Wolfgang Baumeister *Nature
Reviews Molecular Cell Biology* (2006-02-15) <https://doi.org/d6d5mq>
DOI: [10.1038/nrm1861](https://doi.org/10.1038/nrm1861) · PMID:
[16482091](https://www.ncbi.nlm.nih.gov/pubmed/16482091)

[]{#ref-tGQ6TSUo .anchor}4. **Electron microscopy of frozen hydrated
sections of vitreous ice and vitrified biological samples** AW McDowall,
J-J Chang, R Freeman, J Lepault, CA Walter, J Dubochet *Journal of
Microscopy* (1983-07) <https://doi.org/bdnzmv> DOI:
[10.1111/j.1365-2818.1983.tb04225.x](https://doi.org/10.1111/j.1365-2818.1983.tb04225.x)
· PMID: [6350598](https://www.ncbi.nlm.nih.gov/pubmed/6350598)

[]{#ref-g8QavfwP .anchor}5. **Opening windows into the cell:
focused-ion-beam milling for cryo-electron tomography** Elizabeth Villa,
Miroslava Schaffer, Jürgen M Plitzko, Wolfgang Baumeister *Current
Opinion in Structural Biology* (2013-10) <https://doi.org/f537jp> DOI:
[10.1016/j.sbi.2013.08.006](https://doi.org/10.1016/j.sbi.2013.08.006) ·
PMID: [24090931](https://www.ncbi.nlm.nih.gov/pubmed/24090931)

[]{#ref-16IhS1Nc4 .anchor}6. **Electron tomography of cells** Lu Gan,
Grant J Jensen *Quarterly Reviews of Biophysics* (2011-11-15)
<https://doi.org/czj9hr> DOI:
[10.1017/s0033583511000102](https://doi.org/10.1017/s0033583511000102) ·
PMID: [22082691](https://www.ncbi.nlm.nih.gov/pubmed/22082691)

[]{#ref-Rksh2dxu .anchor}7. **Single-protein detection in crowded
molecular environments in cryo-EM images** JPeter Rickgauer, Nikolaus
Grigorieff, Winfried Denk *eLife* (2017-05-03) <https://doi.org/gnq4q4>
DOI: [10.7554/elife.25648](https://doi.org/10.7554/elife.25648) · PMID:
[28467302](https://www.ncbi.nlm.nih.gov/pubmed/28467302) · PMCID:
[PMC5453696](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5453696)

[]{#ref-Ynb3IP6I .anchor}8. **Label-free single-instance protein
detection in vitrified cells** JPeter Rickgauer, Heejun Choi, Jennifer
Lippincott-Schwartz, Winfried Denk *Cold Spring Harbor Laboratory*
(2020-04-24) <https://doi.org/gpbjfd> DOI:
[10.1101/2020.04.22.053868](https://doi.org/10.1101/2020.04.22.053868)

[]{#ref-18KGpXYPE .anchor}9. **Locating macromolecular assemblies in
cells by 2D template** **matching with cisTEM** Bronwyn A Lucas,
Benjamin A Himes, Liang Xue, Timothy Grant, Julia Mahamid, Nikolaus
Grigorieff *eLife* (2021-06-11) <https://doi.org/gkkc49> DOI:
[10.7554/elife.68946](https://doi.org/10.7554/elife.68946) · PMID:
[34114559](https://www.ncbi.nlm.nih.gov/pubmed/34114559) · PMCID:
[PMC8219381](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8219381)

[]{#ref-10bXZuF3G .anchor}10. **Hallmarks of ribosomopathies** Kim R
Kampen, Sergey O Sulima, Stijn Vereecke, Kim De Keersmaecker *Nucleic
Acids Research* (2019-07-27) <https://doi.org/gpbjfm> DOI:
[10.1093/nar/gkz637](https://doi.org/10.1093/nar/gkz637) · PMID:
[31350888](https://www.ncbi.nlm.nih.gov/pubmed/31350888) · PMCID:
[PMC7026650](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7026650)

[]{#ref-gRoY21jY .anchor}11. **Diagnostic and prognostic implications of
ribosomal protein transcript expression patterns in human cancers**
James M Dolezal, Arie P Dash, Edward V Prochownik *BMC Cancer*
(2018-03-12) <https://doi.org/gc87j9> DOI:
[10.1186/s12885-018-4178-z](https://doi.org/10.1186/s12885-018-4178-z) ·
PMID: [29530001](https://www.ncbi.nlm.nih.gov/pubmed/29530001) · PMCID:
[PMC5848553](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5848553)

[]{#ref-KAJ7221k .anchor}12. **Inhibition of Dihydroorotate
Dehydrogenase Overcomes Differentiation Blockade in Acute Myeloid
Leukemia** David B Sykes, Youmna S Kfoury, François E Mercier, Mathias J
Wawer, Jason M Law, Mark K Haynes, Timothy A Lewis, Amir Schajnovitz,
Esha Jain, Dongjun Lee, ... David T Scadden *Cell* (2016-09)
<https://doi.org/f3r5jr> DOI:
[10.1016/j.cell.2016.08.057](https://doi.org/10.1016/j.cell.2016.08.057)
· PMID: [27641501](https://www.ncbi.nlm.nih.gov/pubmed/27641501) ·
PMCID:
[PMC7360335](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7360335)
