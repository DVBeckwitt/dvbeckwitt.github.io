---
layout: project
title: Detector-space diffraction refinement
date: 2026-01-01
description: >
  Dissertation workflow for fitting and interpreting two-dimensional X-ray
  diffraction images from layered thin films without first collapsing the data
  into one-dimensional profiles.
caption: Forward-modeling workflow for diffraction images from 2D-oriented powders.
image:
  path: /assets/img/projects/detector-space-refinement.png
links:
  - title: Research context
    url: /research/
  - title: CV
    url: /cv/
featured: true
---

This is the central workflow behind my dissertation, _Investigating Disorder in van der Waals Thin Films_. It is designed for layered films that are neither single crystals nor fully random powders. The layer normal can remain aligned to the substrate while in-plane orientation, mosaic spread, and stacking disorder create structured intensity across a two-dimensional detector.

## Problem

A one-dimensional reduction can be convenient, but it discards the spatial relationship between specular spots, off-specular arcs, diffuse streaks, and detector geometry. Those patterns are often the evidence needed to separate alignment, mosaicity, phase content, and disorder.

## Approach

The workflow treats the detector image as the object to model. The forward model connects sample geometry, detector calibration, beam footprint, absorption, refraction, structure-factor weighting, mosaic spread, and stacking-disorder terms to simulated area-detector intensity.

Benchmark systems include ordered Bi<sub>2</sub>Te<sub>3</sub> and Bi<sub>2</sub>Se<sub>3</sub> thin films, which help separate geometry from structure. CVD-grown PbI<sub>2</sub> films provide the disorder-sensitive case, where diffuse intensity along Q<sub>z</sub> is used after the ordered scattering baseline has been established.

## Status and limits

This is an active dissertation framework, not a packaged public code release. The current value is methodological: it clarifies which structural parameters are learnable from measured detector images and which require stronger constraints, better calibration, or complementary measurements.
