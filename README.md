# Quantitative Modelling of Biological Response Dynamics

This repository contains the fitting notebook, submission datasets, reference outputs, and supporting scripts for the manuscript:

**"Quantitative modelling of biological response dynamics reveals novel patterns in plant volatile signalling"**

The current repository still centers on the notebook, but it now also includes explicit planning and regression tools for converting the work into a submission-ready, script-driven project without changing numerical outputs.

## Current State

The main working file is:

- `Quantitative_modelling of_biological_response_dynamics_Submitted_Code_elife2.ipynb`

This notebook currently:

- loads root-level `*_sub.csv` input files
- cleans and reconstructs emission signals
- fits single-curve and triple-curve gamma models
- exports flattened result CSVs into `Submitted_results/`

The notebook is also the current source of truth for exact submission behavior.

## What the Model Produces

For each response curve, the workflow estimates:

- `R_peak`
- `t_onset`
- `t_peak`
- `t_mean`

From these it derives:

- `integral`
- `duration`
- `shape`

Fitting uses a two-stage optimizer:

- `scipy.optimize.differential_evolution`
- `scipy.optimize.minimize(..., method='SLSQP')`

The DE stage is currently seeded (`seed=42`) so repeated runs are reproducible under the same environment.

## Repository Contents

- `Quantitative_modelling of_biological_response_dynamics_Submitted_Code_elife2.ipynb`
  - main analysis and fitting notebook
- `Quantitative modelling of biological response dynamics reveals novel patterns in plant volatile signalling.pdf`
  - manuscript/preprint
- `compare_results.py`
  - regression comparison tool for outputs
- `project_plan.md`
  - human-oriented conversion plan for restructuring the repository
- `AGENTS.md`
  - instructions for an LLM/code agent performing the conversion
- `Submitted_results/`
  - current generated outputs
- `Submitted_results Ref/`
  - reference copy used to confirm output equivalence

## Input Data

The notebook currently uses these project-root input files:

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

Most datasets contain:

- `Emission`
- `Channel_number`
- `comp`
- `time`
- `Type`

And metadata such as:

- `d1_time`
- `d2_time`
- `intensity1`
- `Totalbio`
- `Leaf3`

## Outputs and Regression Check

Generated result files are written to:

- `Submitted_results/`

To check whether a refactor preserves exact output behavior, compare against the reference copy:

```bash
python compare_results.py "Submitted_results" "Submitted_results Ref"
```

This comparison is the current regression test for the project. The submission refactor should be considered correct only if it reproduces the same outputs.

## Environment

Current dependencies are listed in:

- `requirements.txt`

Typical setup:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## How the Notebook Is Organized

The notebook is arranged roughly by manuscript figure:

1. model, cleaning, fitting, and export utilities
2. Figure 1 theoretical behavior
3. Figure 2 single-damage experiments
4. Figure 3 oral secretion analyses across compounds
5. Figure 4 triple-damage and real-herbivore analyses
6. supplementary GLV, gene-expression, shortened-window, and downsampled analyses

Several parameter configs have already been consolidated into shared per-compound definitions inside the notebook for:

- `DMNT`
- `indole`
- `TMTT`
- `sesq`
- `mono`

## Important Notes

- The notebook is still the authoritative implementation.
- The repository is under Git and now includes planning documents for converting the codebase into a package plus script runner.
- `Submitted_results Ref/` is ignored by Git and exists specifically to validate that future refactors do not change outputs.
- `compare_results.py` is intended to be used repeatedly during the conversion to a public submission structure.

## Planned Direction

The intended next step is to move from a notebook-only workflow to a repository with:

- reusable code under `src/emission_model/`
- a command-line runner under `scripts/`
- analysis definitions in config
- the notebook retained for exploration only

That plan is documented in:

- `project_plan.md`
- `AGENTS.md`

## Citation

If you use this repository, cite the manuscript PDF included here:

- Waterman JM, Moore GJ, Amdahl-Culleton LK, Hoefer S, Erb M.
  *Quantitative modelling of biological response dynamics reveals novel patterns in plant volatile signalling.*
