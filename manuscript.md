---
title: Visual proteomics using whole-lamella 2D template matching
keywords:
- cryo-EM
- visual protemics
- ribosome
lang: en-US
date-meta: '2022-03-29'
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
  <meta name="dc.date" content="2022-03-29" />
  <meta name="citation_publication_date" content="2022-03-29" />
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
  <link rel="alternate" type="text/html" href="https://jojoelfe.github.io/deco_lace_template_matching_manuscript/v/0a724b0da1586e2992e709189796c245a3f07ccf/" />
  <meta name="manubot_html_url_versioned" content="https://jojoelfe.github.io/deco_lace_template_matching_manuscript/v/0a724b0da1586e2992e709189796c245a3f07ccf/" />
  <meta name="manubot_pdf_url_versioned" content="https://jojoelfe.github.io/deco_lace_template_matching_manuscript/v/0a724b0da1586e2992e709189796c245a3f07ccf/manuscript.pdf" />
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
([permalink](https://jojoelfe.github.io/deco_lace_template_matching_manuscript/v/0a724b0da1586e2992e709189796c245a3f07ccf/))
was automatically generated
from [jojoelfe/deco_lace_template_matching_manuscript@0a724b0](https://github.com/jojoelfe/deco_lace_template_matching_manuscript/tree/0a724b0da1586e2992e709189796c245a3f07ccf)
on March 29, 2022.
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

ER-HoxA9 cells were maintained in RPMI supplemented with 10% FBS,
penicillin/streptomycin, SCF, and estrogen [@doi:10.1016/j.cell.2016.08.057] at
37C and 5% CO2. 120h prior to grid freezing cells were washed twice in PBS and
cultured in the same medium, except without estrogen. Differentiation was
verified by staining with Hoechst-dye and insepction of nuclear morphology.
Cells were then counted and diluted to 1^106 cells/ml. Grids ( either 200 mesh
copper grids, with a sillicone-oxide and 2um holes with a 2um spacing or 200
mesh gold grids with a thin gold film and 2 um holes in 2um sapcing) were
glow-discharged from both sides using a ... for ... . 3.5 ul of cells suspension
was added to grids on the thin-film side and grids were automatically blotted
from the back-side using a GP2 cryoplunger (Leica) for ... s and rapidly plunged
into liquid ethane at -185C. 

### FIB-milling

Grids were loaded into a Acquilos 2 FIB/SEM  microscope with a stage cooled to
-190C. Grids were sputter-coated with platinum for 15s at 45 mA and then coated
with a layer of platinum-precursor by openin the GIS-valve for 45s. An overview
of the grid was created by montaging SEM images and isolated cells at the center
of gridsquares were selected for FB-milling. Lamella were generated
automatically using the AutoTEM software, resulting in 6-8 um wide lamella with
150-200 um thickness as determined by FIB-imaging of the lamella edge.

### Data collection

Grids were loaded into a Krios Titam TEM operated at 300 keV. The microscope was
setup with a cross-grating grid on the stageby setting the beam-diameter to 900
nm, resulting in the beam being completely visible in the camera. To establish
fringe-free conditions, the "Fine eucentric" procedure of serialEM was used to
move a square of the cross-grating grid to the eucentric position of the
microscope. The effective defocus was then set to 2 um, using the "autofocus"
routine of serialEM. The objective focus of the microscope was changed until no
fringes were visible. The stage was then moved in Z until images had a apparent
defocus of 2 um. The differnce in stage Z-position between the eucentric and
fringe-free conditions was calculate d and noted to move other areas into
fringe-free condition.

Low magnification montages were used to find lamella and lamella that were
sufficiently thin and free of contamination were selected for automated data
collection. The corners of the lamella were manually annotated in SerialEM and
translated into Beam-Imageshift values using SerialEm calibration. A hexagonal
patter of beam-imageshift positions was calculated that covered the area between
he four corners in a serpentine way, with a sqrt(3) * 400 nm horizontal spacing
and 800 nm vertical spacing. Exposures were then taking at each position with a
30 e/A total dose. After each exposure that defocus was estimated using the
ctffind function of SerialEM and the focus for th next exposure was corrected by
the difference between the estimated focus and the desired defocus of 800 um.
Also after each exposure the deviation of the beam from the center of the camera
was measured and corrected using the "CenterBeamFrom IMage" command of SerialEM.

After datacollection a 20s exposure at 2250x magnification of the lamella at
200um defocus was taken for visualization purposes.

### Data pre-processing

Movies were gain-corrected and motion-corrected using a custom version of
unblur. To avoid influence of the beam-edge on motion-correction only a quarter
of the movie in the center of the camera was considered for calculation of the
estimated motion. After movie frames were aligned and summed a mask for the
illuminated area was calculated by lowpass filtering the image at ... A,
thresholding the image at 10% of the maximal value and then lowpass filtering
the mask at ... A. This mask was then used to replace un-illuminated area with
gaussian noise, with the same mean and standard deviation as the illuminated
area. The contrast-transfer function (CTF) was estimated using ctffind, searching
between 0.02 and 2 um defocus. 

### Template matching

The search template was generated from the cryo-EM structure of the mouse large
ribosomal subunit (PDB 6SWA). The ... subunit was deleted from the model and the
simulate program of the cisTEM suite was used to calculate an density map from
the atomic coordinates. The match_template program was used to search for this
template in the preprocessed images, using 1.5 deg angular step in out-of-plane
angles and 1.0 deg in-plane. 21 defocus planes in 200nm steps centered around
the defocus estimates by ctffind were searches. Matches were defined as peaks
above a threshold calulated according to .. .(7.75 for most images).

### Data analysis


## Results

### 2DTM detects large ribosomal subunits in cryo-FIB lamella of mammalian cells

To test whether we could detect individual ribosomes in mammalian cells we
prepared cryo-lamella of mouse neutrophil-like cells. Low-magnification images
of these lamellas clearly shows cellular features consistent with a
neutrophil-like phenotype, mainly a segmented nucleus and a plethora of
membrane-organelles, corresponding to the granules and secretory vesicles of
neutrophils (Fig. {@fig:initmatching}A). We then proceeded to acquire
micrographs on this lamella with a defocus of 0.5-1.0 um, 30 e/A2/s exposure and
1.5 A pixelsize. We manually selected multiple locations in the lamella and
focused using standard low-dose techniques where  focusing is performed on a sacrificial area. The resulting micrographs showed no signs of
crystalline ice and had Thon-rings to  resolution, indicating successful
vitrification. 

We used an atomic model of the 60S mouse ribosomal subunit  (6SWA) for 2D
template matching. In a subset of images the distribution of cross-correlation
scores significantly exceeded the distribution expected from non-signifcant
matching. In the resulting scaled maximum-intensity maps, clear peaks
with SNR thresholds up to 10 were apparent (Fig. {@fig:initmatching2}A). By
using the criterion described by for thresholding potential matches we found
that in images of cytosolic compartments we found evidence of 10-500 ribosomes in
the imaged areas. Notably we found no matches in images that were taken in the
nuclear compartment. In the cytosolic areas we found a drastically different
number of matches, In some areas we found only ~ 50 matches er image area, while
 in another area we found more than 500 matches . This ten-fold difference in
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
area.

To ensure that every electron exposing the sample was captured by the detector,
we focused the electron beam so that the entire beam was placed on the detector.
During canonical low-dose imaging the microscope is configured so that the focal
plan is identical to the eucentric plane of the specimen stage. This leaves the
C2 aperture out of focus, resulting in ripples at the edge of the beam (Figure
2B). While these ripples are low-resolution features that might not interfere
with 2D template matching, which is designed to be robust to low-resolution
noise, we also tested collecting data under a condition where the C2 aperture is
in focus (Figure 2C). 

We then centered a lamella under the electron beam and used beam-image shift of
the microscope to systematically raster the whole surface of the lamella in a
hexagonal pattern. Instead of focusing in a sacrificial area, we determined the
defocus after every exposure using a routine implemented in SerialEM modeled
after CTFFind. The focus was then adjusted based on the difference between
desired and measured defocus. Since we used a serpentine pattern for data
collection every exposure is close to the previous exposure making drastic
changes in the defocus unlikely. Furthermore we started our acquisition pattern
on the platinum deposition edge, so the initial exposure where the defocus was
not yet adjusted did not contain any biologically relevant information. 

We used this strategy to collect data on 8 lamella, 4 using the eucentric focus
condition and 4 using the fringe-free condition. We were able to highly
consistently collect data with a defocus of 8 um (Figure 2D), both in the
eucentric focus and fringe-free focus condition. Together with the nominal
defocus of the microscope this data results in a topological map of the lamella.
To ensure that data was collected consistently, we mapped defocus values as a
function of the applied Beam-image shift (Figure 2E). This demonstrated that the
defocus was consistent over the lamella, with outliers only at isolated images
and in images containing contamination. We also plotted the measure objective
astigmatism of the lamella and found that it varies with the applied Beam-image
shift, become more astigmatic mostly due to beam-image shift in the X
direction. While approaches exist to correct this during the data-collection, we
opted to not use these mechanism for these early experiments and instead rely on
computational correction of these aberrations in order to characterize them. 

### 2D-Template matching of cryo-EMILIA data reveals ribosome distribution 

We developed customized preprocessing protocol to images obtained by cryo-EMILIA
to enable their use for 2D-template matching. First we restricted calculation of
cross-correlation coefficients between individual movie frames to the central
portion of the image to prevent artifacts from the beam edges on estimation of
motion. Then we calculated a mask that defined the illuminated area of the
micrographs and used it to fill non-illumated areas with gaussian noise,
matching mean and standard deviation to the illuminated signal (Figure 3A). The
so processed images were suitable for 2D-template matching and we were able to
obtained matches with the same model used for the data in Figure 1.

### Quantitative analysis of translation activity


## Discussion


- Elizabeth Wright and Grant Jensen Montage tomography papers

- Waffle method for higher throughput, automation of fib-milling

- Throughput and bottlenecks

- Visual proteomics

- Granules containing ribosomes?

- Threshold implications (no matches on most images)

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

![Maximum intensity projection cross-correlation map of micrograph shown in Figure {@fig:initmatching}](tikz:initmatching2){#fig:initmatching2 tag="S1"}

```{.tikz-figure #initmatching2 width=13cm height=9cm draft=false}
\node (anchor) at (0.5,8.35) {}; 
\node[labelNode] {A};
\node[graphicNode] {\includegraphics[width=12cm]{content/code/img/initial_map_match.pdf}};
\iftoggle{draft}{\node [redAnchorNode] {};};

```





![DeCo-LACE approach (A) Graphic demonstrating the data-collection strategy for DeCo-LACE](tikz:approach){#fig:approach}

```{.tikz-figure #approach width=20cm height=15cm draft=false}
\node (anchor) at (0.5,14.35) {}; 
\node[labelNode] {A};
\node[graphicNode] {\includegraphics[width=5cm]{content/graphics/approach/approach.png}};
\draw [densely dotted, red,thick] (3,14.5) -- (3,10);
\draw [densely dotted, red,thick] (3,9.2) -- (3,6.4);

\tikzset{dimen/.style={<->,>=latex,thin,every rectangle node/.style={above right=0.2cm and -0.3cm,fill=white,midway,font=\sffamily}}}

\draw (3.55,10.4) -- ++(0,1.5) coordinate (D1) -- +(0,5pt);
\draw (4.15,10.4) -- ++(0,1.5) coordinate (D2) -- +(0,5pt);
\draw [dimen] (D1) -- (D2) node {$D_{Beam}$};

\draw [->, very thick] (3,10) -- ++(0.5,-0.2)  coordinate (S1) node[midway,below left] {$IS_X$} ;
\draw [->, very thick] (S1) -- (3.85,10.4) node[midway,below right] {$IS_Y$};



\node (anchor) at (6.0,14.35) {}; 
\node[labelNode] {B};

% Place nodes
\node [block] (init) at (8.0,13.35) {\textbf{START} \\ Collect overview image};
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

\node (anchor) at (11.5,14.35) {}; 
\node[labelNode] {C};
\node[graphicNode] {\includegraphics[width=8cm]{content/images/ac_strategy.png}};
\iftoggle{draft}{\node [redAnchorNode] {};};


\node (anchor) at (0.5,4.5) {}; 
\node[labelNode] {C};
\node[graphicNode] (euc) {\includegraphics[height=4.0cm]{content/images/fringebeam.png}};
\node[above = 0cm and 0cm of euc.north] {Eucentric Focus};

\iftoggle{draft}{\node [redAnchorNode] {};};


\node (anchor) at (5.5,4.5) {}; 
\node[labelNode] {D};
\node[graphicNode] (fff) {\includegraphics[height=4.0cm]{content/images/nofringebeam.png}};
\node[above = 0cm and 0cm of fff.north] {Fringe-free Focus};
\iftoggle{draft}{\node [redAnchorNode] {};};

\node (anchor) at (10.5,4.5) {}; 
\node[labelNode] {E};
\node[anchor=north west, below right=-0.5cm and 0cm of anchor] {\includegraphics[height=4.8cm]{content/code/img/defocusplot.pdf}};
\iftoggle{draft}{\node [redAnchorNode] {};};

```


![This is an example-figurern](tikz:lamella_spatial_info){#fig:lamella_spatial_info}

```{.tikz-figure #lamella_spatial_info width=16.5cm height=9cm draft=false}
\node (anchor) at (0.5,8.35) {}; 
\node[labelNode] {A};
\node[graphicNode] {\includegraphics[width=7.5cm]{content/code/img/defocus_defocus_vs_bs_plot.pdf}};
\iftoggle{draft}{\node [redAnchorNode] {};};

\node (anchor) at (0.5,4.35) {}; 
\node[labelNode] {B};
\node[graphicNode] {\includegraphics[width=7.5cm]{content/code/img/defocus_astigmatism_vs_bs_plot.pdf}};
\iftoggle{draft}{\node [redAnchorNode] {};};

\node (anchor) at (8.5,8.35) {}; 
\node[labelNode] {C};
\node[graphicNode] {\includegraphics[width=7.5cm]{content/code/img/defocus_angle_vs_bs_plot.pdf}};
\iftoggle{draft}{\node [redAnchorNode] {};};

```


![This is an example-figurern](tikz:example-figure3){#fig:approach3}

```{.tikz-figure #example-figure3 width=16.5cm height=9cm draft=false}
\node (anchor) at (0.5,8.35) {}; 
\node[labelNode] {A};
\node[graphicNode] {\includegraphics[width=7.5cm]{content/code/img/movement_vs_bs_plot.pdf}};
\iftoggle{draft}{\node [redAnchorNode] {};};


\node (anchor) at (8.5,8.35) {}; 
\node[labelNode] {B};
\node[graphicNode] {\includegraphics[width=7.5cm]{content/code/img/thickness_by_intensity_vs_bs_plot.pdf}};
\iftoggle{draft}{\node [redAnchorNode] {};};

```



![This is an example-figurern](tikz:example-figure4){#fig:approach4}

```{.tikz-figure #example-figure4 width=20cm height=13cm draft=false}
\node (anchor) at (0.5,12.35) {}; 
\node[labelNode] {A};
\node[graphicNode] {\includegraphics[height=5.2cm]{content/images/slicer000.png}};
\iftoggle{draft}{\node [redAnchorNode] {};};
\node (anchor) at (6.5,12.35) {}; 
\node[labelNode] {B};
\node[graphicNode] {\includegraphics[height=5.2cm]{content/images/slicer001.png}};
\iftoggle{draft}{\node [redAnchorNode] {};};
\node (anchor) at (11,12.35) {}; 
\node[labelNode] {C};
\node[graphicNode] {\includegraphics[height=5.2cm]{content/images/slicer002.png}};
\iftoggle{draft}{\node [redAnchorNode] {};};
\node (anchor) at (15.5,12.35) {}; 
\node[labelNode] {D};
\node[graphicNode] {\includegraphics[height=5.2cm]{content/images/slicer003.png}};
\iftoggle{draft}{\node [redAnchorNode] {};};

\node (anchor) at (0.5,6.5) {}; 
\node[labelNode] {E};
\node[graphicNode] {\includegraphics[height=5.2cm]{content/images/slicer005.png}};
\iftoggle{draft}{\node [redAnchorNode] {};};
\node (anchor) at (5,6.5) {}; 
\node[labelNode] {F};
\node[graphicNode] {\includegraphics[height=5.2cm]{content/images/slicer006.png}};
\iftoggle{draft}{\node [redAnchorNode] {};};
\node (anchor) at (9.5,6.5) {}; 
\node[labelNode] {G};
\node[graphicNode] {\includegraphics[height=5.2cm]{content/images/slicer007.png}};
\iftoggle{draft}{\node [redAnchorNode] {};};
\node (anchor) at (14.5,6.5) {}; 
\node[labelNode] {H};
\node[graphicNode] {\includegraphics[height=5.2cm]{content/images/slicer008.png}};
\iftoggle{draft}{\node [redAnchorNode] {};};

```

![This is an example-figurern](tikz:matching){#fig:matching}

```{.tikz-figure #matching width=16cm height=13cm draft=false}
\node (anchor) at (0.5,9.35) {}; 
\node[labelNode] {A};
\node[graphicNode] {\includegraphics[width=7.5cm]{content/images/screenie.png}};
\iftoggle{draft}{\node [redAnchorNode] {};};



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