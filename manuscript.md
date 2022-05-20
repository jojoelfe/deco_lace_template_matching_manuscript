---
title: Defocus Corrected Large Area Cryo-EM (DeCo-LACE) for Label-Free Detection of Molecules across Entire Cell Sections
keywords:
- cryo-EM
- visual protemics
- ribosome
lang: en-US
date-meta: '2022-05-20'
author-meta:
- Johannes Elferich
- Nikolaus Grigorieff
header-includes: |-
  <!--
  Manubot generated metadata rendered from header-includes-template.html.
  Suggest improvements at https://github.com/manubot/manubot/blob/main/manubot/process/header-includes-template.html
  -->
  <meta name="dc.format" content="text/html" />
  <meta name="dc.title" content="Defocus Corrected Large Area Cryo-EM (DeCo-LACE) for Label-Free Detection of Molecules across Entire Cell Sections" />
  <meta name="citation_title" content="Defocus Corrected Large Area Cryo-EM (DeCo-LACE) for Label-Free Detection of Molecules across Entire Cell Sections" />
  <meta property="og:title" content="Defocus Corrected Large Area Cryo-EM (DeCo-LACE) for Label-Free Detection of Molecules across Entire Cell Sections" />
  <meta property="twitter:title" content="Defocus Corrected Large Area Cryo-EM (DeCo-LACE) for Label-Free Detection of Molecules across Entire Cell Sections" />
  <meta name="dc.date" content="2022-05-20" />
  <meta name="citation_publication_date" content="2022-05-20" />
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
  <link rel="alternate" type="text/html" href="https://jojoelfe.github.io/deco_lace_template_matching_manuscript/v/9f26f343eb6707bf20436bc0f58fa1c34dc74c00/" />
  <meta name="manubot_html_url_versioned" content="https://jojoelfe.github.io/deco_lace_template_matching_manuscript/v/9f26f343eb6707bf20436bc0f58fa1c34dc74c00/" />
  <meta name="manubot_pdf_url_versioned" content="https://jojoelfe.github.io/deco_lace_template_matching_manuscript/v/9f26f343eb6707bf20436bc0f58fa1c34dc74c00/manuscript.pdf" />
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
([permalink](https://jojoelfe.github.io/deco_lace_template_matching_manuscript/v/9f26f343eb6707bf20436bc0f58fa1c34dc74c00/))
was automatically generated
from [jojoelfe/deco_lace_template_matching_manuscript@9f26f34](https://github.com/jojoelfe/deco_lace_template_matching_manuscript/tree/9f26f343eb6707bf20436bc0f58fa1c34dc74c00)
on May 20, 2022.
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
of neutrophil-like mouse cells, representing 1-2% of the total cellular
volume. We use 2D template matching (2DTM) to determine localization and orientation
of the large ribosomal subunit in these sections. These data provide "maps" of translational activity across
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
is able to be detected by its strong signal, such as a
fluorescent molecule. In label-free techniques, the physical properties
of molecules themselves are used for detection. An example for this is
proteomics using mass-spectrometry [@doi:10.1038/nbt.1592]. The advantage
of label-free techniques is that they can provide information over
thousands of molecules, while label-dependent techniques offer highly specific
information for a few molecules. Especially spatial information can
often only be achieved using label-dependent techniques, such as
fluorescence microscopy [@doi:10.1038/nmeth817]. 

Cryo-electron microscopy (cryo-EM) has the potential to directly visualize the
arrangement of atoms that compose biomolecules inside of cells, thereby
allowing label-free detection with high spatial accuracy. This has been
called "visual proteomics" [@doi:10.1038/nrm1861]. Since cryo-EM
requires thin samples (\<500nm), imaging of biomolecules inside cells is
restricted to small organisms, thin regions of cells, or samples that
have been suitably thinned. Thinning can be achieved either by
mechanical sectioning [@doi:10.1111/j.1365-2818.1983.tb04225.x] or by
milling using a focused ion beam (FIB) [@doi:10.1016/j.sbi.2013.08.006]. This complex workflow
leads to a low throughput of cryo-EM imaging of cells and is further
limited by the fact that at the required magnifications, typical fields
of view (FOV) are very small compared to mammalian cells, and the FOV
achieved by label-dependent techniques such as fluorescence light microscopy. The
predominant cryo-EM technique for the localization of biomolecules of
defined size and shape inside cells is cryo-electron tomography [@doi:10.1017/S0033583511000102]. However, the requirement of a tilt series at
every imaged location and subsequent image alignment, severely limits
the throughput for molecular localization.

An alternative approach is to identify molecules by their structural
"fingerprint" in single projection using "2D template-matching" (2DTM)
[@doi:10.7554/eLife.25648; @doi:10.1101/2020.04.22.053868;
@doi:10.7554/eLife.68946]. In this
method, a 3D model of a biomolecule is used as a template to find 2D
projections that match the molecules visible in the electron
micrographs. This method requires a projection search on a fine angular
grid, and the projections are used to find local cross-correlation peaks
with the micrograph. Since the location of a biomolecule in the
z-direction causes predictable aberrations to the projection image, this
method can be used to calculate complete 3D coordinates and orientations
of a biomolecule in a cellular sample
[@doi:10.1101/2020.04.22.053868].

Here we apply 2DTM of the ribosome large subunit (LSU) to cryo-FIB milled
neutrophil-like murine cells [@doi:10.1016/j.cell.2016.08.057]. We chose these
 cells because genetic defects in the ribosome machinery often leads to
hematopoietic disease [@doi:10.1093/nar/gkz637] and direct quantification of
ribosome location, number and conformational states in hematopoietic cells could
lead to new insight into hematopoietic disease [@doi:10.1186/s12885-018-4178-z].
To increase the amount of collected data and to provide unbiased sampling of the
whole lamella, we devised a new data-acquisition scheme, "Defocus-Corrected
Large Area Cryo-Electron microscopy" (DeCo-LACE). 2DTM allows us to test whether
aberrations caused by large beam-image shifts and highly condensed beams
deteriorate the high-resolution signal. We find that these aberrations do not
impede LSU detection by 2DTM. The resulting data provide a description of
ribosome distribution in an entire lamella, which represent 1-2% of the cellular
volume. We find a highly heterogeneous density of ribosomes within the cell.
Analysis of the throughput in this method suggests that for the foreseeable
future computation will be the bottleneck for visual proteomics.

## Materials and Methods

### Grid preparation

ER-HoxA9 cells were maintained in RPMI medium supplemented with 10% FBS,
penicillin/streptomycin, SCF, and estrogen [@doi:10.1016/j.cell.2016.08.057] at
37 °C and 5% CO2. 120 h prior to grid preparation, cells were washed twice in PBS
and cultured in the same medium except without estrogen. Differentiation was
verified by staining with Hoechst-dye and inspection of nuclear morphology.
Cells were then counted and diluted to $1\cdot10^6$ cells/ml. Grids (either 200
mesh copper grids, with a sillicone-oxide and 2 µm holes with a 2 µm spacing or
200 mesh gold grids with a thin gold film and 2 µm holes in 2 µm spacing) were
glow-discharged from both sides using a 15 mA for 45 s. 3.5 µl of cell suspension
was added to grids on the thin-film side and grids were blotted from the back
side using a GP2 cryoplunger (Leica) for 8 s and rapidly plunged into liquid
ethane at -185 °C. 

### FIB-milling

Grids were loaded into an Aquilos 2 FIB/SEM (Thermo Fisher) instrument with a
stage cooled to -190 °C. Grids were sputter-coated with platinum for 15 s at 45 mA
and then coated with a layer of platinum-precursor by opening the GIS-valve for
45 s. An overview of the grid was created by montaging SEM images and isolated
cells at the center of gridsquares were selected for FIB-milling. Lamellae were
generated automatically using the AutoTEM software (Thermo Fisher), with the
following parameters:

- Milling angle: 20°
- Rough milling: 3.2 µm thickness, 0.5 nA current
- Medium milling: 1.8 µm thickness, 0.3 nA current, 1.0° overtilt
- Fine milling: 1.0 µm tchickness, 0.1 nA current, 0.5° overtilt
- Finer milling: 700 nm thickness, 0.1 nA curent, 0.2° overtilt
- Polish 1: 450 nm thickness, 50 pA current
- Polish 2: 200 nm thickness, 30 pA current

This resulted in 6-10 µm wide lamella with 150-250 nm thickness as determined by
FIB-imaging of the lamella edges.

### Data collection

Grids were loaded into a Titan Krios TEM (Thermo Fisher) operated at 300 keV and
equipped with a BioQuantum energy filter (Gatan) and K3 camera (Gatan). The
microscope was aligned using a cross-grating grid on the stage. Prior to each
session, we carefully performed the "Image/Beam" calibration in nanoprobe. We
set the magnification to a pixel size of 1.76 Å and condensed the beam to ~ 900 nm
diameter, resulting in the beam being completely visible on the camera. To
establish fringe-free conditions, the "Fine eucentric" procedure of SerialEM [@doi:10.1016/j.jsb.2005.07.007] was
used to move a square of the cross-grating grid to the eucentric position of the
microscope. The effective defocus was then set to 2 µm, using the "autofocus"
routine of SerialEM. The objective focus of the microscope was changed until no
fringes were visible. The stage was then moved in Z until images had an apparent
defocus of 2 µm. The difference in stage Z-position between the eucentric and
fringe-free conditions was used to move other areas into fringe-free condition.

Low magnification montages were used to find lamellae and lamellae that were
sufficiently thin and free of contamination were selected for automated data
collection. Overview images of each lamella were taken at 2250x magnification
(38 Å pixel size). The corners of the lamella in the overview image were manually
annotated in SerialEM and translated into beam image-shift values using SerialEM's
calibration. A hexagonal pattern of beam image-shift positions was calculated
that covered the area between the four corners in a serpentine way, with a
$\sqrt{3}\cdot425$ nm horizontal spacing and $3/4\cdot 850$ nm vertical spacing. Exposures were
 taken at each position with a 30 e^-^/Å$^2$ total dose. After each exposure, the
defocus was estimated using the ctffind function of SerialEM and the focus for
the next exposure was corrected by the difference between the estimated focus
and the desired defocus of 800 nm. Furthermore, after each exposure the
deviation of the beam from the center of the camera was measured and corrected
using the "CenterBeamFromImage" command of SerialEM.

After data collection, a 20 s exposure at 2250x magnification of the lamella at
200 μm defocus was taken for visualization purposes. A Python script implementing
this procedure is available at [Link to repo].

### DeCo-LACE data processing

An overview of the data analysis pipeline is shown in Fig.
{@fig:deco_lace_workflow}. 

#### Pre-processing 
Motion-correction, dose weighting and other preprocessing as detailed below was performed using *cis*TEM [@doi:10.7554/eLife.35383]. To avoid influence of the beam-edge on motion-correction, only a quarter of the
movie in the center of the camera was considered for calculation of the
estimated motion. After movie frames were aligned and summed, a mask for the
illuminated area was calculated by lowpass filtering the image with a 100 Å
resolution cutoff, thresholding the image at 10% of the maximal value and then lowpass
filtering the mask again with a 100 Å resolution cutoff to smooth the mask edges. This mask was
then used to select dark areas in the image and fill the pixels with
Gaussian noise, with the same mean and standard deviation as the illuminated
area. A custom version of the unblur program [@doi:10.7554/eLife.06980]
implementing this procedure is available at [link to decolace branch]. During motion correction images were resampled to a pixel size of 1.5 Å. The
contrast-transfer function (CTF) was estimated using ctffind
[@doi:10.1016/j.jsb.2015.08.008], searching between 0.2 and 2 μm defocus. 

#### 2DTM

The search template was generated from the atomic model of the mouse LSU
(PDB 6SWA, exluding the Epb1 subunit) using the cryo-EM simulator implemented in *cis*TEM
[@doi:10.1107/S2052252521008538]. The
match_template program [@doi:10.7554/eLife.68946] was used to search for this
template in the movie-aligned, exposure-filtered and masked images, using a 1.5°
angular step in out-of-plane angles and a 1.0° angular step in-plane. 11 defocus
planes in 20 nm steps centered around the ctffind-determined defocus were searched. Targets
were defined as detected when their matches with the template produced peaks
with a singal-to-noise ratio (SNR) above a threshold of 7.75, which was chosen
based on the one-false-positive-per-tile criterion [@doi:10.7554/eLife.25648].

#### Montage assembly

The coordinates of each tile $i$,
$\mathbf{c}_{i}$ [2D Vector in pixels] were initialized using beam image-shift of the tile, $\mathbf{b}_i$ [2D Vector in μm],
and the ISToCamera matrix $\mathbf{IC}$, as calibrated by SerialEM: 

$$\mathbf{c}_{i} = \mathbf{IC} \cdot \mathbf{b}_i$$

A list of tile pairs $i,j$ that overlap were assembled by selecting images where
$|\mathbf{c}_i-\mathbf{c}_j| < D_{Beam}$. In order to calculate the precise offset between tiles $i$ and $j$, $\mathbf{r}_{i,j}$, we calculated the cross-correlation between the two tiles, masked to the overlapping illuminated area using the scikit-image
package [@doi:10.7717/peerj.453] was used to calculate refined offsets . The coordinates $\mathbf{c}_{i}$ were then refined by a least-square minimization against $\mathbf{r}_{i,j}$:

$$ \displaystyle{\min_{\mathbf{c}} \sum_{pairs}{(\mathbf{r}_{i,j} - (\mathbf{c}_i-\mathbf{c}_j))^2}}$$

using the scipy package [@doi:10.1038/s41592-019-0686-2]. The masked cross-correlation and the least-square minimization was repeated once more to arrive at the final tile alignment. 

The x,y coordinates of target $n$ detected by 2DTM in the tile $i$,
$\textbf{m}^\textrm{T}_{n,i}$, was transformed into the montage frame by adding
the coordinate of the tile.

$$ \textbf{m}^\textrm{M}_n = \textbf{m}^\textrm{T}_{n,i} + \textbf{c}_i$$

The z coordinate of each target was calculated as the sum of the defocus offset
for the target, the estimated defocus of the tile, and the nominal defocus of
the microscope when the tile was acquired. 

Images were rendered using UCSF ChimeraX [@doi:10.1002/pro.3943]. The Python scripts used for data processing are available
under [repolink].



## Results

### 2DTM detects large ribosomal subunits in cryo-FIB lamellae of mammalian cells

To test whether we could detect individual ribosomes in mammalian cells we
prepared cryo-lamellae of mouse neutrophil-like cells. An overview image
of a representative lamella clearly shows cellular features consistent with a
neutrophil-like phenotype, mainly a segmented nucleus and a plethora of
membrane-organelles, corresponding to the granules and secretory vesicles of
neutrophils (Fig. [@fig:initmatching]A). We then proceeded to acquire
micrographs on this lamella with a defocus of 0.5-1.0 μm, 30 e^-^/Å$^2$/s
exposure and 1.76 Å pixel size. We manually selected multiple locations in the
lamella and acquired micrographs using standard low-dose techniques where
focusing is performed on a sacrificial area. The resulting micrographs showed
smooth bilayered membranes and no signs of crystalline ice (Fig.
[@fig:initmatching]C,D), indicating successful vitrification throughout the
lamella. Successful vitrification is facilitated by the small size (~8 μm diameter) of these cells. 

We used an atomic model of the 60S mouse ribosomal subunit (6SWA) for 2DTM [@doi:10.1016/j.molcel.2020.11.037]. In a
subset of images, the distribution of cross-correlation scores significantly
exceeded the distribution expected from images devoid of detectable targets. In the
resulting scaled maximum-intensity projections (MIPs), clear peaks with SNR
values up to 10 were apparent (Fig. [@fig:initmatching2]A). Using a
threshold criterion to select significant targets (see Methods), we found that in
images of cytosolic compartments there were 10-500 ribosomes within one micrograph
(Fig. [@fig:initmatching]B-E). Notably, we found no targets in areas
corresponding to the nucleus (Fig. [@fig:initmatching]B) or mitochondria
(Fig. [1](#fig:initmatching)D). In the cytoplasm, we found a highly variable
number of targets, only \~ 50 in some exposures (Fig. [@fig:initmatching]E) and
up to 500 in others (Fig. [@fig:initmatching]C). This is a ten-fold
difference in local ribosome concentration, highlighting the importance of
imaging larger areas of a lamella to gain a complete picture of target
distributions. We therefore set out to collect cryo-EM data for 2DTM from
mammalian cell lamellae in a high-throughput unbiased fashion.

### DeCo-LACE for 2D imaging of whole lamellae

In order to obtain high-resolution data from complete lamellae, we used a new
approach for data collection. This approach uses three key strategies: (1) every
electron that exposes a fresh area of the sample is collected on the camera (2)
image shift is used to precisely and quickly raster the surface of a lamella and
(3) focusing is done without using a sacrificial area (Fig. [@fig:approach]A).

To ensure that every electron exposing a fresh area of the sample is captured by
the detector, we adjusted the electron beam size to be entirely contained by the
detector area. During canonical low-dose imaging, the microscope is configured so
that the focal plane is identical to the eucentric plane of the specimen stage.
This leaves the C2 aperture out of focus, resulting in ripples at the edge of
the beam (Fig. [@fig:approach]D). While these ripples are low-resolution
features that likely do not interfere with 2DTM \[cite\], we also tested data
collection under conditions where the C2 aperture is in focus ("fringe-free",
Fig. [@fig:approach]E).

We then centered a lamella on the optical axis of the microscope and used the
image shift controls of the microscope to systematically scan the whole surface
of the lamella in a hexagonal pattern (Fig. [@fig:approach]A,C). Instead of
focusing on a sacrificial area, we determined the defocus from every exposure
after it was taken. The defocus was then adjusted based on the difference
between desired and measured defocus (Fig. [@fig:approach]B). Since we used a
serpentine pattern for data collection, every exposure was close to the previous
exposure, making large changes in the defocus unlikely. Furthermore, we started
our acquisition pattern on the platinum deposition edge to make sure that the
initial exposure where the defocus was not yet adjusted did not contain any
biologically relevant information.

We used this strategy to collect data on eight lamellae, four using the
eucentric focus condition, hereafter referred to as Lamella~EUC~, and four using
the fringe-free condition, hereafter referred to as Lamella~FFF~(Fig.
[@fig:assembly] A+D, Fig.
[@fig:lamella_images]A). We were able to collect data with a highly
consistent defocus of 800 nm (Fig. [@fig:approach]F), both in the eucentric
focus and fringe-free focus condition. To ensure that data were collected
consistently, we mapped defocus values as a function of the applied image shift
(Fig. [@fig:lamella_spatial_info]A). This demonstrated that the defocus was
consistent across a lamella, except for rare outliers and in images containing
contamination. We also plotted the measured objective astigmatism of each
lamella and found that it varies with the applied image shift, becoming more
astigmatic mostly due to image shift in the x direction (Fig.
[@fig:lamella_spatial_info]B). While approaches exist to correct for this
during the data collection [@doi:10.1016/j.jsb.2019.09.013], we opted to not use these approaches in our
initial experiments. We reasoned that because 2DTM depends on high-resolution
information, this would be an excellent test of how much these aberration affect
imaging.

We assembled the tile micrographs into a montage using the image-shift values
and the SerialEM calibration followed by cross-correlation based refinement (see
Methods). In the resulting montages, the same cellular features visible in the
overview images are apparent (Fig. [@fig:assembly]B+E, Fig. [@fig:lamella_images]B), however
due to the high magnification and low defocus many more details, such as the
membrane bilayer separation, can be observed (Fig. [@fig:assembly]C+F). For montages collected using the
eucentric condition, there are clearly visible fringes at the edges between the
tiles (Fig. [@fig:assembly]C), which are absent in the fringe-free focus montages (Fig. [@fig:assembly]F). In our analysis
below, we show that these fringes do not impede target detection by 2DTM, making
them primarily an aesthetic issue. We also note that the tiling
pattern is visible in the montages (Fig. [@fig:assembly]B+E), which we believe is due to the non-linear
behavior of the K3 camera since we can observe these shading artifacts in micrographs of a condensed beam over vacuum (Fig. [@fig:gain]).

The montages show membrane vesicles and granules with highly variable sizes and
density. We found that a substantial number of granules, which are characterized by higher
density inside the the surrounding cytosol [@doi:10.1084/jem.134.4.907], seemed to contain a membrane-enclosed inclusion with density similar to
the surrounding cytosol (Fig. [@fig:lamella_images]C) and could therefore be formed
by an autophagy-like pathway. These granules were
150-300 nm in diameter and the inclusions were 100-200 nm in diameter. Based on
these dimensions the granules are either azurophil or specific granules [@doi:10.1084/jem.134.4.907]. To our
knowledge, these inclusion have not been described in granulocytes and are
further described and discussed below.

### 2DTM of DeCo-LACE data reveals ribosome distribution in cellular cross-sections

In our initial attempts of using 2DTM on micrographs acquired with the DeCo-LACE
protocol, we did not observe any SNR peaks above threshold using the large
subunit of the mouse ribosome (Fig. [@fig:crop_unblur]A). We reasoned that
the edges of the beam might interfere with motion-correction of the movies as
they represent strong low-resolution features that do not move with the sample.
When we cropped the movie frames to exclude the beam edges, the estimated amount
of motion increased (Fig. [@fig:crop_unblur]B), consistent with successful
tracking of sample motion. Furthermore, in the motion-corrected average we could
identify significant SNR peaks (Fig. [@fig:crop_unblur]B), confirming to
high sensitivity of 2DTM to the presents of high-resolution signal preserved in
the images by the motion correction. To streamline data processing, we
implemented a function in unblur to consider only a defined central area of a
movie for estimation of sample motion, while still averaging the complete movie
frames (Fig. [@fig:crop_unblur]C). Using this approach, we motion-corrected
all tiles in the eight lamellae and found consistently total motion below 1 Å
per frame (Fig. [@fig:lamella_motion_thickness] A). In some lamellae we
found increased motion in the lamella center, which indicates areas of variable
mechanical stability within FIB-milled lamellae. In some micrographs we also
observed that the beam edges gave rise to artifacts in the MIP and numerous
false-positive detections at the edge of the illuminated area (Fig. [@fig:crop_unblur]D). A
similar phenomenon was observed on isolated "hot" pixels in unilluminated areas.
To overcome this issue we implemented a function in unblur to replace
dark areas in the micrograph with Gaussian noise (see Methods), with
mean and standard deviation matching the illuminated portion of the micrograph
(Fig. [@fig:crop_unblur]D+E). Together, these pre-processing steps enabled us to perform 2DTM on
all tiles of the eight lamellae.

We used the refined tile positions to calculate the positions of the detected
LSUs in the lamellae (Fig. [@fig:matching_euc]A, Fig. [@fig:matching_fff]A). Overlaying these positions of the lamellae montages reveal ribosome
distribution throughout the FIB-milled slices of individual cells. Organelles
like the nucleus and mitochondria only showed sporadic targets detected with low
SNRs, consistent with the estimated false-positive rate of one per tile. For
each detected target we also calculated the Z positions from the individual
estimated defocus and defocus offset for each tile. When viewed from the side,
the ribosome positions therefore show the slight tilts of the lamellae relative
to the microscope frame of reference (Fig. [@fig:matching_euc]B, Fig.
[@fig:matching_fff]B). Furthermore, the side views indicated that lamellae
were thinner at the leading edge. Indeed, when plotting the transmitted beam
intensities in individual tiles as a function of beam image-shift, we observed
substantially higher intensities at the leading edge (Fig. [@fig:lamella_motion_thickness]B), which in energy-filtered
TEM indicates a thinner sample [@doi:10.1016/j.jsb.2018.06.007]. Even though we prepared the lamellae
with the "overtilt" approach [@doi:10.1016/j.jsb.2016.07.010], this means that ribosome densities across
the lamellae can be skewed by a change in thickness, and better sample
preparation methods are needed to generate more even samples.

Close inspection of the ribosome positions in the lamellae revealed several
interesting features. Ribosomes could be seen associating with membranes, in
patterns reminiscent of the rough endoplasmic reticulum (Fig.
[@fig:matching_euc]C, Fig. [@fig:matching_fff]C) or the outer nuclear
membrane (Fig. [@fig:matching_euc]D). We also observed ribosomes forming
ring-like structures (Fig. [@fig:matching_euc]E), potentially indicating
circularized mRNAs [@pmid:9702200]. While ribosomes were for the most part excluded
from the numerous granules observed in the cytoplasm, in some cases we observed
clusters of ribosomes in the inclusions of double-membraned granules
described earlier (Fig. [@fig:matching_euc]F, Fig. [@fig:matching_fff]D,E). It is, in principle, possible that these targets are situated above or
below the imaged granules, since the granule positions in z cannot be determined
using 2D projections. However, in the case of Fig. [@fig:matching_fff]E, the
detected ribosomes span the whole lamella in the z direction (Fig. [@fig:matching_fff]F), while positions
above or below a granule would result in ribosomes situated exlusively at the
top or bottom of the lamella. This conclusive evidence of ribosomes in
inclusions is consistent with the earlier hypothesis that the inclusions are of
cytoplasmic origin.

### Does DeCo-LACE induce aberrations that affect 2DTM?

Within the eight lamellae we found different number of detected targets (Fig.
[@fig:matching_stat]A). Lamella~EUC~ 1 had the most detected targets, but also has
the largest surface area and contained cytoplasm from two cells. Lamella~FFF~ 4
had the fewest detected targets, but this particular lamella was dominated by a
circular section of the nucleus, with only small pockets of cytoplasm (Fig.
[@fig:lamella_images]). In an attempt to normalize for these differences in
area containing cytoplasm, we compared the number of detected targets per tile in
tiles that contained more than one target, which should exclude tiles with
non-cytosolic content (Fig. [@fig:matching_stat]B). While this measure had
less variability, there were still differences. Lamella~EUC~ 4 had not only the
fewest targets, but also the lowest density, which could be due to this lamella being the 
thinnest, or due to it sectioning the cell in an area with a lower concentration of
ribosomes. Lamella~FFF~ 3 had a substantially higher number of ribosomes per
tile. Since all of these lamellae were made from a cell-line under identical
conditions, this underscores the necessity to collect data from large numbers of
lamellae to overcome the inherent variability. When comparing the distribution of
scores between lamellae, we found them to be fairly comparable with median
SNRs ranging from 8.7 to 9.7 (Fig. [@fig:matching_stat]C). Lamella~EUC~ 1 had slightly lower scores compared
to
the rest, potentially due to its large size and connected mechanical instability
during imaging. Overall, we did not observe differences in the number or SNR of
detected targets between eucentric or fringe-free illumination conditions that
were bigger than the observed inter-lamella variability.

Since the SNR values of 2DTM are highly sensitive to image quality, we reasoned
we could use them to verify that DeCo-LACE does not introduce a systematic loss
of image quality. We considered non-parallel illumination introduced by the
unusually condensed beam and uncharacterized aberrations near the beam
periphery. When plotting the SNR values of detected targets in all eight
lamellae as a function of their location in the tiles, we found uniformly high
SNR values throughout the illuminated areas for both eucentric and fringe-free
focus illumination, demonstrating that both illumination schemed are suitable
for DeCo-LACE (Fig. [@fig:matching_stat]D).

We also wondered whether large image shifts would lead aberration due to
astigmatism or beam tilt [@doi:10.1016/j.jsb.2019.09.013]. We reasoned that if
that was the case the number of detected targets should be highest in the center of the
lamella where the applied beam image-shift is 0. Instead we observed that in
both eucentric and fring-free focus conditions more target where detected at the
"back" edge of the lamella (Fig. [@fig:matching_stat]E]). This may be due to the center of the cell being predominantly
occupied by the nucleus, despite its segmentation in neutrophil-like cells. The
increase in matches at the "back" of the lamellae compared to the "front" can also
be explained by the thickness gradient of the lamellae (Fig. [@fig:lamella_motion_thickness]B,
Fig. [@fig:matching_euc]B, Fig. [@fig:matching_fff]B). In addition, aberrations would be expected to cause average 2DTM SNRs to be higher when beam-image shift
values are small. Instead, we found that SNRs where on average the highes at the
"front" edge of the lamellae, presumably due to the thinner sample. We therefore
conclude that factors other that beam image-shift or beam
condensation aberrations are limiting 2DTM SNRS, predominantly the thickness of
the lamellae.

### Computation is the bottleneck of visual proteomics

As described above, the variability of lamellae, both in terms of experimental
parameters including area, thickness and mechanical stability, and in terms of
biology, such as selection of cell type and location of the section within the
cell, requires collection of orders of magnitude more data than in this study to draw quantitative
and statistically relevant conclusions about the number and location of
molecules under different experimental conditions. The samples used were
prepared in two 24 h sessions on a FIB/SEM instrument, and imaging was performed
during another two 24h session on the TEM microscope. Inspections of the
timestamps of the raw data files revealed that the milling time per lamella was
\~30 minutes and TEM imaging was accomplished in \~10 seconds per tile or 90
minutes for a \~ 6x6 μm lamella. Processing of the data, however, took
substantially longer. Specifically, 2DTM of all tiles took approximately one
week per lamella on 32 A100 GPUs. Computation is therefore a bottleneck in our
current workflow, and further optimizations of the algorithm may be necessary
increase throughput. Alternatively, this bottleneck could be reduced by
increasing the number of processing units.


## Discussion

In this study we developed an approach to image entire cellular cross-section using cryo-EM at high enough resolution to allow for 2DTM detection of the LSU. The two main advantages compared to previous approaches are a high throughput of imaging and the biological context for detected molecules. The requirement to increase throughput in cryo-EM data collection of cellular samples has been recognized in the recent literature. Most approaches describeb so far are tailored towards tomography. Peck et al. [@doi:10.1016/j.jsb.2022.107860] and Yang et al. [@doi:10.1101/2021.12.31.474669] developed approaches to increase the FOV of tomogram data-collection by using a montaging technique. Peck et al. used a similar "condensed-beam" approach as described here. However, the montages are substantially smaller in scope, covering carbon film holes of 2 um diameter. Bouvette et al. [@doi:10.1038/s41467-021-22251-8] and Eisenstein et al. [@doi:10.1101/2022.04.07.487557] are using beam image-shift to collect tilt-series in multiple locations in parallel to increase throughput. However, none of these approaches provide the full coverage of a cellular cross-section that can be achieved using DeCo-Lace.

Since we observed substantial variation in ribosome density within and between lamellae, visual proteomics studies that use cryo-EM to establish changes in molecular organization within cells will require orders of magnitude more data than used in this study. One milestone would be to image enough data to represent one cellular volume, which for a small eukaryotic cells requires imaging approximately 100 lamella. While data collection throughput on the TEM is fundamentally limited by the exposure time, this amount of data could be collected within 12 hour by improving the data acquisition scheme to perform all necessary calculation in parallel with actual exposure of the camera. Sample preparation using a FIB/SEM is also currently a bottleneck, but preparation of large lamellae with multiple cellular cross-sections using methods like WAFFLE [@doi:10.1038/s41467-022-29501-3] might allow sufficient throughput. As stated in the results, at least for 2DTM computation will remain challenging and approximately 17,000 GPU hours would be required for a 100 lamellae dataset. 

As described in [@doi:10.7554/eLife.25648] the 2DTM SNR threshold for detecting a target is chosen to result in one false positive detection per image searched. We would therefore expect to find one false positive detection per tile. We reasoned that the large nuclear area imaged by DeCo-Lace could be used to test whether this assumption is true. In the 670 tiles containing exclusively nucleus (as manually annotated from the overview image) we detected 247 targets, making the false-positive rate more than twofold lower than expected. Since earlier work shows that 2DTM with the LSU can produce matches to nuclear ribosome biogenesis intermediates [@doi:10.1101/2022.04.10.487797], this could even be an overestimate of the false-positive rate. This suggests that the detection threshold could be even lower, which is an area of ongoing research.

We found that even though we used beam image-shift extensively (up to 7 um), we did not see substantially reduced 2DTM SNR values in tiles acquired at high beam image-shift compared to tiles acquired with low or no beam image-shift. This is in contrast to reports in single-particle analysis (SPA) [@doi:10.1107/S2052252520013482] where the induced beam tilt substantially reduced the resolution if it was not corrected during processing. It is possible that 2DTM is less sensitive to beam-tilt aberrations, since the template is free of any aberration and only the image is distorted, while in SPA the beam tilt will affect both the images and the reconstructed template.

As mentioned in the results, we found a consistent shading artifact pattern in our montages, that we believe is the result of non-linear behavior of the K3 camera. Indeed, when we average images with a condensed beam taken over vacuum we found in both focus conditions a consistent background pattern with a brighter region on the periphery of the illuminated area (Fig [@fig:gain]). This might be caused by dynamic adjustment of the internal camera counting threshold which expects columns of the sensor to be evenly illuminated as is the case for SPA applications. Since the signal of this pattern has mainly low-resolution components it is unlikely to affect 2DTM. However, it highlights that the non-linear behavior of the camera has to be taken into account when imaging samples with strongly varying density and unusual illumination schemes. 

Unexpectedly, we observed granules containing a vesicle of putative cytosolic origin. We speculate that upon degranulation, the process in which granules fuse with the plasma membrane, these vesicles would be released into the extracelullar space. The main types of extracellular vesicles of this size are exosomes, up to 100 nm large vesicles derived from fusion of multivesicular bodies with the plasma membrane, and microvesicles, which are derived from direct budding of the plasma membrane [@doi:10.1038/nrm.2017.125]. We suggest that granulocytes could release a third type of extracellular vesicle, granule-derived vesicles (GDV), into the extracellular space. 2DTM showed that a subset of GDVs can contain ribosomes (Fig. [@fig:matching_euc]F, Fig. [@fig:matching_fff]D,E). This could indicate that these vesicles are transporting translation-capable mRNAs, as has been described for exosomes [@doi:10.1038/ncb1596]. Further studies will be necessary to confirm the existence of GDVs in granulocytes isolated from mammals and to understand their functional significance.




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

## Figures

![2D template matching of the large subunit of the ribosome in fib-milled neutrophil-like cells 
(A) Overview image of the lamella. Major cellular regions are labeled, as Nucleus (Nuc), Mitochondria (M), and granular cytoplasm (GrCyt). FOVs where high-magnification images for template matching where acquired are indicated as boxes with the number of detected targets indicated on the bottom right. FOVs displayed in Panels B-E are color-coded. Scalebar corresponds to 1 μm.
(B-E) FOVs with projection of detected LSUs shown in cyan. (B) Perinuclear region, the only detected targets are in the cytoplasmic half. (C) Cytoplasmic region with high density of ribosomes (D) Mitochondrium, as expected there are only detected LSUs in the cytoplasmic region (E) Cytoplasm, with low density of ribosomes. 
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
\node (img) [graphicNode]  {\includegraphics[height=4cm]{content/images/30_matches_m.png}};
\node (img) [graphicNode]  {\includegraphics[height=4cm]{content/images/30_matches.png}};
\node (n3) [box=green, fit=(img)] {};

\node (anchor) at (12.75,9.35) {}; 
\node[labelNode] {C};
\node (img) [graphicNode]  {\includegraphics[height=4cm]{content/images/506_matches_m.png}};
\node (img) [graphicNode]  {\includegraphics[height=4cm]{content/images/506_matches.png}};
\node (n3) [box=red, fit=(img)] {};

\node (anchor) at (6.5,4.75) {}; 
\node[labelNode] {D};
\node (img) [graphicNode]  {\includegraphics[height=4cm]{content/images/17_matches_m.png}};
\node (img) [graphicNode]  {\includegraphics[height=4cm]{content/images/17_matches.png}};
\node (n3) [box=orange, fit=(img)] {};

\node (anchor) at (12.75,4.75) {}; 
\node[labelNode] {E};
\node (img) [graphicNode]  {\includegraphics[height=4cm]{content/images/52_matches_m.png}};
\node (img) [graphicNode]  {\includegraphics[height=4cm]{content/images/52_matches.png}};
\node (n3) [box=magenta, fit=(img)] {};

%%\iftoggle{draft}{\node [redAnchorNode] {};};

```

![2D template matching of the large subunit of the ribosome in fib-milled
neutrophil-like cells (A) Maximum intensity projection (MIP) cross-correlation map of
micrograph shown in Figure
{@fig:initmatching} (B+C) 3D plot of MIP regions indicated by color boxes in Panel A](tikz:initmatching2){#fig:initmatching2 tag="2 - figure supplement 1"}

```{.tikz-figure #initmatching2 width=13cm height=9cm draft=false}
\node (anchor) at (0.5,8.35) {}; 

\node at ([shift={(-0.3cm,0.9cm)}]anchor) [anchor=north west] {\includegraphics[width=12cm]{content/code/img/initial_map_match.pdf}};
\node[labelNode] {A};
\iftoggle{draft}{\node [redAnchorNode] {};};
\node (anchor) at (8.5,8.35) {}; 
\node[labelNode] {B};
\node (anchor) at (8.5,4.85) {}; 
\node[labelNode] {C};
```





![DeCo-LACE approach (A) Graphic demonstrating the data-collection strategy for
DeCo-LACE. The electron beam is condensed to a diameter $D_{Beam}$ that allows captured of
the whole illuminated area on the camera. Beam-image shift along X and Y
($BIS_X$,$$BIS_Y$) is used to scan the whole lamella
(B) Diagram of the collection algorithm
(C) Example overview image of a lamella with the designated acquisition
positions and the used beam diameter indicated with red circles. Scalebar corresponds to 1 μm.
(D+E) Representative micrographs takne with a condensed beam at eucentric focus
(D) or fringe-free focus (E). Scalebar corresponds to 100 nm.
(F) Boxplot of defocus measured by ctffind of micrographs taken by the DeCo-Lace
approach on four lamellae images at eucentric focus and four lamellae imaged with
fringe-free focus.
](tikz:approach){#fig:approach}

```{.tikz-figure #approach width=20cm height=10cm draft=false}
\node (anchor) at (0.5,9.35) {}; 
\node[labelNode] {A};
\node[graphicNode] {\includegraphics[width=5cm]{content/graphics/approach/approach.png}};
\draw [densely dotted, red,thick] (3,9.5) -- (3,5.0);
\draw [densely dotted, red,thick] (3,4.2) -- (3,1.4);

\tikzset{dimen/.style={<->,>=latex,thin,every rectangle node/.style={above right=0.2cm and -0.3cm,fill=white,midway,font=\sffamily}}}

\draw (3.55,5.4) -- ++(0,1.5) coordinate (D1) -- +(0,5pt);
\draw (4.15,5.4) -- ++(0,1.5) coordinate (D2) -- +(0,5pt);
\draw [dimen] (D1) -- (D2) node {$D_{Beam}$};

\draw [->, very thick] (3,5) -- ++(0.5,-0.2)  coordinate (S1) node[midway,below left] {$BIS_X$} ;
\draw [->, very thick] (S1) -- (3.85,5.4) node[midway,below right] {$BIS_Y$};



\node (anchor) at (6.0,9.35) {}; 
\node[labelNode] {B};

% Place nodes
\node [block] (init) at (8.0,8.35) {\textbf{START} \\ Collect overview image};
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

\node (anchor) at (11.5,9.35) {}; 
\node[labelNode] {C};
% X axis is 9.4um
\node[graphicNode] (image) {\includegraphics[width=8cm]{content/code/img/acquisition_positions.png}};
\draw [line width=1.55mm,white] ([xshift=0.5cm, yshift=0.3cm]image.south west) -- ([xshift=1.35cm, yshift=0.3cm]image.south west);
\draw [line width=0.7mm,black] ([xshift=0.5cm, yshift=0.3cm]image.south west) -- ([xshift=1.35cm, yshift=0.3cm]image.south west);
\iftoggle{draft}{\node [redAnchorNode] {};};


\node (anchor) at (0.5,-0.5) {}; 
\node[labelNode] {D};
\node[graphicNode] (euc) {\includegraphics[height=4.0cm]{content/images/fringebeam.png}};
\node[anchor=center] at ([shift={(0.0cm,0.3cm)}]euc.north) {Eucentric Focus};
\draw [line width=1.25mm,white] ([xshift=-0.05cm, yshift=0.1cm]euc.south east) -- ([xshift=-0.8cm, yshift=0.1cm]euc.south east);
\iftoggle{draft}{\node [redAnchorNode] {};};


\node (anchor) at (5.5,-0.5) {}; 
\node[labelNode] {E};
\node[graphicNode] (fff) {\includegraphics[height=4.0cm]{content/images/nofringebeam.png}};
\node[anchor=center] at ([shift={(0.0cm,0.3cm)}]fff.north) {Fringe-free Focus};
\draw [line width=1.25mm,white] ([xshift=-0.05cm, yshift=0.1cm]fff.south east) -- ([xshift=-0.8cm, yshift=0.1cm]fff.south east);
\iftoggle{draft}{\node [redAnchorNode] {};};

\node (anchor) at (10.5,-0.5) {}; 
\node[labelNode] {F};
\node[anchor=north west, below right=-0.5cm and 0cm of anchor] {\includegraphics[height=4.8cm]{content/code/img/defocusplot.pdf}};
\iftoggle{draft}{\node [redAnchorNode] {};};
```


![Defocus estimation of individual tiles of DeCo-Lace montages
(A) Defocus values of individual micrographs taken using the DeCo-Lace approach
plotted as a function of the beam image-shift values. 
(B) Defocus astigmatism of individual micrographs taken using the DeCo-Lace approach
plotted as a function of the beam image-shift values. ](tikz:lamella_spatial_info){#fig:lamella_spatial_info tag="3 - figure supplement 1"}

```{.tikz-figure #lamella_spatial_info width=20.0cm height=10cm draft=false}
\newlength{\panelheight}
\setlength{\panelheight}{4.6cm}


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




![Assembling DeCo-LACE exposures into montages (A)  Overview
image of Lamella~EUC~ 1  taken at low magnification. Scalebar corresponds to 1 μm. (B) Overview of Lamella~EUC~ 1 created by
montaging high magnification images taken with the DeCo-Lace approach. Scalebar corresponds to 1 μm. (C) Zoom-in into red box in panel B. Slight beam-fringe artifacts are visible. Scalebar corresponds to 100 nm.
(D)  Overview
image of Lamella~FFF~ 4  taken at low magnification. Scalebar corresponds to 1 μm. (E) Overview of Lamella~FFF~ 4 created by
montaging high magnification images taken with the DeCo-Lace approach. Scalebar corresponds to 1 μm. (F) Zoom-in into red box in panel E. No beam-fringe artifacts are visible. Scalebar corresponds to 100 nm. ](tikz:assembly){#fig:assembly}
```{.tikz-figure #assembly width=15cm height=5cm draft=false}
\def\panelheight{6.0cm}

\node (anchor) at (0.5,13.0) {}; 
\node[labelNode] {A};
\node[graphicNode] (img) {\includegraphics[height=\panelheight,trim=0.0 0 0cm 0, clip]{content/images/euc_lamella1_view.png}};
% Title
\node[anchor=center,align=center] at ([shift={(0.0cm,0.6cm)}]img.north) {\baselineskip=8pt   \\ 38Å pixel size \\ 300μm defocus};
% scalebar - physical height is 12810 nm
\draw [line width=1.55mm,white] ([xshift=0.5cm, yshift=0.3cm]img.south west) -- ([xshift=0.5cm + \panelheight / 12.81 , yshift=0.3cm]img.south west);
\draw [line width=0.7mm,black] ([xshift=0.5cm, yshift=0.3cm]img.south west) -- ([xshift=0.5cm + \panelheight / 12.81, yshift=0.3cm]img.south west);

\node (anchor) at (5.5,13.0) {}; 
\node[labelNode] {B};
\node[graphicNode] (img) {\includegraphics[height=6.0cm,trim=0 0 0cm 0, clip]{content/images/euc_lamella1_assm.png}};
\node[anchor=center,align=center] at ([shift={(0.0cm,0.7cm)}]img.north) {\baselineskip=8pt Eucentric Focus \\ 1.76Å pixel size \\ 800nm defocus};
% Red Box
\node (rect) at (6.52,10.78) [anchor=center,draw,thick,minimum width=0.375cm,minimum height=0.469cm,color=red] {};
% scalebar - physical height is 12810 nm
\draw [line width=1.55mm,white] ([xshift=0.5cm, yshift=0.3cm]img.south west) -- ([xshift=0.5cm + \panelheight / 12.81 , yshift=0.3cm]img.south west);
\draw [line width=0.7mm,black] ([xshift=0.5cm, yshift=0.3cm]img.south west) -- ([xshift=0.5cm + \panelheight / 12.81, yshift=0.3cm]img.south west);

\node (anchor) at (10.6,13.0) {}; 
\node[labelNode] {C};
% height is 750 nm
\node[graphicNode] (image) {\includegraphics[height=6.0cm]{content/images/euc_lam1_zoomin.png}};
\node (n3) [box=red, fit=(image)] {};
\draw [line width=1.55mm,white] ([xshift=0.5cm, yshift=0.3cm]image.south west) -- ([xshift=1.3cm, yshift=0.3cm]image.south west);
\draw [line width=0.7mm,black] ([xshift=0.5cm, yshift=0.3cm]image.south west) -- ([xshift=1.3cm, yshift=0.3cm]image.south west);


\node (anchor) at (0.5,5.0) {}; 
\node[labelNode] {D};
\node[graphicNode] (img) {\includegraphics[height=6.0cm,trim=0 0 0cm 0, clip]{content/images/fff_lamella4_view.png}};
\node[anchor=center,align=center] at ([shift={(0.0cm,0.6cm)}]img.north) {\baselineskip=8pt  \\ 38Å pixel size \\ 300μm defocus};
% scalebar - physical height is 9337.5 nm
\draw [line width=1.55mm,white] ([xshift=0.5cm, yshift=0.3cm]img.south west) -- ([xshift=0.5cm + \panelheight / 9.3375 , yshift=0.3cm]img.south west);
\draw [line width=0.7mm,black] ([xshift=0.5cm, yshift=0.3cm]img.south west) -- ([xshift=0.5cm + \panelheight / 9.3375, yshift=0.3cm]img.south west);


\node (anchor) at (5.8,5.0) {}; 
\node[labelNode] {E};
\node[graphicNode] (img) {\includegraphics[height=6.0cm,trim=0 0 0cm 0, clip]{content/images/fff_lamella4_assm.png}};
\node[anchor=center,align=center] at ([shift={(0.0cm,0.7cm)}]img.north) {\baselineskip=2pt Fringe-free Focus \\ 1.76Å pixel size \\ 800nm defocus};
\node (rect) at (8.438,3.83) [anchor=center,draw,thick,minimum width=0.375cm,minimum height=0.469cm,color=red] {};
% scalebar - physical height is 9337.5 nm
\draw [line width=1.55mm,white] ([xshift=0.5cm, yshift=0.3cm]img.south west) -- ([xshift=0.5cm + \panelheight / 9.3375 , yshift=0.3cm]img.south west);
\draw [line width=0.7mm,black] ([xshift=0.5cm, yshift=0.3cm]img.south west) -- ([xshift=0.5cm + \panelheight / 9.3375, yshift=0.3cm]img.south west);

\node (anchor) at (11.0,5.0) {}; 
\node[labelNode] {F};
% height is 750 nm
\node[graphicNode] (image) {\includegraphics[height=6.0cm]{content/images/fff_lam4_zoomin.png}};
\node (n3) [box=red, fit=(image)] {};
\draw [line width=1.55mm,white] ([xshift=0.5cm, yshift=0.3cm]image.south west) -- ([xshift=1.3cm, yshift=0.3cm]image.south west);
\draw [line width=0.7mm,black] ([xshift=0.5cm, yshift=0.3cm]image.south west) -- ([xshift=1.3cm, yshift=0.3cm]image.south west);
```







![Motion correction of movies with condensed beams. 
At the top of each panel is an average of the movie that was motion-corrected
with a red dashed box indicating the region that was used to estimate shifts.
Below is a graph indicating the estimated shifts of the individual frames of the
movie. Below this is the MIP of 2DTM using the large subunit of the mouse ribosome.
(A) Motion correction of the whole movie
(B) Notion correction of a cropped region of the movie that eliminates the beam
edges
(C) Motion correction of the whole movie, using only the central region to
estimate the shifts
](tikz:crop_unblur){#fig:crop_unblur tag="4 - figure supplement 1"}

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

\node (anchor) at ([shift={(0.0,-1.0cm)}]0.5,9.5 |- panel.south east) {}; 
\node[labelNode] {D};
\node[graphicNode] (panel) {\includegraphics[height=5cm]{content/images/deco_unblur/zap000.png}};
\node (anchor) at ([shift={(0.0,-0.5cm)}]panel.south west) {}; 
\node[graphicNode] (panel2) {\includegraphics[height=5cm]{content/images/deco_unblur/zap002.png}};

\node (anchor) at ([shift={(1.5,0.0cm)}] panel.north east) {}; 
\node[labelNode] {E};
\node[graphicNode] (panel) {\includegraphics[height=5cm]{content/images/deco_unblur/zap001.png}};
\node (anchor) at ([shift={(0.0,-0.5cm)}]panel.south west) {}; 
\node[graphicNode] (panel) {\includegraphics[height=5cm]{content/images/deco_unblur/zap004.png}};



```






![Motion correction of individual tiles imaged using the DeCo-LACE approach
(A) Total estimated motion of individual micrographs taken using the DeCo-Lace approach
plotted as a function of the beam image-shift values. 
(B) Electron intensity of individual micrographs taken using the DeCo-Lace approach
plotted as a function of the beam image-shift values. ](tikz:lamella_motion_thickness){#fig:lamella_motion_thickness tag="4 - figure supplement 2"}






```{.tikz-figure #lamella_motion_thickness width=20.0cm height=10cm draft=false}
\newlength{\panelheight}
\setlength{\panelheight}{4.6cm}


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




![ Averages of micrographs taken with a condensed beam over vacuum using a Gatan K3 detector. Contrast and Brightness have been adjusted to highlight uneven dose response. (A) Eucentric Focus (B) Fringe-free Focus ](tikz:gain){#fig:gain tag="4 - figure supplement 3"}

```{.tikz-figure #gain width=10.0cm height=2cm draft=false}
\newlength{\panelheight}
\setlength{\panelheight}{7cm}


\node (anchor) at (0.5,3.5) {}; 
\node[labelNode] {A};
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/images/euc_gain.png}};

\node (anchor) at ([shift={(0.5cm,0.0cm)}]panel.north east) {}; 
\node[labelNode] {B};
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/images/fff_gain.png}};
```

![ Overview images of lamellae imaged using the DeCo-LACE approach taken at low-magnification (A) Overviews taken at low magnification. Scalebar corresponds to 1 μm. (B) Overviews assembled using the DeCo-LACE approach. Scalebar corresponds to 1 μm. (C) Representative examples of a class of granules containing a putatively cytosolic inclusion. Scalebar corresponds to 100 nm.
](tikz:lamella_images){#fig:lamella_images tag="4 - figure supplement 4"}

```{.tikz-figure #lamella_images width=20.0cm height=5cm draft=false}
\newlength{\panelheight}
\setlength{\panelheight}{4.4cm}

\node (anchor) at (0.5,4.5) {}; 
\node[labelNode] {A};
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/images/euc_lamella1_view.png}};
% Title
\node[anchor=center,align=center] at ([shift={(0.0cm,0.3cm)}]panel.north) {Lamella$_\textrm{EUC}$ 1};
% scalebar - physical height is 12810 nm
\draw [line width=1.55mm,white] ([xshift=0.5cm, yshift=0.3cm]panel.south west) -- ([xshift=0.5cm + \panelheight / 12.81 , yshift=0.3cm]panel.south west);
\draw [line width=0.7mm,black] ([xshift=0.5cm, yshift=0.3cm]panel.south west) -- ([xshift=0.5cm + \panelheight / 12.81, yshift=0.3cm]panel.south west);
\node (anchor) at ([shift={(0.5cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/images/euc_lamella2_view.png}};
% Title
\node[anchor=center,align=center] at ([shift={(0.0cm,0.3cm)}]panel.north) {Lamella$_\textrm{EUC}$ 2};
% scalebar - physical height is 7027.5 nm
\draw [line width=1.55mm,white] ([xshift=0.5cm, yshift=0.3cm]panel.south west) -- ([xshift=0.5cm + \panelheight / 7.0275 , yshift=0.3cm]panel.south west);
\draw [line width=0.7mm,black] ([xshift=0.5cm, yshift=0.3cm]panel.south west) -- ([xshift=0.5cm + \panelheight / 7.0275, yshift=0.3cm]panel.south west);
\node (anchor) at ([shift={(0.5cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/images/euc_lamella3_view.png}};
% Title
\node[anchor=center,align=center] at ([shift={(0.0cm,0.3cm)}]panel.north) {Lamella$_\textrm{EUC}$ 3};
% scalebar - physical height is 9615 nm
\draw [line width=1.55mm,white] ([xshift=0.5cm, yshift=0.3cm]panel.south west) -- ([xshift=0.5cm + \panelheight / 9.615 , yshift=0.3cm]panel.south west);
\draw [line width=0.7mm,black] ([xshift=0.5cm, yshift=0.3cm]panel.south west) -- ([xshift=0.5cm + \panelheight / 9.615, yshift=0.3cm]panel.south west);
\node (anchor) at ([shift={(0.5cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/images/euc_lamella4_view.png}};
% Title
\node[anchor=center,align=center] at ([shift={(0.0cm,0.3cm)}]panel.north) {Lamella$_\textrm{EUC}$ 4};
% scalebar - physical height is 8625 nm
\draw [line width=1.55mm,white] ([xshift=0.5cm, yshift=0.3cm]panel.south west) -- ([xshift=0.5cm + \panelheight / 8.625 , yshift=0.3cm]panel.south west);
\draw [line width=0.7mm,black] ([xshift=0.5cm, yshift=0.3cm]panel.south west) -- ([xshift=0.5cm + \panelheight / 8.625, yshift=0.3cm]panel.south west);

\node (anchor) at ([shift={(0.0cm,-0.5cm)}]0.5,0 |- panel.south) {}; 
\node[graphicNode]  (panel) {\includegraphics[height=\panelheight]{content/images/fff_lamella1_view.png}};
% Title
\node[anchor=center,align=center] at ([shift={(0.0cm,0.3cm)}]panel.north) {Lamella$_\textrm{FFF}$ 1};
% scalebar - physical height is 8032.5 nm
\draw [line width=1.55mm,white] ([xshift=0.5cm, yshift=0.3cm]panel.south west) -- ([xshift=0.5cm + \panelheight / 8.0325 , yshift=0.3cm]panel.south west);
\draw [line width=0.7mm,black] ([xshift=0.5cm, yshift=0.3cm]panel.south west) -- ([xshift=0.5cm + \panelheight / 8.0325, yshift=0.3cm]panel.south west);
\node (anchor) at ([shift={(0.5cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode]  (panel) {\includegraphics[height=\panelheight]{content/images/fff_lamella2_view.png}};
% Title
\node[anchor=center,align=center] at ([shift={(0.0cm,0.3cm)}]panel.north) {Lamella$_\textrm{FFF}$ 2};
% scalebar - physical height is 10000.5 nm
\draw [line width=1.55mm,white] ([xshift=0.5cm, yshift=0.3cm]panel.south west) -- ([xshift=0.5cm + \panelheight / 10.0005 , yshift=0.3cm]panel.south west);
\draw [line width=0.7mm,black] ([xshift=0.5cm, yshift=0.3cm]panel.south west) -- ([xshift=0.5cm + \panelheight / 10.0005, yshift=0.3cm]panel.south west);
\node (anchor) at ([shift={(0.5cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode]  (panel) {\includegraphics[height=\panelheight]{content/images/fff_lamella3_view.png}};
% Title
\node[anchor=center,align=center] at ([shift={(0.0cm,0.3cm)}]panel.north) {Lamella$_\textrm{FFF}$ 3};
% scalebar - physical height is 9975 nm
\draw [line width=1.55mm,white] ([xshift=0.5cm, yshift=0.3cm]panel.south west) -- ([xshift=0.5cm + \panelheight / 9.975 , yshift=0.3cm]panel.south west);
\draw [line width=0.7mm,black] ([xshift=0.5cm, yshift=0.3cm]panel.south west) -- ([xshift=0.5cm + \panelheight / 9.975, yshift=0.3cm]panel.south west);
\node (anchor) at ([shift={(0.5cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode]  (panel) {\includegraphics[height=\panelheight]{content/images/fff_lamella4_view.png}};
% Title
\node[anchor=center,align=center] at ([shift={(0.0cm,0.3cm)}]panel.north) {Lamella$_\textrm{FFF}$ 4};
% scalebar - physical height is 9337.5 nm
\draw [line width=1.55mm,white] ([xshift=0.5cm, yshift=0.3cm]panel.south west) -- ([xshift=0.5cm + \panelheight / 9.3375 , yshift=0.3cm]panel.south west);
\draw [line width=0.7mm,black] ([xshift=0.5cm, yshift=0.3cm]panel.south west) -- ([xshift=0.5cm + \panelheight / 9.3375, yshift=0.3cm]panel.south west);

\node (anchor) at ([shift={(0.0cm,-1.0cm)}]0.5,0 |- panel.south) {}; 
\node[labelNode] {B};
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/images/euc_lamella1_assm.png}};
% Title
\node[anchor=center,align=center] at ([shift={(0.0cm,0.3cm)}]panel.north) {Lamella$_\textrm{EUC}$ 1: 909 tiles};
% scalebar - physical height is 12810 nm
\draw [line width=1.55mm,white] ([xshift=0.5cm, yshift=0.3cm]panel.south west) -- ([xshift=0.5cm + \panelheight / 12.81 , yshift=0.3cm]panel.south west);
\draw [line width=0.7mm,black] ([xshift=0.5cm, yshift=0.3cm]panel.south west) -- ([xshift=0.5cm + \panelheight / 12.81, yshift=0.3cm]panel.south west);
\node (anchor) at ([shift={(0.5cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/images/euc_lamella2_assm.png}};
% Title
\node[anchor=center,align=center] at ([shift={(0.0cm,0.3cm)}]panel.north) {Lamella$_\textrm{EUC}$ 2: 451 tiles};
% scalebar - physical height is 7027.5 nm
\draw [line width=1.55mm,white] ([xshift=0.5cm, yshift=0.3cm]panel.south west) -- ([xshift=0.5cm + \panelheight / 7.0275 , yshift=0.3cm]panel.south west);
\draw [line width=0.7mm,black] ([xshift=0.5cm, yshift=0.3cm]panel.south west) -- ([xshift=0.5cm + \panelheight / 7.0275, yshift=0.3cm]panel.south west);
\node (anchor) at ([shift={(0.5cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/images/euc_lamella3_assm.png}};
% Title
\node[anchor=center,align=center] at ([shift={(0.0cm,0.3cm)}]panel.north) {Lamella$_\textrm{EUC}$ 3: 513 tiles};
% scalebar - physical height is 9615 nm
\draw [line width=1.55mm,white] ([xshift=0.5cm, yshift=0.3cm]panel.south west) -- ([xshift=0.5cm + \panelheight / 9.615 , yshift=0.3cm]panel.south west);
\draw [line width=0.7mm,black] ([xshift=0.5cm, yshift=0.3cm]panel.south west) -- ([xshift=0.5cm + \panelheight / 9.615, yshift=0.3cm]panel.south west);
\node (anchor) at ([shift={(0.5cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode] (panel) {\includegraphics[height=\panelheight]{content/images/euc_lamella4_assm.png}};
% Title
\node[anchor=center,align=center] at ([shift={(0.0cm,0.3cm)}]panel.north) {Lamella$_\textrm{EUC}$ 4: 497 tiles};
% scalebar - physical height is 8625 nm
\draw [line width=1.55mm,white] ([xshift=0.5cm, yshift=0.3cm]panel.south west) -- ([xshift=0.5cm + \panelheight / 8.625 , yshift=0.3cm]panel.south west);
\draw [line width=0.7mm,black] ([xshift=0.5cm, yshift=0.3cm]panel.south west) -- ([xshift=0.5cm + \panelheight / 8.625, yshift=0.3cm]panel.south west);

\node (anchor) at ([shift={(0.0cm,-0.5cm)}]0.5,0 |- panel.south) {}; 
\node[graphicNode]  (panel) {\includegraphics[height=\panelheight]{content/images/fff_lamella1_assm.png}};
% Title
\node[anchor=center,align=center] at ([shift={(0.0cm,0.3cm)}]panel.north) {Lamella$_\textrm{FFF}$ 1: 438 tiles};
% scalebar - physical height is 10000.5 nm
\draw [line width=1.55mm,white] ([xshift=0.5cm, yshift=0.3cm]panel.south west) -- ([xshift=0.5cm + \panelheight / 10.0005 , yshift=0.3cm]panel.south west);
\draw [line width=0.7mm,black] ([xshift=0.5cm, yshift=0.3cm]panel.south west) -- ([xshift=0.5cm + \panelheight / 10.0005, yshift=0.3cm]panel.south west);
\node (anchor) at ([shift={(0.5cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode]  (panel) {\includegraphics[height=\panelheight]{content/images/fff_lamella2_assm.png}};
% Title
\node[anchor=center,align=center] at ([shift={(0.0cm,0.3cm)}]panel.north) {Lamella$_\textrm{FFF}$ 2: 474 tiles};
% scalebar - physical height is 10000.5 nm
\draw [line width=1.55mm,white] ([xshift=0.5cm, yshift=0.3cm]panel.south west) -- ([xshift=0.5cm + \panelheight / 10.0005 , yshift=0.3cm]panel.south west);
\draw [line width=0.7mm,black] ([xshift=0.5cm, yshift=0.3cm]panel.south west) -- ([xshift=0.5cm + \panelheight / 10.0005, yshift=0.3cm]panel.south west);
\node (anchor) at ([shift={(0.5cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode]  (panel) {\includegraphics[height=\panelheight]{content/images/fff_lamella3_assm.png}};
% Title
\node[anchor=center,align=center] at ([shift={(0.0cm,0.3cm)}]panel.north) {Lamella$_\textrm{FFF}$ 3: 501 tiles};
% scalebar - physical height is 9975 nm
\draw [line width=1.55mm,white] ([xshift=0.5cm, yshift=0.3cm]panel.south west) -- ([xshift=0.5cm + \panelheight / 9.975 , yshift=0.3cm]panel.south west);
\draw [line width=0.7mm,black] ([xshift=0.5cm, yshift=0.3cm]panel.south west) -- ([xshift=0.5cm + \panelheight / 9.975, yshift=0.3cm]panel.south west);
\node (anchor) at ([shift={(0.5cm,0.0cm)}]panel.north east) {}; 
\node[graphicNode]  (panel) {\includegraphics[height=\panelheight]{content/images/fff_lamella4_assm.png}};
% Title
\node[anchor=center,align=center] at ([shift={(0.0cm,0.3cm)}]panel.north) {Lamella$_\textrm{FFF}$ 4: 425 tiles};
% scalebar - physical height is 9337.5 nm
\draw [line width=1.55mm,white] ([xshift=0.5cm, yshift=0.3cm]panel.south west) -- ([xshift=0.5cm + \panelheight / 9.3375 , yshift=0.3cm]panel.south west);
\draw [line width=0.7mm,black] ([xshift=0.5cm, yshift=0.3cm]panel.south west) -- ([xshift=0.5cm + \panelheight / 9.3375, yshift=0.3cm]panel.south west);


\newlength{\padding}
\setlength{\padding}{0.2cm}
\node (anchor) at ([shift={(0.0cm,-1.0cm)}]0.5,0 |- panel.south) {}; 
\node[labelNode] {C};
\node[graphicNode] (panel) {\includegraphics[height=0.75\panelheight]{content/images/granules/zap004.png}};
\node (anchor) at ([shift={(\padding,0.0cm)}]panel.north east) {}; 
\node[graphicNode] (panel) {\includegraphics[height=0.75\panelheight]{content/images/granules/zap012.png}};
\node (anchor) at ([shift={(\padding,0.0cm)}]panel.north east) {}; 
\node[graphicNode] (panel) {\includegraphics[height=0.75\panelheight]{content/images/granules/zap015.png}};
\node (anchor) at ([shift={(\padding,0.0cm)}]panel.north east) {}; 
\node[graphicNode] (panel) {\includegraphics[height=0.75\panelheight]{content/images/granules/zap020.png}};
\node (anchor) at ([shift={(\padding,0.0cm)}]panel.north east) {}; 
\node[graphicNode] (panel) {\includegraphics[height=0.75\panelheight]{content/images/granules/zap006.png}};

\node (anchor) at ([shift={(0.0cm,-\padding)}]0.5,0 |- panel.south) {}; 
\node[graphicNode]  (panel) {\includegraphics[height=0.75\panelheight]{content/images/granules/zap021.png}};
\node (anchor) at ([shift={(\padding,0.0cm)}]panel.north east) {}; 
\node[graphicNode]  (panel) {\includegraphics[height=0.75\panelheight]{content/images/granules/zap022.png}};
\node (anchor) at ([shift={(\padding,0.0cm)}]panel.north east) {}; 
\node[graphicNode]  (panel) {\includegraphics[height=0.75\panelheight]{content/images/granules/zap027.png}};
\node (anchor) at ([shift={(\padding,0.0cm)}]panel.north east) {}; 
\node[graphicNode]  (panel) {\includegraphics[height=0.75\panelheight]{content/images/granules/zap029.png}};
\node (anchor) at ([shift={(\padding,0.0cm)}]panel.north east) {}; 
\node[graphicNode]  (panel) {\includegraphics[height=0.75\panelheight]{content/images/granules/zap023.png}};
% scalebar - physical height is 375 nm
\draw [line width=1.55mm,white] ([xshift=0.5cm, yshift=0.3cm]panel.south west) -- ([xshift=0.5cm + 0.75\panelheight / 3.75 , yshift=0.3cm]panel.south west);
\draw [line width=0.7mm,black] ([xshift=0.5cm, yshift=0.3cm]panel.south west) -- ([xshift=0.5cm + 0.75\panelheight / 3.75, yshift=0.3cm]panel.south west);



```





![Statistics of 2DTM on lamella imaged using DeCo-LACE (A) Number of detected targets in
each lamella (B) Distribution of targets per tile in each lamella. Only tiles
with two or more detected targets were included (C) Distribution of SNRs in each lamella
(D) For each lamella an average of all tiles is shown. Overlaid is a scatterplot
of all detected targets in these tiles according to their in-tile coordinates.
Scatterplot is colored according to the 2DTM SNR. There are no detected targets in the top
circle-circle intersection due to radiation damage from previous exposures. (E) 2D histogram of number of detected targets as a function of beam-image shift (F) Mean 2DTM SNR as a function of beam-image shift](tikz:matching_stat){#fig:matching_stat}

```{.tikz-figure #matching_stat width=15cm height=3cm draft=false}


\node (anchor) at (0.5,2.5) {}; 
\node[labelNode] {A};
\node[graphicNode] (panel) {\includegraphics[width=4.5cm]{content/code/img/num_matches_plot.png}};
\node (anchor) at ([shift={(0.5cm,0.0)}]panel.north east) {}; 
\node[labelNode] {B};
\node[graphicNode] (panel) {\includegraphics[width=4.5cm]{content/code/img/matches_per_tile_plot.png}};
\node (anchor) at ([shift={(0.5cm,0.0)}]panel.north east) {}; 
\node[labelNode] {C};
\node[graphicNode] (panel) {\includegraphics[width=4.5cm]{content/code/img/scores_plot.png}};
\node (anchor) at ([shift={(0.0cm,-0.2)}]0.5,2.5 |- panel.south east) {}; 
\node[labelNode] {D};
\node[graphicNode] (panel) {\includegraphics[width=14cm]{content/code/img/micrograph_with_matches.png}};

\node (anchor) at ([shift={(0.0cm,-0.2)}]0.5,2.5 |- panel.south east) {}; 
\node[labelNode] {E};
\node[graphicNode] (panel) {\includegraphics[width=6cm]{content/code/img/num_matches_vs_bis.png}};

\node (anchor) at ([shift={(1.0cm,0.0)}]panel.north east) {}; 
\node[labelNode] {F};
\node[graphicNode] {\includegraphics[width=6cm]{content/code/img/snrs_vs_bis.png}};

```


![Template matching in lamella imaged using the DeCo-Lace approach at eucentric
focus (A) Montage of Lamella$_\textrm{EUC}$ 1 overlaid with detected targets according to
their montage coordinates colored in orange. Scalebar corresponds to 1 μm. (B) Side view of detected targets in the lamella, such that the
direction of the electron beam is horizontal. (C-F) Magnified area of panel A
showing rough ER with associated ribosomes(C), outer nuclear membrane with
associated ribosomes (D), ribsomes arranged in a circular fashion(E), ribosomes
enclosed in a less electron dense inclusion in a granule(F). Ribosomes are colored in white with the surface of the peptide exit tunnel colored in green and the A, P, and E sites colored in blue, purple, and red, respectively.Scalebar corresponds to 100 nm.](tikz:matching_euc){#fig:matching_euc}

```{.tikz-figure #matching_euc width=17cm height=10cm draft=false}
\newlength{\panelheight}
\setlength{\panelheight}{12cm}

\node (anchor) at (0.5,9.5) {}; 
\node[labelNode] {A};
\node[graphicNode] (assm) {\includegraphics[height=\panelheight]{content/images/euc_lamella1_assm.png}};
\node[graphicNode] {\includegraphics[height=\panelheight]{content/images/euc_lamella1.png}};
\node (rect) at (7.4,3.5) [anchor=center,draw,thick,minimum width=0.3cm,minimum height=0.3cm,color=red] {};
\node (rect) at (1.75,4.5) [anchor=center,draw,thick,minimum width=0.3cm,minimum height=0.3cm,color=green] {};
\node (rect) at (7.2,2.15) [anchor=center,draw,thick,minimum width=0.3cm,minimum height=0.3cm,color=blue!60] {};
\node (rect) at (6.45,6.0) [anchor=center,draw,thick,minimum width=0.47cm,minimum height=0.47cm,color=cyan] {};
% scalebar - physical height is 12810 nm
\draw [line width=1.55mm,white] ([xshift=0.5cm, yshift=0.3cm]assm.south west) -- ([xshift=0.5cm + \panelheight / 12.81 , yshift=0.3cm]assm.south west);
\draw [line width=0.7mm,black] ([xshift=0.5cm, yshift=0.3cm]assm.south west) -- ([xshift=0.5cm + \panelheight / 12.81, yshift=0.3cm]assm.south west);


\node (anchor) at (11.0,9.5) {}; 
\node[labelNode] {B};
\node[anchor=north west, below right=0cm and 0.0cm of anchor] (side) {\includegraphics[height=12cm, trim=20.5cm 0 2cm 0]{content/images/euc_lamella1_side.png}};

\draw [->, thick] ($ (assm.east) + (0.1,0) $) -- node[above=0.2cm, align=center] (c) {} ($ (side.west) + (0.2,0) $);

\centerarc [canvas is zx plane at y=0.75, ->](c.center)(-90:180:0.15);
\draw [very thick] ($ (c.center) + (0,-0.1) $) -- ($ (c.center) + (0,0.2) $);
\node at ($ (c.center) + (0.5,0) $) {90°};

\newlength{\panelheightm}
\setlength{\panelheightm}{2.8cm}
\node (anchor) at (13.0,9.5) {}; 
\node[labelNode] {C};
\node[graphicNode] (pan) {\includegraphics[height=\panelheightm]{content/images/euc_lamella1_detail1.png}};
\node (n3) [box=red, fit=(pan)] {};
% scalebar - physical height is 300 nm
\draw [line width=1.55mm,white] ([xshift=0.2cm, yshift=0.2cm]pan.south west) -- ([xshift=0.2cm + \panelheightm / 3 , yshift=0.2cm]pan.south west);
\draw [line width=0.7mm,black] ([xshift=0.2cm, yshift=0.2cm]pan.south west) -- ([xshift=0.2cm + \panelheightm / 3, yshift=0.2cm]pan.south west);

\node (anchor) at (13.0,6.5) {}; 
\node[labelNode] {D};
\node[graphicNode] (pan) {\includegraphics[height=\panelheightm]{content/images/euc_lamella1_detail2.png}};
\node (n3) [box=green, fit=(pan)] {};

% scalebar - physical height is 300 nm
\draw [line width=1.55mm,white] ([xshift=0.2cm, yshift=0.2cm]pan.south west) -- ([xshift=0.2cm + \panelheightm / 3 , yshift=0.2cm]pan.south west);
\draw [line width=0.7mm,black] ([xshift=0.2cm, yshift=0.2cm]pan.south west) -- ([xshift=0.2cm + \panelheightm / 3, yshift=0.2cm]pan.south west);

\node (anchor) at (13.,3.5) {}; 
\node[labelNode] {E};
\node[graphicNode] (pan) {\includegraphics[height=\panelheightm]{content/images/euc_lamella1_detail3.png}};
\node (n3) [box=blue!60, fit=(pan)] {};

% scalebar - physical height is 300 nm
\draw [line width=1.55mm,white] ([xshift=0.2cm, yshift=0.2cm]pan.south west) -- ([xshift=0.2cm + \panelheightm / 3 , yshift=0.2cm]pan.south west);
\draw [line width=0.7mm,black] ([xshift=0.2cm, yshift=0.2cm]pan.south west) -- ([xshift=0.2cm + \panelheightm / 3, yshift=0.2cm]pan.south west);

\node (anchor) at (13.0,0.5) {}; 
\node[labelNode] {F};
\node[graphicNode] (pan) {\includegraphics[height=\panelheightm]{content/images/euc_lamella1_detail4.png}};
\node (n3) [box=cyan, fit=(pan)] {};

% scalebar - physical height is 500 nm
\draw [line width=1.55mm,white] ([xshift=0.2cm, yshift=0.2cm]pan.south west) -- ([xshift=0.2cm + \panelheightm / 5 , yshift=0.2cm]pan.south west);
\draw [line width=0.7mm,black] ([xshift=0.2cm, yshift=0.2cm]pan.south west) -- ([xshift=0.2cm + \panelheightm / 5, yshift=0.2cm]pan.south west);

```


![Template matching in lamella imaged using the DeCo-Lace approach at fringe-free
focus (A) Montage of Lamella$_\textrm{FFF}$ 4 overlaid with detected targets according to
their montage coordinates colored in orange. Scalebar corresponds to 1 μm. (B) Side view of detected targets in the lamella, such that the
direction of the electron beam is horizontal. (C-E) Magnified area of panel A
showing rough ER with associated ribosomes(C) and ribosomes
enclosed in a less electron dense inclusion in a granule(D,E). (F) Side view of
panel E. Ribosomes are colored in white with the surface of the peptide exit tunnel colored in green and the A, P, and E sites colored in blue, purple, and red, respectively. Scalebar corresponds to 100 nm.](tikz:matching_fff){#fig:matching_fff}

```{.tikz-figure #matching_fff width=17cm height=10cm draft=false}

\newlength{\panelheight}
\setlength{\panelheight}{12cm}

\node (anchor) at (0.5,9.5) {}; 
\node[labelNode] {A};
\node[graphicNode] (assm) {\includegraphics[height=\panelheight]{content/images/fff_lamella4_assm.png}};
\node[graphicNode] {\includegraphics[height=\panelheight]{content/images/fff_lamella4.png}};
\node (rect) at (5.35,5.5) [anchor=center,draw,thick,minimum width=0.4cm,minimum height=0.4cm,color=red] {};
\node (rect) at (8.05,1.75) [anchor=center,draw,thick,minimum width=0.6cm,minimum height=0.6cm,color=green] {};
\node (rect) at (6.45,-1.23) [anchor=center,draw,thick,minimum width=0.5cm,minimum height=0.5cm,color=blue!60] {};
% scalebar - physical height is 9337.5nm
\draw [line width=1.55mm,white] ([xshift=0.5cm, yshift=0.3cm]assm.south west) -- ([xshift=0.5cm + \panelheight / 9.3375 , yshift=0.3cm]assm.south west);
\draw [line width=0.7mm,black] ([xshift=0.5cm, yshift=0.3cm]assm.south west) -- ([xshift=0.5cm + \panelheight / 9.3375, yshift=0.3cm]assm.south west);

\node (anchor) at (11.0,9.5) {}; 
\node[labelNode] {B};
\node[anchor=north west, below right=0cm and 0.0cm of anchor] (side) {\includegraphics[height=12cm, trim=15.5cm 0 2cm 0]{content/images/fff_lamella4_side.png}};

\draw [->, thick] ($ (assm.east) + (0.1,0) $) -- node[above=0.2cm, align=center] (c) {} ($ (side.west) + (0.2,0) $);

\centerarc [canvas is zx plane at y=0.75, ->](c.center)(-90:180:0.15);
\draw [very thick] ($ (c.center) + (0,-0.1) $) -- ($ (c.center) + (0,0.2) $);
\node at ($ (c.center) + (0.5,0) $) {90°};

\newlength{\panelheightm}
\setlength{\panelheightm}{2.8cm}
\node (anchor) at (13.0,9.5) {}; 
\node[labelNode] {C};
\node[graphicNode] (pan) {\includegraphics[height=2.8cm]{content/images/fff_lamella4_detail2.png}};
\node (n3) [box=red, fit=(pan)] {};
% scalebar - physical height is 300 nm
\draw [line width=1.55mm,white] ([xshift=0.2cm, yshift=0.2cm]pan.south west) -- ([xshift=0.2cm + \panelheightm / 3 , yshift=0.2cm]pan.south west);
\draw [line width=0.7mm,black] ([xshift=0.2cm, yshift=0.2cm]pan.south west) -- ([xshift=0.2cm + \panelheightm / 3, yshift=0.2cm]pan.south west);

\node (anchor) at (13.0,6.5) {}; 
\node[labelNode] {D};
\node[graphicNode] (pan) {\includegraphics[height=2.8cm]{content/images/fff_lamella4_detail1.png}};
\node (n3) [box=green, fit=(pan)] {};
% scalebar - physical height is 500 nm
\draw [line width=1.55mm,white] ([xshift=0.2cm, yshift=0.2cm]pan.south west) -- ([xshift=0.2cm + \panelheightm / 5 , yshift=0.2cm]pan.south west);
\draw [line width=0.7mm,black] ([xshift=0.2cm, yshift=0.2cm]pan.south west) -- ([xshift=0.2cm + \panelheightm / 5, yshift=0.2cm]pan.south west);

\node (anchor) at (13.0,3.5) {}; 
\node[labelNode] {E};
\node[graphicNode] (pan){\includegraphics[height=2.8cm]{content/images/fff_lamella4_detail3_back.png}};
\node[graphicNode] {\includegraphics[height=2.8cm]{content/images/fff_lamella4_detail3_close.png}};
\node[graphicNode] {\includegraphics[height=2.8cm]{content/images/fff_lamella4_detail3_far.png}};
\node (n3) [box=blue!60, fit=(pan)] {};
% scalebar - physical height is 400 nm
\draw [line width=1.55mm,white] ([xshift=0.2cm, yshift=0.2cm]pan.south west) -- ([xshift=0.2cm + \panelheightm / 4 , yshift=0.2cm]pan.south west);
\draw [line width=0.7mm,black] ([xshift=0.2cm, yshift=0.2cm]pan.south west) -- ([xshift=0.2cm + \panelheightm / 4, yshift=0.2cm]pan.south west);

\node (anchor) at (13,0.5) {}; 
\node[labelNode] {F};
\node[graphicNode] {\includegraphics[height=2.8cm]{content/images/fff_lamella4_detail3_far_side.png}};
\node[graphicNode] {\includegraphics[height=2.8cm]{content/images/fff_lamella4_detail3_close_side.png}};

```

## References {.page_break_before}

<!-- Explicitly insert bibliography here -->
<div id="refs"></div>
