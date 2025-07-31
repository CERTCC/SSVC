#!/usr/bin/env python
"""
Models the AIVSS Retraining Capabilities decision point.
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

# Retraining Capabilities
#
# 0.0: Continuous and automated retraining triggered by performance degradation, concept drift, or the availability of new data, with minimal human intervention.
# 0.1-0.3: Automated retraining pipeline in place, allowing for regular updates with new data and model improvements.
# 0.4-0.6: Manual retraining possible, but infrequent and time-consuming, with limited automation.
# 0.7-1.0: No capability to retrain the model, or retraining requires significant manual effort and downtime.
# Examples:
# 0.0: Model continuously learns and adapts to new data and changing conditions.
# 0.2: Model is automatically retrained on a regular schedule using an automated pipeline.
# 0.5: Model can be retrained manually, but it requires significant effort and downtime.
# 0.8: Model cannot be updated without rebuilding it from scratch.

CONTINUOUS_AUTOMATED = DecisionPointValue(
    name="Continuous Automated Retraining",
    key="C",
    description="Continuous and automated retraining triggered by performance degradation, concept drift, or new data, with minimal human intervention.",
)

AUTOMATED_PIPELINE = DecisionPointValue(
    name="Automated Pipeline",
    key="A",
    description="Automated retraining pipeline in place, allowing for regular updates with new data and model improvements.",
)

MANUAL = DecisionPointValue(
    name="Manual Retraining",
    key="M",
    description="Manual retraining possible, but infrequent and time-consuming, with limited automation.",
)

NONE = DecisionPointValue(
    name="None",
    key="N",
    description="No capability to retrain the model, or retraining requires significant manual effort and downtime.",
)

RETRAINING_CAPABILITIES = AivssDecisionPoint(
    name="Retraining Capabilities",
    key="RE",
    version="1.0.0",
    description="Degree to which the system supports retraining and adaptation to new data or conditions.",
    values=(CONTINUOUS_AUTOMATED, AUTOMATED_PIPELINE, MANUAL, NONE),
)

VERSIONS = [RETRAINING_CAPABILITIES]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
