# Skills Infrastructure

Implementation guidance for the SSVC agent skill system (spec `SK`).

## Decision Table

| Question | Decision | Rationale |
|----------|----------|-----------|
| Where do skills live? | `.agents/skills/dev/` for dev skills; `.agents/skills/ssvc/` for domain skills | Keeps machine-facing tooling separate from source and docs; two-tier split clarifies audience and lifecycle |
| What format does each skill use? | SKILL.md with YAML front-matter (`name` + `description` required) + `## Purpose` + at least one procedural section | Minimal required surface avoids over-engineering early skills; prose body is what agents actually execute |
| What should CI check? | Valid YAML front-matter, non-empty `name` and `description` fields | Automated enforcement keeps the skill surface reliable without burdening authors |
| Where does CI validation logic live? | Inline Python in `.github/workflows/validate_skills.yml` | Avoids proliferating auxiliary scripts; logic is short and clear in situ |
| How should the workflow trigger? | PRs and push-to-main filtered to `.agents/skills/**/SKILL.md` | Path filtering prevents wasted CI cycles on unrelated changes |

## Directory Layout

```
.agents/
  skills/
    dev/                        ← dev-workflow skills (support SSVC development)
      ingest-idea/
        SKILL.md
      load-specs/
        SKILL.md
      process-concerns/
        SKILL.md
      study-project-docs/
        SKILL.md
    ssvc/                       ← SSVC domain skills (help practitioners apply SSVC)
      evaluate-decision-point/
        SKILL.md
    README.md                   ← explains the two-tier split + SKILL.md format
```

## Canonical SKILL.md Format

### Required front-matter fields

```yaml
---
name: "skill-name"          # unique, kebab-case identifier
description: >
  One or more sentences describing what this skill does and when to invoke it.
  Agents use this text when deciding whether to call the skill.
---
```

### Optional front-matter fields

Any subset of the following may be added when the information is stable:

```yaml
id: "unique-id"
version: "1.0.0"
tags:
  - python
  - testing
runtime:
  language: "python"
  package_manager: "uv"
  framework: "pytest"
capabilities:
  - "Description of what the skill can do"
prerequisites:
  - "Tool or condition required before the skill can run"
env:
  - name: GITHUB_TOKEN
    description: "Required for GitHub API calls"
usage_examples:
  - prompt: "example user prompt that triggers this skill"
    command: "uv run some-command"
```

### Required body sections

After the front-matter block every SKILL.md MUST contain:

1. `## Purpose` — one-paragraph explanation of what the skill is for
2. At least one procedural section (`## Procedure`, `## Workflow`, etc.) — the
   step-by-step instructions an agent executes

### WIP stubs

New skills that are not yet ready for use SHOULD carry a prominent WIP notice
at the top of the `## Purpose` section:

```markdown
> **⚠️ Work in progress.** This skill is a placeholder stub.
> Procedure is intentionally incomplete.
```

## Migrating Existing Dev Skills

The four existing dev skills in `.agents/skills/` must be moved to
`.agents/skills/dev/` and their front-matter normalised to the canonical
format. The normalisation rules are:

1. Keep `name` and `description`. If `description` is missing or blank, add one.
2. Remove non-canonical fields that add noise without value (e.g., `author`,
   `shell`, `commands`, `inputs`, `outputs` from `load-specs`).  
   **Exception:** keep any optional field that is accurate and genuinely useful
   to agents (e.g., `tags`, `usage_examples`).
3. Do not alter any Markdown body content — only the front-matter changes.

## CI Validation

The workflow `.github/workflows/validate_skills.yml` discovers all
`.agents/skills/**/SKILL.md` files and validates each one:

```python
import sys, pathlib
try:
    import yaml
except ImportError:
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "pyyaml", "-q"], check=True)
    import yaml

errors = []
for path in sorted(pathlib.Path(".agents/skills").rglob("SKILL.md")):
    text = path.read_text()
    if not text.startswith("---"):
        errors.append(f"{path}: missing front-matter block")
        continue
    try:
        fm_text = text.split("---", 2)[1]
        fm = yaml.safe_load(fm_text)
    except yaml.YAMLError as e:
        errors.append(f"{path}: invalid YAML front-matter — {e}")
        continue
    for field in ("name", "description"):
        if not fm or not fm.get(field):
            errors.append(f"{path}: missing or empty required field '{field}'")

if errors:
    for e in errors:
        print(f"::error::{e}")
    sys.exit(1)
print(f"All {len(list(pathlib.Path('.agents/skills').rglob('SKILL.md')))} SKILL.md files valid.")
```

## Testing Patterns

Because skill validation is enforced in CI, no unit tests in `src/test/` are
needed for the validator itself. However, if the validator script grows beyond
~50 lines, extract it to `.github/scripts/validate_skills.py` and add a
`src/test/github/test_validate_skills.py` that exercises it with in-memory
fixtures.

## Adding a New Skill

1. Decide tier: dev workflow → `.agents/skills/dev/`; SSVC domain → `.agents/skills/ssvc/`
2. Create `<tier>/<skill-name>/SKILL.md` with required front-matter + `## Purpose` + `## Procedure`
3. Run the CI validation locally:
   ```bash
   python -c "
   import pathlib, yaml, sys
   for p in pathlib.Path('.agents/skills').rglob('SKILL.md'):
       fm = yaml.safe_load(p.read_text().split('---',2)[1])
       assert fm.get('name') and fm.get('description'), f'FAIL: {p}'
   print('OK')
   "
   ```
4. Open a PR — the `validate_skills` CI job will run automatically.
