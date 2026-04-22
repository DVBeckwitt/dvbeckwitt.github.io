# Metrology Resume Example

Source note: original binary removed from Git; use this text version for review.

```text
David V. Beckwitt
Columbia, MO | [phone omitted] | David.Beckwitt@proton.me | linkedin.com/in/DVBeckwitt | github.com/DVBeckwitt
Full CV (PDF)

Summary
Metrology Engineer candidate in R&D instrumentation and thin-film metrology who owns lab-built XRD and XRR metrology at
10+ samples per week for 5+ users with same-day results. Diagnose vacuum leaks, alignment drift, and electronics faults, then
stabilize geometry and analysis with hBN-based procedures and Python automation.

Skills
X-ray metrology: XRD, XRR, GIWAXS, reciprocal-space mapping, calibrant-based geometry verification
Thin films & microscopy: CVD, ALD, PLD build/operation, Raman, SEM/EDS, TEM, profilometry
Software: Python (NumPy/SciPy/pandas), Git, SQL, Excel, reduction pipelines, forward modeling

Experience
Graduate Research Assistant, X-ray Metrology & Instrumentation                                                2021 to Present
University of Missouri, Columbia, MO

• Own operation and maintenance of lab-built XRD and XRR systems for thin-film characterization, sustaining 10+ samples
  per week with same-day results for 5+ users.
• Troubleshoot vacuum leaks, alignment drift, electronics failures, and motor step loss, then verify fixes with a post-repair hBN
  run against fit residual within the historical baseline band and calibrant peak positions show no systematic offset across the
  detector.
• Wrote and versioned SOPs and checklists for calibrant-based alignment and geometry verification to standardize setups across
  users.
• Built Python pipelines that decode hex-encoded raw detector frames into 2D images, apply QA gates anchored to hBN (fit
  residual within the historical baseline band and calibrant peak positions show no systematic offset across the detector), and
  emit standard outputs for integration and reciprocal-space slicing, yielding fewer alignment iterations to reach fit residual
  within the historical baseline band and calibrant peak positions show no systematic offset across the detector and tighter
  uncertainty on disorder and polytype fraction fits and better cross-session repeatability.
• Developed forward simulations and MCMC refinement for geometric misalignment and sample parameters (20+ parameters;
  10 minutes per fit), optimizing pixel-wise residual between measured and simulated 2D intensity (weighted least squares)
  with residual diagnostics to support enables geometry transfer from hBN fits to sample runs, avoiding geometry artifacts and
  stabilizing extracted disorder, structure, and polytype fractions.
• Grew PbI2 films and intercalated structures via CVD and Bi2 Se3 /Bi2 Te3 via ALD, then characterize with XRD/XRR/GIWAXS,
  Raman, SEM/EDS, TEM, and profilometry and quantify phase or polytype fractions via simulation-based fitting. [Publication
  Link]

Research Assistant, Thin-Film PLD Design & Characterization                                                      2017 to 2020
Missouri State University, Springfield, MO

• Designed and built a pulsed laser deposition system (vacuum hardware, optics alignment, controls, diagnostics), then supported
  operation and resolved failures during experiments.
• Characterized thin films using XRD, Raman, SEM/EDS, TEM, and profilometry, maintaining run logs and analysis notes for
  reproducible comparisons across runs.

Research Intern, Thin-Film Deposition & Diagnostics                                                              2019 to 2020
NASA Space Consortium

• Grew Pb-based perovskite thin films via PLD and characterized with SEM, Raman, and profilometry to link process settings
  to morphology and film quality.
• Presented a year-end report summarizing process parameters, metrology procedures, and observed process–structure trends.

R&D Intern, Automated Test Systems Software                                                                                2019
Dynatek Labs

• Developed production software in Visual Basic Script and C for automated hardware test systems in biomedical manufacturing,
  including logging and fail-safe behavior.
• Produced an oven shutoff interlock for silicone bake processes, integrating hardware signals and safety logic, deployed on 2
  ovens and verified against a baseline shutdown check.
Selected Engineering Software
• 2D-Oriented Powder XRD Simulator (repo): DWBA forward model with refraction, footprint, and divergence corrections
  plus calibrant-driven geometry transfer and pseudo-Voigt mosaic distributions for quantitative 2D refinement.
• OSC_Reader (repo): Rigaku RAXIS .osc toolkit for raw-frame loading, interactive inspection, azimuthal integration, and
  peak fitting for homebuilt GIWAXAXS workflows.
• 2D Oriented Powder Visualizer (repo): visual tools for reciprocal-space rods and detector mapping used to explain
  ring–cap physics in talks and internal documentation.

Education
PhD, Physics (Expected)                                                                                       May 2026
University of Missouri, Columbia, MO
MS, Physics                                                                                                   May 2022
University of Missouri, Columbia, MO
BS, Physics                                                                                                   May 2020
Missouri State University, Springfield, MO                                                Minor: Mathematics, Chemistry

Honors
National Neutron Scattering Society Outstanding Student Research Prize (American Conference on Neutron Scattering invited
talk), 2023 | Graduate Professional Council Research & Creative Activity Forum Award (University of Missouri), Columbia,
MO, 2025
```
