#!/usr/bin/env python

"""
Provides TODO writeme
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

ISOLATED = DecisionPointValue(
    key="I",
    name="Isolated",
    definition="Operates in a narrow, stable context with no meaningful external awareness. "
    "No cross-session memory, multi-agent behavior, or identity changes. "
    "Environmental shifts don’t affect behavior unless a human explicitly updates inputs.",
)

CONNECTED = DecisionPointValue(
    key="C",
    name="Connected",
    definition="Uses curated signals, scoped identity roles, or predefined multi-agent patterns to adapt. "
    "Environmental changes can influence behavior, but only within controlled, auditable bounds.",
)

PERVASIVE = DecisionPointValue(
    key="P",
    name="Pervasive",
    definition="Continuously adapts to broad, dynamic environmental inputs and multi-agent activity. "
    "Identity, memory, and context can shift fluidly, creating emergent behavior. "
    "Environmental variation can substantially redirect or amplify its actions.",
)

ENV_ADAPT_01 = AivssDecisionPoint(
    key="EA",
    name="Environment & Adaptation",
    definition="Determines the environment and adaptation level of an AI system based on its context awareness and adaptability.",
    version="1.0.0",
    values=(ISOLATED, CONNECTED, PERVASIVE),
)

VERSIONS = (ENV_ADAPT_01,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
