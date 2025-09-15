#!/usr/bin/env python
"""
Models the CVSS Integrity Impact metric as an SSVC decision point.
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

_II_HIGH = DecisionPointValue(
    name="High",
    key="H",
    definition="There is a total loss of integrity, or a complete loss of protection.",
)

_II_LOW = DecisionPointValue(
    name="Low",
    key="L",
    definition="Modification of data is possible, but the attacker does not have control over the consequence of a "
    "modification, or the amount of modification is constrained. The data modification does not have a "
    "direct, serious impact on the impacted component.",
)

_II_NONE_2 = DecisionPointValue(
    name="None",
    key="N",
    definition="There is no impact to the integrity of the system.",
)
_COMPLETE = DecisionPointValue(
    name="Complete",
    key="C",
    definition="A total compromise of system integrity. There is a complete loss of system protection resulting in "
    "the entire system being compromised. The attacker has sovereign control to modify any system files.",
)

_PARTIAL = DecisionPointValue(
    name="Partial",
    key="P",
    definition="Considerable breach in integrity. Modification of critical system files or information is possible, "
    "but the attacker does not have control over what can be modified, or the scope of what the attacker "
    "can affect is constrained. For example, key system or program files may be overwritten or modified, "
    "but at random or in a limited context or scope.",
)

_II_NONE = DecisionPointValue(
    name="None", key="N", definition="No impact on integrity."
)

INTEGRITY_IMPACT_1 = CvssDecisionPoint(
    name="Integrity Impact",
    definition="This metric measures the impact on integrity a successful exploit of the vulnerability will have on "
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
    definition="This metric measures the impact to integrity of a successfully exploited vulnerability.",
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

_II_HIGH_2 = DecisionPointValue(
    name="High",
    key="H",
    definition="There is a total loss of integrity, or a complete loss of protection.",
)

_II_LOW_2 = DecisionPointValue(
    name="Low",
    key="L",
    definition="Modification of data is possible, but the attacker does not have control over the consequence of a "
    "modification, or the amount of modification is limited. The data modification does not have a direct, "
    "serious impact to the Vulnerable System.",
)


_II_NONE_3 = DecisionPointValue(
    name="None",
    key="N",
    definition="There is no loss of integrity within the Vulnerable System.",
)


INTEGRITY_IMPACT_3_0_0 = CvssDecisionPoint(
    name="Integrity Impact to the Vulnerable System",
    definition="This metric measures the impact to integrity of a successfully exploited vulnerability.",
    key="VI",
    version="3.0.0",
    values=(
        _II_NONE_3,
        _II_LOW_2,
        _II_HIGH_2,
    ),
)


VERSIONS = (INTEGRITY_IMPACT_1, INTEGRITY_IMPACT_2, INTEGRITY_IMPACT_3_0_0)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
