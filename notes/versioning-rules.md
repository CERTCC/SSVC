# Versioning Rules

SSVC uses a **layered versioning strategy**: different levels of the system
use different versioning schemes suited to their specific compatibility semantics.

## Summary

| Level | Scheme | Example | Governed by |
|-------|--------|---------|-------------|
| Decision points and groups | SemVer 2.0.0 | `2.1.0` | ADR-0002, ADR-0004, ADR-0006 |
| JSON schema files | SchemaVer | `1-2-0` | ADR-0015 |
| SSVC project / docs releases | CalVer | `2025.6.0` | ADR-0013 |

---

## Decision Point Versioning (SemVer)

Individual `DecisionPoint` objects are versioned with **Semantic Versioning 2.0.0**
(`MAJOR.MINOR.PATCH`). The semantics map as follows:

### Create a new object when

A *different or fundamentally new concept* is being represented — even if it
superficially resembles an existing decision point. New objects **should** get
new names and new keys. Do not reuse an existing name with a version bump when
the underlying concept has genuinely changed.

### Increment MAJOR when

- An existing value is **removed**.
- Value semantics change such that **older answers are no longer usable**.
- New values are added that **divide previous value semantics ambiguously**.

> **Note:** The ability to map old-to-new semantics is encouraged but not required.

### Increment MINOR when

*(Existing value semantics are preserved.)*

- New options/values are **added**.
- Value names or keys are **changed** (without semantic shift).
- The decision point **name** is changed.

### Increment PATCH when

*(Existing value count and semantics are preserved.)*

- **Typo fixes** in option or decision point names.
- The **description** changes in a way that does not affect semantics.

### Pre-support (v0.x) decision points

A decision point at major version `0` is **pre-support**: all aspects
(key, labels, ordering, descriptions, semantics) are subject to change without
a major-version increment. The Minor version absorbs the full SemVer
major/minor distinction during this phase.

The lowest *supported* version of a decision point is `1.0.0`.

---

## Decision Point Group Versioning (SemVer)

`DecisionPointGroup` objects are also versioned with SemVer. The *core identity*
of a group is the pairing of the **stakeholder role** and the **decision being
modeled**.

### Create a new object when

The stakeholder role and/or the decision being modeled changes. Even if the
constituent decision points remain the same, a shift in either dimension
represents a fork in version history. **New objects must have new names.**

> Name changes alone (e.g. *Patch Applier* → *Deployer* for the same role and
> decision) are **not** a reason to create a new object; they are a patch-level
> event.

### Increment MAJOR when

- A decision point is **added to or removed from** the group, OR
- Any constituent decision point increments its **own major version**.

### Increment MINOR when

- Any constituent decision point increments its **own minor version**.

### Increment PATCH when

- Any constituent decision point increments its **own patch version**, OR
- The group **description** changes, OR
- The group **name** changes.

---

## JSON Schema Versioning (SchemaVer)

SSVC JSON schema files use **SchemaVer** (`MODEL-REVISION-ADDITION`, starting
at `1-0-0`) rather than SemVer. The distinction matters because "breaking" for
a schema means *existing stored data will no longer validate* — a different
concern from API-level breaking changes.

| Component | When to increment | Data-compatibility implication |
|-----------|-------------------|-------------------------------|
| `MODEL` | Incompatible with **any** historical data | Existing data **will not** validate |
| `REVISION` | Incompatible with **some** historical data | Existing data **may not** validate |
| `ADDITION` | Compatible with **all** historical data | Existing data **will** continue to validate |

### Increment MODEL when

- A **required field is removed**.
- A field's **type or allowed values** change in a way that invalidates previously valid data.
- The **root schema structure** changes (e.g. from object to array).

### Increment REVISION when

- A previously **optional field becomes required**.
- An `enum` gains values that affect **round-trip processing** for some consumers.
- Constraints are **tightened** such that some existing data would fail.

### Increment ADDITION when

- A **new optional field** is added.
- A constraint is **relaxed**.
- **Documentation** (`description`, `$comment`) is updated without changing validation behavior.
- An `enum` gains new allowed values that **only expand** what is valid.

### Relationship to SemVer on the same objects

A `DecisionPoint` can be at SemVer `2.1.0` while its JSON schema is at
SchemaVer `1-2-3`. These are independent versioning axes:

- SemVer on the object answers: *"Has the concept or its option space changed?"*
- SchemaVer on the schema answers: *"Will my stored data still validate?"*

---

## Project / Documentation Versioning (CalVer)

The overall SSVC project and documentation releases use **Calendar Versioning**
(`YYYY.M.patch`):

- `YYYY` = four-digit release year.
- `M` = single-digit month (no leading zero).
- `patch` = incremented for subsequent updates within the same month.

*Examples:* `2025.6.0` (first June 2025 release), `2025.6.1` (second),
`2025.11.0` (November 2025).

CalVer suits SSVC as a *living framework* because:

- The version immediately communicates **recency** without counting features.
- Documentation changes that do not alter any domain object can still produce
  a new project version.
- It avoids unproductive debates about whether a change is "major" or "minor"
  at the project level.

Individual domain objects continue to use SemVer regardless of the project
CalVer; the two schemes are complementary.

---

## See Also

- ADR-0002: [Decision Points are Versioned using SemVer](../docs/adr/0002-ssvc-decision-points-are-versioned.md)
- ADR-0005: [Decision Point Group Versioning Rules](../docs/adr/0005-ssvc-decision-point-group-versioning.md)
- ADR-0006: [Decision Point Versioning Rules](../docs/adr/0006-ssvc-decision-point-versioning-rules.md)
- ADR-0013: [SSVC Project Versions Follow CalVer](../docs/adr/0013-ssvc-project-versions.md)
- ADR-0015: [SSVC JSON Schemas Use SchemaVer](../docs/adr/0015-ssvc-json-schemas-use-schemaver.md)
- Spec VR: `specs/versioning.yaml`
