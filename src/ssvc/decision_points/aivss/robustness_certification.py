#!/usr/bin/env python
"""
Models the AIVSS Robustness Certification decision point.
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

# Robustness Certification
#
# 0.0: Formal robustness certification obtained from a reputable third-party organization.
# 0.1-0.3: Rigorous robustness testing against a wide range of attacks and using multiple metrics (e.g., CLEVER, Robustness Gym).
# 0.4-0.6: Basic robustness testing against a limited set of attacks or using simple metrics.
# 0.7-1.0: No robustness testing performed.
# Examples:
# 0.0: Model certified by a recognized certification body for robustness against specific attack types.
# 0.2: Model evaluated using a comprehensive robustness testing framework like Robustness Gym.
# 0.5: Model tested against FGSM attacks with a limited range of perturbation budgets.
# 0.8: No testing for robustness against adversarial examples.

FORMAL = DecisionPointValue(
    name="Formal",
    key="F",
    description="Formal robustness certification obtained from a reputable third-party organization.",
)

RIGOROUS = DecisionPointValue(
    name="Rigorous",
    key="R",
    description="Rigorous robustness testing against a wide range of attacks and using multiple metrics.",
)

BASIC = DecisionPointValue(
    name="Basic",
    key="B",
    description="Basic robustness testing against a limited set of attacks or using simple metrics.",
)

_NONE = DecisionPointValue(
    name="None",
    key="N",
    description="No robustness testing performed.",
)

ROBUSTNESS_CERTIFICATION = AivssDecisionPoint(
    name="Robustness Certification",
    key="RC",
    version="1.0.0",
    description="Degree to which the model's robustness has been certified or tested, from 0.0 (formally certified) to 1.0 (no testing performed).",
    values=(FORMAL, RIGOROUS, BASIC, _NONE),
)

VERSIONS = [ROBUSTNESS_CERTIFICATION]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
