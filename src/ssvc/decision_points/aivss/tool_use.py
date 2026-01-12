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
Provides the AIVSS Tool Use Decision Point for SSVC.
"""
from ssvc.decision_points.aivss.base import AivssDecisionPoint
from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_points.helpers import print_versions_and_diffs

VIEWER = DecisionPointValue(
    key="V",
    name="Viewer",
    definition="The agent can only read and analyze information without making any changes.",
)
OPERATOR = DecisionPointValue(
    key="O",
    name="Operator",
    definition="The agent can make changes within a controlled environment, such as test systems or local files.",
)
ADMINISTRATOR = DecisionPointValue(
    key="A",
    name="Administrator",
    definition="The agent has full control and can make changes to privileged systems, including production environments.",
)

TOOL_USE = AivssDecisionPoint(
    key="TU",
    name="Tool Use",
    definition="Determines the tool use level of an AI agent based on its capabilities to interact with systems.",
    version="1.0.0",
    values=(VIEWER, OPERATOR, ADMINISTRATOR),
)

VERSIONS = (TOOL_USE,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
