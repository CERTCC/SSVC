#!/usr/bin/env python
"""
Models the CVSS Confidentiality Impact metric as an SSVC decision point.
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

_HIGH = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="There is total loss of confidentiality, resulting in all resources within the impacted component "
    "being divulged to the attacker. Alternatively, access to only some restricted information is "
    "obtained, but the disclosed information presents a direct, serious impact. For example, an attacker "
    "steals the administrator's password, or private encryption keys of a web server.",
)

_LOW = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="There is some loss of confidentiality. Access to some restricted information is obtained, "
    "but the attacker does not have control over what information is obtained, or the amount or kind of "
    "loss is constrained. The information disclosure does not cause a direct, serious loss to the "
    "impacted component.",
)

_CI_NONE_2 = SsvcDecisionPointValue(
    name="None",
    key="N",
    description="There is no loss of confidentiality within the impacted component.",
)

_COMPLETE = SsvcDecisionPointValue(
    name="Complete",
    key="C",
    description="A total compromise of critical system information. A complete loss of system protection resulting in "
    "all critical system files being revealed. The attacker has sovereign control to read all of the "
    "system's data (memory, files, etc).",
)

_PARTIAL = SsvcDecisionPointValue(
    name="Partial",
    key="P",
    description="There is considerable informational disclosure. Access to critical system files is possible. There "
    "is a loss of important information, but the attacker doesn't have control over what is obtainable or "
    "the scope of the loss is constrained.",
)

_CI_NONE = SsvcDecisionPointValue(
    name="None",
    key="N",
    description="No impact on confidentiality.",
)

CONFIDENTIALITY_IMPACT_1 = CvssDecisionPoint(
    name="Confidentiality Impact",
    description="This metric measures the impact on confidentiality of a successful exploit of the vulnerability on "
    "the target system.",
    key="C",
    version="1.0.0",
    values=(
        _CI_NONE,
        _PARTIAL,
        _COMPLETE,
    ),
)
"""
Defines None, Partial, and Complete values for CVSS Confidentiality Impact.
"""

CONFIDENTIALITY_IMPACT_2 = CvssDecisionPoint(
    name="Confidentiality Impact",
    description="This metric measures the impact to the confidentiality of the information resources managed by a "
    "software component due to a successfully exploited vulnerability.",
    key="C",
    version="2.0.0",
    values=(
        _CI_NONE_2,
        _LOW,
        _HIGH,
    ),
)
"""
Updates None. Removes Partial and Complete. Adds Low and High values for CVSS Confidentiality Impact.
"""


_HIGH_1 = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="There is total loss of confidentiality, resulting in all resources within the impacted component "
    "being divulged to the attacker. Alternatively, access to only some restricted information is "
    "obtained, but the disclosed information presents a direct, serious impact. For example, an attacker "
    "steals the administrator's password, or private encryption keys of a web server.",
)

_LOW_1 = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="There is some loss of confidentiality. Access to some restricted information is obtained, "
    "but the attacker does not have control over what information is obtained, or the amount or kind of "
    "loss is constrained. The information disclosure does not cause a direct, serious loss to the "
    "impacted component.",
)

_CI_NONE_3 = SsvcDecisionPointValue(
    name="None",
    key="N",
    description="There is no loss of confidentiality within the impacted component.",
)

CONFIDENTIALITY_IMPACT_2_0_1 = CvssDecisionPoint(
    name="Confidentiality Impact",
    description="This metric measures the impact to the confidentiality of the information managed by the system due "
    "to a successfully exploited vulnerability. Confidentiality refers to limiting information access "
    "and disclosure to only authorized users, as well as preventing access by, or disclosure to, "
    "unauthorized ones.",
    key="C",
    version="2.0.1",
    values=(
        _CI_NONE_3,
        _LOW_1,
        _HIGH_1,
    ),
)


VERSIONS = (
    CONFIDENTIALITY_IMPACT_1,
    CONFIDENTIALITY_IMPACT_2,
    CONFIDENTIALITY_IMPACT_2_0_1,
)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
