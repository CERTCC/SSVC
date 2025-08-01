#!/usr/bin/env python
"""
Models the AIVSS Model Inversion decision point.
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

# Model Inversion
#
# 0.0: Model provably resistant to model inversion attacks, with formal guarantees on the privacy of the training data.
# 0.1-0.3: Strong defenses against model inversion, such as differential privacy or data sanitization techniques, significantly increasing the difficulty of reconstructing training data.
# 0.4-0.6: Some measures to mitigate model inversion (e.g., limiting model output precision), but significant risks remain.
# 0.7-1.0: High risk of model inversion attacks, sensitive training data can be easily reconstructed from model outputs or gradients.
# Examples:
# 0.0: Model is formally proven to be resistant to model inversion under specific attack models.
# 0.2: Model is trained with differential privacy, providing strong guarantees against model inversion.
# 0.5: Model's output is rounded or perturbed to make inversion more difficult, but some information may still be leaked.
# 0.9: An attacker can easily reconstruct faces or other sensitive data from the model's outputs

PROVABLY_RESISTANT = DecisionPointValue(
    name="Provably Resistant",
    key="P",
    description="Model provably resistant to model inversion attacks, with formal guarantees on the privacy of the training data.",
)

STRONG_DEFENSES = DecisionPointValue(
    name="Strong Defenses",
    key="S",
    description="Strong defenses against model inversion, such as differential privacy or data sanitization techniques, significantly increasing the difficulty of reconstructing training data.",
)

SOME_MITIGATION = DecisionPointValue(
    name="Some Mitigation",
    key="M",
    description="Some measures to mitigate model inversion (e.g., limiting model output precision), but significant risks remain.",
)

HIGH_RISK = DecisionPointValue(
    name="High Risk",
    key="H",
    description="High risk of model inversion attacks, sensitive training data can be easily reconstructed from model outputs or gradients.",
)

MODEL_INVERSION = AivssDecisionPoint(
    name="Model Inversion",
    key="MI",
    version="1.0.0",
    description="Degree to which the model is resistant to model inversion attacks and protects the privacy of training data.",
    values=(PROVABLY_RESISTANT, STRONG_DEFENSES, SOME_MITIGATION, HIGH_RISK),
)

VERSIONS = [MODEL_INVERSION]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()

