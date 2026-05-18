# Decision Point Groups Removal

Implementation guidance for `specs/dp-groups-removal.yaml` (spec ID: DPG).

Originated from GitHub Idea #902:
_"Do we still need Decision Point Groups now that we have `DecisionTable`?"_

---

## Background

`DecisionPointGroup` was the original way to bundle related `DecisionPoint`
objects together (e.g., all decision points used by the Deployer role).
`DecisionTable` supersedes it: a table already carries its own decision points,
version, name, and outcomes. `DecisionPointGroup` has emitted a
`DeprecationWarning` on instantiation since the class was last touched.

The goal is to complete the deprecation lifecycle in three phases, ending with
the complete deletion of `ssvc/dp_groups/`.

---

## Decision Table (Design Choices)

| Question | Decision | Rationale |
|---|---|---|
| Delete `ssvc/dp_groups/ssvc/collections.py`? | Yes, delete it | SSVCv1/v2/v2.1 bundling is not yet available as `DecisionTable` objects, but historical grouping will be backfilled per #920; the gap is acceptable. |
| Migrate `policy_generator.py`? | Yes, in-scope; replace `DecisionPointGroup` entirely with `DecisionTable` | Union types prolong the deprecated path. |
| Remove `doctools.dump_schemas` entry? | Yes, in-scope | Leaving it causes `ImportError` once `base.py` is deleted. |
| Keep `DecisionPointGroup` JSON schema files in `data/schema/`? | Yes, keep as static files | External tooling may reference schema URLs; freezing them is safer than deleting. |
| CVSS collections removal? | Blocked by #922, #923, #924 | No `DecisionTable` equivalents exist for CVSS v1–v3 yet. |
| Major version bump required? | Yes | Deleting public modules (`ssvc.dp_groups.base`, `ssvc.dp_groups.ssvc.*`) is a breaking change. |

---

## Phases

### Phase 1 — Remove SSVC dp_group modules (unblocked)

Files to **delete**:

```
src/ssvc/dp_groups/ssvc/supplier.py
src/ssvc/dp_groups/ssvc/deployer.py
src/ssvc/dp_groups/ssvc/coordinator_triage.py
src/ssvc/dp_groups/ssvc/coordinator_publication.py
src/ssvc/dp_groups/ssvc/collections.py
src/ssvc/dp_groups/ssvc/__init__.py
src/ssvc/dp_groups/base.py
src/test/dp_groups/test_dp_groups.py
src/test/dp_groups/__init__.py
src/test/dp_groups/          (directory)
```

Files to **edit**:

- `src/ssvc/utils/defaults.py` — remove `"ssvc.dp_groups"` from `IMPORTABLES`

Verify no remaining imports anywhere:

```bash
grep -r "from ssvc.dp_groups\|import ssvc.dp_groups\|DecisionPointGroup\|get_all_decision_points_from" \
  src/ --include="*.py" | grep -v __pycache__
```

Expected: only hits in `src/ssvc/dp_groups/cvss/` and `src/ssvc/policy_generator.py`
(which is handled in Phase 2).

### Phase 2 — Migrate `policy_generator.py` (unblocked, can run in parallel with Phase 1)

`PolicyGenerator.__init__` currently:

```python
def __init__(self, dp_group: DecisionPointGroup, outcomes):
    ...
    self.dpg: DecisionPointGroup = dp_group
```

Change to:

```python
def __init__(self, decision_table: DecisionTable, outcomes):
    ...
    self.dt: DecisionTable = decision_table
```

The internal usage of `self.dpg` iterates over decision points; `DecisionTable`
exposes them via `.decision_points` (same attribute name as `DecisionPointGroup`
uses), so iteration code should require minimal change.

Also update `doctools.py`:

```python
# Before
for _class in (DecisionPoint, DecisionTable, SsvcObjectRegistry,
               DecisionPointGroup, SelectionList):

# After
for _class in (DecisionPoint, DecisionTable, SsvcObjectRegistry, SelectionList):
```

Remove the import of `DecisionPointGroup` from `doctools.py` after the above.

#### Demo / `__main__` block update pattern

The demo in `policy_generator.py` currently builds a `DecisionPointGroup`
directly. Replace it with an import of an existing `DecisionTable`, e.g.:

```python
from ssvc.decision_tables.ssvc.deployer_dt import DEPLOYER_DECISION_TABLE

with PolicyGenerator(DEPLOYER_DECISION_TABLE, outcomes) as pg:
    pg.generate()
```

### Phase 3 — Remove CVSS dp_group collections (blocked by #922, #923, #924)

Only proceed after all three CVSS backfill issues are merged.

Files to **delete**:

```
src/ssvc/dp_groups/cvss/collections.py
src/ssvc/dp_groups/cvss/__init__.py
src/ssvc/dp_groups/cvss/          (directory)
src/ssvc/dp_groups/__init__.py
src/ssvc/dp_groups/               (directory, now empty)
```

Files to **keep** (static, do not regenerate):

```
data/schema/v2/Decision_Point_Group-2-0-0.schema.json
data/schema/v2/DecisionPointGroup_2_0_0.schema.json
```

To prevent `make regenerate_json` from overwriting them, ensure
`doctools.dump_schemas` no longer emits `DecisionPointGroup` (done in Phase 2).

---

## Layer / Import Rules

- `ssvc.dp_groups` → deprecated, remove all cross-package imports
- `ssvc.decision_tables` → the canonical replacement
- `ssvc.policy_generator` → MUST only import from `ssvc.decision_tables` after Phase 2

---

## Testing Pattern

After Phase 1:

```bash
# Confirm no remaining ssvc.dp_groups imports (except cvss/)
grep -r "from ssvc.dp_groups.ssvc\|from ssvc.dp_groups.base" src/ --include="*.py" | grep -v __pycache__
# Expected: empty

# Run full test suite
uv run pytest -v
```

After Phase 2:

```python
# Test that PolicyGenerator works with a DecisionTable
from ssvc.decision_tables.ssvc.deployer_dt import DEPLOYER_DECISION_TABLE
from ssvc.policy_generator import PolicyGenerator
from ssvc.outcomes.ssvc.deployer import DEFER, SCHEDULED, OUT_OF_CYCLE, IMMEDIATE

with PolicyGenerator(DEPLOYER_DECISION_TABLE, [DEFER, SCHEDULED, OUT_OF_CYCLE, IMMEDIATE]) as pg:
    result = pg.generate()
assert result is not None
```

---

## Related Issues

| Issue | Title | Relationship |
|---|---|---|
| #920 | Backfill `DecisionTable` for SSVC v1/v2 role groups | Informational (future work) |
| #922 | Backfill `DecisionTable` for CVSS v1 | **Blocks Phase 3** |
| #923 | Backfill `DecisionTable` for CVSS v2 | **Blocks Phase 3** |
| #924 | Backfill `DecisionTable` for CVSS v3 | **Blocks Phase 3** |
