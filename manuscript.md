---
title: Visual proteomics using whole-lamella 2D template matching
keywords:
- cryo-EM
- visual protemics
- ribosome
lang: en-US
date-meta: '2022-04-14'
author-meta:
- Johannes Elferich
- Nikolaus Grigorieff
header-includes: |-
  <!--
  Manubot generated metadata rendered from header-includes-template.html.
  Suggest improvements at https://github.com/manubot/manubot/blob/main/manubot/process/header-includes-template.html
  -->
  <meta name="dc.format" content="text/html" />
  <meta name="dc.title" content="Visual proteomics using whole-lamella 2D template matching" />
  <meta name="citation_title" content="Visual proteomics using whole-lamella 2D template matching" />
  <meta property="og:title" content="Visual proteomics using whole-lamella 2D template matching" />
  <meta property="twitter:title" content="Visual proteomics using whole-lamella 2D template matching" />
  <meta name="dc.date" content="2022-04-14" />
  <meta name="citation_publication_date" content="2022-04-14" />
  <meta name="dc.language" content="en-US" />
  <meta name="citation_language" content="en-US" />
  <meta name="dc.relation.ispartof" content="Manubot" />
  <meta name="dc.publisher" content="Manubot" />
  <meta name="citation_journal_title" content="Manubot" />
  <meta name="citation_technical_report_institution" content="Manubot" />
  <meta name="citation_author" content="Johannes Elferich" />
  <meta name="citation_author_institution" content="RNA Therapeutic Institute, UMass Chan Medical School" />
  <meta name="citation_author_institution" content="HHMI" />
  <meta name="citation_author_orcid" content="0000-0002-9911-706X" />
  <meta name="citation_author" content="Nikolaus Grigorieff" />
  <meta name="citation_author_institution" content="RNA Therapeutic Institute, UMass Chan Medical School" />
  <meta name="citation_author_institution" content="HHMI" />
  <meta name="citation_author_orcid" content="0000-0002-1506-909X" />
  <link rel="canonical" href="https://jojoelfe.github.io/deco_lace_template_matching_manuscript/" />
  <meta property="og:url" content="https://jojoelfe.github.io/deco_lace_template_matching_manuscript/" />
  <meta property="twitter:url" content="https://jojoelfe.github.io/deco_lace_template_matching_manuscript/" />
  <meta name="citation_fulltext_html_url" content="https://jojoelfe.github.io/deco_lace_template_matching_manuscript/" />
  <meta name="citation_pdf_url" content="https://jojoelfe.github.io/deco_lace_template_matching_manuscript/manuscript.pdf" />
  <link rel="alternate" type="application/pdf" href="https://jojoelfe.github.io/deco_lace_template_matching_manuscript/manuscript.pdf" />
  <link rel="alternate" type="text/html" href="https://jojoelfe.github.io/deco_lace_template_matching_manuscript/v/38fd04bb92cfffb0ea0e0e112da741a0da4b716a/" />
  <meta name="manubot_html_url_versioned" content="https://jojoelfe.github.io/deco_lace_template_matching_manuscript/v/38fd04bb92cfffb0ea0e0e112da741a0da4b716a/" />
  <meta name="manubot_pdf_url_versioned" content="https://jojoelfe.github.io/deco_lace_template_matching_manuscript/v/38fd04bb92cfffb0ea0e0e112da741a0da4b716a/manuscript.pdf" />
  <meta property="og:type" content="article" />
  <meta property="twitter:card" content="summary_large_image" />
  <link rel="icon" type="image/png" sizes="192x192" href="https://manubot.org/favicon-192x192.png" />
  <link rel="mask-icon" href="https://manubot.org/safari-pinned-tab.svg" color="#ad1457" />
  <meta name="theme-color" content="#ad1457" />
  <!-- end Manubot generated metadata -->
bibliography:
- content/manual-references.json
manubot-output-bibliography: output/references.json
manubot-output-citekeys: output/citations.tsv
manubot-requests-cache-path: ci/cache/requests-cache
manubot-clear-requests-cache: false
...






