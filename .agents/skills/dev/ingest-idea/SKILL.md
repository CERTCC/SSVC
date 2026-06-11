---
name: ingest-idea
description: >
  Process a raw design idea from a GitHub Idea-type issue into formal specs
  and implementation notes, then close the idea issue, open a docs-only PR,
  and create a GitHub implementation Issue as a sub-issue of the idea issue.
  Runs a structured interview (grill-me), writes specs/<topic>.yaml and
  notes/<topic>.md, archives the idea to plan/history/, opens a docs-only PR
  with the specs-notes label, and creates a GitHub Issue tagged
  group:unscheduled. Use when the user says "ingest idea", references a GitHub
  Idea issue number, or wants to convert an idea into spec and notes files.
---

# Skill: Ingest Idea

Convert a GitHub Idea-type issue into durable specs and notes, then close the
idea issue and open a docs-only PR. This is the full end-to-end workflow:
interview → write → archive → PR → implementation issue.

## Workflow

### 1. Identify the target idea

If the user specified a GitHub issue number (e.g., `#42` or just `42`),
skip to step 2.

Otherwise, query GitHub for open Idea-type issues and present them to the
user as a multiple-choice list using `ask_user`. Include a **"Create a new
idea"** option at the end.

```bash
gh issue list --repo CERTCC/SSVC \
  --limit 200 \
  --json number,title,issueType \
  --jq '.[] | select(.issueType.name == "Idea") | "#\(.number): \(.title)"'
```

Build a `choices` array from the results (e.g. `["#42: Exploitation signal",
"#51: Decision point refactor", "Create a new idea"]`). Wait for the user's
selection before continuing.

#### 1a. Creating a new idea (if selected)

Ask the user to describe the idea in freeform text (using `ask_user`).
Synthesize a short, descriptive title from the description, then create
a GitHub Idea-type issue:

```bash
IDEA_BODY="<freeform description from user>"
IDEA_TITLE="<synthesized title>"
REPO_NODE_ID="MDEwOlJlcG9zaXRvcnkyMzU4MDkzNTU="
IDEA_TYPE_ID="IT_kwDOAjf0s84B_EoA"

TITLE_JSON=$(printf '%s' "${IDEA_TITLE}" \
  | python3 -c "import sys,json; print(json.dumps(sys.stdin.read()))")
BODY_JSON=$(printf '%s' "${IDEA_BODY}" \
  | python3 -c "import sys,json; print(json.dumps(sys.stdin.read()))")

IDEA_NUMBER=$(gh api graphql -f query="
mutation {
  createIssue(input: {
    repositoryId: \"${REPO_NODE_ID}\"
    title: ${TITLE_JSON}
    body: ${BODY_JSON}
    issueTypeId: \"${IDEA_TYPE_ID}\"
  }) {
    issue { number }
  }
}" --jq '.data.createIssue.issue.number')
echo "Created idea issue #${IDEA_NUMBER}"
```

Continue with step 2 using `IDEA_NUMBER`.

### 2. Read the idea

Fetch the idea from GitHub:

```bash
gh issue view "${IDEA_NUMBER}" --repo CERTCC/SSVC --json number,title,body
```

Use the issue title and body as the idea content for all subsequent steps.

### 3. Explore the codebase

Invoke the `study-project-docs` skill. It loads all specs, reads plan/,
docs/adr/, notes/, and docs/reference/code/, and scans src/ssvc/ and
src/test/.

Answer questions from exploration rather than asking the user where possible.

### 4. Interview with grill-me

Invoke the `grill-me` skill. Follow its instructions to walk every design
decision branch one at a time using `ask_user`, providing a recommendation
for each question. Reach shared understanding before writing anything.

### 5. Write the spec file

Create or modify `specs/<topic>.yaml` following `specs/meta-specifications.yaml`
conventions and the ID scheme already in use:

- Use a `FILE_PREFIX-SECTION_#-###` ID scheme (e.g., `EX-01-001`)
- Define requirements as YAML structures with RFC 2119 keywords
- Include an overview section with source reference and scope note
- Organize by category with clear section headings

### 6. Write the notes file

Create or modify `notes/<topic>.md` with implementation guidance:

- Decision table (question → decision → rationale)
- Key design patterns and code examples
- Call-site migration guide if replacing existing patterns
- Testing pattern examples
- Layer / import rules relevant to the change

### 7. Update specs/README.md

Add the new spec to both:

- The **Spec Files** table (file → ID → Kind → Topic)
- The **ID Prefix Convention** section if a new prefix is introduced

### 8. Lint markdown

Invoke the `format-markdown` skill on all new/modified markdown files. Fix
any errors before proceeding.

### 9. Archive the idea

Append a record to `plan/history/ideas.md` (create the file if it doesn't
exist). Include the full original idea text with a `**Processed**` line:

```bash
DATE=$(date +%Y-%m-%d)
cat >> plan/history/ideas.md <<ENDOFENTRY

---

## IDEA-${IDEA_NUMBER}: <short idea title>

<full idea title and body here>

**Processed**: ${DATE} — design decisions captured in
\`specs/<topic>.yaml\` and \`notes/<topic>.md\`.
ENDOFENTRY
```

### 10. Open a docs-only PR

Create a branch, commit all spec/notes/README changes, and open a PR
carrying the `specs-notes` label. Reference the originating idea issue in
the PR body so GitHub auto-links them:

