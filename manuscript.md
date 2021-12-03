---
title: Visual proteomics using whole-lamella 2D template matching
keywords:
- cryo-EM
- visual protemics
- ribosome
lang: en-US
date-meta: '2021-12-03'
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
  <meta name="dc.date" content="2021-12-03" />
  <meta name="citation_publication_date" content="2021-12-03" />
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
  <link rel="alternate" type="text/html" href="https://jojoelfe.github.io/fowl_template_matching_manuscript/v/db82defa439d15e470068f0e987566e9c143c51f/" />
  <meta name="manubot_html_url_versioned" content="https://jojoelfe.github.io/fowl_template_matching_manuscript/v/db82defa439d15e470068f0e987566e9c143c51f/" />
  <meta name="manubot_pdf_url_versioned" content="https://jojoelfe.github.io/fowl_template_matching_manuscript/v/db82defa439d15e470068f0e987566e9c143c51f/manuscript.pdf" />
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
([permalink](https://jojoelfe.github.io/fowl_template_matching_manuscript/v/db82defa439d15e470068f0e987566e9c143c51f/))
was automatically generated
from [jojoelfe/fowl_template_matching_manuscript@db82def](https://github.com/jojoelfe/fowl_template_matching_manuscript/tree/db82defa439d15e470068f0e987566e9c143c51f)
on December 3, 2021.
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

During hematopoiesis all cells of the blood derive from a common set of stem and progenitor cells in the bone marrow. How is the differentiation of these morphologically and functionally diverse cells orchestrated and how is differentiation outcome is encoded in progenitor cells? To provide answers to this question we are using a “visual proteomics” approach where we determine cellular state by quantifying the localization, orientation, and functional state of biomolecules in cells by label-free cryo-electron microscopy (cryo-EM) imaging. Our lab has developed an algorithm called 2D template matching, where all possible projections of a reference structure are compared with cryo-EM images of cells to derive the location and orientation of all instances of a biomolecule. We used this approach to find large ribosomal subunits in cryo-EM images of differentiating hematopoietic precursor cells. A new data-acquisition scheme called “Fast Observation of Whole Lamella” (FOWL) was employed to find ribosomes in complete cellular cross-sections. We find highly heterogeneous distribution of ribosomes in differentiated cells and are working on optimizing data-collection and data-processing to achieve the throughput that allows imaging the equivalent of multiple cellular volumes. We envision that using these high-throughput visual proteomics approaches can become a complimentary technique to other single-cell techniques, such as flow-cytometry and single-cell sequencing.




## Introduction


## References {.page_break_before}

<!-- Explicitly insert bibliography here -->
<div id="refs"></div>