<small><em>
This manuscript
([permalink](https://jojoelfe.github.io/deco_lace_template_matching_manuscript/v/38fd04bb92cfffb0ea0e0e112da741a0da4b716a/))
was automatically generated
from [jojoelfe/deco_lace_template_matching_manuscript@38fd04b](https://github.com/jojoelfe/deco_lace_template_matching_manuscript/tree/38fd04bb92cfffb0ea0e0e112da741a0da4b716a)
on April 14, 2022.
</em></small>

## Authors



+ **Johannes Elferich**<br>
    ![ORCID icon](images/orcid.svg){.inline_icon width=16 height=16}
    [0000-0002-9911-706X](https://orcid.org/0000-0002-9911-706X)
    · ![GitHub icon](images/github.svg){.inline_icon width=16 height=16}
    [jojoelfe](https://github.com/jojoelfe)<br>
  <small>
     RNA Therapeutic Institute, UMass Chan Medical School; HHMI
  </small>

+ **Nikolaus Grigorieff**<br>
    ![ORCID icon](images/orcid.svg){.inline_icon width=16 height=16}
    [0000-0002-1506-909X](https://orcid.org/0000-0002-1506-909X)
    · ![GitHub icon](images/github.svg){.inline_icon width=16 height=16}
    [nikogrigorieff](https://github.com/nikogrigorieff)<br>
  <small>
     RNA Therapeutic Institute, UMass Chan Medical School; HHMI
  </small>



## Abstract {.page_break_before}



Localization of biomolecules inside a cell is an important goal of biological
imaging. Fluorescence microscopy can localize biomolecules inside whole cells
and tissues, but its ability to count biomolecules and accuracy of the spatial
coordinates is limited by the wavelength of visible light. Cryo-electron
microscopy (cryo-EM) provides highly accurate position and orientation
information of biomolecules but is often confined to small fields of view inside
a cell, limiting biological context. In this study we use a new data-acquisition
scheme called “Defocus-Corrected Large-Area cryo-EM” (DeCo-LACE) to collect
high-resolution cryo-EM data over entire sections (100 – 200 nm thick lamellae)
of neutrophil-like mouse cells, representing roughly 1% of the total cellular
volume. We use 2D template matching (2DTM) to determine localization and orientation
of the large ribosomal subunit in these sections, detect bound small
ribosomal subunits and assign ribosomes to polysomes based on their relative orientations to each other. These data provide "maps" of translational activity across
sections of mammalian cells. This new high-throughput cryo-EM
data collection approach together with 2DTM will advance visual
proteomics and complement other single-cell "omics" techniques, such as
flow-cytometry and single-cell sequencing. 



## Introduction

A major goal in understanding cellular processes is the knowledge of the
amounts, location, interactions, and conformations of biomolecules
inside the cell. This knowledge can be obtained by approaches broadly
divided into label- and label-free techniques. In label-dependent
techniques a probe is physically attached to a molecule of interest that
is able to detected with a high signal-to-noise signal, such as a
fluorescent molecule. In label-free techniques the physical properties
of molecules themselves are used for detection. An example for this is
proteomics using mass-spectrometry [@doi:10.1038/nbt.1592]. The advantage
of label-free techniques is that they can provide information over
thousands of molecules, while label-techniques offer highly specific
information for a few molecules. Especially spatial information can
often only be achieved using label-dependent techniques, such as
fluorescence microscopy [@doi:10.1038/nmeth817]. 

Cryo-electron microscopy has the potential to directly visualize the
arrangement of atoms that compose biomolecules inside of cells, thereby
allowing label-free detection with high spatial accuracy. This has been
called "visual proteomics" [@doi:10.1038/nrm1861]. Since cryo-EM
requires thin samples (\<500nm), imaging of biomolecules inside cells is
restricted to small organisms, thin regions of cells, or samples that
have been suitably thinned. Thinning can be achieved either by
mechanical sectioning [@doi:10.1111/j.1365-2818.1983.tb04225.x] or by
milling using a focused ion beam (FIB) [@doi:10.1016/j.sbi.2013.08.006]. his complex workflow
leads to a low throughput of cryo-EM imaging of cells and is further
limited by the fact that at the required magnifications, typical fields
of view (FOV) are very small compared to mammalian cells, and the FOV
achieved by label-techniques such as fluorescence light microscopy. The
predominant cryo-EM technique for the localization of biomolecules of
defined size and shape inside cells is cryo-electron tomography [@doi:10.1017/S0033583511000102]. However, the requirement of a tilt series at
every imaged location and subsequent image alignment, severely limits
the throughput for molecular localization.

An alternative approach is to identify molecules by their structural
"fingerprint" in single projection using "2D template-matching" (2DTM)
[@doi:10.7554/eLife.25648; @doi:10.1101/2020.04.22.053868;
@doi:10.7554/eLife.68946]. In this
method a 3D model of a biomolecule is used as a template to find 2D
projections that match the molecules visible in the electron
micrographs. This method requires a projection search on a fine angular
grid, and the projections are used to find local cross-correlation peaks
with the micrograph. Since the location of a biomolecule in the
z-direction causes predictable aberrations to the projection image, this
method can be used to calculate complete 3D coordinates and orientations
of a biomolecule in a cellular sample
[@doi:10.1101/2020.04.22.053868]

Hematopoiesis is the process of generating the various cell types of the blood in
the bone marrow. Disregulation of the process results in diseases like leukemia.
Understanding how hematopoietic stem and progenitor cells are programmed to
diffferentiate to the appropriate cell type would be provide new insight how
hematopoiesis can be misregulated. Of special interest is the regulation of
translation during hematopoiesis. This is exemplified by the observation that
genetic defects in the ribosome machinery often leads to hematopoietic
disease[@doi:10.1093/nar/gkz637]. As such direct quantification of ribosome
location, number and conformational states could lead to new insight into
hematopoietic disease [@doi:10.1186/s12885-018-4178-z]. 

Here we apply 2D-template matching of ribosomes to cryo-FIB milled
neutrophil-like murine cells [@doi:10.1016/j.cell.2016.08.057]. To increase the
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

ER-HoxA9 cells were maintained in RPMI medium supplemented with 10% FBS,
penicillin/streptomycin, SCF, and estrogen [@doi:10.1016/j.cell.2016.08.057] at
37C and 5% CO2. 120h prior to grid preparation, cells were washed twice in PBS
and cultured in the same medium except without estrogen. Differentiation was
verified by staining with Hoechst-dye and inspection of nuclear morphology.
Cells were then counted and diluted to $1\cdot10^6$ cells/ml. Grids ( either 200 mesh
copper grids, with a sillicone-oxide and 2um holes with a 2um spacing or 200
mesh gold grids with a thin gold film and 2 um holes in 2um spacing) were
glow-discharged from both sides using a 15 mA for 45s . 3.5 ul of cell
suspension was added to grids on the thin-film side and grids were automatically
blotted from the back side using a GP2 cryoplunger (Leica) for 8 s and rapidly
plunged into liquid ethane at -185°C. 

### FIB-milling

Grids were loaded into a Acquilos 2 FIB/SEM  microscope with a stage cooled to
-190°C. Grids were sputter-coated with platinum for 15s at 45 mA and then coated
with a layer of platinum-precursor by opening the GIS-valve for 45s. An overview
of the grid was created by montaging SEM images and isolated cells at the center
of gridsquares were selected for FB-milling. Lamella were generated
automatically using the AutoTEM software, with the following parameters:

- Milling angle: 20°
- Rough milling: 3.2 µm thickness, 0.5nA current
- Medium milling: 1.8 µm thickness, 0.3nA current, 1.0° overtilt
- Fine milling: 1.0 µm tchickness, 0.1nA current, 0.5° overtilt
- Finer milling: 700 nm thickness, 0.1nA curent, 0.2° overtilt
- Polish 1: 450nm thickness, 50 pA current
- Polish 2: 200nm thickness, 30 pA current

This resulted in 6-8 um wide lamella with
150-250nm thickness as determined by FIB-imaging of the lamella edge.

### Data collection

Grids were loaded into a Krios Titan TEM (Thermore Fisher) operated at 300 keV
and equipped with a BioQuantum energy filter (Gatan) and K3 camera (Gatan). The
microscope was aligned using a cross-grating grid on the stage. Prior to each
session we carefully performed the Image/Beam calibration in nanoprobe. Then we
set the magnification to a pixel size of 1.76Å and condensed the beam to ~
900nm diameter, resulting in the beam being completely visible on the camera.
To establish fringe-free conditions, the "Fine eucentric" procedure of serialEM
was used to move a square of the cross-grating grid to the eucentric position of
the microscope. The effective defocus was then set to 2 um, using the
"autofocus" routine of serialEM. The objective focus of the microscope was
changed until no fringes were visible. The stage was then moved in Z until
images had a apparent defocus of 2 um. The difference in stage Z-position
between the eucentric and fringe-free conditions was then used to move other
areas into fringe-free condition.

Low magnification montages were used to find lamella and lamella that were
sufficiently thin and free of contamination were selected for automated data
collection. Vverview images of each lamella were taken at 2250x magnification
(39Å pixel-sixe). The corners of the lamella in the overview image were manually
annotated in SerialEM and translated into Beam-Imageshift values using SerialEM
calibration. A hexagonal pattern of Beam-Imageshift positions was calculated
that covered the area between the four corners in a serpentine way, with a
sqrt(3) * 400 nm horizontal spacing and 800 nm vertical spacing. Exposures were
then taken at each position with a 30 e/Å2 total dose. After each exposure that
defocus was estimated using the ctffind function of SerialEM and the focus for
the next exposure was corrected by the difference between the estimated focus
and the desired defocus of 800 nm. Furthermore, after each exposure the
deviation of the beam from the center of the camera was measured and corrected
using the "CenterBeamFromImage" command of SerialEM.

After datacollection a 20s exposure at 2250x magnification of the lamella at
200um defocus was taken for visualization purposes. A python script implementing
this procedure is available at [Link to repo].

### Data pre-processing

To avoid influence of the beam-edge on motion-correction only a quarter
of the movie in the center of the camera was considered for calculation of the
estimated motion. After movie frames were aligned and summed a mask for the
illuminated area was calculated by lowpass filtering the image at 100Å,
thresholding the image at 10% of the maximal value and then lowpass filtering
the mask at 100Å. This mask was then used to replace un-illuminated area with
gaussian noise, with the same mean and standard deviation as the illuminated
area. A custom version of the unblur program implementing this procedure is
available at (TODO). 
The contrast-transfer function (CTF) was estimated using ctffind, searching
between 0.02 and 2 um defocus. 

### 2DTM

The search template was generated from the cryo-EM structure of the mouse large
ribosomal subunit (PDB 6SWA) using the simulate program in cisTEM [cite]. The
atomic coordinates corresponding to Epb1 were deleted from the model and the
simulate program of the cisTEM suite was used to calculate an density map from
the atomic coordinates. The match_template program was used to search for this
template in the preprocessed images, using 1.5° angular step in out-of-plane
angles and 1.0° in-plane. 11 defocus planes in 20nm steps centered around
the defocus estimates by ctffind were searched. Matches were defined as peaks
above a threshold of 7.75, which was chosen based on a one false positive per
tile criterium [cite].

### DeCo-LACE data processing

An overview of the data analysis pipeline is shown in Fig.
{@fig:deco_lace_workflow}. Initial coordinates of each Tile $i$, $\textbf{c}_{init,i}$ were derived
from the Beam-Image-Shift of the tile $BIS_i$ and the ISToCamera matrix
$\mathbf{IC}$: 

$$\textbf{c}_{init,i} = \mathbf{IC} \cdot BIS_i$$

To refine the montage a list of overlapping tile pairs
$|\textbf{c}_i-\textbf{c}_j| < 900\textrm{nm}$ were compiled and the offsets
$\textbf{o}_{i,j} = \textbf{c}_i-\textbf{c}_j$ were refined by using a masked
cross-correlation of the overlap region as implemented in the scikit-image
package [cite]. Refined coordinates were then derived by minimizing the
least-deviation of the new offsets and tile positions:

$$ min\sum_{pairs}{(\textbf{o}_{refined,i,j} - (\textbf{c}_i-\textbf{c}_j))^2}$$

using the scipy package [cite]. This refinement was then repeated once more. 

The x,y coordinates of 2DTM match $n$ in the tile $i$, $\textbf{m}^\textrm{T}_{n,i}$, was
transformed into the montage frame by adding the coordinate of the tile.

$$ \textbf{m}^\textrm{M}_n = \textbf{m}^\textrm{T}_{n,i} +
\textbf{c}_i$$

The z coordinate of each match was calculated as the sum of the defocus offset
for each match, the estimated defocus of the tile, and the nominal defocus of
the microscope when the tile was acquired. The python scripts used are available
under [repolink].



## Results

### 2DTM detects large ribosomal subunits in cryo-FIB lamella of mammalian cells

To test whether we could detect individual ribosomes in mammalian cells we
prepared cryo-lamella of mouse neutrophil-like cells. Low-magnification images
of these lamellas clearly shows cellular features consistent with a
neutrophil-like phenotype, mainly a segmented nucleus and a plethora of
membrane-organelles, corresponding to the granules and secretory vesicles of
neutrophils (Fig. {@fig:initmatching}A). We then proceeded to acquire
micrographs on this lamella with a defocus of 0.5-1.0 um, 30 e/Å2/s exposure and
1.5 Å pixelsize. We manually selected multiple locations in the lamella and
acquired micrographs using standard low-dose techniques where focusing is performed on a
sacrificial area. The resulting micrographs showed no signs of crystalline ice
and smooth bilayered membranes (Fig. {@fig:initmatching}C,D), indicating successful vitrification. 

We used an atomic model of the 60S mouse ribosomal subunit  (6SWA) for 2DTM. In a subset of images the distribution of cross-correlation
scores significantly exceeded the distribution expected from non-signifcant
matching. In the resulting scaled maximum-intensity maps, clear peaks with SNR
thresholds up to 10 were apparent (Fig. {@fig:initmatching2}A). By using the
criterion described by for thresholding potential matches we found that in
images of cytosolic compartments we found evidence of 10-500 ribosomes in the
imaged areas (Fig. {@fig:initmatching}B-E). Notably, we found no matches in images ares corresponding to the
nucleus(Fig. {@fig:initmatching}B) or mitochondria (Fig. {@fig:initmatching}D). In the cytosolic areas we found a drastically different
number of matches, In some areas we found only ~ 50 matches per image area (Fig. {@fig:initmatching}E), while
 in another area we found more than 500 matches (Fig. {@fig:initmatching}C). This ten-fold difference in
local ribosome concentration , but we realized that current data acquistion
protocols are limited in that only a small area of the lamella is actually
imaged and, due to the manual selection of acquision positions based on the
overview image, might be biased towards cellular region that appear appealing to
the experimentalist. We therefore set out to collect cryo-EM data for 2DTM from
mammalian lamella in a high-throughput unbiased fashion.

### DECO-LACE for 2D imaging of whole lamella

In order to obtain high-resolution data for complete lamella we used a new
approach for data collection. This approach uses three key strategies: (1)
ensures that every electron that exposes the sample is collected on the camera
(2) uses beam-image shift to precisely and quickly raster the surface of the
lamella and (3) uses a focusing strategy that does not rely on a sacrificial
area (Fig. {@fig:approach}A).

To ensure that every electron exposing the sample was captured by the detector,
we focused the electron beam so that the entire beam was placed on the detector.
During canonical low-dose imaging the microscope is configured so that the focal
plan is identical to the eucentric plane of the specimen stage. This leaves the
C2 aperture out of focus, resulting in ripples at the edge of the beam (Fig. {@fig:approach}D). While these ripples are low-resolution features that might not interfere
with 2D template matching, which is designed to be robust to low-resolution
noise, we also tested collecting data under a condition where the C2 aperture is
in focus (Fig. {@fig:approach}E). 

We then centered a lamella under the electron beam and used beam-image shift of
the microscope to systematically raster the whole surface of the lamella in a
hexagonal pattern(Fig. {@fig:approach}A,C). Instead of focusing in a sacrificial area, we determined the
defocus after every exposure by fitting the Thon rings. The focus was then adjusted based on the difference between
desired and measured defocus (Fig. {@fig:approach}B). Since we used a serpentine pattern for data
collection every exposure is close to the previous exposure making drastic
changes in the defocus unlikely. Furthermore we started our acquisition pattern
on the platinum deposition edge, so the initial exposure where the defocus was
not yet adjusted did not contain any biologically relevant information. 

We used this strategy to collect data on 8 lamella, 4 using the eucentric focus
condition, from hereon referred to as Lamella~EUC~, and 4 using the fringe-free
condition, from hereon referred to as Lamella~FFF~(Fig. {@fig:lamella_images}).
We were able to highly consistently collect data with a defocus of 800nm (Fig.
{@fig:approach}F), both in the eucentric focus and fringe-free focus condition.
To ensure that data was collected consistently, we mapped defocus values as a
function of the applied Beam-image shift (Fig. {@fig:lamella_spatial_info}A).
This demonstrated that the defocus was consistent over the lamella, with
outliers only at isolated images and in images containing contamination. We also
plotted the measure objective astigmatism of the lamella and found that it
varies with the applied Beam-image shift, become more astigmatic mostly due to
beam-image shift in the X direction(Fig. {@fig:lamella_spatial_info}B). While
approaches exist to correct this during the data-collection [cite], we opted to not use
these approaches in our initial experiments. We reasoned that because 2DTM depends on high-resolution information, this would be an excellent test of how much these aberration affect imaging.

We assembled the tile micrographs into a montage using the Beam-Image-shift value and the SerialEM calibration followed by cross-correlation based refinement (see Methods). In the resulting montages the same cellular features than in the overview images are apparent (Fig. {@fig:lamella_spatial_info}G-J), however due to the high magnification and low defocus many more details, such as the membrane bilayer seperation can be observed. For montages collected using the eucentric there are clearly visible fringes at the edges between the tiles, which are absent in the fringe-free focus montage. However, it is unclear whether these fringes impede molecular detection or due to their low-resolution nature are only an aesthetic issue. We also note that the tiling pattern is visible in the montages, which we believe is due to the non-linear behaviour of the K3 camera (see Dicussion).

While inspecting the montages we noticed that the membrane vesicles and granules are highly variable in size and electron density of their content. We found furthermore that a substantial number of granules with a high electron density seemed to contain a membrane-enclosed inclusion with electron-density similar to the surrounding cytosol (Fig. [TODO]). [Describe measurements]

### 2DTM of DeCo-LACE data reveals ribosome distribution in cellular cross-sections

In initial attempts of using 2DTM on micrographs acquired with the DeCo-LACE
protocol, we did not observe any SNR peaks above threshold using the large
subunit of the mouse ribosome (Fig. {@fig:crop_unblur}A). We reasoned that the
edges of the beam might interfere with motion-correction of the movie as they
would remain stationary or move differently than the sample. Indeed when we
cropped movie to exclude the beam edges we found that the estimated motion was
larger than estimated on the uncropped movie (Fig. {@fig:crop_unblur}B).
Furthermore, in the motion-corrected average we could identify SNR peaks above
detection threshold (Fig. {@fig:crop_unblur}B), indicating that 2DTM is very
sensitive to accurate motion correction and that the beam edge did interfere
with motion-correction. In order to avoid having to crop the movies we
implemented a function in unblur to consider only the cropped area for
estimation of shifts, but average the complete movie (Fig. {@fig:crop_unblur}B).
Using this approach we motion-corrected all tiles in the 8 lamella and found
consistently total motion below 1Å per frame (Fig.
{@fig:lamella_motion_thickness} A). In some lamella we found increased motion in
the center of the lamella, which indicates that mechanical stability of
FIB-milled lamella might not be homogeneous over the lamella surface. In some
micrographs we also observed that the beam edges gave rise to artifacts in the
cross-correlation mip and numerous false-positive matches at the edge of the
illuminated area (Fig. TODO). A similar phenomenon was observed on isolated
"hot" pixels in the unilluminated area. To overcome this issue we implemented a
function in unblur to replace unillluminated areas in the micrograph with
gaussian noise, with mean and standard deviation matched to the illuminated
portion of the micrograph (Fig. TODO). Together, these special pre-processing
steps enabled us to perform 2DTM on all tiles of the 8 lamellae.

We then used the refined tile positions to calculate the positions of the
matched LSUs in the lamellae (Fig. {@fig:matching_euc} A, Fig.
{@fig:matching_fff} A). Overlaying these positions of the lamella montages
reveal ribsome distribution throughout the FIB-milled slice of individual cells.
Organelles like the nucleus and mitochondria only showed sporadic matches with
low SNRs, consistent with the estimated false-positive rate on one per tile.
During the assembly we calculated the Z positions from the indivdual estimated
defocus levels and the focus plane of the microscope during acquisition of each
tile. When viewed from the side the ribosome position therefore show the slope
of the lamella in the microscope frame (Fig. {@fig:matching_euc} B, Fig.
{@fig:matching_fff} B). Furthermore, the side-views indicated that lamellae were
thinner at the leading edge. Indeed, when we plotted the electron intensities in
individual tiles as a function of Beam-Image shift we observed substantially
higher intensities at the leading edge, which in energy-filtered TEM indicates a
thinner sample [cite]. Even though we prepared the lamellae with the "overtile"
approach [cite], this means that ribosome densities across the lamellae can be
schewed by the changes in thickness and better sample preparation methods are
needed to generate more even samples. 

Close inspection of the ribosome positions in the lamellae revealed multi
interesting features. Ribosomes could be seen associating with the membrane, in
patterns reminiscent of the rough endoplasmic reticulum (Fig.
{@fig:matching_euc} C, Fig. {@fig:matching_fff} C) or the outer nuclear membrane
(Fig. {@fig:matching_euc} D). We also observed ribosomes forming ring-like
structures (Fig. {@fig:matching_euc} E), potentially indicating circularized
mRNAs [cite]. While ribosomes were for the most part excluded from the numerous
granules observed in the cytoplasm, in some circumstances we observed clusters
of ribosomes in the lower electron density inclusion in the class of
double-membraned granules described earlier (Fig. {@fig:matching_euc} F, Fig.
{@fig:matching_fff} D,E). It is, in principle, possible that these matches are
situated above or below the imaged granule, since the granules position in Z
cannot be determined using a 2D projection. However, in the case of Fig.
{@fig:matching_fff} E, the matched ribosomes span the whole lamella  in the Z
direction, while a position above or below the granule would result in ribosome
situated exlusively at the top or bottom of the lamella. This conclusive
evidence of ribosomes in the inclusion is consistent with the earlier hypothesis
that the inclusion is of cytoplasmic origin.

Between the 8 lamellae we found different number of matches (Fig.
{@fig:matching_stat} A). Lamella~EUC~ 1 resulted in the most matches, but also has the largest surface area and contained
cytoplasm of two cells. Lamella~FFF~ 4 had the fewest matches, but this particular slice was dominated by a circular
nucleus slice, with only small pockets of cytoplasm (Fig.
{@fig:lamella_images}). In an attempt to normalize for these differences in
lamella surface area we compared the number of matches per tile in tiles which
contained more than one match, which should exclude tiles with non-cytosolic
content (Fig. {@fig:matching_stat} B). While this measure had less variablity,
there were still differences. Lamella~EUC~ 4 had not only the fewest
matches, but also the lowest density, which could be due to the thickness of the
lamella or due to a slice through low-ribosome content region. Lamella~FFF~
3 had substantially higher number of ribosomes per tile. Since all
of these lamella were milled into identical cells under identical conditions,
this underscores the necessity to collect data on large numbers of lamella in
order to overcome inherent variability. When comparing the distribution of
scores between the lamella we found them to be fairly comparable with a median
of .... Lamella~EUC~ 1 had slightly lower scores compared to others,
potentially due to the large size and connected mechanical instabillity during
imaging. Overall we did not observe a  difference in number or SNR of matches between eucentric or fringe-free focus illumination that was bigger that inter-lamella variability. 

Since the SNR values of 2DTM are highly sensitive to image quality we reasoned we could use them to verify that DeCo-LACE does not introduce systematic errors. We first wondered whether the unusually condensed beam would be prone to non-parallel illumination or whether at the outside of the beam unknown aberration would distort the image. We reasoned that this would lead to lower SNR values at the inside edge of the illuminated area. When we plotted SNR values in all 8 lamellae as a function of there location in tiles we found high SNR value up to the edge of the illuminated area for both eucentric and fringe-free focus illumination, again demonstrating that both illumination schemed are suitable for DeCo-LACE.

We also wondered whether high Beam-Image shift values would lead aberration due to the astigmatism or beam tilt [cite]. [TODO plot scores vs BIS, euc vs fff]

### Computation is the bottleneck of visual proteomics

As described above the variability of lamella, both in terms of technique such as area, thickness and mechanical stability, and of biology, such as selection of cell and location of the slice in relation to the complete cell, could be overcome by collecting orders of magnitude more data. This will be essential to allow robust statistical comparisons of macromolecule number and location between different experimental conditions. 



## Discussion



- Elizabeth Wright and Grant Jensen Montage tomography papers

- Waffle method for higher throughput, automation of fib-milling

- Throughput and bottlenecks

- lamella mechanical properties, radiation damage, other ways to to thin?

- eucentric vs fringe free illumination

- Visual proteomics

- Granules containing ribosomes?

- Threshold implications (no matches on most images)

- K3 not linear

## Figures

![2D template matching of the large subunit of the ribosome in fib-milled neutrophil-like cells 
(A) Overview image of the lamella. Major cellular regions are labeled, as Nucleus (Nuc), Mitochondria (M), and granular cytoplasm (GrCyt). FOVs where high-magnification images for template matching where acquired are indicated as boxes with the number of matches indicated on the bottom right. FOVs displayed in Panels B-E are color-coded.
(B-E) FOVs with projection of ribosome LSU matches shown in green. (B) Perinuclear region, the only matches are in the cytoplasmic half. (C) Cytoplasmic region with high density of ribosomes (D) Mitochondrium, as expected there are only matches in the cytoplasmic region (E) Cytoplasm, with low density of ribosomes. 
](tikz:initmatching){#fig:initmatching}

```{.tikz-figure #initmatching width=19cm height=10cm draft=false}
\node (anchor) at (0.5,9.35) {}; 
\node[labelNode] {A};
\node[graphicNode] {\includegraphics[height=9cm]{content/images/the_lamella.png}};

\node[annotNode] at (3.5,8.35) {\contour{white}{Nuc}};
\node[annotNode] at (1.75,4.0) {\contour{white}{Nuc}};

\node[annotNode] at (3.2,4.7) {\contour{white}{M}};
\node[annotNode] at (2.75,2.25) {\contour{white}{M}};

\node[annotNode] at (1.5,8.0) {\contour{white}{GrCyt}};
\node[annotNode] at (4.5,3.5) {\contour{white}{GrCyt}};


\node (rect) at (1.1,7.5) [anchor=center,draw,thick,minimum width=0.85cm,minimum height=0.6cm,color=blue!60] {};
\node[mnNode, color=blue!60] {\contour{white}{2}};

\node (rect) at (3.2,7.3) [anchor=center,draw,thick,minimum width=0.85cm,minimum height=0.6cm,color=blue!60] {};
\node[mnNode, color=blue!60] {\contour{white}{0}};

\node (rect) at (4.5,6.25) [anchor=center,draw,thick,minimum width=0.85cm,minimum height=0.6cm,color=red] {};
\node[mnNode, color=red] {\contour{white}{506}};

\node (rect) at (3.4,5.5) [anchor=center,draw,thick,minimum width=0.85cm,minimum height=0.6cm,color=blue!60] {};
\node[mnNode, color=blue!60] {\contour{white}{16}};

\node (rect) at (2.75,3.5) [anchor=center,draw,thick,minimum width=0.85cm,minimum height=0.6cm,color=green] {};
\node[mnNode, color=green] {\contour{white}{30}};

\node (rect) at (2.65,2.35) [anchor=center,draw,thick,minimum width=0.85cm,minimum height=0.6cm,color=orange] {};
\node[mnNode, color=orange] {\contour{white}{17}};

\node (rect) at (1.25,1.5) [anchor=center,draw,thick,minimum width=0.85cm,minimum height=0.6cm,color=blue!60] {};
\node[mnNode, color=blue!60] {\contour{white}{8}};

\node (rect) at (4.0,2.2) [anchor=center,draw,thick,minimum width=0.85cm,minimum height=0.6cm,color=magenta] {};
\node[mnNode, color=magenta] {\contour{white}{52}};


\node (anchor) at (6.5,9.35) {}; 
\node[labelNode] {B};
\node (img) [graphicNode]  {\includegraphics[height=4cm]{content/images/30_matches.png}};
\node (n3) [box=green, fit=(img)] {};

\node (anchor) at (12.75,9.35) {}; 
\node[labelNode] {C};
\node (img) [graphicNode]  {\includegraphics[height=4cm]{content/images/506_matches.png}};
\node (n3) [box=red, fit=(img)] {};

\node (anchor) at (6.5,4.75) {}; 
\node[labelNode] {D};
\node (img) [graphicNode]  {\includegraphics[height=4cm]{content/images/17_matches.png}};
\node (n3) [box=orange, fit=(img)] {};

\node (anchor) at (12.75,4.75) {}; 
\node[labelNode] {E};
\node (img) [graphicNode]  {\includegraphics[height=4cm]{content/images/52_matches.png}};
\node (n3) [box=magenta, fit=(img)] {};

%%\iftoggle{draft}{\node [redAnchorNode] {};};

```

![2D template matching of the large subunit of the ribosome in fib-milled
neutrophil-like cells (A) Maximum intensity projection cross-correlation map of
micrograph shown in Figure
{@fig:initmatching} (B+C) 3D plot of MIP regions indicated by color boxes in Panel A](tikz:initmatching2){#fig:initmatching2 tag="S1"}

```{.tikz-figure #initmatching2 width=13cm height=9cm draft=false}
\node (anchor) at (0.5,8.35) {}; 
\node[labelNode] {A};
\node[graphicNode] {\includegraphics[width=12cm]{content/code/img/initial_map_match.pdf}};
\iftoggle{draft}{\node [redAnchorNode] {};};

```





![DeCo-LACE approach (A) Graphic demonstrating the data-collection strategy for
DeCo-LACE. The electron beam is condensed to a diameter $D_{Beam}$ that allows captured of
the whole illuminated area on the camera. Beam-image shift along X and Y
($BIS_X$,$$BIS_Y$) is used to raster the whole lamella
(B) Diagram of the collection algorithm
(C) Example overview image of a lamella with the designated acquisition
positions and the used beam diameter indicated with red circles
(D+E) Representative micrographs takne with a condensed beam at eucentric focus
(D) or fringe-free focus (E)
(F) Boxplot of defocus measured by ctffind of micrographs taken by the DeCo-Lace
approach on 4 lamella images at eucentric focus and 4 lamella imaged with
fringe-free focus.
(F+G) Lamella overview images of lamella imaged at eucentric focus (F) Overview
image taken at low magnification (40Å pixel size) (G) Overview created by
montaging high magnification images taken with the DeCo-Lace approach (1.5Å
pixelsize)
(H+I) Lamella overview images of lamella imaged at fringe-free focus (H) Overview
image taken at low magnification (40Å pixel size) (I) Overview created by
montaging high magnification images taken with the DeCo-Lace approach (1.5Å
pixelsize) ](tikz:approach){#fig:approach}

```{.tikz-figure #approach width=20cm height=20cm draft=false}
\node (anchor) at (0.5,19.35) {}; 
\node[labelNode] {A};
\node[graphicNode] {\includegraphics[width=5cm]{content/graphics/approach/approach.png}};
\draw [densely dotted, red,thick] (3,19.5) -- (3,15.0);
\draw [densely dotted, red,thick] (3,14.2) -- (3,11.4);

\tikzset{dimen/.style={<->,>=latex,thin,every rectangle node/.style={above right=0.2cm and -0.3cm,fill=white,midway,font=\sffamily}}}

\draw (3.55,15.4) -- ++(0,1.5) coordinate (D1) -- +(0,5pt);
\draw (4.15,15.4) -- ++(0,1.5) coordinate (D2) -- +(0,5pt);
\draw [dimen] (D1) -- (D2) node {$D_{Beam}$};

\draw [->, very thick] (3,15) -- ++(0.5,-0.2)  coordinate (S1) node[midway,below left] {$IS_X$} ;
\draw [->, very thick] (S1) -- (3.85,15.4) node[midway,below right] {$IS_Y$};



\node (anchor) at (6.0,19.35) {}; 
\node[labelNode] {B};

% Place nodes
\node [block] (init) at (8.0,18.35) {\textbf{START} \\ Collect overview image};
\node [block, below = 0.3cm of init.south] (identify) {Setup hexagonal grid covering lamella area};
\node [block, below = 0.3cm of identify.south] (mutate) {Beam-imageshift to tile n=i};
\node [block, below = 0.3cm of mutate.south] (transfer) {Capture exposure and determine defocus by CTF fitting};
\node [block, below = 0.3cm of transfer.south] (evaluate) {Adjust defocus by difference between expected and measured value};

% Draw edges
\path [line] (init) -- (identify);
\path [line] (identify) -- (mutate);
\path [line] (mutate) -- (transfer);
\path [line] (transfer) -- (evaluate);
\path [line] (evaluate) -|  ([xshift=0.5cm, yshift=0cm]transfer.east) |- (mutate);

\node (anchor) at (11.5,19.35) {}; 
\node[labelNode] {C};
\node[graphicNode] {\includegraphics[width=8cm]{content/images/ac_strategy.png}};
\iftoggle{draft}{\node [redAnchorNode] {};};


\node (anchor) at (0.5,9.5) {}; 
\node[labelNode] {D};
\node[graphicNode] (euc) {\includegraphics[height=4.0cm]{content/images/fringebeam.png}};
\node[above = 0cm and 0cm of euc.north] {Eucentric Focus};

\iftoggle{draft}{\node [redAnchorNode] {};};


\node (anchor) at (5.5,9.5) {}; 
\node[labelNode] {E};
\node[graphicNode] (fff) {\includegraphics[height=4.0cm]{content/images/nofringebeam.png}};
\node[above = 0cm and 0cm of fff.north] {Fringe-free Focus};
\iftoggle{draft}{\node [redAnchorNode] {};};

\node (anchor) at (10.5,9.5) {}; 
\node[labelNode] {F};
\node[anchor=north west, below right=-0.5cm and 0cm of anchor] {\includegraphics[height=4.8cm]{content/code/img/defocusplot.pdf}};
\iftoggle{draft}{\node [redAnchorNode] {};};



\node (anchor) at (0.5,4.5) {}; 
\node[labelNode] {G};
\node[graphicNode] {\includegraphics[height=4.5cm]{content/images/euc_lamella1_view_morph.png}};

\node (anchor) at (5,4.5) {}; 
\node[labelNode] {H};
\node[graphicNode] {\includegraphics[height=4.5cm]{content/images/euc_lamella1_1000px.png}};

\node (anchor) at (9.5,4.5) {}; 
\node[labelNode] {I};
\node[graphicNode] {\includegraphics[height=4.5cm]{content/images/fff_lamella4_view_morphed.png}};

\node (anchor) at (14,4.5) {}; 
\node[labelNode] {J};
\node[graphicNode] {\includegraphics[height=4.5cm]{content/images/fff_lamella4_1000px.png}};

```




![
Overview images of lamellae imaged using the DeCo-LACE approach taken at low-magnification
](tikz:lamella_images){#fig:lamella_images tag="S2"}

```{.tikz-figure #lamella_images width=20.0cm height=5cm draft=false}
\def\panelheight{4.6cm}

\node (anchor) at (0.5,4.5) {}; 
\node[labelNode] {A};
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/images/slicer000.png}};
\node (anchor) at ([shift={(0.5cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/images/slicer001.png}};
\node (anchor) at ([shift={(0.5cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/images/slicer002.png}};
\node (anchor) at ([shift={(0.5cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/images/slicer003.png}};

\node (anchor) at ([shift={(0.0cm,-0.5cm)}]0.5,0 |- panel.south) {}; 
\node[graphicNode]  (panel) {\includegraphics[height=\panelheight]{content/images/slicer005.png}};
\node (anchor) at ([shift={(0.5cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode]  (panel) {\includegraphics[height=\panelheight]{content/images/slicer006.png}};
\node (anchor) at ([shift={(0.5cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode]  (panel) {\includegraphics[height=\panelheight]{content/images/slicer007.png}};
\node (anchor) at ([shift={(0.5cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode]  (panel) {\includegraphics[height=\panelheight]{content/images/slicer008.png}};

```

![Defocus estimation of individual tiles of DeCo-Lace montages
(A) Defocus values of individual micrographs taken using the DeCo-Lace approach
plotted as a function of the Beam-Image-Shift values. 
(B) Defocus astigmatism of individual micrographs taken using the DeCo-Lace approach
plotted as a function of the Beam-Image-Shift values. ](tikz:lamella_spatial_info){#fig:lamella_spatial_info tag="S3"}

```{.tikz-figure #lamella_spatial_info width=20.0cm height=10cm draft=false}
\def\panelheight{4.6cm}


\node (anchor) at (0.5,9.5) {}; 
\node[labelNode] {A};
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/code/img/defocus_defocus_vs_bs_plot_euc_lamella1.png}};
\node (anchor) at ([shift={(-0.4cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/code/img/defocus_defocus_vs_bs_plot_euc_lamella2.png}};
\node (anchor) at ([shift={(-0.4cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/code/img/defocus_defocus_vs_bs_plot_euc_lamella3.png}};
\node (anchor) at ([shift={(-0.4cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/code/img/defocus_defocus_vs_bs_plot_euc_lamella4.png}};

\node (anchor) at ([shift={(0.0cm,-0.5cm)}]0.5,0 |- panel.south) {}; 
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/code/img/defocus_defocus_vs_bs_plot_fff_lamella1.png}};
\node (anchor) at ([shift={(-0.4cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/code/img/defocus_defocus_vs_bs_plot_fff_lamella2.png}};
\node (anchor) at ([shift={(-0.4cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/code/img/defocus_defocus_vs_bs_plot_fff_lamella3.png}};
\node (anchor) at ([shift={(-0.4cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/code/img/defocus_defocus_vs_bs_plot_fff_lamella4.png}};
\node (anchor) at ([shift={(-0.4cm,4.0cm)}]panel.north east) {}; 
\node[graphicNode] (key) {\includegraphics[height=\panelheight]{content/code/img/defocus_defocus_vs_bs_plot_colorbar.png}};

\node (anchor) at ([shift={(0.0cm,-1.0cm)}]0.5,0 |- panel.south) {}; 
\node[labelNode] {B};
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/code/img/defocus_astigmatism_vs_bs_plot_euc_lamella1.png}};
\node (anchor) at ([shift={(-0.4cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/code/img/defocus_astigmatism_vs_bs_plot_euc_lamella2.png}};
\node (anchor) at ([shift={(-0.4cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/code/img/defocus_astigmatism_vs_bs_plot_euc_lamella3.png}};
\node (anchor) at ([shift={(-0.4cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/code/img/defocus_astigmatism_vs_bs_plot_euc_lamella4.png}};

\node (anchor) at ([shift={(0.0cm,-0.5cm)}]0.5,0 |- panel.south) {}; 
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/code/img/defocus_astigmatism_vs_bs_plot_fff_lamella1.png}};
\node (anchor) at ([shift={(-0.4cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/code/img/defocus_astigmatism_vs_bs_plot_fff_lamella2.png}};
\node (anchor) at ([shift={(-0.4cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/code/img/defocus_astigmatism_vs_bs_plot_fff_lamella3.png}};
\node (anchor) at ([shift={(-0.4cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/code/img/defocus_astigmatism_vs_bs_plot_fff_lamella4.png}};
\node (anchor) at ([shift={(-0.4cm,4.0cm)}]panel.north east) {}; 
\node[graphicNode] (key) {\includegraphics[height=\panelheight]{content/code/img/defocus_astigmatism_vs_bs_plot_colorbar.png}};

```

![Motion correction of movies with condensed beams. 
At the top of each panel is an average of the movie that was motion-corrected
with a red dashed box indicating the region that was used to estimate shifts.
Below is a graph indicating the estimated shifts of the individual frames of the
movie. Below this is the MIP of 2DTM using the large subunit of the mouse ribosome.
(A) Motion correction of the whole movie
(B) Notion correction of a cropped region of the movie that eliminates the beam
edges
(C) Motion correction of the whole movie, using only hte cropped region to
estimate the shifts
](tikz:crop_unblur){#fig:crop_unblur tag="S4"}

```{.tikz-figure #crop_unblur width=20.0cm height=10cm draft=false}
\def\panelheight{4.6cm}

\node (anchor) at (0.5,9.5) {}; 
\node[labelNode] {A};
\node[graphicNode] (panel) {\includegraphics[width=5cm]{content/images/crop_unblur_initial.png}};
\node (box1) [box=red, fit=(panel), dashed] {};

\node (anchor) at ([shift={(0.0,-0.5cm)}]panel.south west) {}; 
\node[graphicNode] (panel) {\includegraphics[width=5cm]{content/code/img/crop_unblur_motiontrace_initial.png}};

\node (anchor) at ([shift={(0.0,-0.5cm)}]panel.south west) {}; 
\node[graphicNode] (panel) {\includegraphics[width=5cm]{content/code/img/crop_unblur_mip_initial_alignment.png}};



\node (anchor) at ([shift={(1.5,0.0cm)}]0.5,9.5 -| panel.north east) {}; 
\node[labelNode] {B};
\node[graphicNode] (panel) {\includegraphics[width=5cm]{content/images/crop_unblur_cropped.png}};
\node (box2) [box=red, fit=(panel), dashed] {};

\node (anchor) at ([shift={(0.0,-0.5cm)}]panel.south west) {}; 
\node[graphicNode] (panel) {\includegraphics[width=5cm]{content/code/img/crop_unblur_motiontrace_cropped.png}};

\node (anchor) at ([shift={(0.0,-0.5cm)}]panel.south west) {}; 
\node[graphicNode] (panel) {\includegraphics[width=5cm]{content/code/img/crop_unblur_mip_cropped_alignment.png}};

\node (anchor) at ([shift={(1.5,0.0cm)}]0.5,9.5 -| panel.north east) {}; 
\node[labelNode] {C};
\node[graphicNode] (panel) {\includegraphics[width=5cm]{content/images/crop_unblur_initial.png}};
\draw[red, dashed, line width=0.8mm] ([shift={(-0.7,-1.2cm)}]panel.north east) -- 
                                     ([shift={(0.7,-1.2cm)}]panel.north west) --
                                     ([shift={(0.7,1.2cm)}]panel.south west) --
                                     ([shift={(-0.7,1.2cm)}]panel.south east) --
                                     ([shift={(-0.7,-1.2cm)}]panel.north east);

\node (anchor) at ([shift={(0.0,-0.5cm)}]panel.south west) {}; 
\node[graphicNode] (panel) {\includegraphics[width=5cm]{content/code/img/crop_unblur_motiontrace_final.png}};

\node (anchor) at ([shift={(0.0,-0.5cm)}]panel.south west) {}; 
\node[graphicNode] (panel) {\includegraphics[width=5cm]{content/code/img/crop_unblur_mip_final_alignment.png}};


```

![Motion correction of individual tiles imaged using the DeCo-LACE approach
(A) Total estimated motion of individual micrographs taken using the DeCo-Lace approach
plotted as a function of the Beam-Image-Shift values. 
(B) Electron intensity of individual micrographs taken using the DeCo-Lace approach
plotted as a function of the Beam-Image-Shift values. ](tikz:lamella_motion_thickness){#fig:lamella_motion_thickness tag="S5"}

```{.tikz-figure #lamella_motion_thickness width=20.0cm height=10cm draft=false}
\def\panelheight{4.6cm}


\node (anchor) at (0.5,9.5) {}; 
\node[labelNode] {A};
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/code/img/movement_vs_bs_plot_euc_lamella1.png}};
\node (anchor) at ([shift={(-0.4,0.0cm)}]panel.north east) {}; 
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/code/img/movement_vs_bs_plot_euc_lamella2.png}};
\node (anchor) at ([shift={(-0.4,0.0cm)}]panel.north east) {}; 
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/code/img/movement_vs_bs_plot_euc_lamella3.png}};
\node (anchor) at ([shift={(-0.4,0.0cm)}]panel.north east) {}; 
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/code/img/movement_vs_bs_plot_euc_lamella4.png}};

\node (anchor) at ([shift={(0.0cm,-0.5cm)}]0.5,0 |- panel.south) {}; 
\node[graphicNode]  (panel) {\includegraphics[height=\panelheight]{content/code/img/movement_vs_bs_plot_fff_lamella1.png}};
\node (anchor) at ([shift={(-0.4,0.0cm)}]panel.north east) {}; 
\node[graphicNode]  (panel) {\includegraphics[height=\panelheight]{content/code/img/movement_vs_bs_plot_fff_lamella2.png}};
\node (anchor) at ([shift={(-0.4,0.0cm)}]panel.north east) {};
\node[graphicNode]  (panel) {\includegraphics[height=\panelheight]{content/code/img/movement_vs_bs_plot_fff_lamella3.png}};
\node (anchor) at ([shift={(-0.4,0.0cm)}]panel.north east) {}; 
\node[graphicNode]  (panel) {\includegraphics[height=\panelheight]{content/code/img/movement_vs_bs_plot_fff_lamella4.png}};
\node (anchor) at ([shift={(-1.0cm,4.0cm)}]panel.north east) {}; 
\node[graphicNode] (key) {\includegraphics[height=\panelheight]{content/code/img/movement_vs_bs_plot_colorbar.png}};

\node (anchor) at ([shift={(0.0cm,-1.0cm)}]0.5,0 |- panel.south) {}; 
\node[labelNode] {B};
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/code/img/thickness_by_intensity_vs_bs_plot_euc_lamella1.png}};
\node (anchor) at ([shift={(-0.4cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/code/img/thickness_by_intensity_vs_bs_plot_euc_lamella2.png}};
\node (anchor) at ([shift={(-0.4cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/code/img/thickness_by_intensity_vs_bs_plot_euc_lamella3.png}};
\node (anchor) at ([shift={(-0.4cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/code/img/thickness_by_intensity_vs_bs_plot_euc_lamella4.png}};

\node (anchor) at ([shift={(0.0cm,-0.5cm)}]0.5,0 |- panel.south) {}; 
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/code/img/thickness_by_intensity_vs_bs_plot_fff_lamella1.png}};
\node (anchor) at ([shift={(-0.4cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/code/img/thickness_by_intensity_vs_bs_plot_fff_lamella2.png}};
\node (anchor) at ([shift={(-0.4cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/code/img/thickness_by_intensity_vs_bs_plot_fff_lamella3.png}};
\node (anchor) at ([shift={(-0.4cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/code/img/thickness_by_intensity_vs_bs_plot_fff_lamella4.png}};
\node (anchor) at ([shift={(-1.0cm,4.0cm)}]panel.north east) {}; 
\node[graphicNode] (key) {\includegraphics[height=\panelheight]{content/code/img/thickness_by_intensity_vs_bs_plot_colorbar.png}};

```


![Statistics of 2DTM on lamella imaged using DeCo-LACE (A) Number of matches of
each lamella (B) Distribution of matches per tile in each lamella. Only tiles
with two or more matches were included (C) Distribution of SNRs in each lamella
(D) For each lamella an average of all tiles is shown. Overlaid is a scatterplot
of all matches in these tiles according to their in-tile coordinates.
Scatterplot is color according to the SNR. There are no matches in the top
circle-circle intersection due to radiation damage from previous exposures.](tikz:matching_stat){#fig:matching_stat}

```{.tikz-figure #matching_stat width=15cm height=3cm draft=false}


\node (anchor) at (0.5,2.5) {}; 
\node[labelNode] {A};
\node[graphicNode] (panel) {\includegraphics[width=4.5cm]{content/code/img/num_matches_plot.png}};
\node (anchor) at ([shift={(0.5cm,0.0)}]panel.north east) {}; 
\node[labelNode] {B};
\node[graphicNode] (panel) {\includegraphics[width=4.5cm]{content/code/img/scores_plot.png}};
\node (anchor) at ([shift={(0.5cm,0.0)}]panel.north east) {}; 
\node[labelNode] {C};
\node[graphicNode] {\includegraphics[width=4.5cm]{content/code/img/matches_per_tile_plot.png}};
\node (anchor) at ([shift={(0.0cm,-1.0)}]0.5,2.5 |- panel.south east) {}; 
\node[labelNode] {D};
\node[graphicNode] {\includegraphics[width=14cm]{content/code/img/micrograph_with_matches.png}};
```


![Template matching in lamella imaged using the DeCo-Lace approach at eucentric
focus (A) Montage of Lamella$_\textrm{EUC}$ 1 overlaid with matches according to
their montage coordinates (B) Side view of matches in the lamella, such that the
direction of the electron beam is horizontal. (C-F) Magnified area of panel A
showing rough ER with associated ribosomes(C), outer nuclear membrane with
associated ribosomes (D), ribsomes arranged in a circular fashion(E), ribosomes
enclosed in a less electron dense inclusion in a granule(F). ](tikz:matching_euc){#fig:matching_euc}

```{.tikz-figure #matching_euc width=17cm height=10cm draft=false}


\node (anchor) at (0.5,9.5) {}; 
\node[labelNode] {A};
\node[graphicNode] {\includegraphics[height=12cm]{content/images/euc_lamella1_1000px.png}};
\node[graphicNode] {\includegraphics[height=12cm]{content/images/euc_lamella1_just_matches.png}};

\node (anchor) at (11.0,9.5) {}; 
\node[labelNode] {B};
\node[anchor=north west, below right=0cm and -4.5cm of anchor] {\includegraphics[height=12cm]{content/images/euc_lamella1_just_matches_side.png}};

\node (anchor) at (13.0,9.5) {}; 
\node[labelNode] {C};
\node[graphicNode] {\includegraphics[height=2.8cm]{content/images/euc_lamella1_just_matches_er_ribos.png}};

\node (anchor) at (13.0,6.5) {}; 
\node[labelNode] {D};
\node[graphicNode] {\includegraphics[height=2.8cm]{content/images/euc_lamella1_just_matches_nucleus.png}};

\node (anchor) at (13.,3.5) {}; 
\node[labelNode] {E};
\node[graphicNode] {\includegraphics[height=2.8cm]{content/images/euc_lamella1_just_matches_circle.png}};

\node (anchor) at (13.0,0.5) {}; 
\node[labelNode] {F};
\node[graphicNode] {\includegraphics[height=2.8cm]{content/images/euc_lamella1_just_matches_contained.png}};

```


![Template matching in lamella imaged using the DeCo-Lace approach at fringe-free
focus (A) Montage of Lamella$_\textrm{FFF}$ 4 overlaid with matches according to
their montage coordinates (B) Side view of matches in the lamella, such that the
direction of the electron beam is horizontal. (C-E) Magnified area of panel A
showing rough ER with associated ribosomes(C) and ribosomes
enclosed in a less electron dense inclusion in a granule(D,E). (F) Side view of
panel E with ribosomes situated inside the granule colored accoding
to SNR and other ribosomes colored in grey.](tikz:matching_fff){#fig:matching_fff}

```{.tikz-figure #matching_fff width=17cm height=10cm draft=false}



\node (anchor) at (0.5,9.5) {}; 
\node[labelNode] {A};
\node[graphicNode] {\includegraphics[height=12cm]{content/images/fff_lamella4_1000px.png}};
\node[graphicNode] {\includegraphics[height=12cm]{content/images/fff_lamella4_just_matches.png}};

\node (anchor) at (11.0,9.5) {}; 
\node[labelNode] {B};
\node[anchor=north west, below right=0cm and -4cm of anchor] {\includegraphics[height=12cm]{content/images/fff_lamella4_just_matches_side.png}};

\node (anchor) at (13.0,9.5) {}; 
\node[labelNode] {C};
\node[graphicNode] {\includegraphics[height=2.8cm]{content/images/fff_lamella4_just_matches_det3.png}};

\node (anchor) at (13.0,6.5) {}; 
\node[labelNode] {D};
\node[graphicNode] {\includegraphics[height=2.8cm]{content/images/fff_lamella4_just_matches_det1.png}};

\node (anchor) at (13.0,3.5) {}; 
\node[labelNode] {E};
\node[graphicNode] {\includegraphics[height=2.8cm]{content/images/fff_lamella4_just_matches_det4.png}};

\node (anchor) at (13,0.5) {}; 
\node[labelNode] {F};
\node[graphicNode] {\includegraphics[height=2.8cm]{content/images/fff_lamella4_just_matches_det6.png}};

```


![Workflow of DeCo-Lace processing](tikz:deco_lace_workflow){#fig:deco_lace_workflow}

```{.tikz-figure #deco_lace_workflow width=18cm height=18cm draft=false}
\begin{scope}[
          blocks/.style = {rectangle, draw, fill=blue!20, text width=15em, align=center, rounded corners, minimum height=2em,inner sep=0.5em},
          inputs/.style = {rectangle,draw,fill=cyan!20, inner sep=0.5em},
          every path/.style={line width=1pt}
]
\node [inputs,anchor=north] (struc) at (3.0,17.5) {\textbf{6SWA Structure}};

\node [inputs,anchor=north] (movies) at (9.0,17.5) {\textbf{Movies}};
\node [inputs,anchor=north] (meta) at (15.0,17.5) {\textbf{SerialEM Metadata}};

\node [inputs,anchor=north] (over) at (3.0,1.5) {\textbf{Overview Image}};

\node [blocks,anchor=north] (simu) at (3.0,15.5) {\textbf{Generate Template} \\ \textit{simulate}
\begin{itemize}
    \item   Generate electron density map at 1.5{\AA}  pixel-size
\end{itemize}};

\node [blocks,anchor=north] (mc) at (9.0,15.5) {\textbf{Motion correction} \\ \textit{unblur\_decolace}
\begin{itemize}
    \item   Motion correction using central area of movie
    \item   Mask out unilluminated areas and replace with noise
\end{itemize}};

\node [inputs,below = 0.5 cm of mc.south] (images) {\textbf{Images}};

\node [blocks,below = 0.5 cm of images.south] (ctf) {\textbf{Ctf estimation} \\ \textit{ctffind4} 
\begin{itemize}
    \item Standard CTF estimation
\end{itemize}};
\node [blocks,below = 0.7 cm of ctf.south] (match) {\textbf{Template matching} \\ \textit{match\_template} \\ Template matching using 6swa as template};

\begin{scope}[on background layer]

\node[draw,very thick, dashed, inner sep=0.5em, rounded corners, fill=blue!10,
    fit=(mc) (ctf) (match)] (gui) {};
\end{scope}
\node[below left=0.1cm and 0cm of gui.south east, font=\fontannot] {cisTEM GUI};

\node [blocks,below = 1.4 cm of match.south] (refine) {\textbf{Refine matches} \\ \textit{refine\_matches.py/refine\_template} \\ Refine matches and compile list of all matches in a lamella};

\node [inputs,below = 0.5 cm of refine.south] (refstar) {\textbf{matches\_in\_tiles.star}};


\node [blocks,anchor=center] (assem) at (images.east -| meta.south) {\textbf{Assemble montage} \\ \textit{assemble\_montage.py} 
\begin{itemize}
    \item Create list of all tiles and their respective coordinates
    \item Create binned montage image
\end{itemize}};

\node [inputs,below = 0.5 cm of assem.south] (monstar) {\textbf{montage.star}};

\node [blocks,anchor=center] (assemma) at (refstar.east -| monstar.south) {\textbf{Assemble matches} \\ \textit{assemble\_matches.py} 
\begin{itemize}
    \item Transfer coordinates of matches into the montage coordinate system
\end{itemize}};

\node [inputs,below = 0.5 cm of assemma.south] (monmastar) {\textbf{matches\_in\_montage.star}};


%% Draw lines
\draw[->] (struc) -- (simu);

\draw[->] (movies) -- (mc);
\draw[->] (mc) -- (images);
\draw[->] (images) -- (ctf);
\draw[->] (ctf) -- (match);
\draw[->] (match) -- (refine);

\draw[->] (meta) -- (assem);
\draw[->] (images) -- (assem);

\draw[->] (simu) |- (match);
\draw[->] (simu) |- (refine);

\draw[->] (assem) -- (monstar);
\draw[->] (monstar) -- (assemma);

\draw[->] (refine) -- (refstar);
\draw[->] (refstar) -- (assemma);
\draw[->] (assemma) -- (monmastar);

\end{scope}
```

## References {.page_break_before}

<!-- Explicitly insert bibliography here -->
<div id="refs"></div>
