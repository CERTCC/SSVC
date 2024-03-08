#!/usr/bin/env python
"""
Models the CVSS Integrity Impact metric as an SSVC decision point.
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

_II_HIGH = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="There is a total loss of integrity, or a complete loss of protection.",
)

_II_LOW = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="Modification of data is possible, but the attacker does not have control over the consequence of a "
    "modification, or the amount of modification is constrained. The data modification does not have a "
    "direct, serious impact on the impacted component.",
)

_II_NONE_2 = SsvcDecisionPointValue(
    name="None",
    key="N",
    description="There is no impact to the integrity of the system.",
)
_COMPLETE = SsvcDecisionPointValue(
    name="Complete",
    key="C",
    description="A total compromise of system integrity. There is a complete loss of system protection resulting in "
    "the entire system being compromised. The attacker has sovereign control to modify any system files.",
)

_PARTIAL = SsvcDecisionPointValue(
    name="Partial",
    key="P",
    description="Considerable breach in integrity. Modification of critical system files or information is possible, "
    "but the attacker does not have control over what can be modified, or the scope of what the attacker "
    "can affect is constrained. For example, key system or program files may be overwritten or modified, "
    "but at random or in a limited context or scope.",
)

_II_NONE = SsvcDecisionPointValue(
    name="None", key="N", description="No impact on integrity."
)

INTEGRITY_IMPACT_1 = CvssDecisionPoint(
    name="Integrity Impact",
    description="This metric measures the impact on integrity a successful exploit of the vulnerability will have on "
    "the target system.",
    key="I",
    version="1.0.0",
    values=(
        _II_NONE,
        _PARTIAL,
        _COMPLETE,
    ),
)
"""
Defines None, Partial, and Complete values for CVSS Integrity Impact.
"""

INTEGRITY_IMPACT_2 = CvssDecisionPoint(
    name="Integrity Impact",
    description="This metric measures the impact to integrity of a successfully exploited vulnerability.",
    key="I",
    version="2.0.0",
    values=(
        _II_NONE_2,
        _II_LOW,
        _II_HIGH,
    ),
)
"""
Updates None. Removes Partial and Complete. Adds Low and High values for CVSS Integrity Impact.
"""

_II_HIGH_2 = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="There is a total loss of integrity, or a complete loss of protection.",
)

_II_LOW_2 = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="Modification of data is possible, but the attacker does not have control over the consequence of a "
    "modification, or the amount of modification is limited. The data modification does not have a direct, "
    "serious impact to the Vulnerable System.",
)


_II_NONE_3 = SsvcDecisionPointValue(
    name="None",
    key="N",
    description="There is no loss of integrity within the Vulnerable System.",
)


INTEGRITY_IMPACT_2_0_1 = CvssDecisionPoint(
    name="Integrity Impact",
    description="This metric measures the impact to integrity of a successfully exploited vulnerability.",
    key="I",
    version="2.0.1",
    values=(
        _II_NONE_3,
        _II_LOW_2,
        _II_HIGH_2,
    ),
)

versions = [INTEGRITY_IMPACT_1, INTEGRITY_IMPACT_2, INTEGRITY_IMPACT_2_0_1]


def main():
    print_versions_and_diffs(versions)


if __name__ == "__main__":
    main()
