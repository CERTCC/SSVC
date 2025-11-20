#!/usr/bin/env python
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
"""
Provides the Agentic Impact Level Decision Point for SSVC.
"""

from ssvc.decision_points.aivss.base import AivssDecisionPoint
from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_points.helpers import print_versions_and_diffs

COPILOT = DecisionPointValue(
    key="C",
    name="CoPilot",
    definition="The agent is primarily a copilot or assistant. "
    "Its actions are heavily constrained, requiring human oversight. "
    "The agent explicitly does not have rights to execute code.",
)

SPECIALIST = DecisionPointValue(
    key="S",
    name="Specialist",
    definition="The agent is a specialist with significant autonomy within a defined domain."
        "It can use powerful tools and may learn from interactions.",
)

PRIME_MOVER = DecisionPointValue(
    key="P",
    name="Prime Mover",
    definition="The agent is a prime mover with broad autonomy. "
    "It can orchestrate other systems, modify its own logic, and interact with critical infrastructure."
)

AIL_01 = AivssDecisionPoint(
    key="AIL",
    name="Agentic Impact Level",
    definition="Determines the agentic impact level of a vulnerability based on its characteristics and potential effects.",
    version="1.0.0",
    values=(COPILOT, SPECIALIST, PRIME_MOVER),
)


VERSIONS = (AIL_01, )
LATEST = VERSIONS[-1]

if __name__ == "__main__":
    for version in VERSIONS:
        print_versions_and_diffs(VERSIONS)
