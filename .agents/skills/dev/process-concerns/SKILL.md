---
name: process-concerns
description: >
  Batch-process docs/reference/codebase/CONCERNS.md into GitHub Concern-type
  issues. Optionally runs a focused acquire-codebase-knowledge scan first.
  Deduplicates against existing open Concern issues — updating the body and
  appending a refresh comment on matches, creating new issues otherwise.
  Does not write to specs/, notes/, or open a PR.
  Use when you want to turn a codebase scan into a set of tracked GitHub issues.
---

# Skill: Process Concerns

Convert `docs/reference/codebase/CONCERNS.md` into GitHub `type:Concern`
issues. One issue per concern item. Deduplicates against open Concern issues
before creating anything.

## Constants

```text
REPO           = CERTCC/SSVC
REPO_NODE_ID   = MDEwOlJlcG9zaXRvcnkyMzU4MDkzNTU=
CONCERN_TYPE   = IT_kwDOAjf0s84B_2VT
```

---

## Workflow

### Phase 0 — Decide on Scan Freshness

Ask the user (via `ask_user`):

> Should I run a fresh `acquire-codebase-knowledge` scan (focused on
> CONCERNS.md) to get the latest snapshot, or use the existing
> `docs/reference/codebase/CONCERNS.md` as-is?

Choices:

1. **Run a fresh focused scan (Recommended)**
2. **Use the existing CONCERNS.md**

If the user chooses a fresh scan, invoke `acquire-codebase-knowledge` with
focus area `CONCERNS.md` only (do not regenerate the other six documents).
After the scan completes, proceed with the newly generated file.

### Phase 1 — Load Situation Awareness

List **all open Concern-type issues** in the repository using the GraphQL API
(the `gh issue list --json issueType` field is not supported by the CLI for
this repo — use GraphQL instead):

```bash
gh api graphql -f query='
query {
  repository(owner: "CERTCC", name: "SSVC") {
    issues(first: 200, states: [OPEN], filterBy: { issueTypeId: "IT_kwDOAjf0s84B_2VT" }) {
      nodes { number title }
    }
  }
}' --jq '.data.repository.issues.nodes[] | "#\(.number): \(.title)"'
```

Store the resulting list (numbers + titles) for deduplication in Phase 3.

### Phase 2 — Parse CONCERNS.md into topics

Read `docs/reference/codebase/CONCERNS.md`. **Do not assume a fixed format.**
The file is generated and its structure may differ across runs (tables, prose,
numbered lists, bullet points, or a mix). Instead, apply semantic extraction:

1. **Read the whole file** and identify every distinct concern, risk, debt
   item, or fragile area it describes — regardless of how it is formatted.
2. For each topic, extract whatever the file provides:
   - **Title**: the clearest short label for the concern (heading text,
     bold phrase, bullet key, or a synthesized summary if no label is present)
   - **Narrative**: any explanatory text, implications, or context
   - **Evidence**: file paths, module names, or line references (backtick
     strings, paths ending in `.py` / `.yml` / `.md`, etc.)
   - **Severity signal**: any explicit severity language ("high", "critical",
     "medium", "low") or implicit priority cues (section placement, wording)
   - **Category signal**: any language indicating the type of concern (risk,
     debt, security, performance, fragility, etc.)
3. **Infer severity** when no explicit label is given:
   - Items in sections labelled "high", "top", "critical" → `high`
   - Items in sections labelled "medium" → `medium`
   - Items in sections labelled "low", "minor", "constraint" → `low`
   - Default to `medium` when no signal is present
4. **Skip sections that are clearly not concerns** — e.g. sections titled
   "Safe operating advice", "Recommendations", "How to use this document",
   or similar guidance/meta sections that contain no trackable risk items.

### Phase 3 — Create or Update Issues

For each concern item from Phase 2:

#### 3a — Deduplication Check

Compare the concern's title text against the titles of existing open Concern
issues (loaded in Phase 1). Use semantic similarity — titles do not have to
be identical, but the subject matter must clearly match.

- **Match found** → proceed to **3b (Update)**.
- **No match** → proceed to **3c (Create)**.

#### 3b — Update Existing Issue

1. Synthesize a current, descriptive title from the item data (if notably
   different from the existing title, update it; otherwise leave it).
2. Rebuild the issue body from the concern template (see **Issue Body Format**
   below) using the latest scan data.
3. Edit the issue body:

   ```bash
   gh issue edit "${ISSUE_NUMBER}" \
     --repo CERTCC/SSVC \
     --body "$(cat body.md)"
   ```

