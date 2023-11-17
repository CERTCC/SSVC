#!/usr/bin/env python
"""
CVSS Subsequent System Confidentiality Impact
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
from ssvc.decision_points.helpers import print_versions_and_diffs

NEGLIGIBLE = SsvcDecisionPointValue(
    name="Negligible",
    key="N",
    description="There is no loss of confidentiality within the Subsequent System or all confidentiality impact is "
    "constrained to the Vulnerable System.",
)

LOW = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="There is some loss of confidentiality. Access to some restricted information is obtained, but the "
    "attacker does not have control over what information is obtained, or the amount or kind of loss is "
    "limited. The information disclosure does not cause a direct, serious loss to the Subsequent System.",
)

HIGH = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="There is a total loss of confidentiality, resulting in all resources within the Subsequent System "
    "being divulged to the attacker. Alternatively, access to only some restricted information is obtained, "
    "but the disclosed information presents a direct, serious impact.",
)

SUBSEQUENT_CONFIDENTIALITY_IMPACT_1 = CvssDecisionPoint(
    name="Confidentiality Impact to the Subsequent System",
    key="SC",
    description="This metric measures the impact to the confidentiality of the information managed by the system due "
    "to a successfully exploited vulnerability. Confidentiality refers to limiting information access and "
    "disclosure to only authorized users, as well as preventing access by, or disclosure to, unauthorized "
    "ones. The resulting score is greatest when the loss to the system is highest.",
    version="1.0.0",
    values=(
        NEGLIGIBLE,
        LOW,
        HIGH,
    ),
)

versions = [
    SUBSEQUENT_CONFIDENTIALITY_IMPACT_1,
]


def main():
    print_versions_and_diffs(versions)


if __name__ == "__main__":
    main()
