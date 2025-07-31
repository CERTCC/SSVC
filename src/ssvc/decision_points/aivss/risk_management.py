#!/usr/bin/env python
"""
Models the AIVSS Risk Management decision point.
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

# Risk Management
#
# 0.0: Proactive and continuous AI risk management, with a dedicated AI risk management team, regular risk assessments, and a strong focus on anticipating and mitigating emerging AI risks.
# 0.1-0.3: Comprehensive AI risk management framework in place, with specific processes for identifying, assessing, mitigating, and monitoring AI risks, fully integrated into the organizational risk framework.
# 0.4-0.6: Basic risk assessment for AI systems, limited mitigation strategies, AI risks partially integrated into the organizational risk framework.
# 0.7-1.0: No AI-specific risk management processes, AI risks not considered in the overall organizational risk framework.
# Examples:
# 0.0: AI risk management is a continuous process, integrated with the organization's overall risk management and governance structures.
# 0.2: A comprehensive AI risk management framework is in place, with regular risk assessments and mitigation plans.
# 0.5: AI risks are assessed on an ad-hoc basis, with limited mitigation strategies.
# 0.8: AI risks are not considered in the organization's risk management processes.

PROACTIVE_CONTINUOUS = DecisionPointValue(
    name="Proactive and Continuous",
    key="P",
    description="Proactive and continuous AI risk management, with a dedicated AI risk management team, regular risk assessments, and a strong focus on anticipating and mitigating emerging AI risks.",
)

COMPREHENSIVE_FRAMEWORK = DecisionPointValue(
    name="Comprehensive Framework",
    key="C",
    description="Comprehensive AI risk management framework in place, with specific processes for identifying, assessing, mitigating, and monitoring AI risks, fully integrated into the organizational risk framework.",
)

BASIC_ASSESSMENT = DecisionPointValue(
    name="Basic Assessment",
    key="B",
    description="Basic risk assessment for AI systems, limited mitigation strategies, AI risks partially integrated into the organizational risk framework.",
)

NONE = DecisionPointValue(
    name="None",
    key="N",
    description="No AI-specific risk management processes, AI risks not considered in the overall organizational risk framework.",
)

RISK_MANAGEMENT = AivssDecisionPoint(
    name="Risk Management",
    key="RM",
    version="1.0.0",
    description="Degree to which AI risk management is implemented and integrated into the organization's risk framework.",
    values=(PROACTIVE_CONTINUOUS, COMPREHENSIVE_FRAMEWORK, BASIC_ASSESSMENT, NONE),
)

VERSIONS = [RISK_MANAGEMENT]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
