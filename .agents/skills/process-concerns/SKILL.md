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

### Phase 2 — Parse CONCERNS.md

Read `docs/reference/codebase/CONCERNS.md`. The file uses **prose/narrative
format** (not tables). Extract individual concern items from the following
sections:

| Section heading | Severity | Category |
|---|---|---|
| High-priority concerns | high | Top risk |
| Medium-priority concerns | medium | Technical debt |
| Lower-priority constraints | low | Other |
| Change-risk hotspots | medium | Fragile / high-churn area |

**Do not create issues for the "Safe operating advice" section** — it is
guidance text, not a concern to track.

For each numbered item under the first three sections (e.g. `### 1. Title`),
extract:
- **Title**: the heading text after the number (e.g. `Global registry with
  import-time side effects`)
- **Body narrative**: the paragraph(s) following the heading
- **Evidence**: any backtick file paths or module names mentioned in the text
- **Severity**: derived from the parent section (see table above)
- **Category**: derived from the parent section (see table above)

For the **Change-risk hotspots** section, each bullet point is its own concern
item. The bullet text is the title; the file paths within it are the evidence.

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

Map CONCERNS.md sections to Category checkboxes:

| CONCERNS.md section | Category checkbox |
|---|---|
| High-priority concerns | Top risk |
| Medium-priority concerns | Technical debt |
| Lower-priority constraints | Other |
| Change-risk hotspots | Fragile / high-churn area |

---

## Constraints

- Do **not** write to `specs/`, `notes/`, `AGENTS.md`, or open a PR.
- Do **not** delete entries from `CONCERNS.md` — it is a generated file.
- Do **not** assign a `size:` label.
- Do **not** add a parent issue or link issues to each other.
- Do **not** create issues for the "Safe operating advice" section.
- Always check for existing open Concern issues before creating a new one.
- Use `ask_user` for all user-facing questions; never ask in plain text.
- Use the GraphQL API (not `gh issue list --json issueType`) for listing
  Concern issues — the CLI JSON field is not available for this repo.

## Checklist

- [ ] User chose scan freshness (fresh focused scan or use existing)
- [ ] All open Concern issues loaded via GraphQL for situation awareness
- [ ] CONCERNS.md parsed into per-item concerns (numbered items + hotspot bullets)
- [ ] "Safe operating advice" section skipped
- [ ] Each item deduplicated against open issues (by title similarity)
- [ ] Matched items: body updated + refresh comment added
- [ ] New items: Concern issue created with `group:unscheduled` + `concern` labels
- [ ] Summary table printed
