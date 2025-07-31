#!/usr/bin/env python
"""
Models the AIVSS Safety-Critical decision point.
"""

#  Copyright (c) 2025 Carnegie Mellon University.
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

from ssvc.decision_points.aivss.base import AivssDecisionPoint
from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_points.helpers import print_versions_and_diffs

# Safety-Critical
#
# 0.0: System formally verified to meet safety-critical standards (e.g., ISO 26262 for automotive, IEC 62304 for medical devices).
# 0.1-0.3: Rigorous safety testing performed, including edge cases and failure scenarios, with failsafe mechanisms and human oversight.
# 0.4-0.6: Basic safety measures in place (e.g., some redundancy), but no rigorous safety testing or formal verification.
# 0.7-1.0: System used in safety-critical applications (e.g., autonomous driving, medical diagnosis) without proper safety considerations or failsafe mechanisms.
# Examples:
# 0.0: System is certified to meet relevant safety standards for its application domain.
# 0.2: System undergoes rigorous safety testing and has multiple failsafe mechanisms in place.
# 0.5: System has some backup systems, but they have not been thoroughly tested.
# 0.9: System used to control a critical function without any redundancy or failsafe mechanisms.

FORMALLY_VERIFIED = DecisionPointValue(
    name="Formally Verified",
    key="F",
    description="System formally verified to meet safety-critical standards (e.g., ISO 26262, IEC 62304).",
)

RIGOROUS_TESTING = DecisionPointValue(
    name="Rigorous Testing",
    key="R",
    description="Rigorous safety testing performed, including edge cases and failure scenarios, with failsafe mechanisms and human oversight.",
)

BASIC_MEASURES = DecisionPointValue(
    name="Basic Measures",
    key="B",
    description="Basic safety measures in place, but no rigorous safety testing or formal verification.",
)

NO_CONSIDERATION = DecisionPointValue(
    name="No Consideration",
    key="N",
    description="System used in safety-critical applications without proper safety considerations or failsafe mechanisms.",
)

SAFETY_CRITICAL = AivssDecisionPoint(
    name="Safety-Critical",
    key="SC",
    version="1.0.0",
    description="Degree to which the system meets safety-critical standards and incorporates safety mechanisms.",
    values=(FORMALLY_VERIFIED, RIGOROUS_TESTING, BASIC_MEASURES, NO_CONSIDERATION),
)

VERSIONS = [SAFETY_CRITICAL]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
