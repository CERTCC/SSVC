#!/usr/bin/env python
"""
Provides a decision point for the [CVSS Qualitative Severity Rating Scale](https://www.first.org/cvss/v4.0/specification-document#Qualitative-Severity-Rating-Scale).
"""
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

from ssvc.decision_points import SsvcDecisionPointValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs

QS_NONE = SsvcDecisionPointValue(
    name="None",
    key="N",
    description="No severity rating (0.0)",
)

LOW = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="Low (0.1 - 3.9)",
)
MEDIUM = SsvcDecisionPointValue(
    name="Medium",
    key="M",
    description="Medium (4.0 - 6.9)",
)
HIGH = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="High (7.0 - 8.9)",
)
CRITICAL = SsvcDecisionPointValue(
    name="Critical",
    key="C",
    description="Critical (9.0 - 10.0)",
)

QUALITATIVE_SEVERITY = CvssDecisionPoint(
    name="CVSS Qualitative Severity Rating Scale",
    key="QS",
    description="The CVSS Qualitative Severity Rating Scale provides "
    "a categorical representation of a CVSS Score.",
    version="1.0.0",
    values=(
        QS_NONE,
        LOW,
        MEDIUM,
        HIGH,
        CRITICAL,
    ),
)

VERSIONS = (QUALITATIVE_SEVERITY,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
