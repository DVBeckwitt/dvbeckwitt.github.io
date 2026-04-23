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
[Publications & Talks](/outputs/){:.btn}
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

## Outputs

Selected papers, manuscripts, talks, and posters are collected on [Publications & Talks](/outputs/). The CV remains the full formal record.

[View publications and talks](/outputs/){:.btn}

## Earlier work

Earlier materials work included graphene, oxide thin films, pulsed laser deposition, vapor deposition, Raman spectroscopy, SEM, EDS, profilometry, and diffraction. That background informs the current emphasis on connecting detector data to real growth and characterization constraints.
