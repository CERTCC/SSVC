# Idea History

This file archives processed GitHub Idea-type issues. Each entry records the
original idea and a reference to where the design decisions were captured.

---

## IDEA-1143: Add versioning rules for DecisionTable objects

Add versioning rules for DecisionTable objects

Currently, SSVC's `DecisionTable` objects lack versioning rules. This is a
significant omission — without versioning conventions, it is unclear how to
track changes to decision tables, how to communicate compatibility, or how to
deprecate old versions. We should define versioning semantics (e.g., semantic
versioning), rules for when a version bump is required, and how versions
should be represented in the Python model and JSON/CSV data files.

**Processed**: 2026-05-18 — design decisions captured in
`specs/versioning.yaml` (new VR-05 group, VR-05-001 through VR-05-007).
Also: VR-01-006 downgraded from SHOULD to MAY; VR-02 tightened to cover
only DecisionPointGroup (DecisionTable reference removed).
