#!/usr/bin/env python

"""
Provides the AIVSS Multi-Agent Interactions Decision Point for SSVC.
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

# ## 3. Multi-Agent Interactions
# - Solo — operates alone; no coordination.
# - Scripted — interacts through predefined handoffs or protocols.
# - Orchestrated — dynamic teaming, swarms, emergent behavior, or markets.

SOLO = DecisionPointValue(
    key="S",
    name="Solo",
    definition="Operates alone; no coordination.",
)

SCRIPTED = DecisionPointValue(
    key="R",
    name="Scripted",
    definition="Interacts through predefined handoffs or protocols.",
)

ORCHESTRATED = DecisionPointValue(
    key="O",
    name="Orchestrated",
    definition="Dynamic teaming, swarms, emergent behavior, or markets.",
)

MULTI_AGENT_INTERACTIONS_01 = AivssDecisionPoint(
    key="MAI",
    name="Multi-Agent Interactions",
    definition=(
        "Characterizes how, and how flexibly, an AI system coordinates with other agents or services."
    ),
    version="1.0.0",
    values=(SOLO, SCRIPTED, ORCHESTRATED),
)

VERSIONS = (MULTI_AGENT_INTERACTIONS_01,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
