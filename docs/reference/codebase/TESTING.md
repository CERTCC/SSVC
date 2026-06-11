# SSVC Testing Guide

## What is tested

The suite exercises:
- domain models (`DecisionPoint`, `DecisionTable`, outcomes, selections, mixins);
- registry behavior and duplicate/version handling;
- FastAPI routers via `TestClient`;
- documentation helpers and doctools artifact generation;
- CSV analysis and graph/topology helpers;
- spec registry schema and lint behavior under `metadata/specs/`.

## Test layout

Tests live in `src/test/` and largely mirror production structure:
- `api/` and `api/routers/`
- `decision_points/`
- `decision_tables/` with namespace subtrees
- `registry/`, `utils/`, `outcomes/`, `dp_groups/`, `metadata/specs/`
- top-level tests for `csv_analyzer`, `doctools`, `mixins`, `namespaces`, `policy_generator`, `selection`

This layout matches the normative testing spec topic (`TS`), which requires tests under `src/test/` with mirrored structure and `test_<module>.py` naming.

## Execution commands

- `make test` — preferred local command; also regenerates `namespace_patterns.py` prerequisite.
- `uv run pytest -v` — direct local run.
- `make docker_test` — containerized run.
- `uv run pytest src/test/...` — targeted subtree execution.

Current baseline: `make test` passes locally in this repository state.

## Test style and isolation rules

- Pytest is the runner, but many tests are written as `unittest.TestCase` classes.
- API tests create a fresh `FastAPI` app and include only the router under test.
- Router tests commonly replace the router module's global registry variable (`decision_point.r = self.r`) with a fresh `SsvcObjectRegistry`.
- Registry-backed tests call `reset(force=True)` before loading fixtures.
- Fixture objects that must not auto-register are commonly instantiated with `registered=False`.
- Spec tests are more pytest-native and use fixtures such as `tmp_path` and local YAML directories.

## Quality signals and gaps

Strong signals:
- broad coverage across runtime models, API, doctools, and specs;
- CI runs pytest on pushes and pull requests to `main`;
- docs build and link checks are separate workflows.

Known gaps:
- no coverage threshold or `pytest-cov` configuration;
- no end-to-end deployed API test;
- warnings are tolerated in baseline runs, especially around deprecated `DecisionPointGroup`, selection serialization, and config drift.

## Warnings agents should recognize

A clean pass may still emit warnings for:
- `DecisionPointGroup` deprecation;
- Pydantic serializer warnings in `Selection` / `SelectionList` paths;
- pytest falling back from `testpaths` because `pyproject.toml` points to `test` while the suite lives in `src/test/`.

## Practical change checklist

When changing runtime code:
- run `make test`;
- if namespace grammar or generated artifacts are affected, run `make dev` or `make regenerate_json` as appropriate;
- if docs content or data-backed pages change, consider the docs build workflows (`mkdocs build`, link check) as part of validation.
