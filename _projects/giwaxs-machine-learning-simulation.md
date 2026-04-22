---
layout: project
title: GIWAXS simulation and machine learning
date: 2025-09-01
description: >
  PyTorch-based research workflow that uses simulated GIWAXS images to train
  convolutional neural networks for automated structure-analysis screening.
caption: Simulated GIWAXS images used for machine-learning-assisted structure analysis.
image:
  path: /assets/img/projects/giwaxs-machine-learning.png
links:
  - title: Research context
    url: /research/
featured: true
---

This project pairs physical simulation with machine-learning-assisted image screening. The aim is not to replace a diffraction model with a black box. The aim is to make high-dimensional GIWAXS images easier to triage, compare, and interpret before more expensive fitting steps.

## Problem

GIWAXS detector images can change in several coupled ways when geometry, site occupancy, Debye-Waller factors, mosaicity, or disorder change. A researcher can often see that a pattern is different, but systematic screening across many candidate structures or simulated conditions becomes slow.

## Approach

The workflow trains convolutional neural networks on simulated GIWAXS data. Simulation gives controlled input parameters and known labels, while the neural network provides a fast pattern-recognition layer. Physical modeling remains the reference point for interpretation.

## Status and limits

This is an experimental research workflow rather than a stand-alone public package. Its strongest use is screening and hypothesis generation. Its main limitation is the same as any simulation-trained model: the training distribution must be close enough to the measured experiment to be meaningful.
