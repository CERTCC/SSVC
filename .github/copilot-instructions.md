# GitHub Copilot Instructions for SSVC

This repository contains the **Stakeholder-Specific Vulnerability Categorization (SSVC)** project, which provides a system for prioritizing actions during vulnerability management.

## Project Overview

SSVC is a modular decision-making framework for vulnerability management that includes:
- Python modules for decision points, decision tables, and outcomes
- MkDocs-based documentation website
- Interactive calculators and policy explorers
- JSON/CSV data files for decision tables
- Docker and Make-based development and deployment

## Technology Stack

- **Primary Language**: Python 3.x
- **Package Management**: uv (package and project manager)
- **Build Tool**: Make
- **Documentation**: MkDocs with Material theme
- **Testing**: pytest
- **Data Models**: Pydantic for JSON schema validation
- **Scientific Computing**: NumPy, SciPy, scikit-learn
- **Web Framework**: FastAPI (for API endpoints)
- **Containerization**: Docker and Docker Compose

## Project Structure

- `/src/ssvc/` - Core Python modules for SSVC functionality
  - `decision_points/` - Decision point definitions
  - `decision_tables/` - Decision table implementations
  - `api/` - FastAPI application
  - `outcomes/` - Outcome definitions
  - `dp_groups/` - Decision point groups
  - `registry/` - Registry functionality
- `/docs/` - Markdown documentation source files
- `/data/` - JSON and CSV data files for decision tables
- `/src/test/` - Unit tests
- `/docker/` - Docker configurations
- `/obsolete/` - Deprecated code (do not modify)

## Make Commands

Use `make help` to see all available commands. Common targets include:

