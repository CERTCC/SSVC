"""Pydantic schema for ``specs/*.yaml`` structured requirement files.

Design principle: YAML is the authoritative data source.  The schema
validates what is present but does **not** silently inject defaults for
absent fields.  Inheritable fields (``kind``, ``scope``) are required at
the file level and optional at group/spec level; effective values are
resolved by the registry loader, not by Pydantic defaults.

TODO: Consider extracting this module (ssvc.metadata.specs) into a
standalone shared library (e.g. ``certcc-spec-registry``) so that both
SSVC and Vultron can depend on it rather than maintaining parallel copies.
"""

#  Copyright (c) 2026 Carnegie Mellon University.
#  NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE
#  ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS.
#  CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND,
#  EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT
#  NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR
#  MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE
#  OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE
#  ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM
#  PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
#  Licensed under a MIT (SEI)-style license, please see LICENSE or contact
#  permission@sei.cmu.edu for full terms.
#  [DISTRIBUTION STATEMENT A] This material has been approved for
#  public release and unlimited distribution. Please see Copyright notice
#  for non-US Government use and distribution.
#  This Software includes and/or makes use of Third-Party Software each
#  subject to its own license.
#  DM24-0278

from __future__ import annotations

from enum import StrEnum
from typing import Annotated, Union

from pydantic import BaseModel, StringConstraints, field_validator

from ssvc.metadata.base import NonEmptyStr

SpecIdStr = Annotated[
    str,
    StringConstraints(pattern=r"^[A-Z]{2,8}(-\d{2}(-\d{3})?)?$"),
]


class RFC2119Priority(StrEnum):
    """RFC 2119 priority levels for requirements."""

    MUST = "MUST"
    MUST_NOT = "MUST_NOT"
    SHOULD = "SHOULD"
    SHOULD_NOT = "SHOULD_NOT"
    MAY = "MAY"


class RelationType(StrEnum):
    """Relationship types between spec requirements."""

    IMPLEMENTS = "implements"
    SUPERSEDES = "supersedes"
    EXTENDS = "extends"
    DEPENDS_ON = "depends_on"
    CONFLICTS = "conflicts"
    REFINES = "refines"
    DERIVES_FROM = "derives_from"
    VERIFIES = "verifies"
    PART_OF = "part_of"
    CONSTRAINS = "constrains"


class SpecKind(StrEnum):
    """Portability tier for a spec requirement.

    The five tiers form a portability hierarchy.  Use them to filter which
    specs apply to your project:

    - ``general``        — Universal: any project, any language.
                           Examples: idempotency, linter discipline, CI
                           security.
    - ``pattern``        — Architectural / framework approach: language-agnostic
                           and domain-independent.
                           Examples: hexagonal architecture, event-driven
                           dispatch, structured logging format.
    - ``domain``         — Project domain: language-agnostic but specific to
                           the problem domain of this repository.
                           Examples (for SSVC): decision point logic,
                           scoring tree semantics, stakeholder outcome
                           definitions.
    - ``language``       — Python ecosystem: any Python project.
                           Examples: pydantic conventions, pytest, FastAPI
                           patterns.
    - ``implementation`` — This specific codebase.
                           Examples: file paths under ``src/ssvc/``, class
                           names, tooling configuration.

    Portability use cases
    ~~~~~~~~~~~~~~~~~~~~~
    - Implementing the domain in Python          → all five tiers
    - Implementing the domain in another language → general + pattern + domain
    - Different domain, same Python stack         → general + pattern + language
    - Architectural wisdom, any language          → general + pattern
    - Universal wisdom only                       → general
    """

    GENERAL = "general"
    PATTERN = "pattern"
    DOMAIN = "domain"
    LANGUAGE = "language"
    IMPLEMENTATION = "implementation"


class Scope(StrEnum):
    """Deployment scope for a spec requirement."""

    PROTOTYPE = "prototype"
    PRODUCTION = "production"


class SpecTag(StrEnum):
    """Controlled vocabulary of topic tags.

    This is an intentionally small generic set.  Domain-specific tags
    should be added here as the project's spec vocabulary grows.

    TODO: Extend this enum with SSVC-specific tags (e.g. decision-points,
    scoring, stakeholder-roles) as specs are authored.
    """

    CI_CD = "ci-cd"
    CODE_STYLE = "code-style"
    DOCUMENTATION = "documentation"
    PERFORMANCE = "performance"
    SECURITY = "security"
    TESTING = "testing"
    TOOLING = "tooling"


