---
output:
  pdf_document:
    template: template-letter.tex
author:
- Johannes Elferich
- UMass Chan Medical School/HHMI
opening: Dear Editor,
date: 4 Nov 2022

return-address: 
- RNA Therapeutics Institute
- 368 Plantation St
- Worcester MA 01605

fontfamily: mathpazo
fontsize: 12pt
geometry: margin=1in
blockquote: true

signature-before: -8ex
signature-after: 0ex
closing-indentation: 0pt
links-as-notes: true
colorlinks: true
...

Please find enclosed our revised manuscript titled “Defocus Corrected Large Area Cryo-EM (DeCo- LACE) for Label-Free Detection of Molecules across Entire Cell Sections”.

As detailed below, we have carefully considered each comment by the reviewers and revised the manuscript accordingly.

We hope that you will find the manuscript in its revised form suitable as an article for the Tools and Resources section of eLife. 


\longindentation=0pt
\closing{Sincerely,}

\pagebreak

The authors have developed a method aimed at characterizing particles found in wide-view image montages from cellular sections. While it might be seen as an incremental advance over their previous publication on template-matching, enabling users to be able to examine wide fields of view has importance and significance for addressing cell biological questions. There are several limitations to the present study, however, that should be addressed in a revised paper:

1) They have only used the large ribosomal subunit for this study. They should discuss the MW of this object and the fact that it has a significant fraction of nucleic acid, increasing the contrast. They might speculate how the method would work for objects with lower MW and no nucleic acid content.

**Answer:** We added a paragraph to the discussion (lines 295-300). The paragraphincludes the MW of the template used to detect the large ribosomal
subunit (2MDa) and the fraction of RNA. Regarding the amount of included nucleic acid we refer to Spahn et. al. Structure 2000 to discuss the possibility that nucleic acid contribute more the the signal in cryo-EM micrographs. Regarding the question about objects with lower MW we cite Rickgauer et.al.  eLife 2017, which contains data
regarding the MW of proteins that are expected to be detectable.  We note that MW might not only be the only criterion that determines detectability, but that the conformational homogeneity and abundance within the cells also play important roles. 


2) While the method is proposed as a faster alternative to cryo-ET, the
   computational demands seem prohibitive. Can they speculate on how the method
   could be accelerated (and not just by adding more processors)? Given the
   computational bottleneck, can they provide recommendations to readers on when
   the presented approach is appropriate?

**Answer:** We have expanded the paragraph in the discussion with speculation about
approaches to accelerate 2DTM (lines 310-313). It is unclear to us whether
cryo-ET of a similar sized area would be computationally more efficient,
especially given the complex nature and rapid change in processing pipelines. We
note that while 2DTM is computationally demanding, there are few steps and
little user interaction is required. For the discussion of the advantages and
disadvantages of 2DTM compared to cryo-ET we refer to Lucas et.al. eLife 2021.


3) The manuscript could potentially be improved by a more thorough explanation
   of the resolution regime to which the 2DTM signal-to-noise ratio (SNR) values
   are most sensitive. When would one anticipate aberrations like a coma to
   become problematic?

**Answer:** We have updated the discussion paragraph in lines 279-294 with an explanation of the expected resolution ranges compared with the expected coma aberrations as discussed in Cheng et.al. JSB 2018. In summary, we assume that the resoution range being used for 2DTM is lower than the resolution at which coma aberrations are expected to be problematic.

4) Fitting of particle defocus allows detection of the Z-height for each large
   ribosomal subunit. Could the authors estimate what is the precision of the
   detection of Z-height in their experiment and how it depends on the thickness
   of the lamella (˜150...250 nm in this case).

**Answer:** The precision of Z-height estimation in 2DTM has been previously investigated by
comparing it with results from 3D coordinates from cryo-tomography (Lucas. et.
al. eLife 2021). The median difference in the Z-direction between 2DTM and
tomography was found to 59 A, roughly a third of the LSU diameter. While we have
not yet sufficent data from 2DTM+tomography to perform such an analysis as a
function of sample thickness, we note that Lucas et. al. used samples with a
thickness ranging from 80-220 nm, so we don't expect uncertainties to be
substantialy higher in our present study. 

