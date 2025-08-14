#!/usr/bin/env python
"""
Provides a decision point for Incident Severity.
Based on [National Cybersecurity Incident Scoring System (NCISS)](https://www.cisa.gov/sites/default/files/2023-01/cisa_national_cyber_incident_scoring_system_s508c.pdf)
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

# Define the values for the Cyber Incident Severity decision point
# Intentionally omitting the color codes from the original schema at this time
# We can add them later if needed
LEVEL_5 = DecisionPointValue(
    name="Emergency",
    key="5",
    description="Poses an imminent threat to the provision of wide-scale critical infrastructure services, national "
    "government stability, or to the lives of U.S. persons.",
)

LEVEL_4 = DecisionPointValue(
    name="Severe",
    key="4",
    description="Likely to result in a significant impact to public health or safety, national security, economic "
    "security, foreign relations, or civil liberties.",
)

LEVEL_3 = DecisionPointValue(
    name="High",
    key="3",
    description="Likely to result in a demonstrable impact to public health or safety, national security, economic "
    "security, foreign relations, civil liberties, or public confidence.",
)

LEVEL_2 = DecisionPointValue(
    name="Medium",
    key="2",
    description="May impact public health or safety, national security, economic security, foreign relations, civil "
    "liberties, or public confidence.",
)

LEVEL_1 = DecisionPointValue(
    name="Low",
    key="1",
    description="Unlikely to impact public health or safety, national security, economic security, foreign relations, "
    "civil liberties, or public confidence.",
)

LEVEL_0 = DecisionPointValue(
    name="Baseline",
    key="0",
    description="Unsubstantiated or inconsequential event.",
)

# Define the Cyber Incident Severity decision point
INCIDENT_SEVERITY = NcissDecisionPoint(
    name="Incident Severity",
    description="The United States Federal Cybersecurity Centers, in coordination "
    "with departments and agencies with a cybersecurity or cyber operations mission, "
    "adopted a common schema for describing the severity of cyber incidents affecting "
    "the homeland, U.S. capabilities, or U.S. interests.",
    key="IS",
    version="1.0.0",
    values=(
        LEVEL_0,
        LEVEL_1,
        LEVEL_2,
        LEVEL_3,
        LEVEL_4,
        LEVEL_5,
    ),
)

LEVEL_5_1 = DecisionPointValue(
    name="Emergency",
    key="5",
    description="An Emergency priority incident poses an imminent threat to the provision of wide-scale critical infrastructure "
    "services, national government stability, or the lives of U.S. persons.",
)

LEVEL_4_1 = DecisionPointValue(
    name="Severe",
    key="4",
    description="A Severe priority incident is likely to result in a significant impact to public health or safety, national security, "
    "economic security, foreign relations, or civil liberties.",
)

LEVEL_3_1 = DecisionPointValue(
    name="High",
    key="3",
    description="A High priority incident is likely to result in a demonstrable impact to public health or safety, national security, "
    "economic security, foreign relations, civil liberties, or public confidence.",
)

LEVEL_2_1 = DecisionPointValue(
    name="Medium",
    key="2",
    description="A Medium priority incident may affect public health or safety, national security, economic security, foreign "
    "relations, civil liberties, or public confidence.",
)

LEVEL_1_1 = DecisionPointValue(
    name="Low",
    key="1",
    description="A Low priority incident is unlikely to affect public health or safety, national security, economic security, foreign "
    "relations, civil liberties, or public confidence.",
)

LEVEL_0_MINOR = DecisionPointValue(
    name="Baseline - Minor",
    key="0M",
    description="A Baseline–Minor priority incident is an incident that is highly unlikely to affect public health or safety, "
    "national security, economic security, foreign relations, civil liberties, or public confidence. The potential for "
    "impact, however, exists and warrants additional scrutiny.",
)

LEVEL_0_NEGLIGIBLE = DecisionPointValue(
    name="Baseline - Negligible",
    key="0N",
    description="A Baseline–Negligible priority incident is an incident that is highly unlikely to affect public health or safety, "
    "national security, economic security, foreign relations, civil liberties, or public confidence. The potential for "
    "impact, however, exists and warrants additional scrutiny.",
)

INCIDENT_SEVERITY_2 = NcissDecisionPoint(
    name="Incident Severity",
    description="After an incident is scored, it is assigned a priority level. "
    "The six levels listed below are aligned with CISA, "
    "the Department of Homeland Security (DHS), "
    "and the CISS to help provide a common lexicon when discussing incidents. "
    "This priority assignment drives CISA urgency, "
    "pre-approved incident response offerings, "
    "reporting requirements, and recommendations for leadership escalation.",
    key="IS",
    version="2.0.0",
    values=(
        LEVEL_0_MINOR,
        LEVEL_0_NEGLIGIBLE,
        LEVEL_1_1,
        LEVEL_2_1,
        LEVEL_3_1,
        LEVEL_4_1,
        LEVEL_5_1,
    ),
)

VERSIONS = (INCIDENT_SEVERITY, INCIDENT_SEVERITY_2)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
