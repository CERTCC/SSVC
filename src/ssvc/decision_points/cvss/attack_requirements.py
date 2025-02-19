#!/usr/bin/env python
"""
CVSS Attack Requirements
"""
#  Copyright (c) 2023-2025 Carnegie Mellon University and Contributors.
#  - see Contributors.md for a full list of Contributors
#  - see ContributionInstructions.md for information on how you can Contribute to this project
#  Stakeholder Specific Vulnerability Categorization (SSVC) is
#  licensed under a MIT (SEI)-style license, please see LICENSE.md distributed
#  with this Software or contact permission@sei.cmu.edu for full terms.
#  Created, in part, with funding and support from the United States Government
#  (see Acknowledgments file). This program may include and/or can make use of
#  certain third party source code, object code, documentation and other files
#  (“Third Party Software”). See LICENSE.md for more details.
#  Carnegie Mellon®, CERT® and CERT Coordination Center® are registered in the
#  U.S. Patent and Trademark Office by Carnegie Mellon University

from ssvc.decision_points import SsvcDecisionPointValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs

_AT_NONE = SsvcDecisionPointValue(
    name="None",
    key="N",
    description="The successful attack does not depend on the deployment and execution conditions of the vulnerable "
    "system. The attacker can expect to be able to reach the vulnerability and execute the exploit under all or "
    "most instances of the vulnerability.",
)


_PRESENT = SsvcDecisionPointValue(
    name="Present",
    key="P",
    description="The successful attack depends on the presence of specific deployment and execution conditions of "
    "the vulnerable system that enable the attack.",
)

ATTACK_REQUIREMENTS_1 = CvssDecisionPoint(
    name="Attack Requirements",
    key="AT",
    version="1.0.0",
    description="This metric captures the prerequisite deployment and execution conditions or variables of the "
    "vulnerable system that enable the attack.",
    values=(
        _AT_NONE,
        _PRESENT,
    ),
)

VERSIONS = (ATTACK_REQUIREMENTS_1,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
