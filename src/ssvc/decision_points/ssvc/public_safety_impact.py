#!/usr/bin/env python

"""
Provides the Public Safety Impact decision point and its values.
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

MINIMAL_1 = DecisionPointValue(
    name="Minimal",
    definition="The effect is below the threshold for all aspects described in material. ",
    key="M",
)

MATERIAL = DecisionPointValue(
    name="Material",
    definition="Any one or more of these conditions hold. "
    "Physical harm: Does one or more of the following: "
    "(a) Causes physical distress or injury to system users. "
    "(b) Introduces occupational safety hazards. "
    "(c) Reduces and/or results in failure of cyber-physical system safety margins. "
    "Environment: Major externalities (property damage, environmental damage, etc.) are "
    "imposed on other parties. "
    "Financial: Financial losses likely lead to bankruptcy of multiple persons. "
    "Psychological: Widespread emotional or psychological harm, sufficient to necessitate "
    "counseling or therapy, impact populations of people. ",
    key="M",
)

MATERIAL_1 = DecisionPointValue(
    name="Material",
    definition="Any one or more of these conditions hold. "
    "Physical harm: Does one or more of the following: "
    "(a) Causes physical distress or injury to system users. "
    "(b) Introduces occupational safety hazards. "
    "(c) Reduces and/or results in failure of cyber-physical system safety margins. "
    "Environment: Major externalities (property damage, environmental damage, etc.) are "
    "imposed on other parties. "
    "Financial: Financial losses likely lead to bankruptcy of multiple persons. "
    "Psychological: Widespread emotional or psychological harm, sufficient to necessitate "
    "counseling or therapy, impact populations of people. ",
    key="MA",
)


IRREVERSIBLE = DecisionPointValue(
    name="Irreversible",
    definition="Any one or more of these conditions hold. "
    "Physical harm: One or both of the following are true: (a) Multiple fatalities are likely."
    "(b) The cyber-physical system, of which the vulnerable componen is a part, is likely lost or destroyed. "
    " Environment: Extreme or serious externalities (immediate public health threat, environmental damage leading to small "
    " ecosystem collapse, etc.) are imposed on other parties. "
    " Financial: Social systems (elections, financial grid, etc.) supported by the software are destabilized and potentially "
    "collapse. "
    " Psychological: N/A ",
    key="I",
)

SIGNIFICANT = DecisionPointValue(
    name="Significant",
    definition="Safety Impact:(Major OR Hazardous OR Catastrophic)",
    key="S",
)

MINIMAL_2 = DecisionPointValue(
    name="Minimal", definition="Safety Impact:(None OR Minor)", key="M"
)

SIGNIFICANT_1 = DecisionPointValue(
    name="Significant",
    definition="Safety Impact:(Marginal OR Critical OR Catastrophic)",
    key="S",
)

MINIMAL_3 = DecisionPointValue(
    name="Minimal", definition="Safety Impact:Negligible", key="M"
)

# This version is deprecated because it had two values with the same key.
# It is kept here for reference, but should not be used in new code.
# PUBLIC_WELL_BEING_IMPACT_1 = SsvcDecisionPoint(
#     name="Public Well-Being Impact",
#     description="A coarse-grained representation of impact to public well-being.",
#     key="PWI",
#     version="1.0.0",
#     values=(
#         MINIMAL_1,
#         MATERIAL,
#         IRREVERSIBLE,
#     ),
# )

PUBLIC_WELL_BEING_IMPACT_1_1 = SsvcDecisionPoint(
    name="Public Well-Being Impact",
    definition="A coarse-grained representation of impact to public well-being.",
    key="PWI",
    version="1.1.0",
    values=(
        MINIMAL_1,
        MATERIAL_1,
        IRREVERSIBLE,
    ),
)


PUBLIC_SAFETY_IMPACT_2 = SsvcDecisionPoint(
    name="Public Safety Impact",
    definition="A coarse-grained representation of impact to public safety.",
    key="PSI",
    version="2.0.0",
    values=(
        MINIMAL_2,
        SIGNIFICANT,
    ),
)

PUBLIC_SAFETY_IMPACT_2_0_1 = SsvcDecisionPoint(
    name="Public Safety Impact",
    definition="A coarse-grained representation of impact to public safety.",
    key="PSI",
    version="2.0.1",
    values=(
        MINIMAL_3,
        SIGNIFICANT_1,
    ),
)

VERSIONS = (
    # PUBLIC_WELL_BEING_IMPACT_1,
    PUBLIC_WELL_BEING_IMPACT_1_1,
    PUBLIC_SAFETY_IMPACT_2,
    PUBLIC_SAFETY_IMPACT_2_0_1,
)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
