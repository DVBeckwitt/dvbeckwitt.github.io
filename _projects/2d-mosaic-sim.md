---
layout: project
title: 2D Powder Visualizer
date: 2021-01-01
description: >
  Python visualization tools for showing how orientation distributions and
  mosaic spread reshape two-dimensional diffraction patterns.
caption: Visualization tools for orientation and mosaic-spread effects in 2D diffraction.
image:
  path: /assets/img/projects/2d-mosaic-sim.png
links:
  - title: View source on GitHub
    url: https://github.com/DVBeckwitt/2D_Mosaic_Sim
  - title: Research context
    url: /research/
featured: true
redirect_from: /projects/2d-mosaic-sim/
---

2D Powder Visualizer is a Python research tool for visualizing how orientation distributions and mosaic spread appear in two-dimensional diffraction patterns. It sits between simple conceptual sketches and the more detailed detector-space models used in my dissertation work.

## Problem

Layered thin films often produce diffraction that is ordered in one direction and partially disordered in another. The result is not just a set of peaks. It can be arcs, spots, broadened features, and orientation-dependent intensity across a detector image.

## Approach

The project focuses on simulation and custom plotting. It helps connect assumed orientation distributions to visible diffraction features, which makes it useful for reasoning about mosaic spread, preferred orientation, and the limits of standard one-dimensional views.

## Status and limits

This is active research code. It is useful for visualization, interpretation, and model development, but it should not be read as a finished instrument-neutral crystallography package.
