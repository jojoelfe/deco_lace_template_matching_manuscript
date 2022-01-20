---
title: Visual proteomics using whole-lamella 2D template matching
keywords:
- cryo-EM
- visual protemics
- ribosome
lang: en-US
date-meta: '2022-01-20'
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
  <meta name="dc.date" content="2022-01-20" />
  <meta name="citation_publication_date" content="2022-01-20" />
  <meta name="dc.language" content="en-US" />
  <meta name="citation_language" content="en-US" />
  <meta name="dc.relation.ispartof" content="Manubot" />
  <meta name="dc.publisher" content="Manubot" />
  <meta name="citation_journal_title" content="Manubot" />
  <meta name="citation_technical_report_institution" content="Manubot" />
  <meta name="citation_author" content="Johannes Elferich" />
  <meta name="citation_author_institution" content="RNA Therapeutic INstitute, UMass Chan Medical School" />
  <meta name="citation_author_institution" content="HHMI" />
  <meta name="citation_author_orcid" content="0000-0002-9911-706X" />
  <meta name="citation_author" content="Nikolaus Grigorieff" />
  <meta name="citation_author_institution" content="RNA Therapeutic INstitute, UMass Chan Medical School" />
  <meta name="citation_author_institution" content="HHMI" />
  <meta name="citation_author_orcid" content="0000-0002-1506-909X" />
  <link rel="canonical" href="https://jojoelfe.github.io/fowl_template_matching_manuscript/" />
  <meta property="og:url" content="https://jojoelfe.github.io/fowl_template_matching_manuscript/" />
  <meta property="twitter:url" content="https://jojoelfe.github.io/fowl_template_matching_manuscript/" />
  <meta name="citation_fulltext_html_url" content="https://jojoelfe.github.io/fowl_template_matching_manuscript/" />
  <meta name="citation_pdf_url" content="https://jojoelfe.github.io/fowl_template_matching_manuscript/manuscript.pdf" />
  <link rel="alternate" type="application/pdf" href="https://jojoelfe.github.io/fowl_template_matching_manuscript/manuscript.pdf" />
  <link rel="alternate" type="text/html" href="https://jojoelfe.github.io/fowl_template_matching_manuscript/v/1ab3e8bc78dd9f8d18576d6adbf09b518796c249/" />
  <meta name="manubot_html_url_versioned" content="https://jojoelfe.github.io/fowl_template_matching_manuscript/v/1ab3e8bc78dd9f8d18576d6adbf09b518796c249/" />
  <meta name="manubot_pdf_url_versioned" content="https://jojoelfe.github.io/fowl_template_matching_manuscript/v/1ab3e8bc78dd9f8d18576d6adbf09b518796c249/manuscript.pdf" />
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
([permalink](https://jojoelfe.github.io/fowl_template_matching_manuscript/v/1ab3e8bc78dd9f8d18576d6adbf09b518796c249/))
was automatically generated
from [jojoelfe/fowl_template_matching_manuscript@1ab3e8b](https://github.com/jojoelfe/fowl_template_matching_manuscript/tree/1ab3e8bc78dd9f8d18576d6adbf09b518796c249)
on January 20, 2022.
</em></small>

## Authors



+ **Johannes Elferich**<br>
    ![ORCID icon](images/orcid.svg){.inline_icon width=16 height=16}
    [0000-0002-9911-706X](https://orcid.org/0000-0002-9911-706X)
    · ![GitHub icon](images/github.svg){.inline_icon width=16 height=16}
    [jojoelfe](https://github.com/jojoelfe)<br>
  <small>
     RNA Therapeutic INstitute, UMass Chan Medical School; HHMI
  </small>

+ **Nikolaus Grigorieff**<br>
    ![ORCID icon](images/orcid.svg){.inline_icon width=16 height=16}
    [0000-0002-1506-909X](https://orcid.org/0000-0002-1506-909X)
    · ![GitHub icon](images/github.svg){.inline_icon width=16 height=16}
    [nikogrigorieff](https://github.com/nikogrigorieff)<br>
  <small>
     RNA Therapeutic INstitute, UMass Chan Medical School; HHMI
  </small>



## Abstract {.page_break_before}



Localization of biomolecules inside a cell is an important goal of biological imaging. Fluorescence microscopy can localize biomolecules inside whole cells and tissues, but its ability to count biomolecules and accuracy of the spatial coordinates is limited by the wavelength of visible light. On the other hand, cryo-electron microscopy (cryo-EM) provides highly accurate position and orientation information of biomolecules but is often limited to small fields of view inside a cell, providing only limited biological context. In this study we use a new data-acquisition scheme called “Beam-Imageshift for Large Area Cryo-Electron microscopy” (BILACE) to collect high-resolution cryo-EM data over entire sections (100 – 200 nm thick lamellae) of neutrophil-like mouse cells, representing roughly 1% of the total cellular volume. We use 2D template matching to determine localization and orientation of the large ribosomal subunit in these sections. Furthermore, we use 2D template matching to test detected targets for the presence of the small ribosomal subunit and used the relative orientations of the ribosomes to assign them to polysomes. These results provide "maps" of translational activity across sections of mammalian cells. We envision that using this high-throughput cryo-EM data collection approach together with 2D template matching will advance visual proteomics to complement other single-cell "omics" techniques, such as flow-cytometry and single-cell sequencing. 



## Introduction

Understanding of cellular processes requires knowledge of the amount, location,
and interaction of biomolecules inside the cell. Techniques that measure this
can broadly be divided into label, and label-free techniques. In
label-techniques a probe is physically attahced to a molecule is interest that
is able to produce a high signal-to-noise signal, such as a fluorescent probe.
In label-free techniques the physical properties of molecules themselves are
used for detection. An example for this is proteomics using mass-spectrometry.
Broadly the advantage of label-free techniques is that they can provide
information over thousands of molecules, while label-techniques offer higher
fidelity information for a few molecules. Especially spatial information can
most of the time only be achieved using label-tehcniques. 

Cryo-electron microscopy has the potential to directly measure the arrangement
of atoms that compose biomolecules inside of cells, thereby allowing label-free
detection with high spatial accuracy. This has been called "Visual proteomics".
The predominant technique at the moment is cryo-electron tomography. However,
the throughput of these methods in low due to highly complex sample preparation,
data acquisition, and data processing. We have shown that molecules can be
identified by their structural "fingerprint" in single projection using "2D
template-matching".

Hematopoiesis is the process of generating the various cell typs of the blood in
the bone marrow. Disregulation of the process results in diseases like leukemia.
Understaning how hematopoietic stem and progenitor cells are programmed to
diffferentiate to the appropriate cell type would be provide new insight how
hematopoiesis can be misregulated. Of special interest is the regulation of
translation during hematopoiesis. This is exemplified by the observation that
genetic defects in the ribosome machinery often leads to hematopoietic disease.
As such direct quantification of ribosome location, number and conformational
states could lead to new insight into hematopoietic disease. 

Here we apply 2D-template matching to neutrophil-ilke murine cells. By employing
anew data-acquisition scheme we obtained coverage of the whole "lamella"
covering roughly 2% of the cellular volume. 

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

### 2D-Template matching can be used to find ribosomal subunits in cryo-FIB thinned lamella of mammalian cells

To test whether we could detect individual ribosomes in mammalian cells we
prepared cryo-lamella of mouse neutrophil-like cells. Low-magnification images
of these lamellas clearly shows cellular features consistent with a
neutrophil-like phenotype, mainly a segmented nucleus and a plethora of
membrane-organelles, corresponding to the granules and secretory vesicles of
neutrophils. We then proceeded to acquire micrographs on this lamella with a
defocus of 0.5-1.0 um, 30 e/A2/s exposure and 1.5 A pixelsize. We manually
selected multiple locations in the lamella and focused using standard low-dose
techniques, i.e. by first ensuring correct focus by imaging a sacrifical area.
The resoluting micrographs showed no signs of crystalline ice and had thon-rings
to  resolution, indicating successfull vitrification. 

We used an atomic model of the 60S mouse ribosomal subunit  (6SWA) for 2D
template matching. In a subset of images the distribution of cross-correlation
scores significantly exceeded the distribution expected from non-signifcant
matching(Figure 1B). In the resulting scaled maximum-intensity maps, clear peaks
with SNR thresholds up to 10 were apparent (Figure 1C). By using the criterion
described by for thresholding potential matches we found that in images of
cytosolic ompartments we found evidence of 10-500 ribosomes in the imaged areas.
Notably we found no matches in images that were taken in the nuclear
compartment. In the cytosolic areas we found a drastically different number of
matches, In somer areas we found only ~ 50 matches er image area, corresponding
to a concentration of..., while in another area we found more than 500 matches,
corresponding to a concentration of ... .

### cryo-EMILIA for 2D imaging of whole lamella

In order to obtain high-resolution data for complete lamella we used a new
approach for data collection. This approach uses three key strategies: (1)
ensures that every electron that exposes the sample is collected on the camera
(2) uses beam-image shift to precisely and quickly raster the surface of the
lamella and (3) uses a focusing strategy that does not rely on a sacrificial area.
First, we focused the electron beam so that the
entire beam was placed on the detector. We then centered a lamella under the
electron beam and used beam-image shift of the microscope to systematically
raster the whole surface of the lamella in a hexagonal pattern. Instead of
focusing in a sacrifical area, we determined the defocus after every exposure
using a routine implemented in SerialEM modeled after CTFFind. The focus was
then adjusted based on the difference between desired and measured defocus.
Since we used a serpentine pattern for data collection every expsoure is close
to the previous exposure making drastic changes in the defocus unlikely.
Furthermore we started our acquisition pattern on the platinum deposition edge,
so the intial exposure where the defocus was not yet adjusted did not contain
any biologically relevant information. Using this strategy we were able to
highly consistently collect data with a defocus of 8 um (Figure 2B). Together
with the nominal defocus of the microscope this data results in a topological
map of the lamella.

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

![Template matching of ribosomal large subunits in fib-milled neutrophil like cells](figures/figure1_draft.svg){#fig:initmatching}

![This is an example-figurern](tikz:initmatching2){#fig:initmatching2}

```{.tikz-figure #initmatching2 width=16cm height=13cm draft=true}
\node (anchor) at (0.5,9.35) {}; 
\node[labelNode] {A};
\node[graphicNode] {\includegraphics[width=12cm]{content/code/img/initial_map_match.pdf}};
\iftoggle{draft}{\node [redAnchorNode] {};};

```


![This is an example-figurern](tikz:example-figure){#fig:approach}

```{.tikz-figure #example-figure width=16cm height=13cm draft=true}
\node (anchor) at (0.5,9.35) {}; 
\node[labelNode] {A};
\node[graphicNode] {\includegraphics[width=5cm]{content/graphics/approach/approach.png}};
\iftoggle{draft}{\node [redAnchorNode] {};};

\node (anchor) at (6.0,9.35) {}; 
\node[labelNode] {B};
\node[graphicNode] {\includegraphics[width=5cm]{content/images/ac_strategy.png}};
\iftoggle{draft}{\node [redAnchorNode] {};};


\node (anchor) at (11.5,9.35) {}; 
\node[labelNode] {C};
\node[titleNode] {Eucentric Focus};
\node[graphicNode] {\includegraphics[height=3.0cm]{content/images/fringebeam.png}};
\iftoggle{draft}{\node [redAnchorNode] {};};

\node (anchor) at (15,9.35) {}; 
\node[labelNode] {D};
\node[titleNode] {Fringe-free Focus};
\node[graphicNode] {\includegraphics[height=3.0cm]{content/images/nofringebeam.png}};
\iftoggle{draft}{\node [redAnchorNode] {};};

\node (anchor) at (11.5,4.85) {}; 
\node[labelNode] {E};
\node[graphicNode] {\includegraphics[height=4.3cm]{content/code/img/defocusplot.pdf}};
\iftoggle{draft}{\node [redAnchorNode] {};};

```

![This is an example-figurern](tikz:example-figure2){#fig:approach2}

```{.tikz-figure #example-figure2 width=16cm height=13cm draft=true}
\node (anchor) at (0.5,9.35) {}; 
\node[labelNode] {A};
\node[graphicNode] {\includegraphics[width=7.5cm]{content/code/img/defocus_defocus_vs_bs_plot.pdf}};
\iftoggle{draft}{\node [redAnchorNode] {};};

\node (anchor) at (0.5,5.35) {}; 
\node[labelNode] {B};
\node[graphicNode] {\includegraphics[width=7.5cm]{content/code/img/defocus_astigmatism_vs_bs_plot.pdf}};
\iftoggle{draft}{\node [redAnchorNode] {};};

\node (anchor) at (8.5,9.35) {}; 
\node[labelNode] {C};
\node[graphicNode] {\includegraphics[width=7.5cm]{content/code/img/defocus_angle_vs_bs_plot.pdf}};
\iftoggle{draft}{\node [redAnchorNode] {};};

```


![This is an example-figurern](tikz:example-figure3){#fig:approach3}

```{.tikz-figure #example-figure3 width=16cm height=13cm draft=true}
\node (anchor) at (0.5,9.35) {}; 
\node[labelNode] {A};
\node[graphicNode] {\includegraphics[width=7.5cm]{content/code/img/movement_vs_bs_plot.pdf}};
\iftoggle{draft}{\node [redAnchorNode] {};};


\node (anchor) at (8.5,9.35) {}; 
\node[labelNode] {B};
\node[graphicNode] {\includegraphics[width=7.5cm]{content/code/img/thickness_by_intensity_vs_bs_plot.pdf}};
\iftoggle{draft}{\node [redAnchorNode] {};};

```

![This is an example-figurern](tikz:matching){#fig:matching}

```{.tikz-figure #matching width=16cm height=13cm draft=true}
\node (anchor) at (0.5,9.35) {}; 
\node[labelNode] {A};
\node[graphicNode] {\includegraphics[width=7.5cm]{content/images/screenie.png}};
\iftoggle{draft}{\node [redAnchorNode] {};};



```

## References {.page_break_before}

<!-- Explicitly insert bibliography here -->
<div id="refs"></div>
