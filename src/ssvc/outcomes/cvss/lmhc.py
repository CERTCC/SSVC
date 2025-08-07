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
from ssvc.decision_points.cvss.base import CvssDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs

_NONE = DecisionPointValue(name="None", key="N", description="None (0.0)")

_LOW = DecisionPointValue(name="Low", key="L", description="Low (0.1-3.9)")

_MEDIUM = DecisionPointValue(name="Medium", key="M", description="Medium (4.0-6.9)")

_HIGH = DecisionPointValue(name="High", key="H", description="High (7.0-8.9)")

_CRITICAL = DecisionPointValue(
    name="Critical", key="C", description="Critical (9.0-10.0)"
)

LMHC = CvssDecisionPoint(
    name="CVSS Qualitative Severity Rating Scale",
    key="CVSS",
    description="The CVSS Qualitative Severity Rating Scale group.",
    version="1.0.0",
    values=(
        _NONE,
        _LOW,
        _MEDIUM,
        _HIGH,
        _CRITICAL,
    ),
)
"""
The CVSS Qualitative Severity (N,L,M,H,C) Rating Scale outcome group.
"""

VERSIONS = (LMHC,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
