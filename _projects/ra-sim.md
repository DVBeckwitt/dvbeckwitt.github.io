---
layout: project
title: ra_sim
date: 2024-06-01
description: >
  Simulation and analysis software for diffraction data collected on R-Axis IV++
  area detectors, with a focused interface and detector-specific optimization.
caption: Detector-specific analysis tools for R-Axis IV++ diffraction data.
image:
  path: /assets/img/projects/ra-sim.png
links:
  - title: View source on GitHub
    url: https://github.com/DVBeckwitt/ra_sim
  - title: Research context
    url: /research/
redirect_from: /projects/ra-sim/
---

ra_sim is a detector-specific analysis project for R-Axis IV++ diffraction data. It reflects a practical part of my research style: build tools around the instrument and data format actually used in the lab, rather than forcing the experiment into a generic workflow too early.

## Problem

Area-detector data are shaped by detector geometry, calibration choices, instrument configuration, and file format constraints. Those details matter when comparing measured patterns with simulated ones or when setting up optimization around a specific detector.

## Approach

The project combines simulation and analysis routines with optimization methods tailored to the R-Axis IV++ context. The goal is a focused workflow for detector images where the analysis code and the experimental geometry remain coupled.

## Status and limits

This is active research software. It is strongest as a lab-specific analysis and simulation aid. It is not presented as a general replacement for established crystallographic software.
