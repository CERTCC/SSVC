#!/usr/bin/env python
"""
Provides probability-based decision points for SSVC
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

from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_points.basic.base import BasicDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs

# based on https://www.cisecurity.org/ms-isac/services/words-of-estimative-probability-analytic-confidences-and-structured-analytic-techniques
ALMOST_NO_CHANCE = DecisionPointValue(
    name="Almost No Chance",
    key="ANC",
    definition="Probability < 0.05. Almost no chance, remote",
)

VERY_UNLIKELY = DecisionPointValue(
    name="Very Unlikely",
    key="VU",
    definition="0.05 <= Probability < 0.20. Very unlikely, highly improbable.",
)

UNLIKELY = DecisionPointValue(
    name="Unlikely",
    key="U",
    definition="0.20 <= Probability < 0.45. Unlikely, improbable.",
)

ROUGHLY_EVEN_CHANCE = DecisionPointValue(
    name="Roughly Even Chance",
    key="REC",
    definition="0.45 <= Probability < 0.55. Roughly even chance, roughly even odds.",
)

LIKELY = DecisionPointValue(
    name="Likely",
    key="L",
    definition="0.55 <= Probability < 0.80. Likely, probable.",
)

VERY_LIKELY = DecisionPointValue(
    name="Very Likely",
    key="VL",
    definition="0.80 <= Probability < 0.95. Very likely, highly probable.",
)

ALMOST_CERTAIN = DecisionPointValue(
    name="Almost Certain",
    key="AC",
    definition="0.95 <= Probability. Almost certain, nearly certain.",
)

CIS_CTI_WEP = BasicDecisionPoint(
    key="CIS_WEP",
    version="1.0.0",
    name="CIS-CTI Words of Estimative Probability",
    definition="A scale for expressing the likelihood of an event or outcome.",
    values=(
        ALMOST_NO_CHANCE,
        VERY_UNLIKELY,
        UNLIKELY,
        ROUGHLY_EVEN_CHANCE,
        LIKELY,
        VERY_LIKELY,
        ALMOST_CERTAIN,
    ),
)

VERSIONS = [
    CIS_CTI_WEP,
]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
