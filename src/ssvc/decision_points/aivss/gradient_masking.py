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
from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_points.helpers import print_versions_and_diffs

# Gradient Masking/Obfuscation
#
# 0.0: Gradients are completely hidden or formally proven to be unrecoverable.
# 0.1-0.3: Strong gradient masking techniques used (e.g., Shattered Gradients, Thermometer Encoding), making gradient-based attacks significantly more difficult.
# 0.4-0.6: Basic gradient obfuscation methods employed (e.g., adding noise), but gradients can still be partially recovered.
# 0.7-1.0: Gradients are easily accessible and interpretable, no masking techniques used.
# Examples:
# 0.0: Model uses homomorphic encryption or other methods to make gradients completely inaccessible.
# 0.2: Model uses advanced techniques like shattered gradients to make gradient-based attacks computationally expensive.
# 0.5: Some noise is added to gradients, but they still reveal information about the model.
# 0.9: Model's gradients can be easily calculated and visualized.

HIDDEN = DecisionPointValue(
    name="Hidden",
    key="H",
    description="Gradients are completely hidden or formally proven to be unrecoverable.",
)

STRONG = DecisionPointValue(
    name="Strong",
    key="S",
    description="Strong gradient masking techniques used, making gradient-based attacks significantly more difficult.",
)

BASIC = DecisionPointValue(
    name="Basic",
    key="B",
    description="Basic gradient obfuscation methods employed, but gradients can still be partially recovered.",
)

_NONE = DecisionPointValue(
    name="None",
    key="N",
    description="Gradients are easily accessible and interpretable, no masking techniques used.",
)

GRADIENT_MASKING = AivssDecisionPoint(
    name="Gradient Masking/Obfuscation",
    key="GM",
    version="1.0.0",
    description="Measures the effectiveness of gradient masking or obfuscation techniques used to protect against gradient-based attacks.",
    values=(HIDDEN, STRONG, BASIC, _NONE),
)

VERSIONS = [GRADIENT_MASKING]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
