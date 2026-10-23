---
name: technical-impact
description: Use when evaluating the SSVC Technical Impact decision point for a vulnerability report. Determines the technical impact of exploiting the vulnerability on the affected component.
---

# SSVC: Technical Impact

Follow the `eval-against-decision_point` evaluation process.

## Decision Point

**Name:** Technical Impact  
**Question:** What is the technical impact of exploiting the vulnerability on the affected component?

## Dependencies

None. This is a primitive decision point.

## Documentation to Fetch at Runtime

Use the `Read` tool to fetch all of the following files before beginning evaluation. The base path for `@ssvc-docs` is the SSVC repository root.

| File | Path under @ssvc-docs |
|---|---|
| Python source (canonical values) | `src/ssvc/decision_points/ssvc/technical_impact.py` |
| Reference doc | `docs/reference/decision_points/technical_impact.md` |
| How-to guide | `docs/howto/gathering_info/technical_impact.md` |
