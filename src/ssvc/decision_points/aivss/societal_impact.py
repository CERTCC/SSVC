#!/usr/bin/env python
"""
Models the AIVSS Societal Impact decision point.
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

# Societal Impact
#
# 0.0: System designed to maximize positive societal impact and minimize negative consequences, with ongoing monitoring and engagement with affected communities.
# 0.1-0.3: Thorough societal impact assessment conducted, considering a wide range of stakeholders and potential harms, with mitigation strategies in place.
# 0.4-0.6: Some consideration of potential societal impacts, but no comprehensive assessment or proactive mitigation.
# 0.7-1.0: High risk of negative societal impacts (e.g., job displacement, manipulation, erosion of trust), no assessment or mitigation.
# Examples:
# 0.0: System is designed with a strong ethical framework, promoting fairness, transparency, and societal well-being.
# 0.2: A comprehensive societal impact assessment has been conducted, and mitigation strategies are in place.
# 0.5: Developers acknowledge potential negative impacts but have not taken concrete steps to address them.
# 0.8: System could be used for mass surveillance or to spread misinformation without any safeguards.

MAXIMIZED_POSITIVE_IMPACT = DecisionPointValue(
    name="Maximized Positive Impact",
    key="M",
    description="System designed to maximize positive societal impact and minimize negative consequences, with ongoing monitoring and engagement with affected communities.",
)

THOROUGH_ASSESSMENT = DecisionPointValue(
    name="Thorough Assessment",
    key="T",
    description="Thorough societal impact assessment conducted, considering a wide range of stakeholders and potential harms, with mitigation strategies in place.",
)

SOME_CONSIDERATION = DecisionPointValue(
    name="Some Consideration",
    key="S",
    description="Some consideration of potential societal impacts, but no comprehensive assessment or proactive mitigation.",
)

HIGH_RISK = DecisionPointValue(
    name="High Risk",
    key="H",
    description="High risk of negative societal impacts, no assessment or mitigation.",
)

SOCIETAL_IMPACT = AivssDecisionPoint(
    name="Societal Impact",
    key="SI",
    version="1.0.0",
    description="Degree to which the system's societal impact is assessed, monitored, and mitigated.",
    values=(
        MAXIMIZED_POSITIVE_IMPACT,
        THOROUGH_ASSESSMENT,
        SOME_CONSIDERATION,
        HIGH_RISK,
    ),
)

VERSIONS = [SOCIETAL_IMPACT]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