5) How close to the top or the bottom end of the lamella can a ribosome subunit
   be detected? Can it be detected when it is partially milled away? Do the
   molecules in the "middle" of the lamella correspond to higher SNR?

**Answer:** We cannot detect edges of the lamella using a single exposure and therefore
cannot directly measure the distance of a detection from the lamella edge.
In order to address this question we have estimated the lamella thickness in
every tile using (...) and compared it to the range of ribsome detection in the
beam direction. This analysis suggests that ribsome detections are only in a
slice that is ~70 nm thinner that the lamella, suggesting that we could not
detect ribosome ~35nm from the lamella edge, potentially due to radiation damage
during the milling process. Our lab is currently performing a more through
investigation of this phenomenon.

----------

eLife's editorial process also produces an assessment by peers designed to be posted alongside a preprint for the benefit of readers.

Public Evaluation Summary:

The work details a new acquisition method of defocus corrected large area cryo-EM (DeCo-LACE). The data-acquisition approach is highly complementary to the research group's previous work of using high-resolution 2D template-matching (2DTM) to identify macromolecular complexes in dense and heterogeneous cellular specimens. Notably and importantly, the data-acquisition approach minimizes sampling bias. Overall, DeCo-LACE is a very interesting approach to locating large ribosomal subunits in FIB-lamella at scale.


Reviewer #1 (Public Review):

The manuscript is likely of interest to cryo-electron microscopists working on cellular samples. It details a data-acquisition scheme for mapping large areas at a fine pixel size by cryo-electron microscopy for the purpose of macromolecular identification by high-resolution 2D template matching (2DTM). The authors succinctly describe the methodology, as well as detail the apparent effects of microscope aberrations on 2DTM results.

While other montaging approaches have been described recently, the one
presented here differs in its approach to controlling defocus and avoids the
need to sacrifice a biologically meaningful region of a sample. The authors
investigate the compatibility of the data acquisition with their 2DTM method
using cryoFIB-milled mouse neutrophil-like cells and the 60S ribosome as an
example case. In order to minimize unnecessary exposures, the authors restrict
illumination to a circle inscribed on the detector and use beam image-shift in
lieu of stage shift. This approach introduces several optical aberrations for
which the authors investigate the effects on the 2DTM results. The results of
the investigated aberration effects may be of general interest to the cryoEM
community, not just those using montaging methods.


Reviewer #1 (Recommendations for the authors):

The manuscript could potentially be improved by a more thorough explanation of the resolution regime to which the 2DTM signal-to-noise ratio (SNR) values are most sensitive. When would one anticipate aberrations like a coma to become problematic?

Lines 156-158: How does the inclusion of the non-illuminated areas, even when
filled with Gaussian noise, impact the estimate of the false-positive rate?
Could this be the source of the apparent overestimation of the false-positive
rate?

**Answer:** During data processing we do not include matches that occur in the
Gaussian noise filled non-illuminated areas. 

Ln 189: "exclusively".

**Answer:** Thank you for pointing this out. The typo is fixed.

Lines 220-224: Are the authors able to incorporate the effect of coma in the
2DTM routine to see its effect on results or perform simulations on the effect
coma has on the SNR values? When would one expect a coma to become
limiting/negatively affect the SNR? Is it near/beyond the Nyquist of this data
set anyway?

**Answer:** Please refer to the answer to question 3 above.

Lines 267-269:
Reference 27 (Cash et al, 2020) detailed a case of substantial beam image shift
which resulted in |0-6| mrad of beam tilt (up to 20 um image shift) and limited
the reconstruction to 4.9 Å. In Cheng et al, JSB, 2018 the authors could obtain
~3-3.5 Å reconstructions in light of |1.3| mrad beam tilt (~5-8 um image shift),
which is likely closer to the maximum amount of beam tilt being applied in the
presented study.

**Answer:** Thank you for pointing this out. We updated the discussion to include Cheng et al, JSB, 2018, as described in the answer to question 3)

