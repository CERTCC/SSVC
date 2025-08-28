#!/usr/bin/env python
"""
Models the CVSS Availability Impact metric as an SSVC decision point.
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
    definition="There is total loss of availability, resulting in the attacker being able to fully deny access to "
    "resources in the impacted component; this loss is either sustained (while the attacker continues to "
    "deliver the attack) or persistent (the condition persists even after the attack has completed).",
)

_LOW = DecisionPointValue(
    name="Low",
    key="L",
    definition="There is reduced performance or interruptions in resource availability.",
)

_NONE_2 = DecisionPointValue(
    name="None",
    key="N",
    definition="There is no impact to the availability of the system.",
)

_COMPLETE = DecisionPointValue(
    name="Complete",
    key="C",
    definition="Total shutdown of the affected resource. The attacker can render the resource completely unavailable.",
)

_PARTIAL = DecisionPointValue(
    name="Partial",
    key="P",
    definition="Considerable lag in or interruptions in resource availability. For example, a network-based flood "
    "attack that reduces available bandwidth to a web server farm to such an extent that only a small "
    "number of connections successfully complete.",
)

_NONE_1 = DecisionPointValue(
    name="None", key="N", definition="No impact on availability."
)

AVAILABILITY_IMPACT_1 = CvssDecisionPoint(
    name="Availability Impact",
    definition="This metric measures the impact on availability a successful exploit of the vulnerability will have "
    "on the target system.",
    key="A",
    version="1.0.0",
    values=(
        _NONE_1,
        _PARTIAL,
        _COMPLETE,
    ),
)
"""
Defines None, Partial, and Complete values for CVSS Availability Impact.
"""

AVAILABILITY_IMPACT_2 = CvssDecisionPoint(
    name="Availability Impact",
    definition="This metric measures the impact to availability of a successfully exploited vulnerability.",
    key="A",
    version="2.0.0",
    values=(
        _NONE_2,
        _LOW,
        _HIGH,
    ),
)
"""
Updates None. Removes Partial and Complete. Adds Low and High values for CVSS Availability Impact.
"""

_HIGH_2 = DecisionPointValue(
    name="High",
    key="H",
    definition="There is total loss of availability, resulting in the attacker being able to fully deny access to "
    "resources in the impacted component; this loss is either sustained (while the attacker continues to "
    "deliver the attack) or persistent (the condition persists even after the attack has completed).",
)

_LOW_2 = DecisionPointValue(
    name="Low",
    key="L",
    definition="There is reduced performance or interruptions in resource availability. Even if repeated "
    "exploitation of the vulnerability is possible, the attacker does not have the ability to completely "
    "deny service to legitimate users. The resources in the Vulnerable System are either partially "
    "available all of the time, or fully available only some of the time, but overall there is no direct, "
    "serious consequence to the Vulnerable System.",
)

_NONE_3 = DecisionPointValue(
    name="None",
    key="N",
    definition="There is no impact to availability within the Vulnerable System.",
)


AVAILABILITY_IMPACT_3_0_0 = CvssDecisionPoint(
    name="Availability Impact to the Vulnerable System",
    definition="This metric measures the impact to the availability of the impacted system resulting from a "
    "successfully exploited vulnerability.",
    key="VA",
    version="3.0.0",
    values=(
        _NONE_3,
        _LOW_2,
        _HIGH_2,
    ),
)


VERSIONS = (
    AVAILABILITY_IMPACT_1,
    AVAILABILITY_IMPACT_2,
    AVAILABILITY_IMPACT_3_0_0,
)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
