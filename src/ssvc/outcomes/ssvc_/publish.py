#!/usr/bin/env python

#  Copyright (c) 2025 Carnegie Mellon University and Contributors.
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

from ssvc.decision_points.base import DecisionPointValue as DecisionPointValue
from ssvc.decision_points.helpers import print_versions_and_diffs
from ssvc.decision_points.ssvc_.base import SsvcDecisionPoint

_DO_NOT_PUBLISH = DecisionPointValue(
    name="Do Not Publish", key="N", description="Do Not Publish"
)

_PUBLISH = DecisionPointValue(name="Publish", key="P", description="Publish")

PUBLISH = SsvcDecisionPoint(
    name="Publish, Do Not Publish",
    key="PUBLISH",
    description="The publish outcome group.",
    version="1.0.0",
    values=(
        _DO_NOT_PUBLISH,
        _PUBLISH,
    ),
)
"""
The publish outcome group.
"""

VERSIONS = (PUBLISH,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
