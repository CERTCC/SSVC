#!/usr/bin/env python
"""
Models the CVSS Availability Impact metric as an SSVC decision point.
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
    description="There is total loss of availability, resulting in the attacker being able to fully deny access to "
    "resources in the impacted component; this loss is either sustained (while the attacker continues to "
    "deliver the attack) or persistent (the condition persists even after the attack has completed).",
)

_LOW = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="There is reduced performance or interruptions in resource availability.",
)

_NONE_2 = SsvcDecisionPointValue(
    name="None",
    key="N",
    description="There is no impact to the availability of the system.",
)

_COMPLETE = SsvcDecisionPointValue(
    name="Complete",
    key="C",
    description="Total shutdown of the affected resource. The attacker can render the resource completely unavailable.",
)

_PARTIAL = SsvcDecisionPointValue(
    name="Partial",
    key="P",
    description="Considerable lag in or interruptions in resource availability. For example, a network-based flood "
    "attack that reduces available bandwidth to a web server farm to such an extent that only a small "
    "number of connections successfully complete.",
)

_NONE_1 = SsvcDecisionPointValue(
    name="None", key="N", description="No impact on availability."
)

AVAILABILITY_IMPACT_1 = CvssDecisionPoint(
    name="Availability Impact",
    description="This metric measures the impact on availability a successful exploit of the vulnerability will have "
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
    description="This metric measures the impact to availability of a successfully exploited vulnerability.",
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

_HIGH_2 = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="There is total loss of availability, resulting in the attacker being able to fully deny access to "
    "resources in the impacted component; this loss is either sustained (while the attacker continues to "
    "deliver the attack) or persistent (the condition persists even after the attack has completed).",
)

_LOW_2 = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="There is reduced performance or interruptions in resource availability. Even if repeated "
    "exploitation of the vulnerability is possible, the attacker does not have the ability to completely "
    "deny service to legitimate users. The resources in the Vulnerable System are either partially "
    "available all of the time, or fully available only some of the time, but overall there is no direct, "
    "serious consequence to the Vulnerable System.",
)

_NONE_3 = SsvcDecisionPointValue(
    name="None",
    key="N",
    description="There is no impact to availability within the Vulnerable System.",
)


AVAILABILITY_IMPACT_3_0_0 = CvssDecisionPoint(
    name="Availability Impact to the Vulnerable System",
    description="This metric measures the impact to the availability of the impacted system resulting from a "
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