```bash
git switch -c ingest/idea-<IDEA_NUMBER>-<slug>
git add specs/<topic>.yaml notes/<topic>.md specs/README.md plan/history/ideas.md
git commit -m "specs: ingest idea #<IDEA_NUMBER> — <short title>

- Add specs/<topic>.yaml (ID-01 through ID-NN)
- Add notes/<topic>.md with implementation guidance
- Archive idea #<IDEA_NUMBER> to plan/history/ideas.md

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
git push -u origin ingest/idea-<IDEA_NUMBER>-<slug>

gh pr create --repo CERTCC/SSVC \
  --title "specs: ingest idea #<IDEA_NUMBER> — <short title>" \
  --body "Docs-only PR: adds spec and notes for idea #<IDEA_NUMBER>.

Ref #<IDEA_NUMBER>

No .py files changed." \
  --label "specs-notes"
```

### 11. Create a GitHub Issue for implementation

After opening the docs-only PR, create a GitHub Issue to track implementation.
Wire the idea issue as the **parent** of the new implementation issue:

```bash
IMPL_ISSUE_NUMBER=$(gh api graphql -f query="
mutation {
  createIssue(input: {
    repositoryId: \"MDEwOlJlcG9zaXRvcnkyMzU4MDkzNTU=\"
    title: \"<Implementation title from spec>\"
    body: \"## Summary\n\n<Description from spec — one paragraph>\n\n## Acceptance Criteria\n\n- [ ] AC-1: <from spec>\n- [ ] AC-2: <from spec>\n\n## Reference\n\nSpec: \`specs/<topic>.yaml\`\nNotes: \`notes/<topic>.md\`\"
    issueTypeId: \"IT_kwDOAjf0s84AcFLs\"
    labelIds: [\"<group:unscheduled label node ID>\", \"<size: label node ID>\"]
  }) {
    issue { number }
  }
}" --jq '.data.createIssue.issue.number')
```

If the GraphQL label approach is cumbersome, fall back to `gh issue create`
and then set the parent relationship and labels separately:

```bash
IMPL_ISSUE_NUMBER=$(gh issue create --repo CERTCC/SSVC \
  --title "<Implementation title from spec>" \
  --body "## Summary

<Description from spec — one paragraph>

## Acceptance Criteria

- [ ] AC-1: <from spec>
- [ ] AC-2: <from spec>

## Reference

Spec: \`specs/<topic>.yaml\`
Notes: \`notes/<topic>.md\`" \
  --label "group:unscheduled,size:<S|M|L>" \
  | grep -oE '[0-9]+$')

# Wire idea as parent of implementation issue
gh api graphql -f query="
mutation {
  updateIssue(input: {
    id: \"<impl_issue_node_id>\"
    parentId: \"<idea_issue_node_id>\"
  }) { issue { number } }
}"
```

Set the `size:` label based on AC checkbox count:
1–2 ACs → `size:S`; 3–6 ACs → `size:M`; 7+ ACs → `size:L`.

The implementation Issue sits in `group:unscheduled` until a human runs
`review-priorities` to slot it into `plan/PRIORITIES.md`.

After creating the implementation issue, post the closing comment on the
idea issue and close it:

```bash
gh issue comment "${IDEA_NUMBER}" --repo CERTCC/SSVC \
  --body "✅ Ingested.

- Docs PR: <PR_URL>
- Implementation issue: #${IMPL_ISSUE_NUMBER}

Design decisions captured in \`specs/<topic>.yaml\` and \`notes/<topic>.md\`."

gh issue close "${IDEA_NUMBER}" --repo CERTCC/SSVC
```

## Checklist

- [ ] Target idea issue confirmed (specified by user, selected from list, or
  created inline)
- [ ] Idea content fetched from GitHub issue
- [ ] Codebase explored via `study-project-docs` before grilling
- [ ] All design decision branches resolved via grill-me
- [ ] `specs/<topic>.yaml` created with correct ID scheme
- [ ] `notes/<topic>.md` created with decision table + examples
- [ ] `specs/README.md` updated (Spec Files table + ID Prefix section if new)
- [ ] Markdown lint clean
- [ ] Idea archived to `plan/history/ideas.md`
- [ ] Docs-only PR opened with `specs-notes` label and `Ref #<idea_number>`
  in body
- [ ] Implementation GitHub Issue created with `group:unscheduled` and
  `size:` labels; idea issue wired as parent
- [ ] Idea issue commented with links to PR and implementation issue, then
  closed

## Conventions

- **Spec file names**: use the topic name, lowercase hyphenated with `.yaml`
  extension (e.g., `exploitation.yaml`, `decision-points.yaml`)
- **ID prefix**: derive from the topic abbreviation (e.g., `EX`, `DP`)
- **Notes file name**: same slug as spec file with `.md` extension, in
  `notes/` (e.g., `exploitation.md`, `decision-points.md`)
- **History archive**: append to `plan/history/ideas.md` using source ID
  `IDEA-<github_issue_number>`

## Label Naming Rules

All new Issues use `group:unscheduled` by default. If assigning a specific
`group:` label:

- **Never include a priority number** in the label name.
  Use `group:architecture-hardening`, **not** `group:473-architecture-hardening`.
- **Derive the slug** from the priority group title in kebab-case.
- **Check for label existence** before assigning. Create it if missing:

  ```bash
  gh label create "group:<slug>" \
    --repo CERTCC/SSVC \
    --description "<Priority group title (no number)>" \
    --color "#1d76db"
  ```
