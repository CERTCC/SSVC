#!/usr/bin/env python
"""
file: generic
author: adh
created_at: 7/30/25 11:34 AM
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

# Each sub-category within the AI-Specific Metrics is scored on a scale of 0.0 to 1.0, with the following general interpretation:
#
# 0.0: No Known Vulnerability: Indicates no known vulnerability or a formally proven resistance to the specific threat.
# 0.1 - 0.3: Low Vulnerability: Indicates a low vulnerability with strong mitigation in place, but some minor weaknesses may still exist.
# 0.4 - 0.6: Medium Vulnerability: Indicates a moderate vulnerability with some mitigation, but significant weaknesses remain.
# 0.7 - 1.0: Critical/High Vulnerability: Indicates a severe vulnerability with little to no mitigation in place.

_NONE = DecisionPointValue(
    name="None",
    key="N",
    description="No known vulnerability or a formally proven resistance to the specific threat.",
)

LOW = DecisionPointValue(
    name="Low",
    key="L",
    description="Low vulnerability with strong mitigation in place, but some minor weaknesses may still exist.",
)

MEDIUM = DecisionPointValue(
    name="Medium",
    key="M",
    description="Moderate vulnerability with some mitigation, but significant weaknesses remain.",
)

HIGH = DecisionPointValue(
    name="High",
    key="H",
    description="Severe vulnerability with little to no mitigation in place.",
)

GENERIC = AivssDecisionPoint(
    name="Generic AIVSS Decision Point",
    key="GENERIC",
    version="1.0.0",
    description="A generic decision point for AI-Specific Vulnerability Scoring System (AIVSS) metrics.",
    values=[_NONE, LOW, MEDIUM, HIGH],
)


VERSIONS = (GENERIC,)
LATEST = VERSIONS[-1]

def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == '__main__':
    main()
