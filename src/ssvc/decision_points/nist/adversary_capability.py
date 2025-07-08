#!/usr/bin/env python
"""
Provides a decision point for assessing adversary capability based on Table D-3 from NIST SP 800-30 Revision 1.
ASSESSMENT SCALE – CHARACTERISTICS OF ADVERSARY CAPABILITY
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
from ssvc.decision_points.helpers import print_versions_and_diffs
from ssvc.decision_points.nist.base import NistDecisionPoint


VERY_LOW = DecisionPointValue(
    name="Very Low",
    description="The adversary has very limited resources, expertise, and opportunities to support a successful attack.",
    key="VL",
)
LOW = DecisionPointValue(
    name="Low",
    description="The adversary has limited resources, expertise, and opportunities to support a successful attack.",
    key="L",
)
MODERATE = DecisionPointValue(
    name="Moderate",
    description="The adversary has moderate resources, expertise, and opportunities to support multiple successful "
    "attacks.",
    key="M",
)
HIGH = DecisionPointValue(
    name="High",
    description="The adversary has a sophisticated level of expertise, with significant resources and opportunities "
    "to support multiple successful coordinated attacks.",
    key="H",
)
VERY_HIGH = DecisionPointValue(
    name="Very High",
    description="The adversary has a very sophisticated level of expertise, is well-resourced, and can generate "
    "opportunities to support multiple successful, continuous, and coordinated attacks.",
    key="VH",
)

ADVERSARY_CAPABILITY = NistDecisionPoint(
    name="Adversary Capability",
    description="Characteristics of adversary capability",
    key="AC",
    version="1.0.0",
    values=(
        VERY_LOW,
        LOW,
        MODERATE,
        HIGH,
        VERY_HIGH,
    ),
)

VERSIONS = [
    ADVERSARY_CAPABILITY,
]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
