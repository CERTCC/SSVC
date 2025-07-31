#!/usr/bin/env python
"""
Models the AIVSS Membership Inference decision point.
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

# Membership Inference
#
# 0.0: Model provably resistant to membership inference attacks, with formal guarantees on the privacy of individual training data points.
# 0.1-0.3: Strong defenses against membership inference, such as differential privacy or model stacking, significantly reducing the attacker's ability to infer membership.
# 0.4-0.6: Some measures to mitigate membership inference (e.g., regularization, dropout), but significant risks remain.
# 0.7-1.0: High risk of membership inference attacks, attackers can easily determine whether a specific data point was used in the model's training set.
# Examples:
# 0.0: Model is formally proven to be resistant to membership inference under specific attack models.
# 0.2: Model is trained with differential privacy, providing strong protection against membership inference.
# 0.5: Model uses regularization techniques that may reduce the risk of membership inference, but no formal guarantees.
# 0.9: An attacker can easily determine if a particular individual's data was used to train the model.

PROVABLY_RESISTANT = DecisionPointValue(
    name="Provably Resistant",
    key="P",
    description="Model provably resistant to membership inference attacks, with formal guarantees on the privacy of individual training data points.",
)

STRONG_DEFENSES = DecisionPointValue(
    name="Strong Defenses",
    key="S",
    description="Strong defenses against membership inference, such as differential privacy or model stacking, significantly reducing the attacker's ability to infer membership.",
)

SOME_MITIGATION = DecisionPointValue(
    name="Some Mitigation",
    key="M",
    description="Some measures to mitigate membership inference (e.g., regularization, dropout), but significant risks remain.",
)

HIGH_RISK = DecisionPointValue(
    name="High Risk",
    key="H",
    description="High risk of membership inference attacks, attackers can easily determine whether a specific data point was used in the model's training set.",
)

MEMBERSHIP_INFERENCE = AivssDecisionPoint(
    name="Membership Inference",
    key="MINF",
    version="1.0.0",
    description="Degree to which the model is resistant to membership inference attacks and protects the privacy of individual training data points.",
    values=(PROVABLY_RESISTANT, STRONG_DEFENSES, SOME_MITIGATION, HIGH_RISK),
)

VERSIONS = [MEMBERSHIP_INFERENCE]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
