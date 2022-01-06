---
title: Visual proteomics using whole-lamella 2D template matching
keywords:
- cryo-EM
- visual protemics
- ribosome
lang: en-US
date-meta: '2022-01-06'
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
  <meta name="dc.date" content="2022-01-06" />
  <meta name="citation_publication_date" content="2022-01-06" />
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
  <link rel="alternate" type="text/html" href="https://jojoelfe.github.io/fowl_template_matching_manuscript/v/526a225ec7d9a3155b4717e770a46fa6829fcdbb/" />
  <meta name="manubot_html_url_versioned" content="https://jojoelfe.github.io/fowl_template_matching_manuscript/v/526a225ec7d9a3155b4717e770a46fa6829fcdbb/" />
  <meta name="manubot_pdf_url_versioned" content="https://jojoelfe.github.io/fowl_template_matching_manuscript/v/526a225ec7d9a3155b4717e770a46fa6829fcdbb/manuscript.pdf" />
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
([permalink](https://jojoelfe.github.io/fowl_template_matching_manuscript/v/526a225ec7d9a3155b4717e770a46fa6829fcdbb/))
was automatically generated
from [jojoelfe/fowl_template_matching_manuscript@526a225](https://github.com/jojoelfe/fowl_template_matching_manuscript/tree/526a225ec7d9a3155b4717e770a46fa6829fcdbb)
on January 6, 2022.
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

Understanding of cellular processes requires knowledge of the amount, location, and interaction of biomolecules inside the cell. Techniques that measure this can broadly be divided into label, and label-free techniques. In label-techniques a probe is physically attahced to a molecule is interest that is able to produce a high signal-to-noise signal, such as a fluorescent probe. In label-free techniques the physical properties of molecules themselves are used for detection. An example for this is proteomics using mass-spectrometry. Broadly the advantage of label-free techniques is that they can provide information over thousands of molecules, while label-techniques offer higher fidelity information for a few molecules. Especially spatial information can most of the time only be achieved using label-tehcniques. 

Cryo-electron microscopy has the potential to directly measure the arrangement of atoms that compose biomolecules inside of cells, therby allowing label-free detection with high spatial accuracy. This has been called "Visual proteomics". The predominant technique at the moemnt is cryo-electron tomography. However, the throughput of these methods in low due to highly complex sample preparation, data acquisition, and data processing. We have shown that molecules can be identified by their structural "fingerprint" in single projection using "2D temaplte-matching".

Here we apply 2D-template matching to neutrophil-ilke murine cells. By employing anew data-acquisition scheme we obtained coverage of the whole "lamella" covering roughly 2% of the cellular volume. 

## Materials and Methods

### Grid preparation

ER-HoxA9 cells were maintained in RPMI supplemented with 10% FBS, penicillin/streptomycin, SCF, and estrogen [@doi:10.1016/j.cell.2016.08.057] at 37C and 5% CO2. 120h prior to gridd freezing cells were washed twice in PBS and cultured in the same medium, except without estrogen. Differentiation was verified by staining with Hoechst-dye and insepction of nuclear morphology. Cells were then counted and diluted to 1^106 cells/ml. Grids ( either 200 mesh copper grids, with a sillicone-oxide and 2um holes with a 2um spacing or 200 mesh gold grids with a thin gold film and 2 um holes in 2um sapcing) were glow-discharged from both sides using a ... for ... . 3.5 ul of cells suspension was added to grids on the thin-film side and grids were automatically blotted from the back-side using a GP2 cryoplunger (Leica) for ... s and rapidly plunged into liquid ethane at -185C. 

### FIB-milling

Grids were loaded into a Acquilos 2 FIB/SEM  microscope with a stage cooled to -190C. Grids were sputter-coated with platinum for 15s at 45 mA and then coated with a layer of platinum-precursor by openin the GIS-valve for 45s. An overview of the grid was created by montaging SEM images and isolated cells at the center of gridsquares were selected for FB-milling. Lamella were generated automatically using the AutoTEM software, resulting in 6-8 um wide lamella with 150-200 um thickness as determined by FIB-imaging of the lamella edge.

### Data collection

Grids were loaded into a Krios Titam TEM operated at 300 keV. The microscope was setup with a cross-grating grid on the stageby setting the beam-diameter to 900 nm, resulting in the beam being completely visible in the camera. To establish fringe-free conditions, the "Fine eucentric" procedure of serialEM was used to move a square of the cross-grating grid to the eucentric position of the microscope. The effective defocus was then set to 2 um, using the "autofocus" routine of serialEM. The objective focus of the microscope was changed until no fringes were visible. The stage was then moved in Z until images had a apparent defocus of 2 um. The differnce in stage Z-position between the eucentric and fringe-free conditions was calculate d and noted to move other areas into fringe-free condition.

Low magnification montages were used to find lamella and lamella that were sufficently thin and free of contamination were selected for automated data collection. 

### Data pre-processing

### Template matching

### Data analysis


## Results


## Discussion


## Figures

![Template matching of ribosomal large subunits in fib-milled neutrophil like cells](figures/figure1_draft.svg){#fig:initmatching}

![This is an example-figurern](tikz:example-figure){#fig:approach}

```{.tikz-figure #example-figure width=16cm height=13cm draft=true}
\node (anchor) at (0.5,9.35) {}; 
\node[labelNode] {A};
\node[graphicNode] {\includegraphics[width=6cm]{content/graphics/approach/approach.pdf}};
\iftoggle{draft}{\node [redAnchorNode] {};};

\node (anchor) at (6.2,9.35) {}; 
\node[labelNode] {B};
\node[graphicNode] {\includegraphics[height=4.3cm]{content/images/fringebeam.png}};
\iftoggle{draft}{\node [redAnchorNode] {};};

\node (anchor) at (6.2,4.85) {}; 
\node[labelNode] {C};
\node[graphicNode] {\includegraphics[height=4.3cm]{content/images/fringebeam.png}};
\iftoggle{draft}{\node [redAnchorNode] {};};

\node (anchor) at (11.0,9.35) {}; 
\node[labelNode] {D};
\node[graphicNode] {\includegraphics[height=4.3cm]{content/graphics/approach/defocusplot.pdf}};
\iftoggle{draft}{\node [redAnchorNode] {};};

```


## References {.page_break_before}

<!-- Explicitly insert bibliography here -->
<div id="refs"></div>
