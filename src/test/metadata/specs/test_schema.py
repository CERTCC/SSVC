"""Tests for ssvc.metadata.specs.schema."""

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

import pytest
import yaml
from pydantic import ValidationError

from ssvc.metadata.specs.registry import load_registry
from ssvc.metadata.specs.schema import (
    BehaviorStep,
    BehavioralSpec,
    LintWarningCode,
    Postcondition,
    Precondition,
    RFC2119Priority,
    RelationType,
    Relationship,
    Scope,
    SpecFile,
    SpecGroup,
    SpecKind,
    SpecTag,
    StatementSpec,
)


# ---------------------------------------------------------------------------
# SpecIdStr pattern
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "spec_id",
    [
        "AB",
        "ABCDEFGH",
        "AB-01",
        "AB-01-001",
        "ABCD-99-999",
    ],
)
def test_spec_id_str_valid(spec_id):
    spec = StatementSpec(
        id=spec_id,
        priority=RFC2119Priority.MUST,
        statement="MUST do something",
        rationale="Because testing",
    )
    assert spec.id == spec_id


@pytest.mark.parametrize(
    "spec_id",
    [
        "A",  # too short
        "ABCDEFGHI",  # too long (9 chars)
        "ab-01-001",  # lowercase
        "AB-1-001",  # group with 1 digit
        "AB-01-01",  # spec number with 2 digits
        "",  # empty
        "AB_01",  # underscore
    ],
)
def test_spec_id_str_invalid(spec_id):
    with pytest.raises(ValidationError):
        StatementSpec(
            id=spec_id,
            priority=RFC2119Priority.MUST,
            statement="MUST do something",
            rationale="Because testing",
        )


# ---------------------------------------------------------------------------
# StatementSpec — absent optional fields are None
# ---------------------------------------------------------------------------


def test_statement_spec_absent_fields():
    """Optional fields default to None when not provided."""
    spec = StatementSpec(
        id="AB-01-001",
        priority=RFC2119Priority.MUST,
        statement="AB-01-001 MUST satisfy this",
    )
    assert spec.rationale is None
    assert spec.testable is True
    assert spec.kind is None
    assert spec.scope is None
    assert spec.tags is None
    assert spec.relationships is None
    assert spec.lint_suppress is None


def test_statement_spec_full():
    spec = StatementSpec(
        id="AB-01-001",
        priority=RFC2119Priority.SHOULD,
        statement="AB-01-001 SHOULD do the thing",
        rationale="Because it helps",
        testable=False,
        kind=SpecKind.IMPLEMENTATION,
        scope=[Scope.PROTOTYPE],
        tags=[SpecTag.TESTING],
        relationships=[
            Relationship(
                rel_type=RelationType.DEPENDS_ON,
                spec_id="AB-01-002",
                note="needs this first",
            )
        ],
        lint_suppress=[LintWarningCode.TESTABLE_WITHOUT_STEPS],
    )
    assert spec.testable is False
    assert spec.kind == SpecKind.IMPLEMENTATION
    assert spec.scope == [Scope.PROTOTYPE]
    assert spec.tags is not None and len(spec.tags) == 1
    assert spec.relationships is not None and len(spec.relationships) == 1
    assert spec.lint_suppress is not None and len(spec.lint_suppress) == 1


def test_statement_spec_empty_statement_rejected():
    with pytest.raises(ValidationError):
        StatementSpec(
            id="AB-01-001",
            priority=RFC2119Priority.MUST,
            statement="",
            rationale="Because testing",
        )


def test_statement_spec_empty_rationale_rejected():
    with pytest.raises(ValidationError):
        StatementSpec(
            id="AB-01-001",
            priority=RFC2119Priority.MUST,
            statement="AB-01-001 MUST satisfy this",
            rationale="",
        )


