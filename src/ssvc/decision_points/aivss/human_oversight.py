#!/usr/bin/env python
"""
Models the AIVSS Human Oversight decision point.
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

# Human Oversight
#
# 0.0: Human-in-the-loop system with well-defined roles and responsibilities, clear procedures for human-machine collaboration, and mechanisms for human oversight at various stages of the system's operation.
# 0.1-0.3: Clear mechanisms for human review and intervention in the system's decision-making process, with well-defined roles and responsibilities for human operators.
# 0.4-0.6: Limited human oversight, primarily reactive (e.g., users can report errors), no clear mechanisms for human intervention or override.
# 0.7-1.0: No human oversight or intervention in the AI system's decision-making process.
# Examples:
# 0.0: System is designed for human-machine collaboration, with humans playing a central role in the decision-making process.
# 0.2: System has mechanisms for human operators to review and override its decisions in specific cases.
# 0.5: Users can report errors, but there is no process for human intervention in the system's decisions.
# 0.8: System operates autonomously without any human control or monitoring.

HUMAN_IN_LOOP = DecisionPointValue(
    name="Human-in-the-Loop",
    key="H",
    description="Human-in-the-loop system with well-defined roles and responsibilities, clear procedures for human-machine collaboration, and mechanisms for human oversight at various stages of the system's operation.",
)

CLEAR_MECHANISMS = DecisionPointValue(
    name="Clear Mechanisms",
    key="C",
    description="Clear mechanisms for human review and intervention in the system's decision-making process, with well-defined roles and responsibilities for human operators.",
)

LIMITED_OVERSIGHT = DecisionPointValue(
    name="Limited Oversight",
    key="L",
    description="Limited human oversight, primarily reactive (e.g., users can report errors), no clear mechanisms for human intervention or override.",
)

NONE = DecisionPointValue(
    name="None",
    key="N",
    description="No human oversight or intervention in the AI system's decision-making process.",
)

HUMAN_OVERSIGHT = AivssDecisionPoint(
    name="Human Oversight",
    key="HO",
    version="1.0.0",
    description="Degree to which human oversight and intervention are incorporated into the AI system's operation.",
    values=(HUMAN_IN_LOOP, CLEAR_MECHANISMS, LIMITED_OVERSIGHT, NONE),
)

VERSIONS = [HUMAN_OVERSIGHT]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
