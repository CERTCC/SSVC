#!/usr/bin/env python

"""
Provides the Supplier Cardinality decision point and its values.
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
from ssvc.decision_points.ssvc.base import SsvcDecisionPoint

MULTIPLE = DecisionPointValue(
    name="Multiple",
    key="M",
    definition="There are multiple suppliers of the vulnerable component.",
)

ONE = DecisionPointValue(
    name="One",
    key="O",
    definition="There is only one supplier of the vulnerable component.",
)

SUPPLIER_CARDINALITY_1 = SsvcDecisionPoint(
    name="Supplier Cardinality",
    definition="How many suppliers are responsible for the vulnerable component and its remediation or mitigation plan?",
    key="SC",
    version="1.0.0",
    values=(
        ONE,
        MULTIPLE,
    ),
)

VERSIONS = (SUPPLIER_CARDINALITY_1,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
