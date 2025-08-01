#!/usr/bin/env python
"""
Models the AIVSS Accountability decision point.
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

# Accountability
#
# 0.0: Full accountability with mechanisms for redress, remediation, and independent oversight.
# 0.1-0.3: Clear accountability framework in place, with defined roles, responsibilities, and processes for addressing errors and disputes.
# 0.4-0.6: Some responsibility assigned to developers or operators, but no formal accountability framework.
# 0.7-1.0: No clear lines of accountability for system's actions or errors.
# Examples:
# 0.0: System has a formal accountability framework with mechanisms for independent audits and public reporting.
# 0.2: Clear roles and responsibilities defined for development, deployment, and operation, with an incident response plan.
# 0.5: Development team is generally responsible, but there are no clear procedures for handling errors.
# 0.9: Unclear who is responsible when the system makes a mistake.

FULL_ACCOUNTABILITY = DecisionPointValue(
    name="Full Accountability",
    key="F",
    description="Full accountability with mechanisms for redress, remediation, and independent oversight.",
)

FRAMEWORK = DecisionPointValue(
    name="Accountability Framework",
    key="A",
    description="Clear accountability framework in place, with defined roles, responsibilities, and processes for addressing errors and disputes.",
)

SOME_RESPONSIBILITY = DecisionPointValue(
    name="Some Responsibility",
    key="S",
    description="Some responsibility assigned to developers or operators, but no formal accountability framework.",
)

NONE = DecisionPointValue(
    name="None",
    key="N",
    description="No clear lines of accountability for system's actions or errors.",
)

ACCOUNTABILITY = AivssDecisionPoint(
    name="Accountability",
    key="AC",
    version="1.0.0",
    description="Degree to which accountability is established for the system's actions, errors, and outcomes.",
    values=(FULL_ACCOUNTABILITY, FRAMEWORK, SOME_RESPONSIBILITY, NONE),
)

VERSIONS = [ACCOUNTABILITY]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()

