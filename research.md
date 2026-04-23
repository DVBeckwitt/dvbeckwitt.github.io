---
layout: projects
title: Research
description: >
  Detector-space X-ray scattering, layered thin-film disorder, GIWAXS,
  and computational structure analysis.
permalink: /research/
image:
  path: /assets/img/social-card.jpg
  width: 1200
  height: 630
accent_image: /assets/img/research-sidebar-bg.jpg
menu: true
order: 2
show_collection: projects
no_groups: true
---

I ask what can be learned from an X-ray detector image before it is collapsed into a one-dimensional curve.
{:.lead}

Layered van der Waals films often sit between crystal and powder. Their layer normals stay aligned, while in-plane orientation, mosaic spread, and stacking sequence remain partly disordered. That mixed order is visible on the detector.

[Research projects](#research-projects){:.btn}
[Selected outputs](#selected-outputs){:.btn}
[CV](/cv/){:.btn}

<figure class="lead">
  <img
    src="/assets/img/research/detector-space-flow.svg"
    alt="Conceptual workflow from area-detector diffraction image to forward model to structural interpretation."
    width="1200"
    height="420"
    loading="lazy"
  />
  <figcaption>
    My work keeps the detector image close to the model: measured spots, arcs, and diffuse intensity are connected to instrument geometry and then to structural disorder.
  </figcaption>
</figure>

## What data?

The primary evidence is two-dimensional area-detector diffraction and GIWAXS imagery. Specular spots, off-specular arcs, and diffuse intensity each carry information that can disappear when the image is reduced too early.

## What materials?

Ordered Bi<sub>2</sub>Te<sub>3</sub> and Bi<sub>2</sub>Se<sub>3</sub> thin films set the geometric baseline. CVD-grown PbI<sub>2</sub> films provide the disorder-sensitive case, where weak interlayer coupling can produce rotational disorder, mosaic spread, and stacking faults.

## What model?

My dissertation, _Investigating Disorder in van der Waals Thin Films_, builds forward models that connect beam geometry, detector calibration, sample alignment, footprint effects, refraction, absorption, structure-factor weighting, mosaicity, and stacking-disorder terms to simulated detector intensity.

The model is not a replacement for physical interpretation. It is a way to keep the experiment, the instrument, and the structural hypothesis in the same coordinate system.

## What outputs?

The research is meant to estimate orientation, phase content, mosaic spread, and stacking-fault behavior while also marking the limits of what the detector image can determine without stronger constraints or complementary measurements.

## Research projects

The project cards below include dissertation workflows and research software. Public GitHub projects outside this research program are listed on [Projects](/projects/).

- [Detector-space diffraction refinement](/research/detector-space-diffraction-refinement/) connects measured detector intensity to geometry, orientation, mosaicity, and disorder parameters.
- [GIWAXS machine-learning simulation](/research/giwaxs-machine-learning-simulation/) explores simulated detector images for constrained screening and classification.
- [2D_Mosaic_Sim](/research/2d-mosaic-sim/) visualizes how crystal orientation and mosaic spread shape diffraction patterns.
- [ra_sim](/research/ra-sim/) supports simulation and analysis for R-Axis IV++ area-detector data.
- [OSC_Reader](/research/osc-reader/) converts proprietary OSC detector files into inspectable formats.

## Selected outputs

### Articles

- [Insights into the Growth Orientation and Phase Stability of Chemical-Vapor-Deposited Two-Dimensional Hybrid Halide Perovskite Films](https://doi.org/10.1021/acsami.3c14559), _ACS Applied Materials & Interfaces_, 2023.

### In preparation

- _Quantitative Simulation and Refinement of Diffraction from 2D-Oriented Powders_, anticipated Summer 2026.

### Presentations

- [X-Ray Diffraction Investigation into CVD-Grown van der Waals Films: Disorder and Structure](https://www.researchgate.net/publication/393794708_X-Ray_Diffraction_Investigation_into_CVD-Grown_van_der_Waals_Films_Disorder_and_Structure), 2025.
- [Diffraction Investigation of van der Waals Thin Films Using an Area Detector](https://www.researchgate.net/publication/381800645_Diffraction_Investigation_of_van_der_Waals_Thin_Films_Using_an_Area_Detector), ACNS poster, 2024.
- [X-Ray Diffraction Investigation of Disorder in van der Waals Thin Films](https://calendardeploy.missouristate.edu/event/123195), Missouri State University PAMS seminar, 2024.
- [Quantifying Orientational Order of PbI<sub>2</sub> van der Waals Films with X-ray Diffraction using an Area Detector](https://www.researchgate.net/publication/377264935_Quantifying_Orientational_Order_of_PbI2_van_der_Waals_Films_with_X-ray_Diffraction_using_an_Area_Detector), APS Prairie Section presentation, 2023.

More records are available on my [ResearchGate profile](https://www.researchgate.net/profile/David-Beckwitt-3).

## Earlier work

Earlier materials work included graphene, oxide thin films, pulsed laser deposition, vapor deposition, Raman spectroscopy, SEM, EDS, profilometry, and diffraction. That background informs the current emphasis on connecting detector data to real growth and characterization constraints.
