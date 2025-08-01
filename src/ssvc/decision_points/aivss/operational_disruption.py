#!/usr/bin/env python
"""
Models the AIVSS Operational Disruption decision point.
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

# Operational Disruption
#
# 0.0: System designed for high availability and resilience, with real-time monitoring, automated recovery, and regular testing of failover mechanisms.
# 0.1-0.3: Robust operational controls, including redundancy, failover mechanisms, and a comprehensive business continuity and disaster recovery plan.
# 0.4-0.6: Some measures to mitigate operational risks (e.g., limited redundancy), but no comprehensive business continuity plan.
# 0.7-1.0: High risk of significant operational disruption due to system failures or attacks, no backup systems or recovery plans.
# Examples:
# 0.0: System is designed for 24/7 availability with multiple layers of redundancy and automated recovery.
# 0.2: System has a comprehensive business continuity plan that is regularly tested and updated.
# 0.5: System has some redundant components, but failover procedures are not regularly tested.
# 0.8: System failure could bring down critical business operations with no backup.

HIGH_AVAILABILITY = DecisionPointValue(
    name="High Availability",
    key="H",
    description="System designed for high availability and resilience, with real-time monitoring, automated recovery, and regular testing of failover mechanisms.",
)

ROBUST_CONTROLS = DecisionPointValue(
    name="Robust Controls",
    key="R",
    description="Robust operational controls, including redundancy, failover mechanisms, and a comprehensive business continuity and disaster recovery plan.",
)

SOME_MEASURES = DecisionPointValue(
    name="Some Measures",
    key="S",
    description="Some measures to mitigate operational risks, but no comprehensive business continuity plan.",
)

HIGH_RISK = DecisionPointValue(
    name="High Risk",
    key="HR",
    description="High risk of significant operational disruption due to system failures or attacks, no backup systems or recovery plans.",
)

OPERATIONAL_DISRUPTION = AivssDecisionPoint(
    name="Operational Disruption",
    key="OD",
    version="1.0.0",
    description="Degree to which the system is resilient to operational disruption and incorporates business continuity measures.",
    values=(HIGH_AVAILABILITY, ROBUST_CONTROLS, SOME_MEASURES, HIGH_RISK),
)

VERSIONS = [OPERATIONAL_DISRUPTION]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()

