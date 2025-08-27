#!/usr/bin/env python
"""
CVSS Subsequent system availability impact decision point.
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

_SA_HIGH = DecisionPointValue(
    name="High",
    key="H",
    definition="There is a total loss of availability, resulting in the attacker being able to fully deny access to "
    "resources in the Subsequent System; this loss is either sustained (while the attacker continues to "
    "deliver the attack) or persistent (the condition persists even after the attack has completed).",
)

_SA_LOW = DecisionPointValue(
    name="Low",
    key="L",
    definition="Performance is reduced or there are interruptions in resource availability. Even if repeated "
    "exploitation of the vulnerability is possible, the attacker does not have the ability to completely "
    "deny service to legitimate users.",
)

_SA_NONE = DecisionPointValue(
    name="None",
    key="N",
    definition="There is no impact to availability within the Subsequent System or all availability impact is "
    "constrained to the Vulnerable System.",
)


SUBSEQUENT_AVAILABILITY_IMPACT_1 = CvssDecisionPoint(
    name="Availability Impact to the Subsequent System",
    definition="This metric measures the impact on availability a successful exploit of the vulnerability will have "
    "on the Subsequent System.",
    key="SA",
    version="1.0.0",
    values=(
        _SA_NONE,
        _SA_LOW,
        _SA_HIGH,
    ),
)

VERSIONS = (SUBSEQUENT_AVAILABILITY_IMPACT_1,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
