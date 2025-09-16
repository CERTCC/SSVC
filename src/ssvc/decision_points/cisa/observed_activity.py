#!/usr/bin/env python
"""
Provides the NCISS Observed Activity Decision Point.
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

from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_points.cisa.base import NcissDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs

PREPARE = DecisionPointValue(
    key="P",
    name="Prepare",
    definition="Prepare actions are actions taken to establish objectives, intent, and strategy; "
    "identify potential targets and attack vectors; "
    "identify resource requirements; "
    "and develop capabilities.",
)

ENGAGE = DecisionPointValue(
    key="E",
    name="Engage",
    definition="Engage activities are actions taken against a specific target or target set prior to gaining, "
    "but with the intent to gain access to the victim's physical or virtual computer or information systems, "
    "networks, and data stores.",
)

PRESENCE = DecisionPointValue(
    key="R",
    name="Presence",
    definition="Presence is the set of actions taken by the threat actor once access to the target physical or "
    "virtual computer or information system has been achieved. "
    "These actions establish and maintain conditions for the threat actor to perform intended actions "
    "or operate at will against the host physical or virtual computer or information system, network, "
    "or data stores.",
)

EFFECT = DecisionPointValue(
    key="F",
    name="Effect",
    definition="Effects are outcomes of a threat actor’s actions "
    "on a victim’s physical or virtual computer or information systems, networks, and data stores.",
)


OBSERVED_ACTIVITY = NcissDecisionPoint(
    key="OA",
    name="Observed Activity",
    definition="Observed activity describes what is known about threat actor activity on the network.",
    values=(PREPARE, ENGAGE, PRESENCE, EFFECT),
)

VERSIONS = (OBSERVED_ACTIVITY,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