class LintWarningCode(StrEnum):
    """Named linter warnings that can be suppressed via ``lint_suppress``."""

    TESTABLE_WITHOUT_STEPS = "testable_without_steps"
    RATIONALE_TOO_LONG = "rationale_too_long"
    MISSING_TAGS = "missing_tags"


class Relationship(BaseModel):
    """Cross-spec traceability link."""

    rel_type: RelationType
    spec_id: SpecIdStr
    note: str | None = None


class StatementSpec(BaseModel):
    """A single normative statement requirement.

    Inheritable fields (``kind``, ``scope``) default to ``None``, meaning
    "inherit from parent group or file."  The registry loader resolves
    effective values after loading.
    """

    id: SpecIdStr
    priority: RFC2119Priority
    statement: NonEmptyStr
    rationale: NonEmptyStr | None = None
    testable: bool = True
    kind: SpecKind | None = None
    scope: list[Scope] | None = None
    tags: list[SpecTag] | None = None
    relationships: list[Relationship] | None = None
    lint_suppress: list[LintWarningCode] | None = None

    @field_validator("scope", "tags", "relationships", "lint_suppress")
    @classmethod
    def _nonempty_if_present(cls, v: list | None, info: object) -> list | None:
        if v is not None and len(v) == 0:
            field_name = getattr(info, "field_name", "list field")
            raise ValueError(f"{field_name} must be non-empty if present")
        return v


class Precondition(BaseModel):
    """A precondition for a behavioral spec."""

    description: str


class BehaviorStep(BaseModel):
    """A single step in a behavioral spec sequence."""

    order: int
    actor: str
    action: str
    expected: str | None = None


class Postcondition(BaseModel):
    """A postcondition for a behavioral spec."""

    description: str


class BehavioralSpec(StatementSpec):
    """A spec with structured pre/step/post conditions."""

    preconditions: list[Precondition] | None = None
    steps: list[BehaviorStep] | None = None
    postconditions: list[Postcondition] | None = None

    @field_validator("preconditions", "steps", "postconditions")
    @classmethod
    def _nonempty_if_present(cls, v: list | None, info: object) -> list | None:
        if v is not None and len(v) == 0:
            field_name = getattr(info, "field_name", "list field")
            raise ValueError(f"{field_name} must be non-empty if present")
        return v


Spec = Union[BehavioralSpec, StatementSpec]


class SpecGroup(BaseModel):
    """A logical grouping of specs within a file.

    ``kind`` and ``scope`` are optional overrides; when absent, values are
    inherited from the containing :class:`SpecFile`.
    """

    id: SpecIdStr
    title: NonEmptyStr
    description: NonEmptyStr | None = None
    kind: SpecKind | None = None
    scope: list[Scope] | None = None
    specs: list[Spec]

    @field_validator("scope")
    @classmethod
    def _nonempty_if_present(cls, v: list | None, info: object) -> list | None:
        if v is not None and len(v) == 0:
            field_name = getattr(info, "field_name", "list field")
            raise ValueError(f"{field_name} must be non-empty if present")
        return v

    @field_validator("specs")
    @classmethod
    def _specs_nonempty(cls, v: list) -> list:
        if not v:
            raise ValueError("specs must not be empty")
        return v


class SpecFile(BaseModel):
    """One YAML spec file with its groups and file-level metadata.

    ``kind`` and ``scope`` are required at the file level and serve as
    defaults for groups and specs that do not override them.
    """

    id: str
    title: NonEmptyStr
    description: NonEmptyStr
    version: NonEmptyStr
    kind: SpecKind
    scope: list[Scope]
    groups: list[SpecGroup]

    @field_validator("scope")
    @classmethod
    def _scope_nonempty(cls, v: list) -> list:
        if not v:
            raise ValueError("scope must not be empty")
        return v

    @field_validator("groups")
    @classmethod
    def _groups_nonempty(cls, v: list) -> list:
        if not v:
            raise ValueError("groups must not be empty")
        return v