def test_statement_spec_rationale_none_allowed():
    spec = StatementSpec(
        id="AB-01-001",
        priority=RFC2119Priority.MUST,
        statement="AB-01-001 MUST satisfy this",
    )
    assert spec.rationale is None


def test_statement_spec_rationale_omitted_allowed():
    spec = StatementSpec(
        id="AB-01-001",
        priority=RFC2119Priority.MUST,
        statement="AB-01-001 MUST satisfy this",
        rationale=None,
    )
    assert spec.rationale is None


# ---------------------------------------------------------------------------
# Non-empty-if-present list validation
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "field", ["scope", "tags", "relationships", "lint_suppress"]
)
def test_empty_list_rejected(field: str) -> None:
    """Empty lists are rejected — use None for absent."""
    kwargs: dict = {
        "id": "AB-01-001",
        "priority": RFC2119Priority.MUST,
        "statement": "AB-01-001 MUST pass",
        field: [],
    }
    with pytest.raises(ValidationError, match="non-empty"):
        StatementSpec(**kwargs)  # type: ignore[arg-type]


# ---------------------------------------------------------------------------
# BehavioralSpec
# ---------------------------------------------------------------------------


def test_behavioral_spec_with_steps():
    spec = BehavioralSpec(
        id="AB-01-001",
        priority=RFC2119Priority.MUST,
        statement="AB-01-001 MUST follow this workflow",
        rationale="Protocol requirement",
        preconditions=[Precondition(description="System is ready")],
        steps=[
            BehaviorStep(
                order=1,
                actor="sender",
                action="sends the message",
                expected="message delivered",
            )
        ],
        postconditions=[Postcondition(description="State updated")],
    )
    assert spec.steps is not None and len(spec.steps) == 1
    assert spec.steps[0].order == 1
    assert spec.preconditions is not None and len(spec.preconditions) == 1
    assert spec.postconditions is not None and len(spec.postconditions) == 1


def test_behavioral_spec_absent_steps_valid():
    spec = BehavioralSpec(
        id="AB-01-001",
        priority=RFC2119Priority.MUST,
        statement="AB-01-001 MUST do something",
        rationale="Because testing",
    )
    assert spec.steps is None


@pytest.mark.parametrize("field", ["preconditions", "steps", "postconditions"])
def test_behavioral_spec_empty_list_rejected(field: str) -> None:
    kwargs: dict = {
        "id": "AB-01-001",
        "priority": RFC2119Priority.MUST,
        "statement": "AB-01-001 MUST pass",
        field: [],
    }
    with pytest.raises(ValidationError, match="non-empty"):
        BehavioralSpec(**kwargs)  # type: ignore[arg-type]


@pytest.mark.parametrize(
    "field", ["scope", "tags", "relationships", "lint_suppress"]
)
def test_behavioral_spec_inherited_empty_list_rejected(field: str) -> None:
    """Inherited non-empty validators still fire on BehavioralSpec instances."""
    kwargs: dict = {
        "id": "AB-01-001",
        "priority": RFC2119Priority.MUST,
        "statement": "AB-01-001 MUST pass",
        field: [],
    }
    with pytest.raises(ValidationError, match="non-empty"):
        BehavioralSpec(**kwargs)  # type: ignore[arg-type]


# ---------------------------------------------------------------------------
# SpecGroup
# ---------------------------------------------------------------------------


def test_spec_group_valid():
    group = SpecGroup(
        id="AB-01",
        title="Test Group",
        specs=[
            StatementSpec(
                id="AB-01-001",
                priority=RFC2119Priority.MUST,
                statement="AB-01-001 MUST do the thing",
                rationale="Rationale",
            )
        ],
    )
    assert group.id == "AB-01"
    assert len(group.specs) == 1


def test_spec_group_empty_title_rejected():
    with pytest.raises(ValidationError):
        SpecGroup(
            id="AB-01",
            title="",
            specs=[
                StatementSpec(
                    id="AB-01-001",
                    priority=RFC2119Priority.MUST,
                    statement="AB-01-001 MUST exist",
                )
            ],
        )


