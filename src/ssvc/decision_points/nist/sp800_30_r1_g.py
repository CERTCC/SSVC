#!/usr/bin/env python
"""
Provides a 5-level ascending probability scale decision point for SSVC
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
from ssvc.decision_points.nist.base import NISTDecisionPoint
from ssvc.namespaces import FRAG_SEP, NameSpace

# These ranges are based on NIST SP 800-30 Rev. 1 Appendix G

VERY_HIGH = DecisionPointValue(
    name="Very High",
    key="VH",
    definition="96% <= Probability <= 100%. Almost certain.",
)
HIGH = DecisionPointValue(
    name="High",
    key="H",
    definition="80% <= Probability < 96%. Highly likely.",
)
MODERATE = DecisionPointValue(
    name="Moderate",
    key="M",
    definition="21% <= Probability < 80%. Somewhat likely.",
)
LOW = DecisionPointValue(
    name="Low",
    key="L",
    definition="5% <= Probability < 21%. Unlikely.",
)
VERY_LOW = DecisionPointValue(
    name="Very Low",
    key="VL",
    definition="0% <= Probability < 5%. Highly unlikely.",
)


P5X = NISTDecisionPoint(
    namespace=FRAG_SEP.join((NameSpace.NIST, "800-30")),
    key="P_5X",
    version="1.0.0",
    name="Probability Scale in 5 weighted levels, ascending",
    definition="A probability scale with finer resolution at both extremes, based on NIST SP 800-30 Rev. 1 Appendix G",
    values=(
        VERY_LOW,
        LOW,
        MODERATE,
        HIGH,
        VERY_HIGH,
    ),
)

VERSIONS = [P5X]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
