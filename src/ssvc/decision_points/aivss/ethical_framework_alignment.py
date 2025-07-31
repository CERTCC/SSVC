#!/usr/bin/env python
"""
Models the AIVSS Ethical Framework Alignment decision point.
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

# Ethical Framework Alignment
#
# 0.0: System demonstrably adheres to and promotes ethical AI principles, with ongoing monitoring and auditing of ethical performance.
# 0.1-0.3: System design and operation align with established ethical frameworks (e.g., OECD AI Principles, Montreal Declaration for Responsible AI), with mechanisms for addressing ethical concerns.
# 0.4-0.6: Basic awareness of ethical guidelines, limited implementation, no formal ethical review process.
# 0.7-1.0: No consideration of ethical frameworks or principles in the design, development, or deployment of the AI system.
# Examples:
# 0.0: System's ethical performance is regularly assessed, and it actively promotes ethical AI principles.
# 0.2: System design incorporates principles from relevant ethical frameworks, and there is a process for addressing ethical concerns.
# 0.5: Developers are aware of ethical guidelines but have not formally integrated them into the system's design.
# 0.8: System is developed and deployed without any consideration for ethical implications.

PROMOTES_ETHICS = DecisionPointValue(
    name="Promotes Ethics",
    key="P",
    description="System demonstrably adheres to and promotes ethical AI principles, with ongoing monitoring and auditing of ethical performance.",
)

ALIGNS_WITH_FRAMEWORKS = DecisionPointValue(
    name="Aligns with Frameworks",
    key="A",
    description="System design and operation align with established ethical frameworks, with mechanisms for addressing ethical concerns.",
)

AWARENESS = DecisionPointValue(
    name="Awareness",
    key="W",
    description="Basic awareness of ethical guidelines, limited implementation, no formal ethical review process.",
)

NONE = DecisionPointValue(
    name="None",
    key="N",
    description="No consideration of ethical frameworks or principles in the design, development, or deployment of the AI system.",
)

ETHICAL_FRAMEWORK_ALIGNMENT = AivssDecisionPoint(
    name="Ethical Framework Alignment",
    key="EF",
    version="1.0.0",
    description="Degree to which the system aligns with and promotes ethical AI principles and frameworks.",
    values=(PROMOTES_ETHICS, ALIGNS_WITH_FRAMEWORKS, AWARENESS, NONE),
)

VERSIONS = [ETHICAL_FRAMEWORK_ALIGNMENT]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