def test_spec_group_empty_specs_rejected():
    with pytest.raises(ValidationError, match="must not be empty"):
        SpecGroup(id="AB-01", title="Empty Group", specs=[])


def test_spec_group_description_nonempty_if_present():
    with pytest.raises(ValidationError):
        SpecGroup(
            id="AB-01",
            title="Group",
            description="",
            specs=[
                StatementSpec(
                    id="AB-01-001",
                    priority=RFC2119Priority.MUST,
                    statement="AB-01-001 MUST exist",
                )
            ],
        )


def test_spec_group_description_none_allowed():
    group = SpecGroup(
        id="AB-01",
        title="Group",
        specs=[
            StatementSpec(
                id="AB-01-001",
                priority=RFC2119Priority.MUST,
                statement="AB-01-001 MUST exist",
            )
        ],
    )
    assert group.description is None


def test_spec_group_empty_scope_rejected():
    with pytest.raises(ValidationError, match="non-empty"):
        SpecGroup(
            id="AB-01",
            title="Group",
            scope=[],
            specs=[
                StatementSpec(
                    id="AB-01-001",
                    priority=RFC2119Priority.MUST,
                    statement="AB-01-001 MUST exist",
                )
            ],
        )


# ---------------------------------------------------------------------------
# SpecFile
# ---------------------------------------------------------------------------


def test_spec_file_valid():
    sf = SpecFile(
        id="AB",
        title="Test File",
        description="A test file",
        version="0.1",
        kind=SpecKind.GENERAL,
        scope=[Scope.PRODUCTION],
        groups=[
            SpecGroup(
                id="AB-01",
                title="Group",
                specs=[
                    StatementSpec(
                        id="AB-01-001",
                        priority=RFC2119Priority.MUST,
                        statement="AB-01-001 MUST work",
                        rationale="Because",
                    )
                ],
            )
        ],
    )
    assert sf.id == "AB"
    assert len(sf.groups) == 1


def test_spec_file_requires_kind():
    with pytest.raises(ValidationError):
        SpecFile(  # type: ignore[call-arg]
            id="AB",
            title="Test File",
            description="A test file",
            version="0.1",
            scope=[Scope.PRODUCTION],
            groups=[
                SpecGroup(
                    id="AB-01",
                    title="Group",
                    specs=[
                        StatementSpec(
                            id="AB-01-001",
                            priority=RFC2119Priority.MUST,
                            statement="AB-01-001 MUST work",
                        )
                    ],
                )
            ],
        )


def test_spec_file_requires_scope():
    with pytest.raises(ValidationError):
        SpecFile(  # type: ignore[call-arg]
            id="AB",
            title="Test File",
            description="A test file",
            version="0.1",
            kind=SpecKind.GENERAL,
            groups=[
                SpecGroup(
                    id="AB-01",
                    title="Group",
                    specs=[
                        StatementSpec(
                            id="AB-01-001",
                            priority=RFC2119Priority.MUST,
                            statement="AB-01-001 MUST work",
                        )
                    ],
                )
            ],
        )


def test_spec_file_empty_scope_rejected():
    with pytest.raises(ValidationError, match="must not be empty"):
        SpecFile(
            id="AB",
            title="Test File",
            description="A test file",
            version="0.1",
            kind=SpecKind.GENERAL,
            scope=[],
            groups=[
                SpecGroup(
                    id="AB-01",
                    title="Group",
                    specs=[
                        StatementSpec(
                            id="AB-01-001",
                            priority=RFC2119Priority.MUST,
                            statement="AB-01-001 MUST work",
                        )
                    ],
                )
            ],
        )


def test_spec_file_empty_groups_rejected():
    with pytest.raises(ValidationError, match="must not be empty"):
        SpecFile(
            id="AB",
            title="Test File",
            description="A test file",
            version="0.1",
            kind=SpecKind.GENERAL,
            scope=[Scope.PRODUCTION],
            groups=[],
        )


