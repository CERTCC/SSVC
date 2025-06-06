#!/usr/bin/env python
"""
Provides the Supplier Involvement decision point and its values.
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

from ssvc.decision_points.base import SsvcDecisionPoint, SsvcDecisionPointValue
from ssvc.decision_points.helpers import print_versions_and_diffs

UNCOOPERATIVE = SsvcDecisionPointValue(
    name="Uncooperative/Unresponsive",
    key="UU",
    description="The supplier has not responded, declined to generate a remediation, or no longer exists.",
)

COOPERATIVE = SsvcDecisionPointValue(
    name="Cooperative",
    key="C",
    description="The supplier is actively generating a patch or fix; they may or may not have provided a mitigation or work-around in the mean time.",
)

FIX_READY = SsvcDecisionPointValue(
    name="Fix Ready",
    key="FR",
    description="The supplier has provided a patch or fix.",
)

SUPPLIER_INVOLVEMENT_1 = SsvcDecisionPoint(
    name="Supplier Involvement",
    description="What is the state of the supplier’s work on addressing the vulnerability?",
    key="SI",
    version="1.0.0",
    values=(
        FIX_READY,
        COOPERATIVE,
        UNCOOPERATIVE,
    ),
)

VERSIONS = (SUPPLIER_INVOLVEMENT_1,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
