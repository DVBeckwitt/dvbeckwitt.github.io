---
layout: project
title: 2D Powder Simulator
date: 2021-01-01
description: >
  Detector-space diffraction simulation software for 2D-oriented powder films,
  with geometry and model parameters tied to area-detector images.
caption: Detector-space diffraction simulation for 2D-oriented powder films.
image:
  path: /assets/img/projects/ra-sim.png
links:
  - title: View source on GitHub
    url: https://github.com/DVBeckwitt/ra_sim
  - title: Research context
    url: /research/
redirect_from: /projects/ra-sim/
---

2D Powder Simulator is a Python research tool for simulating detector-space diffraction from 2D-oriented powder films. It reflects a practical part of my research style: keep experimental geometry, model parameters, and detector images connected while testing structural interpretations.

## Problem

Area-detector data are shaped by detector geometry, calibration choices, instrument configuration, and sample orientation. Those details matter when comparing measured patterns with simulated ones or setting up optimization around detector-space features.

## Approach

The project combines simulation and analysis routines with geometry-aware model parameters. The goal is a focused workflow where the simulated diffraction pattern and the measured detector image remain directly comparable.

## Status and limits

This is active research software. It is strongest as a dissertation-support tool for 2D-oriented powder analysis. It is not presented as a general replacement for established crystallographic software.
