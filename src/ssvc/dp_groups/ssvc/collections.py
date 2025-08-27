#!/usr/bin/env python
"""
Provides collections of decision points for each version of the SSVC.
"""
#  Copyright (c) 2023-2025 Carnegie Mellon University.
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


from ssvc.dp_groups.base import (
    DecisionPointGroup,
    get_all_decision_points_from,
)
from ssvc.dp_groups.ssvc.coordinator_publication import (
    COORDINATOR_PUBLICATION_1,
)
from ssvc.dp_groups.ssvc.coordinator_triage import COORDINATOR_TRIAGE_1
from ssvc.dp_groups.ssvc.deployer import (
    DEPLOYER_2,
    DEPLOYER_3,
    PATCH_APPLIER_1,
)
from ssvc.dp_groups.ssvc.supplier import PATCH_DEVELOPER_1, SUPPLIER_2


SSVCv1 = DecisionPointGroup(
    name="SSVCv1",
    definition="The first version of the SSVC.",
    version="1.0.0",
    decision_points=get_all_decision_points_from(
        PATCH_APPLIER_1, PATCH_DEVELOPER_1
    ),
)
"""SSVC version 1 decision point group."""

SSVCv2 = DecisionPointGroup(
    name="SSVCv2",
    definition="The second version of the SSVC.",
    version="2.0.0",
    decision_points=get_all_decision_points_from(
        COORDINATOR_PUBLICATION_1, COORDINATOR_TRIAGE_1, DEPLOYER_2, SUPPLIER_2
    ),
)
"""SSVC version 2 decision point group."""

SSVCv2_1 = DecisionPointGroup(
    name="SSVCv2.1",
    definition="The second version of the SSVC.",
    version="2.1.0",
    decision_points=get_all_decision_points_from(
        COORDINATOR_PUBLICATION_1, COORDINATOR_TRIAGE_1, DEPLOYER_3, SUPPLIER_2
    ),
)
"""SSVC version 2.1 decision point group."""

VERSIONS = (SSVCv1, SSVCv2, SSVCv2_1)
LATEST = VERSIONS[-1]


def main():
    for version in VERSIONS:
        print(version.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
