---
name: load-specs
description: >
  Export all project specifications as flat, inheritance-resolved JSON for
  coding agents. Run this at the start of any implementation or design task.
tags:
  - specs
  - requirements
  - agent-context
---

# Skill: Load All Specs as LLM-Optimized JSON

## Purpose

Export all project specifications as a flat, inheritance-resolved JSON
structure optimized for coding agents. This is the **required** way to load
specs before any implementation or design task.

**Do not read raw `specs/*.yaml` files directly.** Those files are for
authoring and linting only. The JSON export resolves inheritance, flattens
group nesting, and provides a consistent structure for agent consumption.

## Procedure

From the repository root, run:

```bash
uv run ssvc-spec-dump
```

This produces compact JSON on stdout. Capture or pipe it as needed.

## Output Structure

The JSON has three top-level arrays:

```json
{
  "topics": [...],
  "requirements": [...],
  "edges": [...]
}
```

### `topics`

One entry per spec topic (source file). Fields: `id`, `title`, `version`, `kind`.
Use this lookup table to resolve the short `topic` field on each requirement
to a human-readable title. **Do not open the source YAML files** — all
requirement content is already in the `requirements` array.

### `requirements`

One entry per requirement. Key fields:

| Field | Meaning |
|---|---|
| `id` | Unique requirement ID (e.g. `AP-01-001`) |
| `topic` | Parent spec topic ID (e.g. `AP`) |
| `group` | Group within the file (e.g. `AP-01`) |
| `group_title` | Human-readable group name |
| `priority` | `MUST`, `MUST_NOT`, `SHOULD`, `SHOULD_NOT`, or `MAY` |
| `statement` | The normative requirement text |
| `kind` | `domain`, `general`, `implementation`, `language`, or `pattern` |
| `scope` | List: `prototype`, `production`, or both |
| `type` | `behavioral` or `statement` |
| `relationships` | Optional inline list of `{rel_type, spec_id, note?}` edges |
| `rationale` | Optional explanatory text |

### `edges`

Centralized list of all relationships across all files:

```json
{"from": "AP-01-001", "rel_type": "depends_on", "to": "RG-01-001"}
```

Edge `rel_type` values: `constrains`, `depends_on`, `derives_from`,
`extends`, `implements`, `part_of`, `refines`, `supersedes`, `verifies`.

## Cross-Cutting Constraints

When implementing any feature, always pay attention to requirements from
these cross-cutting spec files regardless of the primary topic:

- `SR` — spec registry conventions (applies to all spec authoring)
- `CI` — CI/CD integration requirements
- `TS` — testing standards (coverage, test structure)

These apply to all code changes even when working on a specific feature area.

## Examples

```bash
# Full dump (default — always prefer this)
uv run ssvc-spec-dump

# Write to file for reference
uv run ssvc-spec-dump > /tmp/specs.json

# Count requirements
uv run ssvc-spec-dump | python -c "import json,sys; r=json.load(sys.stdin); print(len(r['requirements']))"

# Filter MUST requirements in Python after loading
uv run ssvc-spec-dump | python -c "
import json, sys
data = json.load(sys.stdin)
musts = [r for r in data['requirements'] if r['priority'] == 'MUST']
print(f'{len(musts)} MUST requirements')
"

# Filter by topic
uv run ssvc-spec-dump | python -c "
import json, sys
data = json.load(sys.stdin)
ap = [r for r in data['requirements'] if r['topic'] == 'AP']
print(f'{len(ap)} API requirements')
"
```

## Rationale

The `specs/*.yaml` source files use an authoring-optimized format with
inheritance (kind/scope inherited from file→group→spec), optional rationale,
and group nesting. This structure is good for authors but burdens coding agents
with mental inheritance resolution and navigation of nested structures.

The LLM JSON export:

1. Resolves all inheritance so every requirement has explicit `kind` and `scope`
2. Flattens group nesting so requirements are a simple array
3. Centralizes edges for graph-based dependency planning
4. Omits empty/null fields to minimize token usage
5. Uses readable field names (no abbreviations)

Running this export ensures agents always see the complete, consistent,
authoritative requirement set rather than a subset from browsing individual
files.
