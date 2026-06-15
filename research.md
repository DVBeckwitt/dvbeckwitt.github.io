---
layout: projects
title: Research
description: >
  Dissertation research on detector-space X-ray diffraction simulation,
  2D-oriented powders, layered thin-film disorder, and quantitative WAXS analysis.
permalink: /research/
image:
  path: /assets/img/research/thesis-2d-oriented-powder.png
  width: 1600
  height: 528
accent_image: /assets/img/research-sidebar-bg.jpg
menu: true
order: 2
show_collection: projects
no_groups: true
---

My dissertation asks what can be learned from a two-dimensional X-ray detector image before the data are collapsed into a one-dimensional curve.
{:.lead}

The work focuses on layered thin films in the 2D oriented-powder regime. The layer normal remains approximately aligned to the substrate normal, while the in-plane azimuthal orientation is distributed across crystallites. That mixed order produces detector images with specular features, off-specular arcs, ring segments, and diffuse intensity. Those features carry information about geometry, mosaicity, ordered structure, and stacking disorder.

[Research projects](#research-projects){:.btn}
[Publications & Talks](/outputs/){:.btn}

<figure class="research-figure research-figure--lead">
  <img
    src="/assets/img/research/thesis-2d-oriented-powder.png"
    alt="Schematic of 2D-oriented powder crystallites with layer normals aligned and in-plane orientations distributed."
    width="1600"
    height="528"
    loading="eager"
  />
  <figcaption>
    Thesis Fig. 2.1. The central sample class is a 2D oriented powder: ordered enough to preserve a preferred axis, but azimuthally distributed enough that single-crystal assumptions are too narrow.
  </figcaption>
</figure>

## Thesis frame

The thesis is titled _X-ray Diffraction Characterization and Simulation of 2D-Oriented Powders_. It develops a method-first framework for area-detector WAXS and GIWAXS analysis of layered films that sit between single crystals and fully random powders.

The central choice is to keep the detector image close to the model. A one-dimensional reduction can be useful, but it can also discard the spatial relationship between specular spots, off-specular arcs, diffuse streaks, detector geometry, and sample alignment. The dissertation instead treats the detector image as the primary object of inference, then uses transformed or integrated views only when they isolate a specific constraint.

## Experimental and calibration basis

The framework starts by separating instrument geometry from sample-specific interpretation. Representative hBN calibration images constrain detector center, detector distance, and detector tilt before layered-film parameters are released. Sample alignment and off-centering terms are handled before mosaicity, ordered structure, or disorder are interpreted.

<figure class="research-figure">
  <img
    src="/assets/img/research/thesis-hbn-calibration.png"
    alt="Measured hBN calibration image, optimized ring simulation, and overlay used to constrain detector geometry."
    width="1280"
    height="385"
    loading="lazy"
  />
  <figcaption>
    Thesis Fig. 3.1. Calibration is treated as an upstream inference problem. The hBN ring pattern fixes detector geometry so later film-specific fits are not asked to absorb instrument error.
  </figcaption>
</figure>

## Forward model

The forward calculation links the experimental geometry to detector intensity. It retains beam phase space, detector calibration, sample alignment, finite footprint, refraction, absorption, structure-factor weighting, and mosaic redistribution inside one detector-image calculation. The goal is not to replace physical interpretation with image matching. The goal is to put the experimental state, the instrument state, and the structural hypothesis in the same coordinate system.

<figure class="research-figure">
  <img
    src="/assets/img/research/thesis-mosaic-redistribution.png"
    alt="Four-panel thesis figure showing specular-cap and off-specular-arc mosaic redistribution on diffraction geometry and outgoing-ray maps."
    width="1542"
    height="1102"
    loading="lazy"
  />
  <figcaption>
    Thesis Fig. 5.2. Mosaicity does not appear as a single generic blur. Specular and off-specular features sample different parts of the misorientation distribution, which is why detector-space morphology matters.
  </figcaption>
</figure>

## Sequential refinement workflow

The fitting strategy is staged. Beam and detector parameters are established first. Sample alignment, mosaic/profile terms, ordered scattering, and disorder terms are then introduced in sequence. This staged workflow reduces parameter correlations that would otherwise make different physical effects look interchangeable.

<figure class="research-figure">
  <img
    src="/assets/img/research/thesis-geometry-identifiability.png"
    alt="Heatmap of local geometry-parameter sensitivity showing how detector-space summary metrics respond differently to geometry parameters."
    width="1400"
    height="1313"
    loading="lazy"
  />
  <figcaption>
    Thesis Fig. 5.1. Local detector-space sensitivity tests show that detector center, distance, and tilt-like parameters perturb visible peak fields in different combinations. That supports staged release of parameter classes during refinement.
  </figcaption>
</figure>

## Application I: ordered Bi<sub>2</sub>Te<sub>3</sub> and Bi<sub>2</sub>Se<sub>3</sub> films

Ordered MBE-grown Bi<sub>2</sub>Te<sub>3</sub> and Bi<sub>2</sub>Se<sub>3</sub> films are the ordered-limit benchmark. They test whether the same detector-space formulation can recover geometry, alignment, mosaicity, and ordered structure consistently without introducing a stacking-disorder term.

The important point is methodological. The ordered systems establish what the model can explain with calibration, alignment, mosaic redistribution, and ordered scattering alone. They also create a baseline for deciding when an additional disorder model is required.

<figure class="research-figure">
  <img
    src="/assets/img/research/thesis-ordered-detector-summary.png"
    alt="Detector-space measured, simulated, and residual comparisons for ordered Bi2Te3 and Bi2Se3 films, with profile and Qz checks."
    width="1600"
    height="1095"
    loading="lazy"
  />
  <figcaption>
    Thesis Fig. 6.1. Ordered-film fits compare measured detector views, simulated detector views, residuals, local profile checks, and post-fit Q<sub>z</sub> intensity checks under one staged model state.
  </figcaption>
</figure>

## Application II: stacking disorder in PbI<sub>2</sub> films

CVD-grown PbI<sub>2</sub> films provide the disorder-sensitive application. After the ordered baseline is fixed, systematic diffuse intensity along Q<sub>z</sub> remains unexplained. The dissertation therefore extends the model with stacking-disorder terms and compares a selected Q<sub>r</sub> rod profile against both the ordered baseline and the disorder-enabled model.

This case defines the boundary of the ordered-limit treatment. Some layered films require explicit stacking-disorder parameters before the detector image can be interpreted quantitatively.

<div class="research-figure-grid">
  <figure class="research-figure-card">
    <img
      src="/assets/img/research/thesis-pbi2-stacking-motifs.png"
      alt="Schematic 2H-like and 6H-like local stacking motifs used to motivate the PbI2 disorder model."
      width="1400"
      height="784"
      loading="lazy"
    />
    <figcaption>
      Thesis Fig. 7.1. Local 2H-like and 6H-like stacking motifs motivate the effective Hendricks-Teller rod model used for PbI<sub>2</sub>.
    </figcaption>
  </figure>

  <figure class="research-figure-card">
    <img
      src="/assets/img/research/thesis-pbi2-disorder-summary.png"
      alt="Selected-rod PbI2 disorder refinement showing caked detector-space mask, ordered baseline, disorder fit, and residual comparison."
      width="1600"
      height="1130"
      loading="lazy"
    />
    <figcaption>
      Thesis Fig. 7.2. The selected-rod comparison tests whether diffuse Q<sub>z</sub> intensity is explained after the ordered scattering baseline has been fixed.
    </figcaption>
  </figure>
</div>

## Main claim and limits

This research is about inference control. The detector image is not only a picture of a diffraction pattern. It is the place where instrument geometry, sample alignment, texture, mosaic spread, phase content, and disorder overlap. The thesis contribution is a workflow for separating those effects in a defensible order.

The strongest claim is limited and specific: for layered films in the 2D oriented-powder regime, full detector images can be used as the primary object of quantitative refinement when calibration is explicit, parameter classes are staged, and disorder is introduced only after the ordered baseline fails.

## Research projects

The project cards below connect the thesis workflow to software and analysis tools. Public GitHub projects outside this research program are listed on [Projects](/projects/).

- [Detector-space diffraction refinement](/research/detector-space-diffraction-refinement/) is the dissertation workflow for fitting two-dimensional diffraction images from layered films.
- [2D Powder Simulator](/research/ra-sim/) simulates detector-space diffraction from 2D-oriented powder films with geometry and model parameters tied to area-detector images.
- [2D Powder Visualizer](/research/2d-mosaic-sim/) visualizes how orientation distributions and mosaic spread reshape two-dimensional diffraction patterns.
- [Detector Data Pipeline](/research/osc-reader/) reads proprietary OSC detector images and converts them into accessible formats for inspection and downstream analysis.

## Outputs

Selected publications, talks, and posters are collected on [Publications & Talks](/outputs/). The CV remains the full formal record.

[View publications and talks](/outputs/){:.btn}
[Download CV](/cv/){:.btn}