# ---------------------------------------------------------------------------
# SpecRegistry / load_registry
# ---------------------------------------------------------------------------


def test_registry_duplicate_spec_id_raises(tmp_path):
    dup_data = {
        "id": "DUP",
        "title": "Dup File",
        "description": "Duplicate spec IDs",
        "version": "0.1",
        "kind": "general",
        "scope": ["production"],
        "groups": [
            {
                "id": "DUP-01",
                "title": "Group",
                "specs": [
                    {
                        "id": "DUP-01-001",
                        "priority": "MUST",
                        "statement": "DUP-01-001 MUST be unique",
                        "rationale": "Uniqueness",
                    },
                    {
                        "id": "DUP-01-001",  # duplicate
                        "priority": "SHOULD",
                        "statement": "DUP-01-001 SHOULD also exist",
                        "rationale": "But is duplicate",
                    },
                ],
            }
        ],
    }
    (tmp_path / "dup.yaml").write_text(yaml.dump(dup_data))
    with pytest.raises(ValueError, match="Duplicate spec ID"):
        load_registry(tmp_path)


def test_load_registry_round_trip(spec_dir):
    registry = load_registry(spec_dir)
    assert len(registry.files) == 1
    spec = registry.get("TST-01-001")
    assert spec.priority == RFC2119Priority.MUST


def test_load_registry_empty_dir(tmp_path):
    registry = load_registry(tmp_path)
    assert registry.files == []


def test_registry_get_unknown_raises(spec_dir):
    registry = load_registry(spec_dir)
    with pytest.raises(KeyError):
        registry.get("XX-99-999")


def test_registry_all_specs(spec_dir):
    registry = load_registry(spec_dir)
    assert "TST-01-001" in registry.all_specs


def test_registry_validate_cross_references_clean(spec_dir):
    registry = load_registry(spec_dir)
    assert registry.validate_cross_references() == []


# ---------------------------------------------------------------------------
# Inheritance resolution
# ---------------------------------------------------------------------------


def test_effective_kind_inherits_from_file(spec_dir):
    registry = load_registry(spec_dir)
    assert registry.get_effective_kind("TST-01-001") == SpecKind.GENERAL


def test_effective_scope_inherits_from_file(spec_dir):
    registry = load_registry(spec_dir)
    assert registry.get_effective_scope("TST-01-001") == [Scope.PRODUCTION]


def test_effective_kind_spec_override(tmp_path):
    data = {
        "id": "TST",
        "title": "Test",
        "description": "Test",
        "version": "0.1",
        "kind": "general",
        "scope": ["production"],
        "groups": [
            {
                "id": "TST-01",
                "title": "Group",
                "specs": [
                    {
                        "id": "TST-01-001",
                        "priority": "MUST",
                        "statement": "TST-01-001 MUST pass",
                        "kind": "implementation",
                    }
                ],
            }
        ],
    }
    (tmp_path / "test.yaml").write_text(yaml.dump(data))
    registry = load_registry(tmp_path)
    assert registry.get_effective_kind("TST-01-001") == SpecKind.IMPLEMENTATION


def test_effective_kind_group_override(tmp_path):
    data = {
        "id": "TST",
        "title": "Test",
        "description": "Test",
        "version": "0.1",
        "kind": "general",
        "scope": ["production"],
        "groups": [
            {
                "id": "TST-01",
                "title": "Group",
                "kind": "implementation",
                "specs": [
                    {
                        "id": "TST-01-001",
                        "priority": "MUST",
                        "statement": "TST-01-001 MUST pass",
                    }
                ],
            }
        ],
    }
    (tmp_path / "test.yaml").write_text(yaml.dump(data))
    registry = load_registry(tmp_path)
    assert registry.get_effective_kind("TST-01-001") == SpecKind.IMPLEMENTATION
