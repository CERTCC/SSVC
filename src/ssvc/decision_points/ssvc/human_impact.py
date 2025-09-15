#!/usr/bin/env python

"""
Provides the Human Impact decision point and its values.
"""
#  Copyright (c) 2023-2025 Carnegie Mellon University.
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

LOW_1 = DecisionPointValue(
    name="Low",
    key="L",
    definition="Mission Prevalence:Minimal AND Public Well-Being Impact:Minimal",
)

LOW_2 = DecisionPointValue(
    name="Low",
    key="L",
    definition="Safety Impact:(None OR Minor) AND Mission Impact:(None OR Degraded OR Crippled)",
)

LOW_3 = DecisionPointValue(
    name="Low",
    key="L",
    definition="Safety Impact:(Negligible) AND Mission Impact:(None OR Degraded OR Crippled)",
)

LOW_4 = DecisionPointValue(
    name="Low",
    key="L",
    definition="Safety Impact:(Negligible) AND Mission Impact:(Degraded OR Crippled)",
)


MEDIUM_1 = DecisionPointValue(
    name="Medium",
    key="M",
    definition="Mission Prevalence:Support AND Public Well-Being Impact:(Minimal OR Material)",
)

MEDIUM_2 = DecisionPointValue(
    name="Medium",
    key="M",
    definition="(Safety Impact:(None OR Minor) AND Mission Impact:MEF Failure) OR (Safety Impact:Major AND Mission Impact:(None OR Degraded OR Crippled))",
)

MEDIUM_3 = DecisionPointValue(
    name="Medium",
    key="M",
    definition="(Safety Impact:Negligible AND Mission Impact:MEF Failure) OR (Safety Impact:Marginal AND Mission Impact:(None OR Degraded OR Crippled))",
)

MEDIUM_4 = DecisionPointValue(
    name="Medium",
    key="M",
    definition="(Safety Impact:Negligible AND Mission Impact:MEF Failure) OR (Safety Impact:Marginal AND Mission Impact:(Degraded OR Crippled))",
)


HIGH_1 = DecisionPointValue(
    name="High",
    key="H",
    definition="Mission Prevalence:Essential OR Public Well-Being Impact:(Irreversible)",
)


HIGH_2 = DecisionPointValue(
    name="High",
    key="H",
    definition="(Safety Impact:Hazardous AND Mission Impact:(None OR Degraded OR Crippled)) OR (Safety Impact:Major AND Mission Impact:MEF Failure)",
)

HIGH_3 = DecisionPointValue(
    name="High",
    key="H",
    definition="(Safety Impact:Critical AND Mission Impact:(None OR Degraded OR Crippled)) OR (Safety Impact:Marginal AND Mission Impact:MEF Failure)",
)

HIGH_4 = DecisionPointValue(
    name="High",
    key="H",
    definition="(Safety Impact:Critical AND Mission Impact:(Degraded OR Crippled)) OR (Safety Impact:Marginal AND Mission Impact:MEF Failure)",
)

VERY_HIGH_1 = DecisionPointValue(
    name="Very High",
    key="VH",
    definition="Safety Impact:Catastrophic OR Mission Impact:Mission Failure",
)


MISSION_AND_WELL_BEING_IMPACT_1 = SsvcDecisionPoint(
    name="Mission and Well-Being Impact",
    definition="Mission and Well-Being Impact is a combination of Mission Prevalence and Public Well-Being Impact.",
    key="MWI",
    version="1.0.0",
    values=(
        LOW_1,
        MEDIUM_1,
        HIGH_1,
    ),
)


HUMAN_IMPACT_2 = SsvcDecisionPoint(
    name="Human Impact",
    definition="Human Impact is a combination of Safety and Mission impacts.",
    key="HI",
    version="2.0.0",
    values=(
        LOW_2,
        MEDIUM_2,
        HIGH_2,
        VERY_HIGH_1,
    ),
)

HUMAN_IMPACT_2_0_1 = SsvcDecisionPoint(
    name="Human Impact",
    definition="Human Impact is a combination of Safety and Mission impacts.",
    key="HI",
    version="2.0.1",
    values=(
        LOW_3,
        MEDIUM_3,
        HIGH_3,
        VERY_HIGH_1,
    ),
)

HUMAN_IMPACT_2_0_2 = SsvcDecisionPoint(
    name="Human Impact",
    definition="Human Impact is a combination of Safety and Mission impacts.",
    key="HI",
    version="2.0.2",
    values=(
        LOW_4,
        MEDIUM_4,
        HIGH_4,
        VERY_HIGH_1,
    ),
)


VERSIONS = (
    MISSION_AND_WELL_BEING_IMPACT_1,
    HUMAN_IMPACT_2,
    HUMAN_IMPACT_2_0_1,
    HUMAN_IMPACT_2_0_2,
)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
