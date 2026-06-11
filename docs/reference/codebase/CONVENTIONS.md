# SSVC Codebase Conventions

## Naming

- Python modules and packages use `snake_case`.
- Classes use `PascalCase`.
- Functions, methods, and variables use `snake_case`.
- Constants use `UPPER_SNAKE_CASE`.
- Internal mixins and helper models often use a leading underscore: `_Registered`, `_SchemaVersioned`, `_Namespace`.
- Decision-point and outcome modules usually expose versioned constants plus:
  - `VERSIONS` — append-only ordered tuple of versions;
  - `LATEST` — alias for the newest version.

## Object identity and versioning

- Runtime objects are identified by `namespace:key:version`.
- Decision point values are identified by `namespace:key:version:value_key`.
- Versions are semantic versions validated with `semver`.
- Namespaces must be official enum values or extension namespaces that begin with `x_` and satisfy the ABNF-derived regex.

## Model style

- Pydantic v2 models are the dominant implementation style.
- Cross-cutting behavior is added with mixins rather than deep inheritance hierarchies.
- Validation is pushed into `field_validator` and `model_validator` methods.
- `schemaVersion` is auto-populated by schema-aware models.
- Domain objects auto-register on `model_post_init()` unless created with `registered=False`.

## Formatting and imports

- Formatting is controlled by Black with `line-length = 79`.
- Use absolute imports from `ssvc`, not relative imports.
- Typical import grouping is stdlib, third-party, then internal `ssvc` imports.
- Be aware that `import ssvc` is not a benign import; it walks subpackages and mutates the global registry.

## Domain-module patterns

- Decision point modules usually define reusable `DecisionPointValue` constants first, then one or more versioned decision point objects.
- Decision table modules usually import named decision points/outcomes and instantiate a module-level `DecisionTable` constant.
- `DecisionTable.key` is normalized to a `DT_` prefix if not already present.
- New work should prefer `DecisionTable`; `DecisionPointGroup` is retained for backward compatibility and emits deprecation warnings.

## Logging and error handling

- Logging uses the stdlib `logging` module with per-module loggers.
- Validation failures generally raise `ValueError` or `TypeError` from model validation helpers.
- API routers translate missing registry results into `HTTPException(404)` via `_404_on_none`.
- Duplicate registration with mismatched attributes raises an error rather than silently overwriting.

## Testing conventions that affect implementation

- Tests run under pytest but commonly use `unittest.TestCase` classes.
- Test files live in `src/test/` and are named `test_<module>.py`.
- API tests typically replace a router module's global `r` registry with a fresh `SsvcObjectRegistry`.
- Fixtures that should not mutate the global registry are often created with `registered=False`.

## Generated-artifact discipline

- Do not hand-edit `src/ssvc/utils/namespace_patterns.py`; regenerate it.
- Do not treat `data/json/`, `data/schema/`, or CSV outputs as authoritative when corresponding Python source exists.
- For agent/spec work, use `uv run ssvc-spec-dump`; raw `specs/*.yaml` is authoring format, not the preferred consumption format.
