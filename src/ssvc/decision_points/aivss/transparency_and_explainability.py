#!/usr/bin/env python
"""
Models the AIVSS Transparency and Explainability decision point.
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

# Transparency and Explainability
#
# 0.0: System's decision-making process is fully transparent and formally explainable, with clear causal relationships established.
# 0.1-0.3: Highly explainable, system uses inherently interpretable models (e.g., decision trees) or provides reliable and comprehensive explanations for all decisions.
# 0.4-0.6: Limited explainability, some post-hoc explanations (e.g., LIME, SHAP) can be generated, but they may not be reliable or comprehensive.
# 0.7-1.0: Black-box system, no insight into decision-making process.
# Examples:
# 0.0: System's logic is fully transparent and can be formally verified.
# 0.2: System uses an interpretable model or provides detailed and reliable explanations for each decision.
# 0.5: Post-hoc explanations can be generated, but they are not always accurate or complete.
# 0.8: No explanation provided for the system's decisions.

FULLY_TRANSPARENT = DecisionPointValue(
    name="Fully Transparent",
    key="F",
    description="System's decision-making process is fully transparent and formally explainable, with clear causal relationships established.",
)

HIGHLY_EXPLAINABLE = DecisionPointValue(
    name="Highly Explainable",
    key="H",
    description="Highly explainable, system uses inherently interpretable models or provides reliable and comprehensive explanations for all decisions.",
)

LIMITED_EXPLAINABILITY = DecisionPointValue(
    name="Limited Explainability",
    key="L",
    description="Limited explainability, some post-hoc explanations can be generated, but they may not be reliable or comprehensive.",
)

BLACK_BOX = DecisionPointValue(
    name="Black Box",
    key="B",
    description="Black-box system, no insight into decision-making process.",
)

TRANSPARENCY_AND_EXPLAINABILITY = AivssDecisionPoint(
    name="Transparency and Explainability",
    key="TE",
    version="1.0.0",
    description="Degree to which the system's decision-making process is transparent and explainable.",
    values=(FULLY_TRANSPARENT, HIGHLY_EXPLAINABLE, LIMITED_EXPLAINABILITY, BLACK_BOX),
)

VERSIONS = [TRANSPARENCY_AND_EXPLAINABILITY]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
