#!/usr/bin/env python
"""
Models the AIVSS Threat Intelligence Integration decision point.
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

# Threat Intelligence Integration
#
# 0.0: Proactive threat hunting based on threat intelligence, with automated analysis and correlation of threat data to identify and mitigate potential risks before they impact the system.
# 0.1-0.3: Threat intelligence feeds integrated into security monitoring and response systems, providing automated alerts and updates on emerging threats.
# 0.4-0.6: Basic threat intelligence used (e.g., manually reviewing threat reports), but not systematically integrated into security operations.
# 0.7-1.0: No integration with threat intelligence feeds or other sources of security information.
# Examples:
# 0.0: System uses threat intelligence to proactively identify and mitigate potential vulnerabilities.
# 0.2: System automatically ingests and analyzes threat intelligence feeds, generating alerts for relevant threats.
# 0.5: Security team occasionally reviews threat intelligence reports but takes no specific actions.
# 0.9: Security team is not aware of current threats to AI systems.

PROACTIVE_HUNTING = DecisionPointValue(
    name="Proactive Hunting",
    key="P",
    description="Proactive threat hunting based on threat intelligence, with automated analysis and correlation of threat data to identify and mitigate risks before impact.",
)

INTEGRATED_FEEDS = DecisionPointValue(
    name="Integrated Feeds",
    key="I",
    description="Threat intelligence feeds integrated into security monitoring and response systems, providing automated alerts and updates on emerging threats.",
)

BASIC_USE = DecisionPointValue(
    name="Basic Use",
    key="B",
    description="Basic threat intelligence used, but not systematically integrated into security operations.",
)

NONE = DecisionPointValue(
    name="None",
    key="N",
    description="No integration with threat intelligence feeds or other sources of security information.",
)

THREAT_INTELLIGENCE_INTEGRATION = AivssDecisionPoint(
    name="Threat Intelligence Integration",
    key="TI",
    version="1.0.0",
    description="Degree to which threat intelligence is integrated into security operations and risk mitigation.",
    values=(PROACTIVE_HUNTING, INTEGRATED_FEEDS, BASIC_USE, NONE),
)

VERSIONS = [THREAT_INTELLIGENCE_INTEGRATION]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
