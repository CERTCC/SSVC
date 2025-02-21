#!/usr/bin/env python
"""
Provides CVSS v4 Supplemental Metric for Safety
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

from ssvc.decision_points.base import SsvcDecisionPointValue
from ssvc.decision_points.cvss._not_defined import NOT_DEFINED_X
from ssvc.decision_points.cvss.base import CvssDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs

PRESENT = SsvcDecisionPointValue(
    name="Present",
    key="P",
    description="Consequences of the vulnerability meet definition of IEC 61508 consequence categories of "
    '"marginal," "critical," or "catastrophic."',
)
NEGLIGIBLE = SsvcDecisionPointValue(
    name="Negligible",
    key="N",
    description="Consequences of the vulnerability meet definition of IEC 61508 consequence category "
    '"negligible."',
)
SAFETY_1 = CvssDecisionPoint(
    name="Safety",
    description="The Safety decision point is a measure of the potential for harm to humans or the environment.",
    key="S",
    version="1.0.0",
    values=(
        NOT_DEFINED_X,
        PRESENT,
        NEGLIGIBLE,
    ),
)

VERSIONS = (SAFETY_1,)
LATEST = SAFETY_1


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
