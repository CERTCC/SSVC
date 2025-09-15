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
Provides the defer, scheduled, out-of-cycle, immediate outcome group for use in SSVC.
"""
from ssvc.decision_points.base import DecisionPointValue as DecisionPointValue
from ssvc.decision_points.helpers import print_versions_and_diffs
from ssvc.decision_points.ssvc.base import SsvcDecisionPoint

_DEFER = DecisionPointValue(name="Defer", key="D", definition="Defer")

_SCHEDULED = DecisionPointValue(
    name="Scheduled", key="S", definition="Scheduled"
)

_OUT_OF_CYCLE = DecisionPointValue(
    name="Out-of-Cycle", key="O", definition="Out-of-Cycle"
)

_IMMEDIATE = DecisionPointValue(
    name="Immediate", key="I", definition="Immediate"
)

DSOI = SsvcDecisionPoint(
    name="Defer, Scheduled, Out-of-Cycle, Immediate",
    key="DSOI",
    definition="The original SSVC outcome group.",
    version="1.0.0",
    values=(
        _DEFER,
        _SCHEDULED,
        _OUT_OF_CYCLE,
        _IMMEDIATE,
    ),
)
"""
The original SSVC outcome group.
"""


VERSIONS = (DSOI,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
