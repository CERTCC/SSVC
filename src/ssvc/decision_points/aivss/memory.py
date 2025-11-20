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

# ## 1. Memory Use
# - **Stateless** — no persistence beyond the current interaction.
# - **Local Recall** — remembers within a session or user context.
# - **Shared Memory** — persistent state across sessions, tasks, or teams.

from ssvc.decision_points.aivss.base import AivssDecisionPoint
from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_points.helpers import print_versions_and_diffs

STATELESS = DecisionPointValue(
    key="S",
    name="Stateless",
    definition="No persistence beyond the current interaction.",
)
LOCAL_RECALL = DecisionPointValue(
    key="L",
    name="Local Recall",
    definition="Remembers within a session or user context.",
)
SHARED_MEMORY = DecisionPointValue(
    key="M",
    name="Shared Memory",
    definition="Persistent state across sessions, tasks, or teams.",
)
MEMORY_01 = AivssDecisionPoint(
    key="MU",
    name="Memory Use",
    definition="Determines the memory use level of an AI system based on its persistence and recall capabilities.",
    version="1.0.0",
    values=(STATELESS, LOCAL_RECALL, SHARED_MEMORY),
)
VERSIONS = (MEMORY_01,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
