#!/usr/bin/env python
"""
CVSS Subsequent system availability impact decision point.
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

_SA_HIGH = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="There is a total loss of availability, resulting in the attacker being able to fully deny access to "
    "resources in the Subsequent System; this loss is either sustained (while the attacker continues to "
    "deliver the attack) or persistent (the condition persists even after the attack has completed).",
)

_SA_LOW = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="Performance is reduced or there are interruptions in resource availability. Even if repeated "
    "exploitation of the vulnerability is possible, the attacker does not have the ability to completely "
    "deny service to legitimate users.",
)

_SA_NONE = SsvcDecisionPointValue(
    name="None",
    key="N",
    description="There is no impact to availability within the Subsequent System or all availability impact is "
    "constrained to the Vulnerable System.",
)


SUBSEQUENT_AVAILABILITY_IMPACT_1 = CvssDecisionPoint(
    name="Availability Impact to the Subsequent System",
    description="This metric measures the impact on availability a successful exploit of the vulnerability will have "
    "on the Subsequent System.",
    key="SA",
    version="1.0.0",
    values=(
        _SA_NONE,
        _SA_LOW,
        _SA_HIGH,
    ),
)

VERSIONS = (SUBSEQUENT_AVAILABILITY_IMPACT_1,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
