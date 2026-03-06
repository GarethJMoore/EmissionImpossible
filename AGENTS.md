# AGENTS.md

Purpose

Practical operating guide for future code agents working in this repository.

Current State (as of 2026-03-06)

- A script pipeline exists and is runnable:
  - `scripts/run_analysis.py`
  - `src/emission_model/`
- Input data is in:
  - `data/*_sub.csv`
- Outputs are written to:
  - `results/Submitted_results/`
- Reference outputs are in:
  - `tests/regression/reference/`
- Regression comparator:
  - `tests/regression/compare_results.py`

Non-Negotiable Rule

Treat any output difference as a regression unless the user explicitly approves it.

Required Validation Command

After changing pipeline/model code, run:

`python tests/regression/compare_results.py "results/Submitted_results" "tests/regression/reference"`

Expected result:

`No differences found.`

Notebook Policy

- Keep the notebook available:
  - `notebooks/Quantitative_modelling_of_biological_response_dynamics_Submitted_Code_elife2.ipynb`
- Do not modify notebook logic unless the user explicitly asks.
- Prefer changes in `src/` + `scripts/` and validate with regression checks.

How To Run

Run full pipeline:

`python scripts/run_analysis.py`

Run one analysis:

`python scripts/run_analysis.py --analysis dmnt_dose`

Notes:

- The runner resolves `data/`, `results/`, and config paths relative to repo root, so it can be launched from outside the repo directory.

Safe Working Style

1. Small, validated changes.
2. Preserve parameter bounds, filtering, and file naming unless instructed.
3. Prefer explicit code over abstractions that could hide behavior changes.
4. Report exactly what was changed and whether regression checks passed.

When In Doubt

Use existing pipeline functions in:

- `src/emission_model/pipelines.py`
- `src/emission_model/fitting.py`
- `src/emission_model/cleaning.py`
- `src/emission_model/model.py`

and prove equivalence with `tests/regression/compare_results.py` before claiming completion.
