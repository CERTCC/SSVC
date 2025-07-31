#!/usr/bin/env python
"""
Models the AIVSS Continuous Monitoring decision point.
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

# Continuous Monitoring
#
# 0.0: Real-time monitoring with automated response to detected threats, including dynamic model adaptation and rollback capabilities.
# 0.1-0.3: Comprehensive monitoring of system inputs, outputs, and internal states, with anomaly detection algorithms and automated alerts for suspicious activity.
# 0.4-0.6: Basic monitoring in place (e.g., logging system outputs), but limited analysis and no automated alerts.
# 0.7-1.0: No monitoring for adversarial attacks, anomalies, or performance degradation.
# Examples:
# 0.0: System has real-time intrusion detection and automated response capabilities.
# 0.2: System uses a SIEM system to monitor for anomalies and generate alerts.
# 0.5: System logs are stored but only analyzed manually on a periodic basis.
# 0.9: No logs are collected, and no monitoring is performed.

REAL_TIME_AUTOMATION = DecisionPointValue(
    name="Real-Time Automation",
    key="R",
    description="Real-time monitoring with automated response to detected threats, including dynamic model adaptation and rollback capabilities.",
)

COMPREHENSIVE_MONITORING = DecisionPointValue(
    name="Comprehensive Monitoring",
    key="C",
    description="Comprehensive monitoring of system inputs, outputs, and internal states, with anomaly detection algorithms and automated alerts for suspicious activity.",
)

BASIC_MONITORING = DecisionPointValue(
    name="Basic Monitoring",
    key="B",
    description="Basic monitoring in place, but limited analysis and no automated alerts.",
)

NONE = DecisionPointValue(
    name="None",
    key="N",
    description="No monitoring for adversarial attacks, anomalies, or performance degradation.",
)

CONTINUOUS_MONITORING = AivssDecisionPoint(
    name="Continuous Monitoring",
    key="CM",
    version="1.0.0",
    description="Degree to which the system is continuously monitored for threats, anomalies, and performance degradation.",
    values=(REAL_TIME_AUTOMATION, COMPREHENSIVE_MONITORING, BASIC_MONITORING, NONE),
)

VERSIONS = [CONTINUOUS_MONITORING]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
