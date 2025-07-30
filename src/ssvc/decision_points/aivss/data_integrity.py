#!/usr/bin/env python
"""
Models the AIVSS Data Integrity decision point.
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

# Data Integrity
#
# 0.0: Data integrity formally verified using techniques like blockchain or Merkle trees.
# 0.1-0.3: Strong integrity checks (e.g., digital signatures, cryptographic hashes) and tamper detection mechanisms in place.
# 0.4-0.6: Basic integrity checks (e.g., checksums) used, but no tamper-proof mechanisms.
# 0.7-1.0: No data integrity checks, data can be easily modified without detection.
# Examples:
# 0.0: Data is stored on a blockchain, ensuring immutability and tamper-proof integrity.
# 0.2: Data is digitally signed, and any modification is detected and alerted.
# 0.5: Checksums used to verify data integrity upon access.
# 0.8: Data can be altered without any detection.

FORMALLY_VERIFIED = DecisionPointValue(
    name="Formally Verified",
    key="F",
    description="Data integrity formally verified using techniques like blockchain or Merkle trees.",
)

STRONG_CHECKS = DecisionPointValue(
    name="Strong Checks",
    key="S",
    description="Strong integrity checks and tamper detection mechanisms in place.",
)

BASIC_CHECKS = DecisionPointValue(
    name="Basic Checks",
    key="B",
    description="Basic integrity checks used, but no tamper-proof mechanisms.",
)

_NONE = DecisionPointValue(
    name="None",
    key="N",
    description="No data integrity checks, data can be easily modified without detection.",
)

DATA_INTEGRITY = AivssDecisionPoint(
    name="Data Integrity",
    key="DI",
    version="1.0.0",
    description="Measures taken to ensure the integrity of data used in training and inference.",
    values=(FORMALLY_VERIFIED, STRONG_CHECKS, BASIC_CHECKS, _NONE),
)

VERSIONS = [DATA_INTEGRITY]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
