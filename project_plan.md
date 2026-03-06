# Project Plan

## Convert Notebook Workflow into a Reproducible Submission Repository

## Goal

Convert the current notebook-centered project into a GitHub-ready repository that:

1. Accepts the current input datasets as they exist now.
2. Produces the same result files as the current notebook workflow.
3. Preserves the notebook as an exploratory environment.
4. Exposes a clear, reproducible, script-driven pipeline for paper submission.

The success condition is not just "the code runs". The success condition is:

- the refactored pipeline runs from command line
- it generates the expected output files
- those outputs match the current reference outputs
- the notebook remains available for exploratory work

## Non-Negotiable Constraint

This refactor must preserve exact output behavior for the current submission datasets.

Current reference behavior is represented by:

- input datasets in project root (`*_sub.csv`)
- current output folder `Submitted_results/`
- reference copy `Submitted_results Ref/`
- regression comparison script `compare_results.py`

The refactor is complete only when newly generated outputs can be compared against the reference outputs and all comparisons pass.

## Target Repository Shape

Recommended target layout:

```text
project/
  README.md
  requirements.txt
  AGENTS.md
  compare_results.py
  scripts/
    run_analysis.py
  configs/
    analyses.yaml
  src/
    emission_model/
      __init__.py
      model.py
      cleaning.py
      fitting.py
      io.py
      configs.py
      pipelines.py
  notebooks/
    exploration.ipynb
  tests/
  Submitted_results/
  Submitted_results Ref/
```

Notes:

- The notebook should remain in the repository, but it should stop being the canonical source of the implementation.
- The reusable code should move into `src/emission_model/`.
- The final pipeline should be runnable without opening Jupyter.

## Recommended Module Responsibilities

### `src/emission_model/model.py`

- `model_gamma`
- `shape`
- `duration`
- `total_integral_model_gamma`

### `src/emission_model/cleaning.py`

- `reconstruct_with_svd`
- `subtract_background`
- `clean_and_reconstruct`

### `src/emission_model/fitting.py`

- `run_de_then_slsqp`
- `r_squared`
- `process_single_group`
- `process_single_group_three`

### `src/emission_model/io.py`

- input loading helpers
- results flattening
- `save_results_to_csv`

### `src/emission_model/configs.py`

- shared parameter configs
- per-compound reusable parameter dictionaries

### `src/emission_model/pipelines.py`

- high-level analysis runners
- logic for applying one config to one dataset/compound
- orchestration for single-curve and triple-curve analyses

### `scripts/run_analysis.py`

- command-line entry point
- reads config
- runs analyses
- writes results to output folder

## Configuration Strategy

Do not hardcode figure-by-figure execution in the runner.

Instead, define analyses in a config file. Each analysis entry should specify:

- input file path
- output file name
- preprocessing options
- whether background subtraction is enabled
- normalization column if any
- single-curve or triple-curve mode
- compound name
- allowed type labels or filter logic
- parameter config name
- `lambda_prior`

This allows the exact notebook workflow to be represented declaratively rather than by copied code blocks.

## Migration Strategy

### Phase 1: Freeze current behavior

- Keep the current notebook unchanged as the source of truth for behavior.
- Treat `Submitted_results Ref/` as the expected-output reference.
- Use `compare_results.py` as the regression oracle.

### Phase 2: Extract core functions

- Move pure reusable functions from notebook into `src/emission_model/`.
- Do not change function behavior during extraction.
- Preserve signatures where practical until the pipeline is stable.

### Phase 3: Extract shared configuration

- Move parameter configs into `src/emission_model/configs.py`.
- Move analysis definitions into `configs/analyses.yaml`.
- Encode current dataset-specific choices exactly as they exist now.

### Phase 4: Build runner

- Implement `scripts/run_analysis.py`.
- It should reproduce the current outputs using the extracted modules and config file.
- It should be able to run all analyses in one command.

### Phase 5: Regression validation

- Generate outputs into `Submitted_results/`.
- Compare against `Submitted_results Ref/` using `compare_results.py`.
- Any mismatch must be investigated before further cleanup.

### Phase 6: Rewire notebook

- Convert the notebook so it imports from `src/emission_model/` instead of defining core functions inline.
- Keep notebook plotting and exploration logic if useful.
- Do not make notebook cleanup the blocking item for submission reproducibility.

## Rules for the Refactor

1. Preserve behavior before improving style. The first working refactor should be boring and literal. Avoid cleanups that change data flow, defaults, bounds, or filtering until the regression test passes.
2. Separate exploratory logic from submission logic. The notebook may keep exploratory cells and plotting convenience code. The submission pipeline should be script-driven and minimal.
3. Keep the pipeline data-driven. New analyses should be added by configuration, not by duplicating large code blocks.
4. Do not optimize prematurely. Exact reproducibility matters more than elegance during extraction.
5. Regression checks are mandatory. Use `compare_results.py` after every substantial pipeline change.

## Minimum Acceptance Criteria

The conversion is complete when all of the following are true:

1. A command such as the following works:

   ```bash
   python scripts/run_analysis.py --config configs/analyses.yaml
   ```

2. The command produces the expected output files in `Submitted_results/`.
3. Running:

   ```bash
   python compare_results.py "Submitted_results" "Submitted_results Ref"
   ```

   reports no differences.

4. The repository README explains:

- required inputs
- how to run the pipeline
- where outputs are written
- how to validate outputs against the reference folder

5. The notebook still works as a development/exploration surface.

## Suggested Implementation Order

1. Create package skeleton under `src/emission_model/`.
2. Move core model functions.
3. Move cleaning functions.
4. Move fitting functions.
5. Move result export helpers.
6. Encode current shared parameter configs.
7. Encode current analyses in YAML or Python config.
8. Implement command-line runner.
9. Run pipeline and compare outputs.
10. Only after passing comparison, simplify notebook imports.

## Testing Guidance

At minimum, use three levels of validation:

1. Smoke tests
- script runs without crashing
- result files are written

2. Structural checks
- expected files exist
- expected columns exist

3. Regression checks
- compare generated files with `Submitted_results Ref/`

The regression check is the most important test for this project.

## Known Practical Considerations

- The current notebook is the authoritative record of exact logic.
- Some analysis sections are intentionally specialized.
- Shared parameter configs have already been partially consolidated.
- The GLV, triple-damage, and shortened/downsampled analyses may need special-case config entries.
- Input file names in the public pipeline should match the current project-root `*_sub.csv` files unless there is a deliberate migration step.

## Deliverables

The engineer performing this conversion should aim to produce:

- a runnable package under `src/emission_model/`
- a script-driven pipeline under `scripts/run_analysis.py`
- a config-driven analysis definition file
- an updated README
- a preserved notebook for exploration
- exact-output regression compatibility with `Submitted_results Ref/`

## Definition of Done

This project is ready for paper-code submission when a third party can:

1. install dependencies
2. run the provided analysis command
3. reproduce the paper result CSVs
4. validate that reproduction using `compare_results.py`
5. inspect the notebook for exploratory context without needing it for the core submission workflow
