#!/usr/bin/env python
"""
Model the CVSS Impact Bias as an SSVC decision point.
"""
#  Copyright (c) 2023-2025 Carnegie Mellon University.
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
from ssvc.decision_points.cvss.base import CvssDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs

_AVAILABILITY = DecisionPointValue(
    name="Availability",
    key="A",
    definition="Availability Impact is assigned greater weight than Confidentiality Impact or Integrity Impact.",
)

_INTEGRITY = DecisionPointValue(
    name="Integrity",
    key="I",
    definition="Integrity Impact is assigned greater weight than Confidentiality Impact or Availability Impact.",
)

_CONFIDENTIALITY = DecisionPointValue(
    name="Confidentiality",
    key="C",
    definition="Confidentiality impact is assigned greater weight than Integrity Impact or Availability Impact.",
)

_NORMAL = DecisionPointValue(
    name="Normal",
    key="N",
    definition="Confidentiality Impact, Integrity Impact, and Availability Impact are all assigned the same weight.",
)

IMPACT_BIAS_1 = CvssDecisionPoint(
    name="Impact Bias",
    definition="This metric measures the impact bias of the vulnerability.",
    key="IB",
    version="1.0.0",
    values=(
        _NORMAL,
        _CONFIDENTIALITY,
        _INTEGRITY,
        _AVAILABILITY,
    ),
)
"""
Defines Normal, Confidentiality, Integrity, and Availability values for CVSS Impact Bias.
"""

VERSIONS = (IMPACT_BIAS_1,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