Lines 270-272:
Can the authors elaborate their explanation on the impact of coma on SPA vs
2DTM? I would have thought that a coma would have less of an impact on SPA data
through averaging compensatory directions and more of an impact on 2DTM by
making the reference project less similar to the experimental image.

**Answer:** We have removed the discussion of the impact of coma in SPA vs 2DTM, since as elaborated in Cheng 2018 the current theory does apparently not capture the experimental
observations and as detailed in the answer to question 3) in our case the signal
degradation caused by beamtilt occurs at higher resolutions than used by our
reference. We are currently exploring including fitting coma and other
aberrations during 2DTM to better understand its impact.

Line 342:
Why were images resampled to 1.5 Å? Was this to include information beyond the
physical Nyquist? If so, has this been shown to improve the 2DTM results?

**Answer:** The resampling to 1.5 Å was not intended do include information beyond Nyquist.
Instead we chose 1.5 Å initially since we were expecting information up to 3 Å to
contribute to 2DTM and wanted to slightly lower the magnification compared to
the ~ 1.0 Å pixelsize use previously, to reduce the number of tiles that have to be
acquired. We then chose the first magnification at our Krios that was closest to
1.5 Å physical pixelsize and binned to 1.5 Å, with the idea that this would
simplify combining data from different instruments, which we did not do in this
study.


Figure-4 supplement-1:
Panels D and E are not described in the legend. Are micrographs cropped to the
illuminated area inscribed before 2DTM or is the entirety of the unilluminated
area, filled with Guassian noise, included?

**Answer:** We apologize for the omission of figure legend describing pandel D and E. Indeed, the micrographs are cropped to the illuminated area in order to avoid
performing unnecessary cross-correlation.

Figure 7:
Remove/replace "electron" in the first box.

**Answer:** We have removed "electron" as requested.

Reviewer #2 (Public Review):

The manuscript by Elferisch and colleagues extends the previously reported approach for localization of large ribosomal subunits to larger areas of the dimensions of cells (several square microns). A large area of imaging is achieved by recording minimally overlapping circular exposures followed by an assembly of them into a large image. The large ribosomal subunits are then searched in the 2D images taking the defocus into account. In order to make the approach functional the authors specifically tailored the algorithms to perform motion correction and validated that image shift does not seem to limit the precision of localization of large ribosomal subunits in images. Overall, DeCo-LACE is a very interesting approach to locating large ribosomal subunits in FIB-lamella at scale.


Reviewer #2 (Recommendations for the authors):

The manuscript is technically excellent and well written. I have several important questions that are still not addressed in the current version of the manuscript.
1. Fitting of particle defocus allows detection of the Z-height for each large ribosomal subunit. Could the authors estimate what is the precision of the detection of Z-height in their experiment and how it depends on the thickness of the lamella (˜150...250 nm in this case).

**Answer:** Please refer to our answer to question 4 above. 

2. How close to the top or the bottom end of the lamella can a ribosome subunit be detected? Can it be detected when it is partially milled away? Do the molecules in the "middle" of the lamella correspond to higher SNR?

**Answer:** Please refer to our answer to question 5 above.

3. As all the research using this approach is performed on ribosomal subunits, in order to make the method more general - it should also work on other macromolecules. Could the authors discuss the potential lower limits for detection in FIB lamella?

**Answer:** Please refer to our answer to question 1 above.

Minor questions
1. What is the fraction of overlap between the circular images in percent?

**Answer:** The overlap between adjacent circular tiles was 12.9% for the eucentric focus
condition and 10.3% for the fringe-free focus condition. We have included this
information in the manuscript.

2. The hardware used by the authors is a non-common high-performance unit. Could
   the authors give a time estimate for processing on one full lamella on a more
   conventional consumer GPU such as Nvidia 3000-series?

**Answer:** We benchmarked 2DTM on NVIDIA A6000 GPUs and NVIDIA 3090 GPUs and found
negligible differences in performance. While purchasing consumer GPUs will
certainly be more cost-effective it can be hard to source the required number of
consumer GPUs and find manufactures that build high-density rack-mounted systems containing
multiple consumer grade GPUs.




