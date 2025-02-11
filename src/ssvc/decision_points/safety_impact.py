#!/usr/bin/env python

"""
Provides the Safety Impact decision point and its values.
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

CATASTROPHIC = SsvcDecisionPointValue(
    name="Catastrophic",
    key="C",
    description="Any one or more of these conditions hold. "
    "Physical harm: Multiple immediate fatalities (Emergency response probably cannot save the victims.) "
    "Operator resiliency: Operator incapacitated (includes fatality or otherwise incapacitated). "
    "System resiliency: Total loss of whole cyber-physical system, of which the software is a part. "
    "Environment: Extreme externalities (immediate public health threat, environmental damage leading to small ecosystem collapse, etc.) imposed on other parties. "
    "Financial: Social systems (elections, financial grid, etc.) supported by the software collapse. "
    "Psychological: N/A.",
)

HAZARDOUS = SsvcDecisionPointValue(
    name="Hazardous",
    key="H",
    description="Any one or more of these conditions hold. "
    "Physical harm: Serious or fatal injuries, where fatalities are plausibly preventable via emergency services or other measures. "
    "Operator resiliency: Actions that would keep the system in a safe state are beyond system operator capabilities, resulting in adverse conditions; OR great physical distress to system operators such that they cannot be expected to operate the system properly. "
    "System resiliency: Parts of the cyber-physical system break; system’s ability to recover lost functionality remains intact. "
    "Environment: Serious externalities (threat to life as well as property, widespread environmental damage, measurable public health risks, etc.) imposed on other parties. "
    "Financial: Socio-technical system (elections, financial grid, etc.) of which the affected component is a part is actively destabilized and enters unsafe state. "
    "Psychological: N/A.",
)

MAJOR = SsvcDecisionPointValue(
    name="Major",
    key="J",
    description="Any one or more of these conditions hold. "
    "Physical harm: Physical distress and injuries for users (not operators) of the system. "
    "Operator resiliency: Requires action by system operator to maintain safe system state as a result of exploitation of the "
    "vulnerability where operator actions would be within their capabilities but the actions require their full attention and effort; OR significant distraction or discomfort to operators; OR causes significant occupational safety hazard. "
    "System resiliency: System safety margin effectively eliminated but no actual harm; OR failure of system functional capabilities that support safe operation. "
    "Environment: Major externalities (property damage, environmental damage, etc.) imposed on other parties. "
    "Financial: Financial losses that likely lead to bankruptcy of multiple persons. "
    "Psychological: Widespread emotional or psychological harm, sufficient to be cause for counselling or therapy, to populations of people.",
)

MINOR = SsvcDecisionPointValue(
    name="Minor",
    key="M",
    description="Any one or more of these conditions hold. "
    "Physical harm: Physical discomfort for users (not operators) of the system. "
    "Operator resiliency: Requires action by system operator to maintain safe system state as a result of exploitation of the "
    "vulnerability where operator actions would be well within expected operator abilities; OR causes a minor occupational safety hazard. "
    "System resiliency: Small reduction in built-in system safety margins; OR small reduction in system functional capabilities that support safe operation. "
    "Environment: Minor externalities (property damage, environmental damage, etc.) imposed on other parties. "
    "Financial Financial losses, which are not readily absorbable, to multiple persons. "
    "Psychological: Emotional or psychological harm, sufficient to be cause for counselling or therapy, to multiple persons.",
)

SAF_NONE = SsvcDecisionPointValue(
    name="None",
    key="N",
    description="The effect is below the threshold for all aspects described in Minor.",
)

## Based on the IEC 61508 standard
## Catastrophic, Critical, Marginal, Negligible

CATASTROPHIC_2 = SsvcDecisionPointValue(
    name="Catastrophic",
    key="C",
    description="Any one or more of these conditions hold.<br/><br/>"
    "- *Physical harm*: Multiple loss of life (IEC 61508 Catastrophic).<br/>"
    "- *Operator resiliency*: Operator incapacitated (includes fatality or otherwise incapacitated).<br/>"
    "- *System resiliency*: Total loss of whole cyber-physical system, of which the software is a part.<br/>"
    "- *Environment*: Extreme externalities (immediate public health threat, environmental damage leading to small ecosystem collapse, etc.) imposed on other parties.<br/>"
    "- *Financial*: Social systems (elections, financial grid, etc.) supported by the software collapse.<br/>"
    "- *Psychological*: N/A.",
)

CRITICAL = SsvcDecisionPointValue(
    name="Critical",
    key="R",
    description="Any one or more of these conditions hold.<br/><br/>"
    "- *Physical harm*: Loss of life (IEC 61508 Critical).<br/>"
    "- *Operator resiliency*: Actions that would keep the system in a safe state are beyond system operator capabilities, resulting in adverse conditions; OR great physical distress to system operators such that they cannot be expected to operate the system properly.<br/>"
    "- *System resiliency*: Parts of the cyber-physical system break; system’s ability to recover lost functionality remains intact.<br/>"
    "- *Environment*: Serious externalities (threat to life as well as property, widespread environmental damage, measurable public health risks, etc.) imposed on other parties.<br/>"
    "- *Financial*: Socio-technical system (elections, financial grid, etc.) of which the affected component is a part is actively destabilized and enters unsafe state.<br/>"
    "- *Psychological*: N/A.",
)

MARGINAL = SsvcDecisionPointValue(
    name="Marginal",
    key="M",
    description="Any one or more of these conditions hold.<br/><br/>"
    "- *Physical harm*: Major injuries to one or more persons (IEC 61508 Marginal).<br/>"
    "- *Operator resiliency*: Requires action by system operator to maintain safe system state as a result of exploitation of the "
    "vulnerability where operator actions would be within their capabilities but the actions require their full attention and effort; OR significant distraction or discomfort to operators; OR causes significant occupational safety hazard.<br/>"
    "- *System resiliency*: System safety margin effectively eliminated but no actual harm; OR failure of system functional capabilities that support safe operation.<br/>"
    "- *Environment*: Major externalities (property damage, environmental damage, etc.) imposed on other parties.<br/>"
    "- *Financial*: Financial losses that likely lead to bankruptcy of multiple persons.<br/>"
    "- *Psychological*: Widespread emotional or psychological harm, sufficient to be cause for counselling or therapy, to populations of people.",
)

NEGLIGIBLE = SsvcDecisionPointValue(
    name="Negligible",
    key="N",
    description="Any one or more of these conditions hold.<br/><br/>"
    "- *Physical harm*: Minor injuries at worst (IEC 61508 Negligible).<br/>"
    "- *Operator resiliency*: Requires action by system operator to maintain safe system state as a result of exploitation of the "
    "vulnerability where operator actions would be well within expected operator abilities; OR causes a minor occupational safety hazard.<br/>"
    "- *System resiliency*: Small reduction in built-in system safety margins; OR small reduction in system functional capabilities that support safe operation.<br/>"
    "- *Environment*: Minor externalities (property damage, environmental damage, etc.) imposed on other parties.<br/>"
    "- *Financial*: Financial losses, which are not readily absorbable, to multiple persons.<br/>"
    "- *Psychological*: Emotional or psychological harm, sufficient to be cause for counselling or therapy, to multiple persons.",
)


SAFETY_IMPACT_1 = SsvcDecisionPoint(
    name="Safety Impact",
    description="The safety impact of the vulnerability.",
    key="SI",
    version="1.0.0",
    values=(
        SAF_NONE,
        MINOR,
        MAJOR,
        HAZARDOUS,
        CATASTROPHIC,
    ),
)


SAFETY_IMPACT_2 = SsvcDecisionPoint(
    name="Safety Impact",
    description="The safety impact of the vulnerability. (based on IEC 61508)",
    key="SI",
    version="2.0.0",
    values=(
        NEGLIGIBLE,
        MARGINAL,
        CRITICAL,
        CATASTROPHIC_2,
    ),
)


def main():
    versions = (SAFETY_IMPACT_1, SAFETY_IMPACT_2)

    print_versions_and_diffs(versions)


if __name__ == "__main__":
    main()
