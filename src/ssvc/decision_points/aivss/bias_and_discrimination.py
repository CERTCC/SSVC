#!/usr/bin/env python
"""
Models the AIVSS Bias and Discrimination decision point.
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

# Bias and Discrimination
#
# 0.0: System demonstrably fair and unbiased across different groups, with ongoing monitoring and auditing for bias.
# 0.1-0.3: Rigorous fairness testing using multiple metrics (e.g., equal opportunity, predictive rate parity) and bias mitigation techniques applied (e.g., re-weighting, adversarial debiasing).
# 0.4-0.6: Some awareness of potential bias, basic fairness metrics (e.g., demographic parity) monitored, but no active mitigation.
# 0.7-1.0: High risk of discriminatory outcomes, no bias detection or mitigation methods used.
# Examples:
# 0.0: System's fairness is formally verified and continuously monitored.
# 0.2: System is trained using techniques like adversarial debiasing and regularly audited for fairness.
# 0.5: Fairness metrics are monitored, but no actions are taken to address identified biases.
# 0.9: System consistently produces biased outputs against certain demographic groups.

FAIR_AND_UNBIASED = DecisionPointValue(
    name="Fair and Unbiased",
    key="F",
    description="System demonstrably fair and unbiased across different groups, with ongoing monitoring and auditing for bias.",
)

RIGOROUS_TESTING = DecisionPointValue(
    name="Rigorous Testing",
    key="R",
    description="Rigorous fairness testing using multiple metrics and bias mitigation techniques applied.",
)

AWARENESS = DecisionPointValue(
    name="Awareness",
    key="A",
    description="Some awareness of potential bias, basic fairness metrics monitored, but no active mitigation.",
)

HIGH_RISK = DecisionPointValue(
    name="High Risk",
    key="H",
    description="High risk of discriminatory outcomes, no bias detection or mitigation methods used.",
)

BIAS_AND_DISCRIMINATION = AivssDecisionPoint(
    name="Bias and Discrimination",
    key="BD",
    version="1.0.0",
    description="Degree to which the system is fair and unbiased, and the extent of bias monitoring and mitigation.",
    values=(FAIR_AND_UNBIASED, RIGOROUS_TESTING, AWARENESS, HIGH_RISK),
)

VERSIONS = [BIAS_AND_DISCRIMINATION]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()