4. Append a refresh comment:

   ```bash
   gh issue comment "${ISSUE_NUMBER}" \
     --repo CERTCC/SSVC \
     --body "♻️ Refreshed from codebase scan — $(date +%Y-%m-%d)."
   ```

#### 3c — Create New Issue

Synthesize a short, descriptive title from the item data. Build a body
following the **Issue Body Format** below. Ensure labels exist, create the
issue, then apply labels:

```bash
TITLE_JSON=$(printf '%s' "${TITLE}" \
  | python3 -c "import sys,json; print(json.dumps(sys.stdin.read()))")
BODY_JSON=$(printf '%s' "${BODY}" \
  | python3 -c "import sys,json; print(json.dumps(sys.stdin.read()))")

# Ensure labels exist before applying them
gh label create "group:unscheduled" \
  --repo CERTCC/SSVC \
  --description "Not yet scheduled in PRIORITIES.md" \
  --color "#e4e669" 2>/dev/null || true

gh label create "concern" \
  --repo CERTCC/SSVC \
  --description "Technical risk, debt, or fragile area" \
  --color "#d93f0b" 2>/dev/null || true

ISSUE_NUMBER=$(gh api graphql -f query="
mutation {
  createIssue(input: {
    repositoryId: \"${REPO_NODE_ID}\"
    title: ${TITLE_JSON}
    body: ${BODY_JSON}
    issueTypeId: \"${CONCERN_TYPE}\"
  }) {
    issue { number url }
  }
}" --jq '.data.createIssue.issue.number')

gh issue edit "${ISSUE_NUMBER}" \
  --repo CERTCC/SSVC \
  --add-label "group:unscheduled,concern"

echo "Created concern issue #${ISSUE_NUMBER}"
```

### Phase 4 — Summary

After processing all items, print a summary table:

```text
| # | Title | Action |
|---|-------|--------|
| 42 | Global registry with import-time side effects | created |
| 17 | CSV path inconsistency | updated |
```

---

## Issue Body Format

All Concern issues use the structure from Vultron's concern template (copy
this structure — SSVC does not yet have a `concern.md` issue template):

```markdown
## Summary

<one or two sentences synthesized from the item's heading and narrative>

## Category

- [x] <checked item matching the CONCERNS.md section>
- [ ] Top risk
- [ ] Technical debt
- [ ] Security
- [ ] Performance / scaling
- [ ] Fragile / high-churn area
- [ ] Other

## Severity

<high / medium / low — from the section mapping in Phase 2>

## Evidence

<file paths or module names extracted from the narrative text, one per bullet>

- `path/to/module.py`

## Impact if Ignored

<synthesized from the "Implications:" list or narrative in the source item>

## Suggested Action

<synthesized from any recommended action text, or a reasonable inference
from the concern description if no explicit suggestion is given>
```

Map concern language to Category checkboxes using best judgment:

| Signal in title or narrative | Category checkbox |
|---|---|
| risk, critical, blocking, severe | Top risk |
| debt, cleanup, refactor, TODO, legacy, deprecated | Technical debt |
| auth, injection, secret, exposure, CVE, privilege | Security |
| slow, latency, memory, scale, throughput | Performance / scaling |
| churn, fragile, hot-spot, tightly coupled, brittle | Fragile / high-churn area |
| anything else | Other |

---

## Constraints

- Do **not** write to `specs/`, `notes/`, `AGENTS.md`, or open a PR.
- Do **not** delete entries from `CONCERNS.md` — it is a generated file.
- Do **not** assign a `size:` label.
- Do **not** add a parent issue or link issues to each other.
- Do **not** create issues for sections that are clearly guidance/meta (e.g.
  "Safe operating advice"), not trackable concern items.
- Always check for existing open Concern issues before creating a new one.
- Use `ask_user` for all user-facing questions; never ask in plain text.
- Use the GraphQL API (not `gh issue list --json issueType`) for listing
  Concern issues — the CLI JSON field is not available for this repo.
- Do **not** hard-code section names from a previous CONCERNS.md run —
  always derive topics from the current file content.

## Checklist

- [ ] User chose scan freshness (fresh focused scan or use existing)
- [ ] All open Concern issues loaded via GraphQL for situation awareness
- [ ] CONCERNS.md read and semantically parsed into topics regardless of format
- [ ] Guidance/meta sections skipped (e.g. "Safe operating advice")
- [ ] Each item deduplicated against open issues (by title similarity)
- [ ] Matched items: body updated + refresh comment added
- [ ] New items: Concern issue created with `group:unscheduled` + `concern` labels
- [ ] Summary table printed
