# Quantitative Modelling of Biological Response Dynamics

This repository contains the analysis notebook and supporting data used for the manuscript:

**"Quantitative modelling of biological response dynamics reveals novel patterns in plant volatile signalling"**

The core workflow fits dynamic biological response curves (primarily stress-induced maize volatile emissions) using a re-parameterized gamma model, then compares fitted descriptors across treatments, compounds, and experimental designs.

## What This Project Does

The notebook estimates four primary fit parameters for each emission curve:

- `R_peak`: maximum modeled response
- `t_onset`: onset delay
- `t_peak`: time of peak response
- `t_mean`: mean response time

From these, it derives additional descriptors used throughout the paper:

- `integral`: theoretical total response (area under curve)
- `duration`: response length (`t_mean - t_onset`)
- `shape`: normalized symmetry-like descriptor

The fitting approach combines:

- global optimization (`scipy.optimize.differential_evolution`)
- local constrained refinement (`scipy.optimize.minimize`, SLSQP)

It supports both:

- single-peak responses (most experiments)
- multi-peak responses (triple-damage experiment)

## Repository Layout

- `Quantitative_modelling of_biological_response_dynamics_Submitted_Code_elife2.ipynb`
  - Main analysis notebook (all methods + figure-specific analyses).
- `Quantitative modelling of biological response dynamics reveals novel patterns in plant volatile signalling.pdf`
  - Manuscript/preprint describing model rationale, experiments, and biological interpretation.
- `DataFolder/inputs/`
  - Raw/intermediate input CSV files and helper scripts.
- `DataFolder/inputs/Results_output/`
  - Existing exported fit outputs and helper Python modules (`Model.py`, viewer/plot widgets).
- `main.py`
  - Unrelated minimal script scaffold.

## Notebook Organization (Figure-by-Figure)

The notebook is structured in sections that mirror the manuscript figures:

1. **Model + utilities**
   - model definition (`model_gamma`)
   - descriptors (`shape`, `duration`, `total_integral_model_gamma`)
   - cleaning/reconstruction (`clean_and_reconstruct`, SVD helper, background subtraction)
   - fitting (`process_single_group`, `run_de_then_slsqp`)
   - plotting and export helpers

2. **Figure 1**
   - theoretical behavior of model descriptors

3. **Figure 2 (single damage experiments)**
   - dose dependence
   - time-of-day effects
   - oral secretion context (setup links to Figure 3)
   - leaf developmental stage
   - genotype comparison

4. **Figure 3 (OS, all compounds)**
   - DMNT, indole, TMTT, sesquiterpenes, monoterpenes

5. **Figure 4A-E (triple damage)**
   - multi-peak fitting implementation

6. **Figure 4F-I (real herbivore damage)**
   - single-peak fitting across multiple compounds

7. **Supplementary analyses**
   - GLV kinetics
   - gene-expression kinetics
   - robustness to shortened measurement windows
   - robustness to temporal downsampling

## Inputs and Data Mapping

The notebook currently references several files named like `*_sub.csv` (for example `singledose_sub.csv`) in the working directory.
These `*_sub.csv` files are now present in the project root and match the columns required by the notebook fitting functions.

Practical mapping used in this codebase:

- `singledose_sub.csv` -> `DataFolder/inputs/singledose.csv`
- `time_of_day_sub.csv` -> `DataFolder/inputs/singlecircadian.csv`
- `leaves_sub.csv` -> `DataFolder/inputs/Leaves.csv` (or `Leaves_unsorted.csv`, depending on preprocessing)
- `genotype_sub.csv` -> `DataFolder/inputs/genotypesyn.csv`
- `os_with_sub.csv` -> `DataFolder/inputs/os_with.csv`
- `os_without_sub.csv` -> `DataFolder/inputs/os_without.csv`
- `triple_sub.csv` -> `DataFolder/inputs/triple.csv`
- `herbreal_sub.csv` -> `DataFolder/inputs/herbreal.csv`
- `glvkin_sub.csv` -> `DataFolder/inputs/glvkin.csv`
- `genexpression_real_sub.csv` -> `DataFolder/inputs/genexpression_real.csv`

Most datasets use columns such as:

- `Emission`, `Channel_number`, `comp`, `time`, `Type`
- metadata columns like `d1_time`, `d2_time`, `intensity1`, `Totalbio`, `Leaf3`

Current root-level `*_sub.csv` inputs:

- `singledose_sub.csv`
- `time_of_day_sub.csv`
- `leaves_sub.csv`
- `genotype_sub.csv`
- `os_with_sub.csv`
- `os_without_sub.csv`
- `triple_sub.csv`
- `herbreal_sub.csv`
- `glvkin_sub.csv`
- `genexpression_real_sub.csv`

## Environment Setup

The notebook depends on:

- `numpy`
- `pandas`
- `matplotlib`
- `scipy`
- `scikit-learn`
- Jupyter

Recommended setup:

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install numpy pandas matplotlib scipy scikit-learn jupyter
jupyter notebook
```

Then open:

- `Quantitative_modelling of_biological_response_dynamics_Submitted_Code_elife2.ipynb`

## Running the Analysis

Because this project evolved over time, reproducibility is easiest if you:

1. Start in project root.
2. Confirm the root-level `*_sub.csv` inputs above are present (they are the filenames referenced directly by notebook cells).
3. Create output directory expected by notebook exports:
   - `Submitted_results/`
4. Run cells sequentially section-by-section.

The notebook prints channel-level fit quality (`R²`) and writes flattened result tables via `save_results_to_csv(...)`.

## Outputs

Generated outputs are CSV files containing per-timepoint exploded fit results, including modeled curves and descriptors.

In this repository, many previously generated result files already exist under:

- `DataFolder/inputs/Results_output/`

These include outputs for major compounds and analyses (dose, circadian, genotype, OS, herbivory, GLV, gene expression, and robustness tests).

## Key Findings Reflected in This Code + Paper

From the manuscript and notebook structure, the modeling framework is used to show that:

- time of wounding alters onset/duration/shape even when total emission is unchanged
- oral secretions reshape compound-specific dynamics beyond simple amplitude changes
- emission strength and response duration can vary independently across genotypes
- the framework remains informative under incomplete or lower-resolution sampling and for complex multi-peak responses

## Current Caveats

- The project is notebook-centric and monolithic; there is no single package entrypoint.
- There are two parallel input conventions (`*_sub.csv` in root and raw source files in `DataFolder/inputs/`), so keep paths consistent when re-running or refactoring.
- Output paths are hard-coded (`Submitted_results/`).
- Parameter bounds are often manually tuned per section/compound.
- A small type label mismatch appears in genotype filtering (`NC3000` in code vs `NC300` in data naming), so verify before reruns.

## Suggested Next Cleanup Steps

1. Move shared functions into a versioned Python module (`src/`).
2. Add a single config file that maps figure sections to input files and parameter bounds.
3. Add a deterministic runner script (CLI) for each figure.
4. Add environment lockfile (`requirements.txt` or `pyproject.toml`).
5. Add lightweight tests for model math and fitting constraints.

## Citation

If you use this code, cite the manuscript PDF in this repository:

- Waterman JM, Moore GJ, Amdahl-Culleton LK, Hoefer S, Erb M.
  *Quantitative modelling of biological response dynamics reveals novel patterns in plant volatile signalling.*

