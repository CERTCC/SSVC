# SSVC Technology Stack

## Core runtime choices

- **Python 3.12+**
  - Entire codebase is Python; package metadata requires `>=3.12`.
- **setuptools + setuptools-scm**
  - Standard packaging/build backend with version file generation under `src/ssvc/_version.py`.
- **uv**
  - Used for dependency sync, script execution, locking, and CI installs.

## Primary application libraries

- **Pydantic v2**
  - Foundation for domain models, validation, JSON serialization, and JSON Schema generation.
- **FastAPI**
  - Thin REST wrapper around the registry; no persistence layer behind it.
- **semver**
  - Validates and compares object versions.
- **PyYAML**
  - Loads `specs/*.yaml` into the spec registry.
- **jsonschema**
  - Supports schema validation workflows around generated artifacts.

## Table, graph, and analysis libraries

- **pandas**
  - Converts decision tables to shortform/longform tabular exports and CSV output.
- **networkx**
  - Powers graph creation, topological sorting, and spec relationship graphs.
- **scikit-learn**
  - Used by `csv_analyzer.py` for feature-importance analysis.
- **scipy**
  - Present for analysis/scientific workflows in the broader toolchain.
- **thefuzz**
  - Fuzzy matching utility dependency.

## Documentation stack

- **MkDocs + Material**
  - Builds the published documentation site.
- **mkdocstrings + mkdocstrings-python**
  - Generates API reference pages from Python objects/docstrings.
- **mkdocs-include-markdown-plugin**
  - Reuses Markdown content across docs.
- **markdown-exec**
  - Executes code blocks inside Markdown pages.
- **mkdocs-bibtex**
  - Supports citations.
- **mkdocs-table-reader-plugin**
  - Reads CSV data into docs pages.
- **mkdocs-print-site-plugin**
  - Adds printable/export-friendly output.
- **pymdown-extensions**
  - Enables richer Markdown features.

## Build and local-run tooling

- **Make**
  - Single command surface for dev setup, tests, docs, API, and regeneration.
- **Docker / docker-compose**
  - Optional local container workflow for docs, API, and tests.
- **abnf-to-regexp**
  - Codegen tool used to build `namespace_patterns.py` from ABNF.

## Quality and automation tools

- **pytest**
  - Main test runner.
- **black**
  - Python formatter.
- **markdownlint**
  - Markdown linting/fixing.
- **linkchecker**
  - Validates built-site links in CI.
- **GitHub Actions**
  - Runs tests, docs build checks, markdown linting, link checking, doctools regeneration, and Pages deployment.
- **Dependabot**
  - Updates `uv` dependencies and workflow actions.

## Why this stack fits the codebase

- The project is mostly static, schema-heavy domain data, so Pydantic models and generated artifacts are a natural fit.
- Registry-backed reads are sufficient because the API serves versioned reference objects rather than mutable business transactions.
- NetworkX and pandas match the problem domain of ordered combinations, mappings, and tabular policy outputs.
- MkDocs plus generated data keeps the public website tied closely to the Python source of truth.
