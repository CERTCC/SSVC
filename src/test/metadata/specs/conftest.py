"""Shared fixtures for test/metadata/specs/ tests."""


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

from ssvc.metadata.specs.registry import load_registry

MINIMAL_YAML = {
    "id": "TST",
    "title": "Test Spec File",
    "description": "A spec file for unit testing",
    "version": "0.1",
    "kind": "general",
    "scope": ["production"],
    "groups": [
        {
            "id": "TST-01",
            "title": "Test Group One",
            "specs": [
                {
                    "id": "TST-01-001",
                    "priority": "MUST",
                    "statement": "TST-01-001 MUST satisfy the test",
                    "rationale": "Required for test coverage",
                    "tags": ["testing"],
                }
            ],
        }
    ],
}

SECOND_YAML = {
    "id": "MOR",
    "title": "More Test Specs",
    "description": "Additional spec file for testing",
    "version": "0.2",
    "kind": "general",
    "scope": ["production"],
    "groups": [
        {
            "id": "MOR-01",
            "title": "More Group",
            "specs": [
                {
                    "id": "MOR-01-001",
                    "priority": "SHOULD",
                    "statement": "MOR-01-001 SHOULD also work correctly",
                    "rationale": "Multi-file registry testing",
                    "tags": ["testing"],
                }
            ],
        }
    ],
}


@pytest.fixture
def spec_dir(tmp_path):
    """Single-file spec directory with a minimal valid YAML spec."""
    (tmp_path / "test_specs.yaml").write_text(yaml.dump(MINIMAL_YAML))
    return tmp_path


@pytest.fixture
def multi_spec_dir(tmp_path):
    """Multi-file spec directory with two distinct valid YAML specs."""
    (tmp_path / "test_specs.yaml").write_text(yaml.dump(MINIMAL_YAML))
    (tmp_path / "more_specs.yaml").write_text(yaml.dump(SECOND_YAML))
    return tmp_path


@pytest.fixture
def loaded_registry(spec_dir):
    """Loaded SpecRegistry from the minimal single-file spec_dir."""
    return load_registry(spec_dir)
