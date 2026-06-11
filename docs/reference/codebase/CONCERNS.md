# SSVC Known Concerns

## High-priority concerns

### 1. Global registry with import-time side effects

`import ssvc` eagerly imports large parts of the package and auto-registers module-level objects into a process-global `SsvcObjectRegistry`.

Implications:
- test isolation depends on manual resets or local registry injection;
- importing seemingly harmless modules can mutate runtime state;
- future parallelism or lazy loading is harder.

### 2. Deprecated `DecisionPointGroup` is still active surface area

`dp_groups/` is deprecated in code and warnings, but it is still:
- imported by the package initializer;
- used by `policy_generator.py`;
- present in examples, schemas, tests, and some collections.

This creates a split model: preferred `DecisionTable` vs. still-supported legacy groups.

### 3. Generated-artifact discipline is easy to violate

Several important outputs are generated, committed, or both:
- `src/ssvc/utils/namespace_patterns.py`
- `data/json/`
- `data/schema/`
- CSV outputs under `data/csv/` and `data/csvs/`

Drift risk is real because Python source is authoritative but downstream artifacts are also stored in the repo and consumed by docs/workflows.

## Medium-priority concerns

### 4. CSV path inconsistency

The repository uses both `data/csv/` and `data/csvs/`:
- `doctools.py` writes to `data/csv/`
- `mkdocs.yml` table-reader plugin points at `data/csvs`
- `decision_tables/helpers.py` writes under `data/csvs`

Both directories exist, so behavior works, but the split is a maintenance hazard.

### 5. Pytest config mismatch

`pyproject.toml` sets `testpaths = ["test"]`, while the actual suite lives in `src/test/`.
Pytest currently recovers by searching recursively, but baseline runs emit a config warning.

### 6. Selection serialization warnings

Baseline tests pass, but `Selection` and `SelectionList` paths emit Pydantic warnings because tuple-typed `values` fields sometimes serialize from list-shaped data.
That is not a failure today, but it signals model-shape friction.

### 7. Spec tooling looks reusable but is still local copy

`metadata/specs/schema.py` and `metadata/specs/registry.py` both carry TODOs about extracting the spec-registry subsystem into a shared package.
Until that happens, SSVC owns a local implementation that may diverge from sibling projects.

## Lower-priority constraints

- The API is unauthenticated and effectively suited to read-only or trusted/internal use.
- Main project dependencies include docs/build libraries, so the base environment is heavier than a minimal API/library runtime.
- `site/` exists as generated output inside the repo tree, which can confuse tooling that does not distinguish source from built artifacts.

## Change-risk hotspots

- `src/ssvc/__init__.py`, `registry/`, `_mixins.py` — affect nearly all runtime loading.
- `decision_tables/base.py` and `utils/toposort.py` — affect mapping generation and validation semantics.
- `doctools.py`, `mkdocs.yml`, `data/` paths — affect docs and generated artifacts together.
- `metadata/specs/` — cross-cutting requirements and agent/export behavior.

## Safe operating advice

- Prefer additive changes to versioned decision-point and decision-table modules.
- Treat generated files as outputs, not design sources.
- If touching registry behavior, rerun the full suite, not just targeted tests.
- If touching specs or docs-data generation, verify both pytest and relevant CI-style build paths.
