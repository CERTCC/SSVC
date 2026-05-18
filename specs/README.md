# Specifications

This directory contains the normative requirement specifications for the SSVC
project, stored as structured YAML files and managed by the
`ssvc.metadata.specs` toolchain.

## Purpose

Spec files replace ad-hoc requirement lists with validated, machine-readable
YAML that can be linted, rendered to Markdown, exported to JSON, and consumed
by coding agents. The Python source in `src/ssvc/metadata/specs/` implements
the schema, registry, linter, and exporters.

## Spec Files

| File | ID | Kind | Topic |
|------|----|------|-------|
| `api.yaml` | AP | implementation | FastAPI REST API structure, response format, and error handling |
| `ci.yaml` | CI | general | Continuous integration gates and deployment automation |
| `codegen.yaml` | GN | implementation | Code generation source authority and artifact management |
| `domain-model.yaml` | DM | domain | SSVC object model: decision points, tables, outcomes, mixins |
| `registry.yaml` | RG | implementation | In-memory object registry structure, registration, and lookup |
| `spec-registry.yaml` | SR | general | Requirements for the spec file schema and toolchain itself |
| `testing.yaml` | TS | language | Test organisation, isolation, and quality standards |

### ID Prefix Convention

Each file owns a two-to-eight letter uppercase prefix. All group IDs and spec
IDs within a file must start with that prefix:

```
<FILE-ID>           e.g. DM
<FILE-ID>-<GG>      e.g. DM-01   (group)
<FILE-ID>-<GG>-<NNN>  e.g. DM-01-001  (spec)
```

### SpecKind Portability Tiers

| Kind | Applies to |
|------|-----------|
| `general` | Any project, any language |
| `pattern` | Architectural approach; language-agnostic |
| `domain` | SSVC problem domain; language-agnostic |
| `language` | Python ecosystem |
| `implementation` | This specific codebase |

## Tooling

### Lint

Validate all spec files in this directory:

```bash
uv run ssvc-spec-lint specs/
# or
uv run python -m ssvc.metadata.specs.lint specs/
```

Exit code `0` = no hard errors. Hard errors (duplicate IDs, dangling
cross-references, prefix mismatches) exit with code `1`. Advisory warnings
are printed to stdout but do not affect the exit code.

### Render

Render all specs as Markdown (human-readable):

```bash
uv run python -m ssvc.metadata.specs.render --format md specs/
```

Export as JSON (filterable):

```bash
uv run python -m ssvc.metadata.specs.render --format json specs/
```

### LLM Export

Dump a flat, inheritance-resolved JSON projection for coding agents:

```bash
uv run ssvc-spec-dump
# or filter to a single topic
uv run python -m ssvc.metadata.specs.render --format llm-json --topic DM specs/
```

## Adding a New Spec File

1. Choose a unique uppercase prefix (two to eight letters, e.g. `MY`).
2. Create `specs/my-topic.yaml` following the structure below.
3. Run `uv run ssvc-spec-lint specs/` — fix any reported errors.
4. Add a row to the table in this README.

Minimal skeleton:

```yaml
id: MY
title: My Topic
description: >
  One-paragraph description of the topic covered by this file.
version: "0.1.0"
kind: implementation   # general | pattern | domain | language | implementation
scope: [production]    # prototype | production

groups:
  - id: MY-01
    title: First Group
    description: What this group covers.
    specs:
      - id: MY-01-001
        priority: MUST          # MUST | MUST_NOT | SHOULD | SHOULD_NOT | MAY
        statement: >
          MY-01-001 The system MUST do the thing.
        rationale: >
          One sentence explaining why this requirement exists.
        testable: true
        tags: [tooling]         # ci-cd | code-style | documentation |
                                # performance | security | testing | tooling
```

### Requirement Authoring Checklist

- [ ] Statement is **atomic**: covers exactly one verifiable behaviour.
- [ ] Statement **includes the spec ID** at the start (e.g. `MY-01-001 MUST …`).
- [ ] `rationale` explains *why*, not just *what*.
- [ ] `testable: true` unless the requirement can only be verified by human
      inspection; if `false`, add `lint_suppress: [testable_without_steps]`.
- [ ] At least one `tag` is set.
- [ ] No requirement text is duplicated in another spec file.
