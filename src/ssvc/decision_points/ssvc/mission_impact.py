#!/usr/bin/env python

"""
Provides the Mission Impact decision point and its values.
"""

#  Copyright (c) 2024-2025 Carnegie Mellon University.
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
from ssvc.decision_points.helpers import print_versions_and_diffs
from ssvc.decision_points.ssvc.base import SsvcDecisionPoint

MISSION_FAILURE = DecisionPointValue(
    name="Mission Failure",
    key="MF",
    definition="Multiple or all mission essential functions fail; ability to recover those functions degraded; organization’s ability to deliver its overall mission fails",
)

MEF_FAILURE = DecisionPointValue(
    name="MEF Failure",
    key="MEF",
    definition="Any one mission essential function fails for period of time longer than acceptable; overall mission of the organization degraded but can still be accomplished for a time",
)

MEF_CRIPPLED = DecisionPointValue(
    name="MEF Support Crippled",
    key="MSC",
    definition="Activities that directly support essential functions are crippled; essential functions continue for a time",
)


MI_NED = DecisionPointValue(
    name="Non-Essential Degraded",
    key="NED",
    definition="Degradation of non-essential functions; chronic degradation would eventually harm essential functions",
)

MI_NONE = DecisionPointValue(
    name="None", key="N", definition="Little to no impact"
)

# combine MI_NONE and MI_NED into a single value
DEGRADED = DecisionPointValue(
    name="Degraded",
    key="D",
    definition="Little to no impact up to degradation of non-essential functions; chronic degradation would eventually harm essential functions",
)


MISSION_IMPACT_1 = SsvcDecisionPoint(
    name="Mission Impact",
    definition="Impact on Mission Essential Functions of the Organization",
    key="MI",
    version="1.0.0",
    values=(
        MI_NONE,
        MI_NED,
        MEF_CRIPPLED,
        MEF_FAILURE,
        MISSION_FAILURE,
    ),
)

# SSVC v2.1 combined None and Non-Essential Degraded into a single value
MISSION_IMPACT_2 = SsvcDecisionPoint(
    name="Mission Impact",
    definition="Impact on Mission Essential Functions of the Organization",
    key="MI",
    version="2.0.0",
    values=(DEGRADED, MEF_CRIPPLED, MEF_FAILURE, MISSION_FAILURE),
)

VERSIONS = (MISSION_IMPACT_1, MISSION_IMPACT_2)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
