---
name: evaluate-decision-point
description: >
  Walk through evaluating a single SSVC decision point for a vulnerability.
  Given a decision point (e.g., Exploitation, Automatable, Human Impact) and
  a vulnerability description, guide the user to select the correct value by
  working through the decision point's definition, value descriptions, and
  relevant evidence. Use when a practitioner needs help applying one SSVC
  decision point to a specific vulnerability.
tags:
  - ssvc
  - decision-points
  - vulnerability-management
---

# Skill: Evaluate Decision Point

> **⚠️ Work in progress.** This skill is a placeholder stub.
> The procedure below is a skeleton — steps are intentionally incomplete
> and will be expanded in a follow-up implementation issue.

## Purpose

Help a practitioner correctly evaluate a single SSVC decision point for a
specific vulnerability. The skill loads the decision point definition from
the SSVC registry, presents the possible values with their descriptions, asks
targeted questions to gather relevant evidence, and guides the practitioner
to a well-reasoned value selection.

This skill covers one decision point at a time. To evaluate all decision
points for a vulnerability and reach a prioritisation outcome, invoke this
skill once per decision point, then consult the appropriate decision table.

## Procedure

> **TODO:** Expand each step with concrete instructions and example prompts.

### Step 1 — Identify the decision point

Ask the practitioner which decision point to evaluate, or accept it as a
parameter. Confirm the exact name matches an entry in the SSVC registry.

```bash
# List available decision points
uv run python -c "
from ssvc.registry import registry
for dp in registry.decision_points():
    print(dp.namespace, dp.key, dp.version)
"
```

### Step 2 — Load the decision point definition

Fetch the decision point from the registry and display:
- Its name and description
- Each possible value with its label and description

### Step 3 — Gather evidence

Ask targeted questions that help narrow down the correct value. Questions
should be grounded in the decision point's value descriptions, not in
general vulnerability knowledge.

> **TODO:** Define question templates per decision point.

### Step 4 — Confirm value selection

Present the candidate value, summarise the supporting evidence, and ask the
practitioner to confirm or revise. Record the selected value and rationale.

### Step 5 — Output

Return the selected value in a format suitable for input to a decision table
or for recording in the practitioner's vulnerability tracking system.
