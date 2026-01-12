#!/usr/bin/env python

#  Copyright (c) 2025-2026 Carnegie Mellon University.
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
Provides the AIVSS Autonomy of Action Decision Point for SSVC.
"""
from ssvc.decision_points.aivss.base import AivssDecisionPoint
from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_points.helpers import print_versions_and_diffs


GATED = DecisionPointValue(
    key="G",
    name="Gated",
    definition="The agent cannot act without human approval.",
)

SCOPED = DecisionPointValue(
    key="S",
    name="Scoped",
    definition="The agent can act independently but only in tightly bounded spaces.",
)

FREE_RUNNING = DecisionPointValue(
    key="F",
    name="Free-Running",
    definition="The agent can execute actions in live systems without a human in the loop.",
)

AUTONOMY = AivssDecisionPoint(
    key="AA",
    name="Autonomy of Action",
    definition="Determines the autonomy of action level of a vulnerability based on its characteristics and potential effects.",
    version="1.0.0",
    values=(GATED, SCOPED, FREE_RUNNING),
)

VERSIONS = (AUTONOMY,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
