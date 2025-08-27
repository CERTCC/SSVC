#!/usr/bin/env python
"""
Models CVSS Scope as an SSVC decision point.
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

_CHANGED = DecisionPointValue(
    name="Changed",
    key="C",
    definition="An exploited vulnerability can affect resources beyond the authorization privileges intended by the "
    "vulnerable component. In this case the vulnerable component and the impacted component are different.",
)

_UNCHANGED = DecisionPointValue(
    name="Unchanged",
    key="U",
    definition="An exploited vulnerability can only affect resources managed by the same authority. In this case the "
    "vulnerable component and the impacted component are the same.",
)

SCOPE_1 = CvssDecisionPoint(
    name="Scope",
    definition="the ability for a vulnerability in one software component to impact resources beyond its means, "
    "or privileges",
    key="S",
    version="1.0.0",
    values=(
        _UNCHANGED,
        _CHANGED,
    ),
)
"""
Defines Changed and Unchanged values for CVSS Scope.
"""

VERSIONS = (SCOPE_1,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