- `make dev` - Set up development environment
- `make test` - Run tests locally
- `make docker_test` - Run tests in Docker
- `make docs_local` - Serve documentation locally (http://localhost:8000/SSVC/)
- `make docs` - Build and run documentation in Docker
- `make api_dev` - Run API locally with auto-reload
- `make api` - Build and run API in Docker
- `make mdlint_fix` - Run markdown linting with auto-fix
- `make regenerate_json` - Regenerate JSON files from Python modules

## Development Workflow

## Coding Conventions

### Python Code

- Follow PEP 8 style guidelines
- Use type hints for function signatures and return types
- Use Pydantic models for data validation
- Document classes and functions with docstrings
- Prefer explicit imports over wildcard imports
- Module structure uses absolute imports from `ssvc` package

### Naming Conventions

- Python files: `snake_case.py`
- Classes: `PascalCase`
- Functions/variables: `snake_case`
- Constants: `UPPER_SNAKE_CASE`

## Testing Requirements

### Test Structure

- Unit tests use pytest framework
- Tests are located in `/src/test/`
- Test files follow pattern: `test_*.py`
- Run tests with: `make test` or `uv run pytest -v`

### Test Coverage

- Write tests for new Python modules
- Ensure decision points and tables have corresponding tests
- Test JSON schema validation
- Validate data model serialization/deserialization

### Before Committing

1. Run all tests: `make test`
2. Ensure no test failures
3. Fix any linting issues: `make mdlint_fix`
4. Verify documentation builds: `make docs_local`

## Documentation

### Writing Documentation

- Documentation uses MkDocs with Material theme
- Files are in Markdown format in `/docs/`
- Use Python exec blocks for dynamic content generation
- Include examples and code snippets
- Follow existing documentation structure

### Documentation Features

- Automatic API documentation via mkdocstrings
- Python module imports for dynamic content generation
- BibTeX citations via mkdocs-bibtex
- Add markdown files to site navigation by specifying them in `mkdocs.yml`
- Include markdown files in other markdown files with `mkdocs-include-markdown-plugin`
- Dynamically generate content from python code blocks using the `markdown-exec` plugin

## Data Files

### JSON Files

- Located in `/data/json/`
- Generated from Python Pydantic models
- Use JSON schema validation

### CSV Files

- Located in `/data/csv/`
- Define decision table outcomes
- Generated from python modules (The python data objects are authoritative)
- Allows users to explore customizing SSVC for specific environments

## Common Pitfalls

1. **Import Paths**: Use absolute imports like `from ssvc.module import Class`, not relative imports
2. **PYTHONPATH**: When running scripts directly, set `export PYTHONPATH=$PYTHONPATH:$(pwd)/src`
3. **JSON Regeneration**: After modifying decision points/tables, regenerate JSON with `make regenerate_json`
4. **Docker Context**: Some make targets use Docker, others run locally - check the Makefile
5. **Package Management**: Use `make` commands or `uv` directly, not pip
6. **Obsolete Code and Documentation**: Never modify files in `/obsolete/`, `/doc/`, or `/pdfs/` directories
7. **Porting from other repos**: Always verify that directory paths actually exist in this repo before using them. Don't assume paths from the source repo (e.g., `vultron_pub`) map 1:1 to this one.
8. **Finishing what was started**: If you encounter a broken/incidental issue while working on a primary task, complete the primary task first. Fix incidentals in a follow-up step or commit, not mid-task.

## Agent-Facing Tooling

This project maintains agent-facing infrastructure alongside the codebase:

- **`.agents/skills/`** — Project-local skills (ingest-idea, load-specs, process-concerns, study-project-docs). Always check here for project-specific workflows before inventing one.
- **`uv run ssvc-spec-dump`** — Dumps all YAML specs to stdout as flat JSON. Use this (not raw file reads) to load specs in bulk. This is what the `load-specs` skill invokes.
- **`docs/reference/codebase/`** — Agent-facing codebase reference files: `ARCHITECTURE.md`, `CONVENTIONS.md`, `STRUCTURE.md`, `STACK.md`, `TESTING.md`, `CONCERNS.md`, `INTEGRATIONS.md`. These are always-current and should be preferred over ad-hoc codebase exploration.
- **`specs/`** — Normative YAML spec files for this project (e.g., `domain-model.yaml`, `versioning.yaml`). These are the authoritative source of engineering requirements.
- **`plan/`** — Project planning files: `PRIORITIES.md`, `BUILD_LEARNINGS.md`, `history/`.

## Behavioral Guidelines

### Bulk / Irreversible Actions

Before performing any bulk, destructive, or irreversible action (e.g., updating many GitHub issues, deleting files, mass-renaming), present a plan or summary of what will change and get explicit confirmation. This especially applies to GitHub API calls that affect many issues at once. "Collect and review" requests should surface a list for review — not act on it immediately.

### CONCERNS.md Parsing

`docs/reference/codebase/CONCERNS.md` is generated output and its section structure may change between runs. Parse it semantically (extract concern topics and infer severity from language cues) rather than matching specific hardcoded section headings.

## API Development

- FastAPI application is in `/src/ssvc/api/`
- Run locally with auto-reload: `make api_dev` (serves on http://127.0.0.1:8000/docs)
- Run in Docker: `make api` (serves on http://127.0.0.1:8001/SSVC/)

## Git Workflow

- Create feature branches for new work
- Write descriptive commit messages
- Reference issue numbers in commits when applicable
- Keep commits focused and atomic
- Run tests before pushing

## Additional Resources

- Main documentation: https://certcc.github.io/SSVC/
- Source repository: https://github.com/CERTCC/SSVC
- SSVC Calculator: https://certcc.github.io/SSVC/ssvc-calc/
- Contributing guide: See CONTRIBUTING.md
- Project wiki: https://github.com/CERTCC/SSVC/wiki

## Special Notes

- This project uses a MIT (SEI)-style license with Carnegie Mellon University copyright (see LICENSE file)
- Decision points and tables follow SSVC specification
- Backward compatibility is important for existing data files
- Documentation changes should be reflected in both `/docs/` and `/src/README.md` when applicable
