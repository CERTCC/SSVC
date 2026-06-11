# Agent Skills

This directory contains agent skill descriptors for the SSVC repository.
Skills are Markdown files that describe capabilities an AI coding agent can
invoke to perform structured tasks.

## Two-tier taxonomy

| Tier | Path | Audience | Purpose |
|------|------|----------|---------|
| **dev** | `.agents/skills/dev/` | Agents working on the SSVC codebase | Support SSVC development workflows (spec ingestion, codebase study, concern tracking, etc.) |
| **ssvc** | `.agents/skills/ssvc/` | Agents helping practitioners apply SSVC | SSVC domain work (evaluating decision points, building custom tables, etc.) |

## Canonical SKILL.md format

Every skill directory must contain a `SKILL.md` file. Required front-matter:

```yaml
---
name: "skill-name"       # unique, kebab-case
description: >
  One or more sentences describing what the skill does and when to invoke it.
---
```

Optional front-matter fields (add when stable):
`id`, `version`, `tags`, `runtime`, `capabilities`, `prerequisites`, `env`,
`usage_examples`.

After the front-matter, every `SKILL.md` must contain:

1. `## Purpose` — one paragraph explaining what the skill is for
2. At least one procedural section (`## Procedure` or `## Workflow`)

## Adding a new skill

1. Choose the correct tier (`dev/` or `ssvc/`).
2. Create `<tier>/<skill-name>/SKILL.md` with required front-matter, a
   `## Purpose` section, and at least one procedural section.
3. Validate locally:
   ```bash
   python -c "
   import pathlib, yaml, sys
   errs = []
   for p in pathlib.Path('.agents/skills').rglob('SKILL.md'):
       fm = yaml.safe_load(p.read_text().split('---', 2)[1])
       if not fm or not fm.get('name') or not fm.get('description'):
           errs.append(str(p))
   print('FAIL:', errs) if errs else print('OK')
   "
   ```
4. Open a PR — the `validate_skills` CI job runs automatically.

## CI validation

The workflow `.github/workflows/validate_skills.yml` runs on every PR and
push to `main` when any `SKILL.md` changes. It checks that every skill has
valid YAML front-matter with non-empty `name` and `description` fields.
