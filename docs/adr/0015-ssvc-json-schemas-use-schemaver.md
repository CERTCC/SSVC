---
status: accepted
date: 2024-07-09
deciders: Allen D. Householder, Vijay Sarvepalli
---
# SSVC JSON Schemas Use SchemaVer

## Context and Problem Statement

SSVC defines JSON schemas to validate the structure of data objects such as decision points, decision
point groups, and decision point value selections. As these schemas evolve, we need a versioning scheme
that accurately communicates compatibility expectations to schema consumers.

SSVC already uses [Semantic Versioning (SemVer)](https://semver.org/) for decision points
(see [ADR-0002](0002-ssvc-decision-points-are-versioned.md)) and decision point groups
(see [ADR-0004](0004-ssvc-decision-point-groups-are-versioned.md)).
However, SemVer was designed for software APIs and libraries, where "breaking" means a caller's code
must change. For JSON schemas, "breaking" means something different: it means existing data instances
may no longer validate against the new schema. These are distinct concerns that call for a
purpose-built approach.

## Decision Drivers

- JSON schema changes have data-compatibility semantics that differ from API/code-compatibility semantics.
- Consumers of SSVC schemas need to know whether a schema change will affect validation of their
  existing stored data.
- SemVer's MAJOR/MINOR/PATCH model does not map cleanly onto schema evolution: a "minor" schema
  addition (new optional field) does not break old data but may break some tooling; a field removal
  always breaks all old data.
- A schema-specific versioning convention would make compatibility implications immediately legible
  without consulting a changelog.

## Considered Options

- [Semantic Versioning (SemVer)](https://semver.org/) — already used for decision points and groups
- [SchemaVer](https://docs.snowplow.io/docs/api-reference/iglu/common-architecture/schemaver/) — designed specifically for JSON schema evolution
- [Calendar Versioning (CalVer)](https://calver.org/) — already adopted for overall SSVC project releases

## Decision Outcome

Chosen option: **SchemaVer**, because it was designed specifically for JSON schema versioning and its
three components map directly onto the compatibility questions that matter for schema consumers.

SchemaVer uses the format `MODEL-REVISION-ADDITION`, starting at `1-0-0`. For existing SSVC
schemas, adoption of this ADR preserves the current logical version and normalizes legacy dotted forms
such as `2.0.0` to the equivalent SchemaVer form `2-0-0`; similarly, values already written as
`1-0-1` are treated as already using SchemaVer, while newly introduced schemas begin at `1-0-0`:

| Component  | When to increment | Compatibility implication |
|------------|-------------------|--------------------------|
| `MODEL`    | Schema change is incompatible with **any** historical data | Existing data **will not** validate |
| `REVISION` | Schema change may prevent interaction with **some** historical data | Existing data **may not** validate |
| `ADDITION` | Schema change is compatible with **all** historical data | Existing data **will** continue to validate |

Applied to SSVC schemas:

### Increment MODEL when

- A required field is removed
- A field's type or allowed values change in a way that invalidates previously valid data
- The schema's root structure changes (e.g., from object to array)

### Increment REVISION when

- A previously optional field becomes required (breaks data that omitted it)
- An `enum` gains values that affect round-trip processing for some consumers
- Constraints are tightened in a way that some existing data would fail (e.g., a minimum length
  is added to a string field)

### Increment ADDITION when

- A new optional field is added
- A constraint is relaxed (e.g., removing a `maxLength`)
- Documentation (`description`, `$comment`) is updated without changing validation behavior
- An `enum` gains new allowed values in a way that only expands what is valid

### Consequences

- Good, because schema version strings immediately communicate data-compatibility impact without
  requiring consumers to read a changelog.
- Good, because SchemaVer's semantics are independent of—and complementary to—SemVer on the
  objects those schemas describe (a decision point can be at SemVer `2.0.0` while its schema
  is at SchemaVer `1-2-3`).
- Good, because the approach scales naturally: `MODEL` increments are rare (most schema evolution
  is additive), keeping churn low.
- Neutral, because SchemaVer is less widely known than SemVer, introducing a small learning curve
  for new contributors.
- Bad, because existing schemas that were informally versioned (or unversioned) will need to be
  assigned an initial SchemaVer version, requiring a one-time migration effort.

### Confirmation

- JSON schema files must include a `$schema` or metadata field carrying the SchemaVer string.
- PR review process verifies that the correct SchemaVer component is incremented according to
  these rules before merging schema changes.

## More Information

- [Issue #601](https://github.com/CERTCC/SSVC/issues/601) — original request for this ADR
- [PR #599 discussion](https://github.com/CERTCC/SSVC/pull/599#discussion_r1674439644) — discussion
  that identified the need for a schema-specific versioning approach
- [SchemaVer specification](https://docs.snowplow.io/docs/api-reference/iglu/common-architecture/schemaver/)
- [ADR-0002 — SSVC Decision Points are versioned using Semantic Versioning](0002-ssvc-decision-points-are-versioned.md)
- [ADR-0004 — Decision Point Groups are Versioned using SemVer](0004-ssvc-decision-point-groups-are-versioned.md)
- [ADR-0013 — SSVC Project Versions Follow CalVer](0013-ssvc-project-versions.md)
