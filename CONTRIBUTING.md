# How to contribute

Thanks for your help on improving our stakeholder-specific vulnerability categorization work.
To account for different stakeholder perspectives, we benefit from a diverse group of contributors.

Please see our project documentation in the [wiki](https://github.com/CERTCC/SSVC/wiki) that accompanies this repository
for more information on how you can contribute to the project.

## Development Setup

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) - Fast Python package installer and resolver
- [pre-commit](https://pre-commit.com/) - Git hooks framework

### Installing Dependencies and Git Hooks

1. **Set up the development environment:**

   ```bash
   make dev
   ```

2. **Install pre-commit hooks:**

   ```bash
   uv run pre-commit install
   ```

### Pre-Commit Hooks

This repository uses [pre-commit](https://pre-commit.com/) to enforce code quality standards before commits. The following hooks are configured:

| Hook | Scope | Behavior |
|------|-------|----------|
| **Black** | Python files | Auto-formats code; blocks commit if changes made |
| **Markdownlint** | Markdown files | Auto-fixes linting issues; blocks commit if changes made |
| **Doctools** | Decision point/table Python files | Regenerates JSON files; blocks commit if changes made (review before staging) |
| **Pytest** | All tests | Runs full test suite; non-blocking (warning only) |

**Running hooks manually:**

```bash
uv run pre-commit run --all-files
```

**Skipping hooks (use sparingly):**

```bash
git commit --no-verify
```

## Licenses

See [LICENSE](https://github.com/CERTCC/SSVC/blob/main/LICENSE)

## Questions

If you have any questions, an [issue](https://github.com/CERTCC/SSVC/issues) or
[discussion](https://github.com/CERTCC/SSVC/discussions) is the best way to get in touch with us.
