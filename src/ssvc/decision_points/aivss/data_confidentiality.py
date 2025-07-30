#!/usr/bin/env python
"""
Models the AIVSS Data Confidentiality decision point.
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

# Data Confidentiality
#
# 0.0: Data fully anonymized using techniques like differential privacy or homomorphic encryption.
# 0.1-0.3: Strong encryption (e.g., AES-256) used for data at rest and in transit, strict access controls and key management practices in place.
# 0.4-0.6: Sensitive data with basic access controls (e.g., passwords), but no encryption.
# 0.7-1.0: Highly sensitive data (e.g., PII, financial data) stored or processed with no or minimal protection.
# Examples:
# 0.0: Data is fully anonymized and provably unlinkable to individuals.
# 0.2: Data encrypted at rest and in transit, with strict access controls and key rotation policies.
# 0.5: Data access restricted by user roles, but data is stored in plain text.
# 0.9: Training data includes unencrypted PII accessible to all developers.

from ssvc.decision_points.aivss.base import AivssDecisionPoint
from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_points.helpers import print_versions_and_diffs

FULLY_ANONYMIZED = DecisionPointValue(
    name="Fully Anonymized",
    key="A",
    description="Data fully anonymized using techniques like differential privacy or homomorphic encryption.",
)

STRONG_ENCRYPTION = DecisionPointValue(
    name="Strong Encryption",
    key="E",
    description="Strong encryption (e.g., AES-256) used for data at rest and in transit, strict access controls and key management practices in place.",
)
BASIC_ACCESS_CONTROLS = DecisionPointValue(
    name="Basic Access Controls",
    key="B",
    description="Sensitive data with basic access controls (e.g., passwords), but no encryption.",
)
MINIMAL_PROTECTION = DecisionPointValue(
    name="Minimal Protection",
    key="M",
    description="Highly sensitive data (e.g., PII, financial data) stored or processed with no or minimal protection.",
)

DATA_CONFIDENTIALITY = AivssDecisionPoint(
    name="Data Confidentiality",
    key="DC",
    version="1.0.0",
    description="Measures taken to protect the confidentiality of data used in training and inference.",
    values=[
        FULLY_ANONYMIZED,
        STRONG_ENCRYPTION,
        BASIC_ACCESS_CONTROLS,
        MINIMAL_PROTECTION,
    ],
)

VERSIONS = (DATA_CONFIDENTIALITY,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
