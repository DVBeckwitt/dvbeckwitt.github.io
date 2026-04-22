---
layout: project
title: OSC_Reader
date: 2024-01-01
description: >
  A detector-file converter for reading proprietary OSC diffraction images and
  converting them into accessible formats for inspection and analysis.
caption: Converter for inspecting proprietary detector images without commercial software.
image:
  path: /assets/img/projects/osc-reader.png
links:
  - title: View source on GitHub
    url: https://github.com/DVBeckwitt/OSC_Reader
redirect_from: /projects/osc-reader/
---

OSC_Reader is a small utility built around a common experimental bottleneck: diffraction images are not useful if they are locked inside a file format that is hard to inspect or process outside vendor software.

## Problem

Detector files can be technically valid and still be inconvenient for research. If an image cannot be opened, converted, checked, plotted, or passed into an analysis workflow, then basic quality control becomes slow.

## Approach

The project converts proprietary detector files into accessible formats. That makes it easier to inspect diffraction images, verify that measurements look reasonable, and connect raw detector output to Python-based analysis.

## Status and limits

This is a focused converter and inspection aid. Its value is workflow access. It is not intended to be a full diffraction-analysis package by itself.
