#!/usr/bin/env python
"""
Models the CVSS Integrity Requirement metric as an SSVC decision point.
"""

#  Copyright (c) 2023 Carnegie Mellon University and Contributors.
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
from ssvc.decision_points.cvss.base import CvssDecisionPoint
from ssvc.decision_points.helpers import show_diffs

_NOT_DEFINED = SsvcDecisionPointValue(
    name="Not Defined",
    key="X",
    description="Assigning this value to the metric will not influence the score. It is a signal to the equation to "
    "skip this metric.",
)

_HIGH = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="Loss of integrity is likely to have a catastrophic adverse effect on the organization or individuals "
    "associated with the organization (e.g., employees, customers).",
)

_MEDIUM = SsvcDecisionPointValue(
    name="Medium",
    key="M",
    description="Loss of integrity is likely to have a serious adverse effect on the organization or individuals "
    "associated with the organization (e.g., employees, customers).",
)

_LOW = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="Loss of integrity is likely to have only a limited adverse effect on the organization or individuals "
    "associated with the organization (e.g., employees, customers).",
)

INTEGRITY_REQUIREMENT_1 = CvssDecisionPoint(
    name="Integrity Requirement",
    description="This metric measures the impact to the integrity of a successfully exploited vulnerability.",
    key="CR",
    version="1.0.0",
    values=(
        _LOW,
        _MEDIUM,
        _HIGH,
        _NOT_DEFINED,
    ),
)
"""
Defines Low, Medium, High, and Not Defined values for CVSS Integrity Requirement.
"""

_NOT_DEFINED_2 = SsvcDecisionPointValue(
    name="Not Defined",
    key="X",
    description="Assigning this value indicates there is insufficient information to choose one of the other values. "
    "This has the same effect as assigning High as the worst case.",
)

_HIGH_2 = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="Loss of integrity is likely to have a catastrophic adverse effect on the organization or "
    "individuals associated with the organization (e.g., employees, customers).",
)

_MEDIUM_2 = SsvcDecisionPointValue(
    name="Medium",
    key="M",
    description="Loss of integrity is likely to have a serious adverse effect on the organization or "
    "individuals associated with the organization (e.g., employees, customers).",
)

_LOW_2 = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="Loss of integrity is likely to have only a limited adverse effect on the organization or "
    "individuals associated with the organization (e.g., employees, customers).",
)

INTEGRITY_REQUIREMENT_1_0_1 = CvssDecisionPoint(
    name="Integrity Requirement",
    description="This metric enables the consumer to customize the assessment depending on the importance of the "
    "affected IT asset to the analyst’s organization, measured in terms of Confidentiality.",
    key="CR",
    version="1.0.1",
    values=(
        _LOW_2,
        _MEDIUM_2,
        _HIGH_2,
        _NOT_DEFINED_2,
    ),
)


def main():
    versions = (INTEGRITY_REQUIREMENT_1, INTEGRITY_REQUIREMENT_1_0_1)

    for version in versions:
        print(version.to_json(indent=2))

    show_diffs(versions)


if __name__ == "__main__":
    main()
