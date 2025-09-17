#!/usr/bin/env python
"""
Models the CVSS Confidentiality Impact metric as an SSVC decision point.
"""
#  Copyright (c) 2023-2025 Carnegie Mellon University.
#  NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE
#  ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS.
#  CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND,
#  EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT
#  NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR
#  MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE
#  OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE
#  ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM
#  PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
#  Licensed under a MIT (SEI)-style license, please see LICENSE or contact
#  permission@sei.cmu.edu for full terms.
#  [DISTRIBUTION STATEMENT A] This material has been approved for
#  public release and unlimited distribution. Please see Copyright notice
#  for non-US Government use and distribution.
#  This Software includes and/or makes use of Third-Party Software each
#  subject to its own license.
#  DM24-0278

from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs

_HIGH = DecisionPointValue(
    name="High",
    key="H",
    definition="There is total loss of confidentiality, resulting in all resources within the impacted component "
    "being divulged to the attacker. Alternatively, access to only some restricted information is "
    "obtained, but the disclosed information presents a direct, serious impact. For example, an attacker "
    "steals the administrator's password, or private encryption keys of a web server.",
)

_LOW = DecisionPointValue(
    name="Low",
    key="L",
    definition="There is some loss of confidentiality. Access to some restricted information is obtained, "
    "but the attacker does not have control over what information is obtained, or the amount or kind of "
    "loss is constrained. The information disclosure does not cause a direct, serious loss to the "
    "impacted component.",
)

_CI_NONE_2 = DecisionPointValue(
    name="None",
    key="N",
    definition="There is no loss of confidentiality within the impacted component.",
)

_COMPLETE = DecisionPointValue(
    name="Complete",
    key="C",
    definition="A total compromise of critical system information. A complete loss of system protection resulting in "
    "all critical system files being revealed. The attacker has sovereign control to read all of the "
    "system's data (memory, files, etc).",
)

_PARTIAL = DecisionPointValue(
    name="Partial",
    key="P",
    definition="There is considerable informational disclosure. Access to critical system files is possible. There "
    "is a loss of important information, but the attacker doesn't have control over what is obtainable or "
    "the scope of the loss is constrained.",
)

_CI_NONE = DecisionPointValue(
    name="None",
    key="N",
    definition="No impact on confidentiality.",
)

CONFIDENTIALITY_IMPACT_1 = CvssDecisionPoint(
    name="Confidentiality Impact",
    definition="This metric measures the impact on confidentiality of a successful exploit of the vulnerability on "
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
    definition="This metric measures the impact to the confidentiality of the information resources managed by a "
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


_HIGH_1 = DecisionPointValue(
    name="High",
    key="H",
    definition="There is total loss of confidentiality, resulting in all resources within the impacted component "
    "being divulged to the attacker. Alternatively, access to only some restricted information is "
    "obtained, but the disclosed information presents a direct, serious impact. For example, an attacker "
    "steals the administrator's password, or private encryption keys of a web server.",
)

_LOW_1 = DecisionPointValue(
    name="Low",
    key="L",
    definition="There is some loss of confidentiality. Access to some restricted information is obtained, "
    "but the attacker does not have control over what information is obtained, or the amount or kind of "
    "loss is constrained. The information disclosure does not cause a direct, serious loss to the "
    "impacted component.",
)

_CI_NONE_3 = DecisionPointValue(
    name="None",
    key="N",
    definition="There is no loss of confidentiality within the impacted component.",
)

CONFIDENTIALITY_IMPACT_3_0_0 = CvssDecisionPoint(
    name="Confidentiality Impact to the Vulnerable System",
    definition="This metric measures the impact to the confidentiality of the information managed by the system due "
    "to a successfully exploited vulnerability. Confidentiality refers to limiting information access "
    "and disclosure to only authorized users, as well as preventing access by, or disclosure to, "
    "unauthorized ones.",
    key="VC",
    version="3.0.0",
    values=(
        _CI_NONE_3,
        _LOW_1,
        _HIGH_1,
    ),
)


VERSIONS = (
    CONFIDENTIALITY_IMPACT_1,
    CONFIDENTIALITY_IMPACT_2,
    CONFIDENTIALITY_IMPACT_3_0_0,
)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
