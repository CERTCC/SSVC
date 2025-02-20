#!/usr/bin/env python

"""
Provides the Public Safety Impact decision point and its values.
"""

#  Copyright (c) 2024-2025 Carnegie Mellon University and Contributors.
#  - see Contributors.md for a full list of Contributors
#  - see ContributionInstructions.md for information on how you can Contribute to this project
#  Stakeholder Specific Vulnerability Categorization (SSVC) is
#  licensed under a MIT (SEI)-style license, please see LICENSE.md distributed
#  with this Software or contact permission@sei.cmu.edu for full terms.
#  Created, in part, with funding and support from the United States Government
#  (see Acknowledgments file). This program may include and/or can make use of
#  certain third party source code, object code, documentation and other files
#  (“Third Party Software”). See LICENSE.md for more details.
#  Carnegie Mellon®, CERT® and CERT Coordination Center® are registered in the
#  U.S. Patent and Trademark Office by Carnegie Mellon University

from ssvc.decision_points.base import SsvcDecisionPoint, SsvcDecisionPointValue
from ssvc.decision_points.helpers import print_versions_and_diffs

MINIMAL_1 = SsvcDecisionPointValue(
    name="Minimal",
    description="The effect is below the threshold for all aspects described in material. ",
    key="M",
)

MATERIAL = SsvcDecisionPointValue(
    name="Material",
    description="Any one or more of these conditions hold. "
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

IRREVERSIBLE = SsvcDecisionPointValue(
    name="Irreversible",
    description="Any one or more of these conditions hold. "
    "Physical harm: One or both of the following are true: (a) Multiple fatalities are likely."
    "(b) The cyber-physical system, of which the vulnerable componen is a part, is likely lost or destroyed. "
    " Environment: Extreme or serious externalities (immediate public health threat, environmental damage leading to small "
    " ecosystem collapse, etc.) are imposed on other parties. "
    " Financial: Social systems (elections, financial grid, etc.) supported by the software are destabilized and potentially "
    "collapse. "
    " Psychological: N/A ",
    key="I",
)

SIGNIFICANT = SsvcDecisionPointValue(
    name="Significant",
    description="Safety Impact:(Major OR Hazardous OR Catastrophic)",
    key="S",
)

MINIMAL_2 = SsvcDecisionPointValue(
    name="Minimal", description="Safety Impact:(None OR Minor)", key="M"
)

SIGNIFICANT_1 = SsvcDecisionPointValue(
    name="Significant",
    description="Safety Impact:(Marginal OR Critical OR Catastrophic)",
    key="S",
)

MINIMAL_3 = SsvcDecisionPointValue(
    name="Minimal", description="Safety Impact:Negligible", key="M"
)


PUBLIC_WELL_BEING_IMPACT_1 = SsvcDecisionPoint(
    name="Public Well-Being Impact",
    description="A coarse-grained representation of impact to public well-being.",
    key="PWI",
    version="1.0.0",
    values=(
        MINIMAL_1,
        MATERIAL,
        IRREVERSIBLE,
    ),
)

PUBLIC_SAFETY_IMPACT_2 = SsvcDecisionPoint(
    name="Public Safety Impact",
    description="A coarse-grained representation of impact to public safety.",
    key="PSI",
    version="2.0.0",
    values=(
        MINIMAL_2,
        SIGNIFICANT,
    ),
)

PUBLIC_SAFETY_IMPACT_2_0_1 = SsvcDecisionPoint(
    name="Public Safety Impact",
    description="A coarse-grained representation of impact to public safety.",
    key="PSI",
    version="2.0.1",
    values=(
        MINIMAL_3,
        SIGNIFICANT_1,
    ),
)

VERSIONS = (
    PUBLIC_WELL_BEING_IMPACT_1,
    PUBLIC_SAFETY_IMPACT_2,
    PUBLIC_SAFETY_IMPACT_2_0_1,
)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
