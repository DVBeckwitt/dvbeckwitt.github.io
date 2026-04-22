---
layout: page
title: Research
description: >
  Research by David Beckwitt on quantitative X-ray diffraction, layered
  van der Waals thin films, detector-space modeling, and computational
  analysis of disorder.
permalink: /research/
accent_image: /assets/img/research-sidebar-bg.jpg
menu: true
order: 2
---

My research develops quantitative X-ray diffraction and GIWAXS methods for layered van der Waals thin films. These films often sit between the textbook limits of a single crystal and a fully random powder: the layer normal remains aligned to the substrate, while in-plane orientation, mosaic spread, and stacking disorder create complex two-dimensional detector images.
{:.lead}

Rather than reducing an area-detector image to a one-dimensional profile at the start, I treat the full detector image as the primary object of inference. This keeps specular spots, off-specular arcs, and diffuse disorder-sensitive intensity available during modeling.

[Applied tools](#research-software){:.btn}
[Selected outputs](#selected-outputs){:.btn}
[CV](/cv/){:.btn}

## Dissertation Project

My dissertation, _Investigating Disorder in van der Waals Thin Films_, develops a detector-space framework for X-ray diffraction characterization and simulation of 2D-oriented powders. The method combines area-detector WAXS measurements with forward diffraction models that include beam geometry, detector calibration, sample alignment, finite footprint effects, refraction, absorption, structure-factor weighting, mosaicity, and stacking-disorder terms.

The central goal is practical: determine which structural parameters are learnable from measured diffraction images of layered thin films. Ordered Bi<sub>2</sub>Te<sub>3</sub> and Bi<sub>2</sub>Se<sub>3</sub> films serve as benchmark systems for separating geometry, alignment, mosaicity, and ordered structure. CVD-grown PbI<sub>2</sub> films provide the disorder-sensitive case, where diffuse intensity along Q<sub>z</sub> is used to quantify stacking-fault behavior after the ordered scattering baseline has been established.

## Current Research Themes

### Area-Detector X-ray Diffraction

I use area detectors to study diffraction patterns that contain both specular and off-specular information. In layered films with azimuthal disorder, off-specular reflections form arcs or ring segments, while specular reflections remain concentrated near the surface-normal direction. Preserving both signatures makes it possible to model oriented-powder behavior more quantitatively than a conventional one-dimensional reduction.

### Disorder in van der Waals Thin Films

Much of my recent work centers on PbI<sub>2</sub> and related hybrid halide perovskite films grown by chemical vapor deposition. These films grow with strong out-of-plane alignment but can develop rotational disorder and stacking faults because of weak van der Waals coupling between layers. My analysis links detector-image morphology to orientational order, phase content, and stacking-disorder parameters.

### Computational Modeling and Machine Learning

I write Python-based simulation and analysis tools for diffraction images, detector calibration, and parameter refinement. Current work also uses simulated GIWAXS data to train machine-learning models for automated structure analysis. The goal is not to replace physical modeling. It is to make high-dimensional diffraction images easier to screen, interpret, and fit.

## Materials and Questions

| Materials system | Structural question | Primary methods |
|:--|:--|:--|
| Bi<sub>2</sub>Te<sub>3</sub> and Bi<sub>2</sub>Se<sub>3</sub> thin films | How do geometry, alignment, and mosaicity appear in ordered layered films? | Area-detector WAXS, detector calibration, forward modeling |
| CVD-grown PbI<sub>2</sub> thin films | How do stacking faults and rotational disorder appear in detector-space intensity? | GIWAXS, diffuse scattering models, CVD growth control |
| Hybrid halide perovskite films | How do growth orientation and phase stability depend on processing and structure? | XRD, GIWAXS, phase analysis, thin-film characterization |
{:.stretch-table}

## Selected Outputs

### Journal Articles

- [Insights into the Growth Orientation and Phase Stability of Chemical-Vapor-Deposited Two-Dimensional Hybrid Halide Perovskite Films](https://doi.org/10.1021/acsami.3c14559), _ACS Applied Materials & Interfaces_, 2023.

### In Preparation

- _Quantitative Simulation and Refinement of Diffraction from 2D-Oriented Powders_, anticipated Summer 2026.

### Selected Presentations

- [X-Ray Diffraction Investigation into CVD-Grown van der Waals Films: Disorder and Structure](https://www.researchgate.net/publication/393794708_X-Ray_Diffraction_Investigation_into_CVD-Grown_van_der_Waals_Films_Disorder_and_Structure), presentation, 2025.
- [Diffraction Investigation of van der Waals Thin Films Using an Area Detector](https://www.researchgate.net/publication/381800645_Diffraction_Investigation_of_van_der_Waals_Thin_Films_Using_an_Area_Detector), ACNS poster, 2024.
- [X-Ray Diffraction Investigation of Disorder in van der Waals Thin Films](https://calendardeploy.missouristate.edu/event/123195), Missouri State University PAMS seminar, 2024.
- [Quantifying Orientational Order of PbI<sub>2</sub> van der Waals Films with X-ray Diffraction using an Area Detector](https://www.researchgate.net/publication/377264935_Quantifying_Orientational_Order_of_PbI2_van_der_Waals_Films_with_X-ray_Diffraction_using_an_Area_Detector), APS Prairie Section presentation, 2023.

More outputs and presentation records are available on my [ResearchGate profile](https://www.researchgate.net/profile/David-Beckwitt-3).

## Research Software

- [2D_Mosaic_Sim](https://github.com/DVBeckwitt/2D_Mosaic_Sim): X-ray diffraction simulator for visualizing diffraction patterns from materials with specified crystal orientations.
- [ra_sim](https://github.com/DVBeckwitt/ra_sim): analysis and simulation tools for diffraction data from R-Axis IV++ detectors.
- [OSC_Reader](https://github.com/DVBeckwitt/OSC_Reader): converter for proprietary detector files into accessible formats for image inspection and analysis.

## Earlier Materials Work

Before my current dissertation project, I worked on thin-film synthesis and characterization in graphene, transition-metal oxides, and related materials systems. That work included pulsed laser deposition, chemical and physical vapor deposition, Raman spectroscopy, SEM, EDS, profilometry, and X-ray diffraction.

Those projects shaped the practical emphasis of my current research: build models and tools that stay close to real instrument behavior and real experimental data.
