# AGENTS.md

Purpose

This repository is being converted from a notebook-centered research workflow into a GitHub-ready paper-code repository.

The primary requirement is exact reproducibility of current outputs for the current submission datasets.

You must treat the current notebook behavior as the source of truth unless the user explicitly instructs otherwise.


Core Objective

Refactor the project so that:

- input data can be processed through a script-driven pipeline,
- the same outputs currently produced by the notebook are reproduced,
- the notebook remains available for exploration and fitting work,
- the final structure is suitable for public GitHub release.


Critical Constraint

Do not accept "close enough" output.

The repository contains a regression comparison tool:

- `compare_results.py`

It also contains:

- current outputs in `Submitted_results/`
- reference outputs in `Submitted_results Ref/`

Any refactor that changes outputs must be treated as a regression unless the user explicitly approves the change.


What Success Looks Like

The conversion is successful only if:

1. A script-based runner can generate outputs from the current input data.
2. Generated outputs match the reference outputs.
3. `python compare_results.py "Submitted_results" "Submitted_results Ref"` reports no differences.


Required Working Style

1. Preserve behavior before improving design.

Extract functions first. Avoid changing defaults, parameter bounds, filtering logic, file names, or data flow unless necessary.

2. Use regression checks constantly.

After any substantial refactor to the pipeline, regenerate outputs and compare them against the reference folder.

3. Keep the notebook usable.

The notebook may remain as a consumer of the extracted package. It does not need to remain the canonical implementation.

4. Prefer explicit over clever.

This is scientific code for submission. Readability and reproducibility matter more than abstraction density.

5. Avoid silent behavior changes.

If a cleanup could alter numerical output, treat it as risky and validate it immediately.


Repository Intent

Target architecture:

- reusable package under `src/emission_model/`
- command-line runner under `scripts/`
- analysis definitions in config
- exploratory notebook kept separately

Likely module split:

- `model.py`
- `cleaning.py`
- `fitting.py`
- `io.py`
- `configs.py`
- `pipelines.py`


Required Validation Workflow

When changing pipeline code:

1. run the pipeline
2. regenerate outputs into `Submitted_results/`
3. run:

   `python compare_results.py "Submitted_results" "Submitted_results Ref"`

4. if any differences appear, stop and identify why

Do not claim the refactor is complete before this comparison passes.


Do Not Do These Things

- Do not delete the notebook unless explicitly asked.
- Do not replace exact output matching with approximate similarity.
- Do not rename input files casually.
- Do not rewrite scientific logic just to make it prettier.
- Do not collapse experiment-specific behavior into generic code unless regression checks confirm equivalence.


Preferred Conversion Order

1. Freeze the notebook behavior as reference.
2. Extract core pure functions into `src/emission_model/`.
3. Extract parameter configs into a shared config module.
4. Encode per-analysis settings in a config file.
5. Implement a script-driven runner.
6. Reproduce outputs.
7. Validate outputs with `compare_results.py`.
8. Rewire notebook imports after the script pipeline is stable.


Expected Engineering Standard

The final repo should allow a user to:

1. install dependencies
2. run one command to generate outputs
3. inspect outputs in `Submitted_results/`
4. compare outputs against `Submitted_results Ref/`
5. use the notebook for exploration if desired


Communication Expectations

If acting as an LLM agent:

- explain planned structural changes before making them
- surface risks that could alter outputs
- explicitly state when regression checks were run
- report mismatches concretely
- prefer small validated steps over broad rewrites


Definition of Done

The work is done when the repository is organized for public submission and the script-generated outputs match the reference outputs exactly.
