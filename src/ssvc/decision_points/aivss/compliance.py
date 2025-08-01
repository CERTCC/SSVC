#!/usr/bin/env python
"""
Models the AIVSS Compliance decision point.
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

# Compliance
#
# 0.0: System exceeds regulatory requirements and sets industry best practices for compliance, with a proactive approach to adapting to new regulations.
# 0.1-0.3: Full compliance with relevant regulations and industry standards, with a dedicated compliance team and regular audits.
# 0.4-0.6: Basic understanding of regulations, some ad-hoc compliance efforts, but no formal compliance program.
# 0.7-1.0: No awareness of or compliance with relevant regulations (e.g., GDPR, CCPA, HIPAA) or industry standards.
# Examples:
# 0.0: System is designed to be compliant by design, exceeding regulatory requirements and setting industry best practices.
# 0.2: System is fully compliant with all applicable regulations, with regular audits and a dedicated compliance team.
# 0.5: Some efforts are made to comply with regulations, but there are significant gaps and no formal compliance program.
# 0.8: System collects and processes personal data without user consent or proper safeguards, violating data privacy regulations.

EXCEEDS_REQUIREMENTS = DecisionPointValue(
    name="Exceeds Requirements",
    key="E",
    description="System exceeds regulatory requirements and sets industry best practices for compliance, with a proactive approach to adapting to new regulations.",
)

FULL_COMPLIANCE = DecisionPointValue(
    name="Full Compliance",
    key="F",
    description="Full compliance with relevant regulations and industry standards, with a dedicated compliance team and regular audits.",
)

BASIC_UNDERSTANDING = DecisionPointValue(
    name="Basic Understanding",
    key="B",
    description="Basic understanding of regulations, some ad-hoc compliance efforts, but no formal compliance program.",
)

NONE = DecisionPointValue(
    name="None",
    key="N",
    description="No awareness of or compliance with relevant regulations or industry standards.",
)

COMPLIANCE = AivssDecisionPoint(
    name="Compliance",
    key="CO",
    version="1.0.0",
    description="Degree to which the system complies with relevant regulations and industry standards.",
    values=(EXCEEDS_REQUIREMENTS, FULL_COMPLIANCE, BASIC_UNDERSTANDING, NONE),
)

VERSIONS = [COMPLIANCE]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()

