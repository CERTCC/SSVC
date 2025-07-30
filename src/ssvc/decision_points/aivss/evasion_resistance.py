#!/usr/bin/env python
"""
Models the AIVSS Evasion Resistance decision point.
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

from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_points.helpers import print_versions_and_diffs

# Evasion Resistance
#
# 0.0: Formally verified robustness against a wide range of evasion attacks.
# 0.1-0.3: Robust to most known evasion attacks, multiple defense mechanisms employed (e.g., adversarial training, input sanitization, certified robustness).
# 0.4-0.6: Susceptible to some evasion attacks, basic adversarial training or input validation in place.
# 0.7-1.0: Highly susceptible to common evasion attacks (e.g., FGSM, PGD). No or minimal defenses.
# Examples:
# 0.0: Model's robustness proven through formal methods.
# 0.2: Model uses a combination of adversarial training, input filtering, and certified robustness techniques.
# 0.5: Model trained with adversarial examples, but still vulnerable to more sophisticated attacks.
# 0.8: Model easily fooled by adding small perturbations to input images.

VERIFIED = DecisionPointValue(
    name="Verified",
    key="V",
    description="Formally verified robustness against a wide range of evasion attacks.",
)

ROBUST = DecisionPointValue(
    name="Robust",
    key="R",
    description="Robust to most known evasion attacks, multiple defense mechanisms employed.",
)

SUSCEPTIBLE = DecisionPointValue(
    name="Susceptible",
    key="S",
    description="Susceptible to some evasion attacks, basic adversarial training or input validation in place.",
)

HIGHLY_SUSCEPTIBLE = DecisionPointValue(
    name="Highly Susceptible",
    key="HS",
    description="Highly susceptible to common evasion attacks. No or minimal defenses.",
)

EVASION_RESISTANCE = AivssDecisionPoint(
    name="Evasion Resistance",
    key="ER",
    version="1.0.0",
    description="Resistance to evasion attacks.",
    values=(VERIFIED, ROBUST, SUSCEPTIBLE, HIGHLY_SUSCEPTIBLE),
)

VERSIONS = [EVASION_RESISTANCE]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
