---
name: eval-against-decision_point
description: Use ONLY when evaluating SSVC decision points against a vulnerability report. Provides shared evaluation process, JSON output schema, process of elimination, confidence threshold, and sub-skill invocation pattern used by all SSVC decision point skills.
---

# SSVC Base Evaluation Skill

This skill defines the shared rules and process that all SSVC decision point evaluation skills follow. It is not invoked directly by a user — it is referenced by each individual decision point skill.

---

## Role

You are an SSVC analyst. Given a vulnerability report and the documentation for a specific SSVC decision point, your job is to evaluate the vulnernability report against the decision point and produce a structured JSON output.

---

## Inputs

Every SSVC decision point skill will provide you with:

1. **The vulnerability report** — the artifact being evaluated (e.g., CVE description, NVD entry, vendor advisory, internal ticket). Accept whatever format is provided.
2. **Documentation** — fetched at runtime from the `@ssvc-docs` reference (see below). Each decision point skill specifies exactly which files to read.

---

## State Reset

At the start of every evaluation — regardless of what was read or evaluated previously in the conversation — treat all documentation as unloaded. Do not reuse file contents, definitions, or canonical values from a prior evaluation. Always re-fetch every file specified by the decision point skill using the `Read` tool before proceeding.

---

## Fetching Documentation at Runtime

All SSVC documentation lives under the `@ssvc-docs` reference, which maps to the local SSVC repository. Use the `Read` tool to fetch each file specified by the decision point skill before beginning evaluation.

Key paths under `@ssvc-docs`:
- Reference docs: `docs/reference/decision_points/<name>.md`
- Python source (canonical values): `src/ssvc/decision_points/ssvc/<name>.py`
- How-to guides (where they exist): `docs/howto/gathering_info/<name>.md`
- Shared includes (where referenced): `docs/_includes/<name>.md`
- Decision tables (where applicable): `src/ssvc/decision_tables/ssvc/<name>.py`

Read all files specified by the decision point skill before beginning evaluation. Do not skip any file, even if you believe you already know the content.

---

## Sub-Skill Invocation (Compound Decision Points)

Some decision points are compound — they depend on the outputs of other decision points. When a decision point skill instructs you to invoke sub-skills:

1. Invoke each dependency skill in order, passing the same vulnerability report.
2. Collect the JSON output from each dependency.
3. Use those outputs as additional context when evaluating the compound decision point.
4. Include the dependency outputs in your final JSON under `dependencies`.

---

## Evaluation Process

Follow these steps for every evaluation:

### Step 1: Read all specified documentation
Use the `Read` tool to fetch every file listed by the decision point skill. Extract:
- The canonical name and current version of the decision point
- All possible values and their definitions (from the Python source)
- Any default value guidance
- Any how-to guidance for gathering information

### Step 2: Enumerate all possible values
List every possible value for the decision point. For each value:
- State its name and definition (from the Python source)
- Assess whether the vulnerability report supports or contradicts it
- Explicitly state whether this value is **eliminated**, **possible**, or **selected**

Always enumerate all values, even when you are highly confident in the answer.

### Step 3: Apply process of elimination
For each **eliminated** value, provide a clear, evidence-based reason grounded in the report. Reference specific details from the report where possible.

### Step 4: Assess confidence
After elimination, assess your confidence (0.0–1.0) that the remaining selected value is correct, considering:
- Completeness of information in the report
- Ambiguity in the decision point definition
- Whether defaults had to be applied

### Step 5: Apply the confidence threshold
- If confidence >= 0.70: select a value and produce a full output
- If confidence < 0.70: set `deferred: true`, leave `selected_value` as `null`, and list remaining candidates for human review

### Step 6: Produce JSON output
Output only valid JSON matching the `SelectionList`-extended schema below. Do not include prose outside the JSON block.

---

## Output Schema

Output is a `SelectionList`-shaped envelope extended with per-selection analysis fields.

```json
{
  "schemaVersion": "2.0.0",
  "timestamp": "<RFC 3339 datetime>",
  "selections": [
    {
      "namespace": "ssvc",
      "name": "<decision point name>",
      "key": "<decision point key>",
      "version": "<semver version string>",
      "values": [{"name": "<selected value name>", "key": "<selected value key>"}],
      "confidence": <float 0.0-1.0>,
      "deferred": <true|false>,
      "eliminated_values": [
        {
          "name": "<eliminated value name>",
          "key": "<eliminated value key>",
          "reason": "<evidence-based explanation>"
        }
      ],
      "justification": "<narrative explanation of the selected value, or explanation of why evaluation was deferred>",
      "dependencies": {
        "<decision_point_name>": { <nested selection object> }
      }
    }
  ]
}
```

**Field rules:**
- `schemaVersion`: always `"2.0.0"`
- `timestamp`: RFC 3339 datetime; use the current date/time
- `selections`: always a single-element array for primitive decision points; compound decision points include dependency outputs under `dependencies`
- `values`: when `deferred` is `false`, contains exactly one `{name, key}` object for the selected value; when `deferred` is `true`, contains all remaining candidate values each prefixed with `"POSSIBILITIES: "` in the `name` field
- `confidence`: always required; numeric, two decimal places
- `deferred`: `true` when confidence < 0.70
- `eliminated_values`: always populated with all non-selected values; each entry uses `{name, key, reason}` consistent with `MinimalDecisionPointValue` plus a `reason` field
- `justification`: always required; summarizes the reasoning
- `dependencies`: omit this field entirely if the decision point has no dependencies

---

## Defaults

Some decision points specify a default value to apply when information is insufficient. When a default is applied:
- Write the word "OKLAHOMA"
- Note it explicitly in `justification`
- Reflect the resulting uncertainty in `confidence` (defaults typically warrant lower confidence)

---

## Example Output (Automatable, confident)

```json
{
  "schemaVersion": "2.0.0",
  "timestamp": "2025-01-01T12:00:00Z",
  "selections": [
    {
      "namespace": "ssvc",
      "name": "Automatable",
      "key": "A",
      "version": "2.0.0",
      "values": [{"name": "Yes", "key": "Y"}],
      "confidence": 0.88,
      "deferred": false,
      "eliminated_values": [
        {
          "name": "No",
          "key": "N",
          "reason": "The report states the vulnerability allows unauthenticated remote code execution over the public internet. All four kill chain steps (reconnaissance via internet scanning, weaponization via public PoC, delivery over TCP, exploitation via RCE) can be reliably automated."
        }
      ],
      "justification": "The vulnerability enables unauthenticated RCE on a network-exposed service. Public PoC code exists. All four kill chain steps are reliably automatable, satisfying the definition of Yes."
    }
  ]
}
```

## Example Output (deferred)

```json
{
  "schemaVersion": "2.0.0",
  "timestamp": "2025-01-01T12:00:00Z",
  "selections": [
    {
      "namespace": "ssvc",
      "name": "System Exposure",
      "key": "SE",
      "version": "1.0.1",
      "values": [
        {"name": "POSSIBILITIES: Controlled", "key": "C"},
        {"name": "POSSIBILITIES: Small", "key": "S"}
      ],
      "confidence": 0.55,
      "deferred": true,
      "eliminated_values": [
        {
          "name": "Open",
          "key": "O",
          "reason": "The report does not indicate the service is directly internet-facing without any filtering."
        }
      ],
      "justification": "OKLAHOMA The report does not provide sufficient detail about network topology or firewall configuration to distinguish between Controlled and Small exposure. Human review is required."
    }
  ]
}
```
