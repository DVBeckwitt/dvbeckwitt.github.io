---
layout: project
title: 2D_Mosaic_Sim
date: 2025-01-01
description: >
  Python tools for simulating and visualizing X-ray diffraction patterns from
  materials with specified crystal orientations and mosaic spread.
caption: X-ray diffraction simulation tools for oriented materials.
image:
  path: /assets/img/projects/2d-mosaic-sim.png
links:
  - title: View source on GitHub
    url: https://github.com/DVBeckwitt/2D_Mosaic_Sim
  - title: Research context
    url: /research/
featured: true
---

2D_Mosaic_Sim is a Python research tool for visualizing how specified crystal orientations appear in X-ray diffraction patterns. It sits between simple conceptual sketches and the more detailed detector-space models used in my dissertation work.

## Problem

Layered thin films often produce diffraction that is ordered in one direction and partially disordered in another. The result is not just a set of peaks. It can be arcs, spots, broadened features, and orientation-dependent intensity across a detector image.

## Approach

The project focuses on simulation and custom plotting. It helps connect assumed orientation distributions to visible diffraction features, which makes it useful for reasoning about mosaic spread, preferred orientation, and the limits of standard one-dimensional views.

## Status and limits

This is active research code. It is useful for visualization, interpretation, and model development, but it should not be read as a finished instrument-neutral crystallography package.
