#!/usr/bin/env python

"""
Provides the Safety Impact decision point and its values.
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

CATASTROPHIC = DecisionPointValue(
    name="Catastrophic",
    key="C",
    definition="Any one or more of these conditions hold. "
    "Physical harm: Multiple immediate fatalities (Emergency response probably cannot save the victims.) "
    "Operator resiliency: Operator incapacitated (includes fatality or otherwise incapacitated). "
    "System resiliency: Total loss of whole cyber-physical system, of which the software is a part. "
    "Environment: Extreme externalities (immediate public health threat, environmental damage leading to small ecosystem collapse, etc.) imposed on other parties. "
    "Financial: Social systems (elections, financial grid, etc.) supported by the software collapse. "
    "Psychological: N/A.",
)

HAZARDOUS = DecisionPointValue(
    name="Hazardous",
    key="H",
    definition="Any one or more of these conditions hold. "
    "Physical harm: Serious or fatal injuries, where fatalities are plausibly preventable via emergency services or other measures. "
    "Operator resiliency: Actions that would keep the system in a safe state are beyond system operator capabilities, resulting in adverse conditions; OR great physical distress to system operators such that they cannot be expected to operate the system properly. "
    "System resiliency: Parts of the cyber-physical system break; system’s ability to recover lost functionality remains intact. "
    "Environment: Serious externalities (threat to life as well as property, widespread environmental damage, measurable public health risks, etc.) imposed on other parties. "
    "Financial: Socio-technical system (elections, financial grid, etc.) of which the affected component is a part is actively destabilized and enters unsafe state. "
    "Psychological: N/A.",
)

MAJOR = DecisionPointValue(
    name="Major",
    key="J",
    definition="Any one or more of these conditions hold. "
    "Physical harm: Physical distress and injuries for users (not operators) of the system. "
    "Operator resiliency: Requires action by system operator to maintain safe system state as a result of exploitation of the "
    "vulnerability where operator actions would be within their capabilities but the actions require their full attention and effort; OR significant distraction or discomfort to operators; OR causes significant occupational safety hazard. "
    "System resiliency: System safety margin effectively eliminated but no actual harm; OR failure of system functional capabilities that support safe operation. "
    "Environment: Major externalities (property damage, environmental damage, etc.) imposed on other parties. "
    "Financial: Financial losses that likely lead to bankruptcy of multiple persons. "
    "Psychological: Widespread emotional or psychological harm, sufficient to be cause for counselling or therapy, to populations of people.",
)

MINOR = DecisionPointValue(
    name="Minor",
    key="M",
    definition="Any one or more of these conditions hold. "
    "Physical harm: Physical discomfort for users (not operators) of the system. "
    "Operator resiliency: Requires action by system operator to maintain safe system state as a result of exploitation of the "
    "vulnerability where operator actions would be well within expected operator abilities; OR causes a minor occupational safety hazard. "
    "System resiliency: Small reduction in built-in system safety margins; OR small reduction in system functional capabilities that support safe operation. "
    "Environment: Minor externalities (property damage, environmental damage, etc.) imposed on other parties. "
    "Financial Financial losses, which are not readily absorbable, to multiple persons. "
    "Psychological: Emotional or psychological harm, sufficient to be cause for counselling or therapy, to multiple persons.",
)

SAF_NONE = DecisionPointValue(
    name="None",
    key="N",
    definition="The effect is below the threshold for all aspects described in Minor.",
)

## Based on the IEC 61508 standard
## Catastrophic, Critical, Marginal, Negligible

CATASTROPHIC_2 = DecisionPointValue(
    name="Catastrophic",
    key="C",
    definition="Any one or more of these conditions hold.<br/><br/>"
    "- *Physical harm*: Multiple loss of life (IEC 61508 Catastrophic).<br/>"
    "- *Operator resiliency*: Operator incapacitated (includes fatality or otherwise incapacitated).<br/>"
    "- *System resiliency*: Total loss of whole cyber-physical system, of which the software is a part.<br/>"
    "- *Environment*: Extreme externalities (immediate public health threat, environmental damage leading to small ecosystem collapse, etc.) imposed on other parties.<br/>"
    "- *Financial*: Social systems (elections, financial grid, etc.) supported by the software collapse.<br/>"
    "- *Psychological*: N/A.",
)

CRITICAL = DecisionPointValue(
    name="Critical",
    key="R",
    definition="Any one or more of these conditions hold.<br/><br/>"
    "- *Physical harm*: Loss of life (IEC 61508 Critical).<br/>"
    "- *Operator resiliency*: Actions that would keep the system in a safe state are beyond system operator capabilities, resulting in adverse conditions; OR great physical distress to system operators such that they cannot be expected to operate the system properly.<br/>"
    "- *System resiliency*: Parts of the cyber-physical system break; system’s ability to recover lost functionality remains intact.<br/>"
    "- *Environment*: Serious externalities (threat to life as well as property, widespread environmental damage, measurable public health risks, etc.) imposed on other parties.<br/>"
    "- *Financial*: Socio-technical system (elections, financial grid, etc.) of which the affected component is a part is actively destabilized and enters unsafe state.<br/>"
    "- *Psychological*: N/A.",
)

MARGINAL = DecisionPointValue(
    name="Marginal",
    key="M",
    definition="Any one or more of these conditions hold.<br/><br/>"
    "- *Physical harm*: Major injuries to one or more persons (IEC 61508 Marginal).<br/>"
    "- *Operator resiliency*: Requires action by system operator to maintain safe system state as a result of exploitation of the "
    "vulnerability where operator actions would be within their capabilities but the actions require their full attention and effort; OR significant distraction or discomfort to operators; OR causes significant occupational safety hazard.<br/>"
    "- *System resiliency*: System safety margin effectively eliminated but no actual harm; OR failure of system functional capabilities that support safe operation.<br/>"
    "- *Environment*: Major externalities (property damage, environmental damage, etc.) imposed on other parties.<br/>"
    "- *Financial*: Financial losses that likely lead to bankruptcy of multiple persons.<br/>"
    "- *Psychological*: Widespread emotional or psychological harm, sufficient to be cause for counselling or therapy, to populations of people.",
)

NEGLIGIBLE = DecisionPointValue(
    name="Negligible",
    key="N",
    definition="Any one or more of these conditions hold.<br/><br/>"
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
    definition="The safety impact of the vulnerability.",
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
    definition="The safety impact of the vulnerability. (based on IEC 61508)",
    key="SI",
    version="2.0.0",
    values=(
        NEGLIGIBLE,
        MARGINAL,
        CRITICAL,
        CATASTROPHIC_2,
    ),
)


VERSIONS = (SAFETY_IMPACT_1, SAFETY_IMPACT_2)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
