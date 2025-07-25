#!/usr/bin/env python

"""
Provides an SSVC decision point for critical software designation.
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
from ssvc.decision_points.helpers import print_versions_and_diffs
from ssvc.decision_points.ssvc.base import SsvcDecisionPoint

YES = DecisionPointValue(
    name="Yes",
    key="Y",
    description="System meets a critical software definition.",
)

NO = DecisionPointValue(
    name="No",
    key="N",
    description="System does not meet a critical software definition.",
)

CRITICAL_SOFTWARE_1 = SsvcDecisionPoint(
    name="Critical Software",
    description="Denotes whether a system meets a critical software definition.",
    key="CS",
    version="1.0.0",
    values=(
        NO,
        YES,
    ),
)

VERSIONS = (CRITICAL_SOFTWARE_1,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
