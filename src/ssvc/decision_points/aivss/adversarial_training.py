#!/usr/bin/env python
"""
Models the AIVSS Adversarial Training decision point.
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

# Adversarial Training
#
# 0.0: Continuous adversarial training with evolving attack techniques, incorporating new attacks as they are discovered, and using formal verification methods to ensure robustness.
# 0.1-0.3: Robust adversarial training against a wide range of attacks (e.g., PGD, C&W) with larger perturbation budgets, using multiple techniques (e.g., ensemble adversarial training, certified defenses).
# 0.4-0.6: Basic adversarial training with a limited set of attack types (e.g., FGSM) and small perturbation budgets.
# 0.7-1.0: No adversarial training used during model development.
# Examples:
# 0.0: Model undergoes continuous adversarial training and is formally verified for robustness against specific attack models.
# 0.2: Model is trained using a combination of different adversarial training techniques and attack types.
# 0.5: Model is trained with FGSM-generated adversarial examples.
# 0.8: Model is not trained to be resistant to any adversarial examples.

CONTINUOUS = DecisionPointValue(
    name="Continuous Adversarial Training",
    key="C",
    description="Continuous adversarial training with evolving attack techniques, incorporating new attacks as they are discovered, and using formal verification methods to ensure robustness.",
)

ROBUST = DecisionPointValue(
    name="Robust Adversarial Training",
    key="R",
    description="Robust adversarial training against a wide range of attacks with larger perturbation budgets, using multiple techniques.",
)

BASIC = DecisionPointValue(
    name="Basic Adversarial Training",
    key="B",
    description="Basic adversarial training with a limited set of attack types and small perturbation budgets.",
)

NONE = DecisionPointValue(
    name="None",
    key="N",
    description="No adversarial training used during model development.",
)

ADVERSARIAL_TRAINING = AivssDecisionPoint(
    name="Adversarial Training",
    key="AT",
    version="1.0.0",
    description="Degree to which adversarial training is used to improve model robustness.",
    values=(CONTINUOUS, ROBUST, BASIC, NONE),
)

VERSIONS = [ADVERSARIAL_TRAINING]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()

