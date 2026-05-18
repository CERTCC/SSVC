# SSVC Integrations and Boundaries

## Runtime integration boundaries

### HTTP API

The only application network boundary is the FastAPI service in `src/ssvc/api/`.

Base prefix:
- `/ssvc/api/v1`

Route families:
- `decision_point` / `decision_points`
- `decision_table` / `decision_tables`
- `objects`
- `types`, `namespaces`, `keys`, `versions`
- `examples`

Behavior:
- `GET` routes read from the in-memory registry.
- `POST` routes in `/examples` validate payloads against Pydantic models and return them; they do not write state.
- There is no auth, database session, cache, or external service dependency behind these routes.

### Filesystem boundary

Important file-backed interfaces:
- `specs/*.yaml` — authored engineering requirements.
- `data/json/` — generated JSON examples and registry export.
- `data/schema/` — generated JSON Schemas published by the docs site.
- `data/csv/` and `data/csvs/` — generated decision-table artifacts consumed by docs/tooling.
- `docs/` — MkDocs source that reads generated artifacts and Markdown content.

## CI/CD and repository automation

GitHub Actions workflows are the main external automation surface:
- `python-app.yml` — installs deps, runs pytest, builds the package, uploads artifact.
- `docs_build_check.yml` — validates MkDocs build.
- `lint_md_changes.yml` — lints changed Markdown files.
- `link_checker.yml` — builds the site and checks links.
- `run_doctools.yml` — regenerates `data/` on PRs touching `src/ssvc/**`.
- `deploy_site.yml` — builds and deploys the MkDocs site to GitHub Pages from `publish` branch pushes.

Related GitHub integrations:
- Dependabot updates `uv` dependencies and workflow actions.
- CODEOWNERS, issue templates, and PR templates define repository process boundaries.

## Published/public endpoints

- Documentation site: `https://certcc.github.io/SSVC/`
- Schema base URL used in generated `$id` fields: `https://certcc.github.io/SSVC/data/schema/`
- Repository/project links in package metadata point to GitHub (`CERTCC/SSVC`).

The repo builds package artifacts in CI, but there is no checked-in workflow here that publishes releases to PyPI.

## Documentation-site external assets

`mkdocs.yml` pulls in or links to external browser-side resources:
- MathJax CDN
- `tablesort` CDN
- jQuery CDN
- D3 CDN
- Google Analytics

These affect the published site, not the core Python runtime or API behavior.

## Docker boundary

Local container workflows are defined under `docker/`:
- `docker-compose.yml` provides docs/API/test services.
- `docker/env_example` shows the only documented env var: `COMPOSE_PROJECT_NAME=ssvc`.

Docker is optional for development; local `uv` + `make` workflows are first-class.

## What is not integrated

The codebase does **not** contain a runtime integration with:
- relational or document databases;
- message queues;
- background job systems;
- external REST/SOAP clients;
- cloud SDKs;
- authentication/identity providers.

That absence is intentional: the system is mostly static reference data, validation logic, docs generation, and registry-backed reads.
