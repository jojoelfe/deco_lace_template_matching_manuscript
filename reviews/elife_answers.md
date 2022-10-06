The authors have developed a method aimed at characterizing particles found in wide-view image montages from cellular sections. While it might be seen as an incremental advance over their previous publication on template-matching, enabling users to be able to examine wide fields of view has importance and significance for addressing cell biological questions. There are several limitations to the present study, however, that should be addressed in a revised paper:

1) They have only used the large ribosomal subunit for this study. They should discuss the MW of this object and the fact that it has a significant fraction of nucleic acid, increasing the contrast. They might speculate how the method would work for objects with lower MW and no nucleic acid content.

** We have included the MW of the used template to find the large ribosomal
subunit and the fraction of RNA vs protein. Regarding objects with lower MW we
have an included a citation to the following paper in eLife that contains data
regarding the MW of proteins that is expected to be sufficient to be
detected.Regarding the amount of included nucleic acid we refer to Span, et. al.
that determined the relative contribution of nucleic acid ve protein on the
signal in cryo-EM micrographs. We also note that these might not only be the
only criterion that determines detectability, but that the conformation
homogeneity and abundance within the cells also play important roles. **


2) While the method is proposed as a faster alternative to cryo-ET, the
   computational demands seem prohibitive. Can they speculate on how the method
   could be accelerated (and not just by adding more processors)? Given the
   computational bottleneck, can they provide recommendations to readers on when
   the presented approach is appropriate?

** We have expanded a paragraph in the discussion with speculation about
approaches to accelerate 2DTM. We also included some speculation about 


3) The manuscript could potentially be improved by a more thorough explanation of the resolution regime to which the 2DTM signal-to-noise ratio (SNR) values are most sensitive. When would one anticipate aberrations like a coma to become problematic?

4) Fitting of particle defocus allows detection of the Z-height for each large ribosomal subunit. Could the authors estimate what is the precision of the detection of Z-height in their experiment and how it depends on the thickness of the lamella (˜150...250 nm in this case).

5) How close to the top or the bottom end of the lamella can a ribosome subunit be detected? Can it be detected when it is partially milled away? Do the molecules in the "middle" of the lamella correspond to higher SNR?

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

Lines 156-158: How does the inclusion of the non-illuminated areas, even when filled with Gaussian noise, impact the estimate of the false-positive rate? Could this be the source of the apparent overestimation of the false-positive rate?

Ln 189: "exclusively".

Lines 220-224: Are the authors able to incorporate the effect of coma in the 2DTM routine to see its effect on results or perform simulations on the effect coma has on the SNR values? When would one expect a coma to become limiting/negatively affect the SNR? Is it near/beyond the Nyquist of this data set anyway?

Lines 267-269:
Reference 27 (Cash et al, 2020) detailed a case of substantial beam image shift which resulted in |0-6| mrad of beam tilt (up to 20 um image shift) and limited the reconstruction to 4.9 Å. In Cheng et al, JSB, 2018 the authors could obtain ~3-3.5 Å reconstructions in light of |1.3| mrad beam tilt (~5-8 um image shift), which is likely closer to the maximum amount of beam tilt being applied in the presented study.

Lines 270-272:
Can the authors elaborate their explanation on the impact of coma on SPA vs 2DTM? I would have thought that a coma would have less of an impact on SPA data through averaging compensatory directions and more of an impact on 2DTM by making the reference project less similar to the experimental image.

Line 342:
Why were images resampled to 1.5 Å? Was this to include information beyond the
physical Nyquist? If so, has this been shown to improve the 2DTM results?

The resampling to 1.5 Å was not intended do include information beyond nyquist.
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

We apoligize for the omission of figure legend describing pandel D and E.
Indeed, the micrographs are cropped to the illuminated area in order to avoid
performing unnecessary cross-correlation.

Figure 7:
Remove/replace "electron" in the first box.


Reviewer #2 (Public Review):

The manuscript by Elferisch and colleagues extends the previously reported approach for localization of large ribosomal subunits to larger areas of the dimensions of cells (several square microns). A large area of imaging is achieved by recording minimally overlapping circular exposures followed by an assembly of them into a large image. The large ribosomal subunits are then searched in the 2D images taking the defocus into account. In order to make the approach functional the authors specifically tailored the algorithms to perform motion correction and validated that image shift does not seem to limit the precision of localization of large ribosomal subunits in images. Overall, DeCo-LACE is a very interesting approach to locating large ribosomal subunits in FIB-lamella at scale.


Reviewer #2 (Recommendations for the authors):

The manuscript is technically excellent and well written. I have several important questions that are still not addressed in the current version of the manuscript.
1. Fitting of particle defocus allows detection of the Z-height for each large ribosomal subunit. Could the authors estimate what is the precision of the detection of Z-height in their experiment and how it depends on the thickness of the lamella (˜150...250 nm in this case).
2. How close to the top or the bottom end of the lamella can a ribosome subunit be detected? Can it be detected when it is partially milled away? Do the molecules in the "middle" of the lamella correspond to higher SNR?
3. As all the research using this approach is performed on ribosomal subunits, in order to make the method more general - it should also work on other macromolecules. Could the authors discuss the potential lower limits for detection in FIB lamella?

Minor questions
1. What is the fraction of overlap between the circular images in percent?

The overlap between adjacent circular tiles was 12.9% for the eucentric focus
condition and 10.3% for the fringe-free focus condition. We have included this
information in the manuscript.

2. The hardware used by the authors is a non-common high-performance unit. Could the authors give a time estimate for processing on one full lamella on a more conventional consumer GPU such as Nvidia 3000-series?


