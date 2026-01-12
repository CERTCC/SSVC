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
Provides TODO writeme
"""
from ssvc.decision_points.aivss.base import AivssDecisionPoint
from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_points.helpers import print_versions_and_diffs

# ## 4\. Goal-Driven Planning
#
# Unlike self-mod, planning truly has *three distinct qualitative regimes*, and you should keep all three.
#
# ### Planning Levels
#
# - **Reactive** — single-step, no planning horizon.
# - **Assisted** — multi-step planning, human executes or approves.
# - **Autonomous** — multi-step planning and execution by the system itself.
#
# **Why 3?** People behave meaningfully differently when an AI can only react vs. can plan vs. can plan-and-execute. These are policy-relevant distinctions.
REACTIVE = DecisionPointValue(
    key="R",
    name="Reactive",
    definition="The agent can only respond to immediate inputs without planning.",
)
ASSISTED = DecisionPointValue(
    key="A",
    name="Assisted",
    definition="The agent can plan multiple steps ahead but requires human execution or approval.",
)
AUTONOMOUS = DecisionPointValue(
    key="U",
    name="Autonomous",
    definition="The agent can plan and execute multiple steps independently.",
)
GOAL_DRIVEN_PLANNING = AivssDecisionPoint(
    key="GDP",
    name="Goal-Driven Planning",
    definition="Determines the goal-driven planning capabilities of an AI agent based on its ability to plan and execute actions over multiple steps.",
    version="1.0.0",
    values=(REACTIVE, ASSISTED, AUTONOMOUS),
)

VERSIONS = (GOAL_DRIVEN_PLANNING,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
