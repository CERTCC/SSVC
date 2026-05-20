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

---

## IDEA-1151: Establish two-tier skill directory structure and canonical skill interface

Bootstrap the skills infrastructure in the SSVC repository by establishing a
two-tier directory structure (`.agents/skills/dev/` and `.agents/skills/ssvc/`)
and defining a canonical SKILL.md format. Replaces the flat `.agents/skills/`
layout and lays the groundwork for SSVC domain skills.

Key deliverables: restructure skill directories; add placeholder
`.agents/skills/ssvc/evaluate-decision-point/SKILL.md` (WIP stub); define
canonical SKILL.md frontmatter (required: `name` + `description` only); update
existing dev skills to conform; add `.agents/skills/README.md`; add
`specs/skills.yaml` (prefix SK); add CI validation workflow
`.github/workflows/validate_skills.yml`.

Design decisions: skills stay under `.agents/`; required front-matter is
`name` + `description` only; CI uses a new standalone workflow with inline
Python filtered to `.agents/skills/**/SKILL.md`.

**Processed**: 2026-05-20 — design decisions captured in
`specs/skills.yaml` and `notes/skills.md`.
