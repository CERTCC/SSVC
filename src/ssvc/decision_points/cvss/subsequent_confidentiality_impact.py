#!/usr/bin/env python
"""
CVSS Subsequent System Confidentiality Impact
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

NEGLIGIBLE = DecisionPointValue(
    name="Negligible",
    key="N",
    definition="There is no loss of confidentiality within the Subsequent System or all confidentiality impact is "
    "constrained to the Vulnerable System.",
)

LOW = DecisionPointValue(
    name="Low",
    key="L",
    definition="There is some loss of confidentiality. Access to some restricted information is obtained, but the "
    "attacker does not have control over what information is obtained, or the amount or kind of loss is "
    "limited. The information disclosure does not cause a direct, serious loss to the Subsequent System.",
)

HIGH = DecisionPointValue(
    name="High",
    key="H",
    definition="There is a total loss of confidentiality, resulting in all resources within the Subsequent System "
    "being divulged to the attacker. Alternatively, access to only some restricted information is obtained, "
    "but the disclosed information presents a direct, serious impact.",
)

SUBSEQUENT_CONFIDENTIALITY_IMPACT_1 = CvssDecisionPoint(
    name="Confidentiality Impact to the Subsequent System",
    key="SC",
    definition="This metric measures the impact to the confidentiality of the information managed by the system due "
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

VERSIONS = (SUBSEQUENT_CONFIDENTIALITY_IMPACT_1,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
