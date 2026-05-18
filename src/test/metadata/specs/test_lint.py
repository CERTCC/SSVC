"""Tests for ssvc.metadata.specs.lint."""

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

import yaml

from ssvc.metadata.specs.lint import lint


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _write_yaml(path, data, filename="specs.yaml"):
    (path / filename).write_text(yaml.dump(data))


def _minimal_spec(spec_id="TST-01-001", priority="MUST", extra=None):
    spec = {
        "id": spec_id,
        "priority": priority,
        "statement": f"{spec_id} MUST do the thing",
        "rationale": "Because testing",
        "tags": ["testing"],
    }
    if extra:
        spec.update(extra)
    return {
        "id": "TST",
        "title": "Test File",
        "description": "Test spec file",
        "version": "0.1",
        "kind": "general",
        "scope": ["production"],
        "groups": [
            {
                "id": "TST-01",
                "title": "Group",
                "specs": [spec],
            }
        ],
    }


# ---------------------------------------------------------------------------
# Clean cases
# ---------------------------------------------------------------------------


def test_lint_clean_dir(tmp_path, capsys):
    _write_yaml(tmp_path, _minimal_spec())
    result = lint(tmp_path)
    captured = capsys.readouterr()
    assert result == 0
    assert "[ERROR]" not in captured.err


def test_lint_empty_dir(tmp_path):
    result = lint(tmp_path)
    assert result == 0


# ---------------------------------------------------------------------------
# Hard errors
# ---------------------------------------------------------------------------


def test_lint_duplicate_spec_ids(tmp_path, capsys):
    data = _minimal_spec("DUP-01-001")
    data["id"] = "DUP"
    data["groups"][0]["id"] = "DUP-01"
    data["groups"][0]["specs"][0]["statement"] = "DUP-01-001 MUST be unique"
    _write_yaml(tmp_path, data, "file1.yaml")
    _write_yaml(tmp_path, data, "file2.yaml")
    result = lint(tmp_path)
    assert result == 1


def test_lint_dangling_relationship(tmp_path, capsys):
    data = _minimal_spec(
        extra={
            "relationships": [
                {"rel_type": "depends_on", "spec_id": "XX-99-999"}
            ]
        }
    )
    _write_yaml(tmp_path, data)
    result = lint(tmp_path)
    captured = capsys.readouterr()
    assert result == 1
    assert "XX-99-999" in captured.err


def test_lint_group_prefix_mismatch(tmp_path, capsys):
    data = _minimal_spec()
    data["groups"][0]["id"] = "ZZZ-01"  # wrong prefix
    _write_yaml(tmp_path, data)
    result = lint(tmp_path)
    assert result == 1


def test_lint_spec_id_prefix_mismatch(tmp_path, capsys):
    data = _minimal_spec()
    data["groups"][0]["specs"][0]["id"] = "TST-02-001"  # wrong group
    data["groups"][0]["specs"][0][
        "statement"
    ] = "TST-02-001 MUST be in wrong group"
    _write_yaml(tmp_path, data)
    result = lint(tmp_path)
    assert result == 1


# ---------------------------------------------------------------------------
# Advisory warnings
# ---------------------------------------------------------------------------


def test_lint_warns_missing_tags(tmp_path, capsys):
    data = _minimal_spec()
    del data["groups"][0]["specs"][0]["tags"]
    _write_yaml(tmp_path, data)
    result = lint(tmp_path)
    captured = capsys.readouterr()
    assert result == 0
    assert "[WARN]" in captured.out
    assert "no tags" in captured.out


def test_lint_warns_testable_false_no_steps(tmp_path, capsys):
    data = _minimal_spec(extra={"testable": False})
    _write_yaml(tmp_path, data)
    result = lint(tmp_path)
    captured = capsys.readouterr()
    assert result == 0
    assert "testable=false" in captured.out


def test_lint_suppress_testable_warning(tmp_path, capsys):
    data = _minimal_spec(
        extra={
            "testable": False,
            "lint_suppress": ["testable_without_steps"],
        }
    )
    _write_yaml(tmp_path, data)
    result = lint(tmp_path)
    captured = capsys.readouterr()
    assert result == 0
    assert "testable=false" not in captured.out


def test_lint_warns_rationale_too_long(tmp_path, capsys):
    long_rationale = "x" * 501
    data = _minimal_spec(extra={"rationale": long_rationale})
    _write_yaml(tmp_path, data)
    result = lint(tmp_path)
    captured = capsys.readouterr()
    assert result == 0
    assert "rationale exceeds" in captured.out
