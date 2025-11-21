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

'''
Provides TODO writeme
'''
from ssvc.decision_points.aivss.base import AivssDecisionPoint
from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_points.helpers import print_versions_and_diffs

# Execution Power
# Categories : Constrained, Capable, High Leverage

CONSTRAINED = DecisionPointValue(
    key="C",
    name="Constrained",
    definition="The AI agent has limited execution power, restricting its ability to perform actions autonomously or interact with external systems.",
)

CAPABLE = DecisionPointValue(
    key="CA",
    name="Capable",
    definition="The AI agent has moderate execution power, allowing it to perform certain actions autonomously and interact with external systems under supervision.",
)

HIGH_LEVERAGE = DecisionPointValue(
    key="H",
    name="High Leverage",
    definition="The AI agent has extensive execution power, enabling it to perform actions autonomously and interact with external systems with minimal supervision.",
)

EXECUTION_POWER = AivssDecisionPoint(
    key="EP",
    name="Execution Power",
    definition="Determines the level of execution power granted to an AI agent, influencing its ability to perform actions autonomously and interact with external systems.",
    version="1.0.0",
    values=(CONSTRAINED, CAPABLE, HIGH_LEVERAGE),
)

VERSIONS = (EXECUTION_POWER,)
LATEST = VERSIONS[-1]

def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == '__main__':
    main()
