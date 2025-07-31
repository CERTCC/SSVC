#!/usr/bin/env python
"""
Models the AIVSS Reputational Damage decision point.
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

from ssvc.decision_points.aivss.base import AivssDecisionPoint
from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_points.helpers import print_versions_and_diffs

# Reputational Damage
#
# 0.0: System designed to minimize reputational risks, with ongoing monitoring of public perception, proactive engagement with stakeholders, and a robust crisis management plan.
# 0.1-0.3: Reputational risk assessment conducted, considering various scenarios and stakeholders, with communication plans and mitigation strategies in place.
# 0.4-0.6: Some awareness of reputational risks, limited monitoring of public perception, but no proactive measures to address negative publicity.
# 0.7-1.0: High risk of severe reputational damage due to system errors, biases, or security breaches, no mitigation strategies.
# Examples:
# 0.0: System is designed to be transparent and ethical, minimizing the risk of reputational damage, and the company has a strong track record of responsible AI practices.
# 0.2: A reputational risk assessment has been conducted, and a crisis communication plan is in place.
# 0.5: Company monitors social media for negative comments but has no plan to address them.
# 0.9: System errors or biases could lead to widespread public criticism and loss of trust.

MINIMIZED_RISK = DecisionPointValue(
    name="Minimized Risk",
    key="M",
    description="System designed to minimize reputational risks, with ongoing monitoring, stakeholder engagement, and a crisis management plan.",
)

RISK_ASSESSMENT = DecisionPointValue(
    name="Risk Assessment",
    key="R",
    description="Reputational risk assessment conducted, with communication plans and mitigation strategies in place.",
)

AWARENESS = DecisionPointValue(
    name="Awareness",
    key="A",
    description="Some awareness of reputational risks, limited monitoring of public perception, but no proactive measures.",
)

HIGH_RISK = DecisionPointValue(
    name="High Risk",
    key="H",
    description="High risk of severe reputational damage due to system errors, biases, or security breaches, no mitigation strategies.",
)

REPUTATIONAL_DAMAGE = AivssDecisionPoint(
    name="Reputational Damage",
    key="RD",
    version="1.0.0",
    description="Degree to which the system and organization mitigate reputational risks and manage public perception.",
    values=(MINIMIZED_RISK, RISK_ASSESSMENT, AWARENESS, HIGH_RISK),
)

VERSIONS = [REPUTATIONAL_DAMAGE]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
