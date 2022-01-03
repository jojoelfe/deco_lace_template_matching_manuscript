---
title: Visual proteomics using whole-lamella 2D template matching
keywords:
- cryo-EM
- visual protemics
- ribosome
lang: en-US
date-meta: '2022-01-03'
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
  <meta name="dc.date" content="2022-01-03" />
  <meta name="citation_publication_date" content="2022-01-03" />
  <meta name="dc.language" content="en-US" />
  <meta name="citation_language" content="en-US" />
  <meta name="dc.relation.ispartof" content="Manubot" />
  <meta name="dc.publisher" content="Manubot" />
  <meta name="citation_journal_title" content="Manubot" />
  <meta name="citation_technical_report_institution" content="Manubot" />
  <meta name="citation_author" content="Johannes Elferich" />
  <meta name="citation_author_institution" content="RNA Therapeutic INstitute, UMass Chan Medical SChool" />
  <meta name="citation_author_institution" content="HHMI" />
  <meta name="citation_author_orcid" content="XXXX-XXXX-XXXX-XXXX" />
  <meta name="citation_author" content="Nikolaus Grigorieff" />
  <meta name="citation_author_institution" content="RNA Therapeutic INstitute, UMass Chan Medical SChool" />
  <meta name="citation_author_institution" content="HHMI" />
  <meta name="citation_author_orcid" content="XXXX-XXXX-XXXX-XXXX" />
  <link rel="canonical" href="https://jojoelfe.github.io/fowl_template_matching_manuscript/" />
  <meta property="og:url" content="https://jojoelfe.github.io/fowl_template_matching_manuscript/" />
  <meta property="twitter:url" content="https://jojoelfe.github.io/fowl_template_matching_manuscript/" />
  <meta name="citation_fulltext_html_url" content="https://jojoelfe.github.io/fowl_template_matching_manuscript/" />
  <meta name="citation_pdf_url" content="https://jojoelfe.github.io/fowl_template_matching_manuscript/manuscript.pdf" />
  <link rel="alternate" type="application/pdf" href="https://jojoelfe.github.io/fowl_template_matching_manuscript/manuscript.pdf" />
  <link rel="alternate" type="text/html" href="https://jojoelfe.github.io/fowl_template_matching_manuscript/v/f16ad49442325e67935666d2f54a5ab26f6c3bff/" />
  <meta name="manubot_html_url_versioned" content="https://jojoelfe.github.io/fowl_template_matching_manuscript/v/f16ad49442325e67935666d2f54a5ab26f6c3bff/" />
  <meta name="manubot_pdf_url_versioned" content="https://jojoelfe.github.io/fowl_template_matching_manuscript/v/f16ad49442325e67935666d2f54a5ab26f6c3bff/manuscript.pdf" />
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
([permalink](https://jojoelfe.github.io/fowl_template_matching_manuscript/v/f16ad49442325e67935666d2f54a5ab26f6c3bff/))
was automatically generated
from [jojoelfe/fowl_template_matching_manuscript@f16ad49](https://github.com/jojoelfe/fowl_template_matching_manuscript/tree/f16ad49442325e67935666d2f54a5ab26f6c3bff)
on January 3, 2022.
</em></small>

## Authors



+ **Johannes Elferich**<br>
    ![ORCID icon](images/orcid.svg){.inline_icon width=16 height=16}
    [XXXX-XXXX-XXXX-XXXX](https://orcid.org/XXXX-XXXX-XXXX-XXXX)
    · ![GitHub icon](images/github.svg){.inline_icon width=16 height=16}
    [jojoelfe](https://github.com/jojoelfe)<br>
  <small>
     RNA Therapeutic INstitute, UMass Chan Medical SChool; HHMI
  </small>

+ **Nikolaus Grigorieff**<br>
    ![ORCID icon](images/orcid.svg){.inline_icon width=16 height=16}
    [XXXX-XXXX-XXXX-XXXX](https://orcid.org/XXXX-XXXX-XXXX-XXXX)
    · ![GitHub icon](images/github.svg){.inline_icon width=16 height=16}
    [nikogrigorieff](https://github.com/nikogrigorieff)<br>
  <small>
     RNA Therapeutic INstitute, UMass Chan Medical SChool; HHMI
  </small>



## Abstract {.page_break_before}



Localization and characterization of biomolecules inside a cell is the fundamental quest of all biological imaging. Fluorescence microscopy can localize biomolecules inside whole cells and tissues, but its ability to count biomolecules and accuracy of the spatial coordinates is limited by the wavelength of visible light. Cryo-electron microscopy on the other hand provides highly accurate position and orientation information of biomolecules but is often limited to small fields of view inside a cell, providing only limited biological context. In this study we use a data-acquisition scheme called “Fast Observation of Whole Lamella” (FOWL) to collect cryo-electron microscopy data over thin central sections, representing roughly 1% of the total cellular volume, of neutrophil-like mouse cells. We use 2D-template matching to determine localization and orientation of the large subunit of the ribosome in these cross-sections. We furthermore use 2D-template matching to test for complex formation with the small ribosomal subunit and used relative orientations of ribosome to assign ribosomes to polysomes. Overall these results provide a "map" of translational activity in cross-sections of mammalian cells. We envision that using these high-throughput cryo-EM data collection and 2D template matching approaches will advance visual proteomics to complement other single-cell "omics" techniques, such as flow-cytometry and single-cell sequencing.



## Introduction


## Figures

\begin{tikzpicture}

\def \n {5}
\def \radius {3cm}
\def \margin {8} % margin in angles, depends on the radius

\foreach \s in {1,...,\n}
{
  \node[draw, circle] at ({360/\n * (\s - 1)}:\radius) {$\s$};
  \draw[->, >=latex] ({360/\n * (\s - 1)+\margin}:\radius)
    arc ({360/\n * (\s - 1)+\margin}:{360/\n * (\s)-\margin}:\radius);
}
\end{tikzpicture}


## References {.page_break_before}

<!-- Explicitly insert bibliography here -->
<div id="refs"></div>
