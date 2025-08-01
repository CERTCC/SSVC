#!/usr/bin/env python
"""
Models the AIVSS Model Extraction decision point.
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

# Model Extraction
#
# 0.0: Model provably resistant to model extraction, with formal guarantees on the difficulty of creating a functional copy.
# 0.1-0.3: Strong defenses against model extraction, such as anomaly detection on API queries, model watermarking, and legal agreements with users, making it significantly more difficult and costly to steal the model.
# 0.4-0.6: Some measures to mitigate model extraction (e.g., rate limiting, watermarking), but a determined attacker can still succeed.
# 0.7-1.0: High risk of model extraction, attackers can easily create a functional copy of the model by querying its API.
# Examples:
# 0.0: Model is designed to be resistant to model extraction, and its functionality cannot be replicated through black-box queries.
# 0.2: Model uses watermarking and anomaly detection to detect and prevent extraction attempts.
# 0.5: API access is rate-limited, but an attacker can still extract the model over a longer period.
# 0.8: An attacker can create a copy of the model by making a large number of API calls.

PROVABLY_RESISTANT = DecisionPointValue(
    name="Provably Resistant",
    key="P",
    description="Model provably resistant to model extraction, with formal guarantees on the difficulty of creating a functional copy.",
)

STRONG_DEFENSES = DecisionPointValue(
    name="Strong Defenses",
    key="S",
    description="Strong defenses against model extraction, such as anomaly detection on API queries, model watermarking, and legal agreements with users, making it significantly more difficult and costly to steal the model.",
)

SOME_MITIGATION = DecisionPointValue(
    name="Some Mitigation",
    key="M",
    description="Some measures to mitigate model extraction (e.g., rate limiting, watermarking), but a determined attacker can still succeed.",
)

HIGH_RISK = DecisionPointValue(
    name="High Risk",
    key="H",
    description="High risk of model extraction, attackers can easily create a functional copy of the model by querying its API.",
)

MODEL_EXTRACTION = AivssDecisionPoint(
    name="Model Extraction",
    key="ME",
    version="1.0.0",
    description="Degree to which the model is resistant to model extraction attacks and the difficulty of replicating its functionality.",
    values=(PROVABLY_RESISTANT, STRONG_DEFENSES, SOME_MITIGATION, HIGH_RISK),
)

VERSIONS = [MODEL_EXTRACTION]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()

