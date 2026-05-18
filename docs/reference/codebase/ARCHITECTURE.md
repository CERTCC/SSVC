# SSVC Codebase Architecture

## System shape

SSVC is a static domain-model library with three attached delivery layers:
- an in-memory object registry used as the runtime index;
- a thin FastAPI API that exposes registry contents;
- build-time tooling that emits JSON, CSV, schema, and documentation artifacts.

The authoritative sources are:
- Python object definitions under `src/ssvc/` for decision points, outcomes, decision tables, examples, and schemas;
- YAML spec files under `specs/` for normative engineering requirements.

Generated outputs under `data/`, `site/`, and `src/ssvc/utils/namespace_patterns.py` are derived artifacts.

## Primary runtime flow

### 1. Import-time registry population

```text
import ssvc
  -> src/ssvc/__init__.py imports IMPORTABLES
  -> utils.importer.import_modules(..., include_children=True)
  -> package walk loads decision_points/, outcomes/, decision_tables/, dp_groups/
  -> module-level Pydantic objects are instantiated
  -> _Registered.model_post_init() calls notify_registration(self)
  -> registry hook in ssvc.registry.__init__ inserts object into SsvcObjectRegistry
```

Notes:
- Registration is eager and happens as a side effect of importing the package.
- Object identity is effectively `namespace:key:version`.
- Registry structure is `type -> namespace -> key -> version`.

### 2. API query flow

```text
HTTP request
  -> FastAPI app in src/ssvc/api/main.py
  -> router in src/ssvc/api/v1/routers/
  -> registry lookup helper (lookup_objtype/lookup_namespace/lookup_key/lookup_version)
  -> Pydantic model returned as JSON
```

The API does not persist data. `POST` routes under `/examples` validate payloads against models and echo them back.

### 3. Artifact generation flow

```text
make regenerate_json
  -> ssvc.doctools
  -> import/register all objects
  -> dump JSON examples, CSV tables, registry JSON, and JSON Schemas under data/
```

Related build paths:
- `run_doctools.yml` regenerates `data/` on PRs touching `src/ssvc/**`.
- MkDocs builds the website from `docs/` plus generated artifacts in `data/`.

### 4. Spec tooling flow

```text
specs/*.yaml
  -> metadata.specs.schema + metadata.specs.registry
  -> ssvc-spec-lint validates authoring rules
  -> ssvc-spec-dump exports flat JSON for agents
```

The spec subsystem is separate from the runtime object registry. It is build/tooling metadata, not API backing storage.

## Layer rules

### Domain definitions
- `decision_points/`: define ordered value sets and versioned decision points.
- `outcomes/`: define ordered outcome sets using the same object patterns.
- `decision_tables/`: compose decision points into validated mappings and tabular exports.
- `selection.py`: minimal evaluation-time representations derived from decision points.

Must not own:
- HTTP routing;
- filesystem orchestration beyond local helpers;
- long-lived persistence.

### Cross-cutting model infrastructure
- `_mixins.py` provides versioning, namespacing, schema versioning, timestamps, and auto-registration.
- `namespaces.py` and `utils/field_specs.py` enforce namespace and field constraints.
- `utils/toposort.py` and `csv_analyzer.py` encode ordering and feature-analysis helpers used by tables and policies.

### Registry layer
- `registry/` owns lookup, registration, duplicate detection, latest-version resolution, and hierarchical storage.
- It is intentionally in-memory and process-local.
- It should remain ignorant of HTTP, MkDocs, and GitHub workflow behavior.

### Delivery/tooling layers
- `api/` translates registry lookups into HTTP resources.
- `doctools.py`, `doc_helpers.py`, and `decision_tables/helpers.py` translate models into published artifacts.
- `metadata/specs/` validates and exports engineering specifications.

## Architectural invariants from ADRs and code

- Decision points are versioned using SemVer.
- Decision point groups are versioned but deprecated; `DecisionTable` is the preferred abstraction.
- Decision points and outcomes are ordered sets.
- Outcome sets are separate from decision point groups.
- “Decision table” is the preferred terminology over “decision tree”.
- Namespaces are constrained to official enum values or extension namespaces beginning with `x_`.
- JSON schemas use explicit `schemaVersion` and a published `$id` under `https://certcc.github.io/SSVC/data/schema/`.

## Practical rules for agents

- Do not hand-edit generated artifacts when the Python or spec source is authoritative.
- Assume `import ssvc` has side effects; isolate tests and scripts accordingly.
- Prefer `DecisionTable` for new modeling work; treat `dp_groups/` as compatibility surface.
- When documenting or implementing against specs, use `uv run ssvc-spec-dump` rather than reading raw YAML.
