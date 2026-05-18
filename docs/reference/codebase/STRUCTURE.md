# SSVC Codebase Structure

## Top-level repository map

- `src/ssvc/` — primary Python package.
- `src/test/` — pytest suite; mirrors production package areas.
- `specs/` — normative requirement files for the engineering/spec system.
- `docs/` — MkDocs source for the published documentation site.
- `docs/adr/` — architectural decision records.
- `data/` — generated JSON, schema, and CSV/CSVS artifacts consumed by docs and tooling.
- `docker/` — Dockerfile, compose file, and example environment file.
- `.github/workflows/` — CI, docs build, link checking, data regeneration, and Pages deploy.
- `wip_notes/` — draft/internal notes; not authoritative output.
- `obsolete/`, `doc/`, `pdfs/` — historical/reference material; not active implementation targets.
- `site/` — built MkDocs site output.

## Main package map: `src/ssvc/`

### Runtime package entry points
- `__init__.py` — eager importer that walks subpackages and populates the registry.
- `api/main.py` — FastAPI `app`; served by `uvicorn ssvc.api.main:app`.
- `registry/__init__.py` — creates the global `SsvcObjectRegistry` and attaches the registration hook.

### Core modeling packages
- `decision_points/`
  - Namespace-specific decision points (`ssvc`, `cvss`, `cisa`, `nist`, `basic`, `example`).
  - Common pattern inside a module: value constants, versioned object constants, `VERSIONS`, `LATEST`.
- `outcomes/`
  - Outcome sets for SSVC, CVSS, CISA, basic examples, and extension namespaces.
- `decision_tables/`
  - Concrete decision tables by namespace plus shared validation/export logic in `base.py` and `helpers.py`.
- `dp_groups/`
  - Deprecated `DecisionPointGroup` compatibility layer plus old grouped collections.
- `selection.py`
  - `Selection`, `SelectionList`, and minimal value/reference models for evaluation payloads.

### Tooling and support modules
- `doctools.py` — writes JSON examples, CSV tables, registry exports, and schemas under `data/`.
- `csv_analyzer.py` — checks topological ordering and feature importance of CSV tables.
- `policy_generator.py` — older graph-based policy generator built around deprecated groups.
- `doc_helpers.py` / `md_gen.py` — helpers for documentation formatting.
- `examples.py` — sample objects returned by `/examples` API routes.
- `metadata/specs/` — spec-file schema, registry, linting, rendering, and LLM export.
- `utils/` — defaults, field specs, importer, namespace regex support, schema ordering, misc helpers, topological sort.
- `namespaces.py` — namespace validation and official namespace enum.

## API surface layout

- `api/v1/routers/decision_point.py` and `decision_table.py` — single-object lookup by `id` query string.
- `api/v1/routers/decision_points.py` and `decision_tables.py` — collection, namespace, key, version, and latest endpoints.
- `api/v1/routers/objects.py` — explicit typed object paths.
- `api/v1/routers/types.py`, `namespaces.py`, `keys.py`, `versions.py` — registry browsing endpoints.
- `api/v1/routers/examples.py` — sample-object GETs and model-validation POSTs.
- `api/v1/response_models/` — typed wrappers and aliases for API responses.

Base API prefix: `/ssvc/api/v1`.

## Tests layout

Representative mirrors under `src/test/`:
- `api/routers/` ↔ `src/ssvc/api/v1/routers/`
- `decision_points/` ↔ `src/ssvc/decision_points/`
- `decision_tables/` ↔ `src/ssvc/decision_tables/`
- `registry/`, `utils/`, `metadata/specs/`, `outcomes/`, `dp_groups/`
- top-level tests for `csv_analyzer`, `doctools`, `mixins`, `namespaces`, `policy_generator`, `selection`

## Command entry points

Defined in `pyproject.toml`:
- `ssvc_csv_analyzer` → `ssvc.csv_analyzer:main`
- `ssvc_doctools` → `ssvc.doctools:main`
- `ssvc-spec-lint` → `ssvc.metadata.specs.lint:main`
- `ssvc-spec-dump` → `ssvc.metadata.specs.render:main_llm_json`

Developer entry points in `Makefile`:
- `make dev`, `make test`, `make docker_test`
- `make docs_local`, `make docs`
- `make api_dev`, `make api`
- `make regenerate_json`, `make mdlint_fix`

## Generated and derived paths to recognize

- `src/ssvc/utils/namespace_patterns.py` — generated from ABNF; do not hand-edit.
- `data/json/` — generated decision point, decision table, and registry JSON.
- `data/schema/` — generated JSON Schemas.
- `data/csv/` and `data/csvs/` — generated table artifacts used by tooling/docs.
- `site/` — built documentation site.
- `docs/reference/code/` — mkdocstrings website material, not a good source of agent-oriented architecture context.
