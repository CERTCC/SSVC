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
Provides the AIVSS Self-Modification Decision Point for SSVC.
"""

from ssvc.decision_points.aivss.base import AivssDecisionPoint
from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_points.helpers import print_versions_and_diffs

FIXED = DecisionPointValue(
    key="F",
    name="Fixed",
    definition="The agent cannot modify its own code, configuration, or behavior.",
)

TUNABLE = DecisionPointValue(
    key="T",
    name="Tunable",
    definition="The agent can modify its configuration or prompts but not its core code or behavior.",
)

MUTABLE = DecisionPointValue(
    key="M",
    name="Mutable",
    definition="The agent can modify its own code, configuration, or behavior.",
)

SELF_MODIFICATION_1_0_0 = AivssDecisionPoint(
    key="SM",
    name="Self-Modification",
    definition="Determines the self-modification capabilities of an AI agent based on its ability to alter its own code, configuration, or behavior.",
    version="1.0.0",
    values=(FIXED, MUTABLE),
)

SELF_MODIFICATION_1_1_0 = AivssDecisionPoint(
    key="SM",
    name="Self-Modification",
    definition="Determines the self-modification capabilities of an AI agent based on its ability to alter its own code, configuration, or behavior.",
    version="1.1.0",
    values=(FIXED, TUNABLE, MUTABLE),
)

VERSIONS = (SELF_MODIFICATION_1_0_0, SELF_MODIFICATION_1_1_0)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
