#!/usr/bin/env python
"""
Model the CVSS Impact Bias as an SSVC decision point.
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
from ssvc.decision_points.cvss.base import CvssDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs

_AVAILABILITY = SsvcDecisionPointValue(
    name="Availability",
    key="A",
    description="Availability Impact is assigned greater weight than Confidentiality Impact or Integrity Impact.",
)

_INTEGRITY = SsvcDecisionPointValue(
    name="Integrity",
    key="I",
    description="Integrity Impact is assigned greater weight than Confidentiality Impact or Availability Impact.",
)

_CONFIDENTIALITY = SsvcDecisionPointValue(
    name="Confidentiality",
    key="C",
    description="Confidentiality impact is assigned greater weight than Integrity Impact or Availability Impact.",
)

_NORMAL = SsvcDecisionPointValue(
    name="Normal",
    key="N",
    description="Confidentiality Impact, Integrity Impact, and Availability Impact are all assigned the same weight.",
)

IMPACT_BIAS_1 = CvssDecisionPoint(
    name="Impact Bias",
    description="This metric measures the impact bias of the vulnerability.",
    key="IB",
    version="1.0.0",
    values=(
        _NORMAL,
        _CONFIDENTIALITY,
        _INTEGRITY,
        _AVAILABILITY,
    ),
)
"""
Defines Normal, Confidentiality, Integrity, and Availability values for CVSS Impact Bias.
"""

versions = [
    IMPACT_BIAS_1,
]


def main():
    print_versions_and_diffs(versions)


if __name__ == "__main__":
    main()
