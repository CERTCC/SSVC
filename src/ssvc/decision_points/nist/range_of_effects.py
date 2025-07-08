#!/usr/bin/env python
"""
Provides a decision point for assessing the range of effects for non-adversarial threat sources based on Table D-6 from NIST SP 800-30 Revision 1.
ASSESSMENT SCALE – RANGE OF EFFECTS FOR NON-ADVERSARIAL THREAT SOURCES
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
    description="The effects of the error, accident, or act of nature are minimal, involving few if any of the cyber "
    "resources of the [Tier 3: information systems; Tier 2: mission/business processes or EA segments, "
    "common infrastructure, or support services; Tier 1: organization/governance structure], "
    "and involving no critical resources.",
    key="VL",
)
LOW = DecisionPointValue(
    name="Low",
    description="The effects of the error, accident, or act of nature are limited, involving some of the cyber "
    "resources of the [Tier 3: information systems; Tier 2: mission/business processes or EA segments, "
    "common infrastructure, or support services; Tier 1: organization/governance structure], "
    "but involving no critical resources.",
    key="L",
)
MODERATE = DecisionPointValue(
    name="Moderate",
    description="The effects of the error, accident, or act of nature are wide-ranging, involving a significant "
    "portion of the cyber resources of the [Tier 3: information systems; Tier 2: mission/business "
    "processes or EA segments, common infrastructure, or support services; Tier 1: "
    "organization/governance structure], including some critical resources.",
    key="M",
)
HIGH = DecisionPointValue(
    name="High",
    description="The effects of the error, accident, or act of nature are extensive, involving most of the cyber "
    "resources of the [Tier 3: information systems; Tier 2: mission/business processes or EA segments, "
    "common infrastructure, or support services; Tier 1: organization/governance structure], "
    "including many critical resources.",
    key="H",
)
VERY_HIGH = DecisionPointValue(
    name="Very High",
    description="The effects of the error, accident, or act of nature are sweeping, involving almost all of the cyber "
    "resources of the [Tier 3: information systems; Tier 2: mission/business processes or EA segments, "
    "common infrastructure, or support services; Tier 1: organization/governance structure].",
    key="VH",
)

RANGE_OF_EFFECTS = NistDecisionPoint(
    name="Range of Effects",
    description="Range of effects for non-adversarial threat sources",
    key="RE",
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
    RANGE_OF_EFFECTS,
]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
