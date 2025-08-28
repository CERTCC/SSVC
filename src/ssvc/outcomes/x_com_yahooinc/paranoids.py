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
Provides a decision point for the `x_com_yahooinc` namespace.
"""

from ssvc.decision_points.base import (
    DecisionPoint,
    DecisionPointValue as DecisionPointValue,
)
from ssvc.decision_points.helpers import print_versions_and_diffs

_TRACK_5 = DecisionPointValue(name="Track 5", key="5", definition="Track")

_TRACK_CLOSELY_4 = DecisionPointValue(
    name="Track Closely 4", key="4", definition="Track Closely"
)

_ATTEND_3 = DecisionPointValue(name="Attend 3", key="3", definition="Attend")

_ATTEND_2 = DecisionPointValue(name="Attend 2", key="2", definition="Attend")

_ACT_1 = DecisionPointValue(name="Act 1", key="1", definition="Act")

_ACT_ASAP_0 = DecisionPointValue(
    name="Act ASAP 0", key="0", definition="Act ASAP"
)

THE_PARANOIDS = DecisionPoint(
    name="theParanoids",
    key="PARANOIDS",
    definition="PrioritizedRiskRemediation outcome group based on TheParanoids.",
    namespace="x_com.yahooinc#prioritized-risk-remediation",
    version="1.0.0",
    values=(
        _TRACK_5,
        _TRACK_CLOSELY_4,
        _ATTEND_3,
        _ATTEND_2,
        _ACT_1,
        _ACT_ASAP_0,
    ),
)
"""
Outcome group based on TheParanoids' PrioritizedRiskRemediation.
Their model is a 6-point scale, with 0 being the most urgent and 5 being the least.
See https://github.com/theparanoids/PrioritizedRiskRemediation
"""

VERSIONS = (THE_PARANOIDS,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
