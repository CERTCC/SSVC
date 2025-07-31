#!/usr/bin/env python
"""
Models the AIVSS Operations decision point.
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

# Operations
#
# 0.0: Continuous security monitoring with automated incident response capabilities, regular security audits, and a dedicated security operations center (SOC).
# 0.1-0.3: Comprehensive security monitoring using a SIEM system, automated alerts for suspicious activity, and a well-defined incident response plan that is regularly tested.
# 0.4-0.6: Basic security monitoring (e.g., manually reviewing logs), limited incident response capabilities, no formal incident response plan.
# 0.7-1.0: No security monitoring or incident response plan, system logs not collected or analyzed.
# Examples:
# 0.0: A dedicated SOC monitors the system 24/7, with automated incident response capabilities and regular security audits.
# 0.2: A SIEM system is used to monitor security events, generate alerts, and trigger incident response procedures.
# 0.5: System logs are collected and manually reviewed on a weekly basis, and there is a basic incident response plan.
# 0.8: No logs are collected, and there is no process for responding to security incidents.

CONTINUOUS_MONITORING = DecisionPointValue(
    name="Continuous Monitoring",
    key="C",
    description="Continuous security monitoring with automated incident response, regular security audits, and a dedicated SOC.",
)

COMPREHENSIVE_MONITORING = DecisionPointValue(
    name="Comprehensive Monitoring",
    key="M",
    description="Comprehensive security monitoring using a SIEM system, automated alerts, and a well-defined, regularly tested incident response plan.",
)

BASIC_MONITORING = DecisionPointValue(
    name="Basic Monitoring",
    key="B",
    description="Basic security monitoring, limited incident response capabilities, no formal incident response plan.",
)

NONE = DecisionPointValue(
    name="None",
    key="N",
    description="No security monitoring or incident response plan, system logs not collected or analyzed.",
)

OPERATIONS = AivssDecisionPoint(
    name="Operations",
    key="OP",
    version="1.0.0",
    description="Degree to which security monitoring and incident response are implemented in operations.",
    values=(CONTINUOUS_MONITORING, COMPREHENSIVE_MONITORING, BASIC_MONITORING, NONE),
)

VERSIONS = [OPERATIONS]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
