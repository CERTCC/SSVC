#!/usr/bin/env python
"""
Provides an outcome set to assess the level of risk based on NIST SP 800-30 Revision 1.
ASSESSMENT SCALE – LEVEL OF RISK
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

# TABLE I-3: ASSESSMENT SCALE – LEVEL OF RISK
# Qualitative
# Values
# Semi-Quantitative
# Values Description
# Very High 96-100 10
# Very high risk means that a threat event could be expected to have multiple severe or
# catastrophic adverse effects on organizational operations, organizational assets, individuals,
# other organizations, or the Nation.
# High 80-95 8
# High risk means that a threat event could be expected to have a severe or catastrophic adverse
# effect on organizational operations, organizational assets, individuals, other organizations, or the
# Nation.
# Moderate 21-79 5 Moderate risk means that a threat event could be expected to have a serious adverse effect on
# organizational operations, organizational assets, individuals, other organizations, or the Nation.
# Low 5-20 2 Low risk means that a threat event could be expected to have a limited adverse effect on
# organizational operations, organizational assets, individuals, other organizations, or the Nation.
# Very Low 0-4 0 Very low risk means that a threat event could be expected to have a negligible adverse effect on
# organizational operations, organizational assets, individuals, other organizations, or the Nation.

VERY_LOW = DecisionPointValue(
    name="Very Low",
    description="Very low risk means that a threat event could be expected to have a negligible adverse effect on organizational operations, organizational assets, individuals, other organizations, or the Nation.",
    key="VL",
)

LOW = DecisionPointValue(
    name="Low",
    description="Low risk means that a threat event could be expected to have a limited adverse effect on organizational operations, organizational assets, individuals, other organizations, or the Nation.",
    key="L",
)

MODERATE = DecisionPointValue(
    name="Moderate",
    description="Moderate risk means that a threat event could be expected to have a serious adverse effect on organizational operations, organizational assets, individuals, other organizations, or the Nation.",
    key="M",
)
HIGH = DecisionPointValue(
    name="High",
    description="High risk means that a threat event could be expected to have a severe or catastrophic adverse effect on organizational operations, organizational assets, individuals, other organizations, or the Nation.",
    key="H",
)
VERY_HIGH = DecisionPointValue(
    name="Very High",
    description="Very high risk means that a threat event could be expected to have multiple severe or catastrophic adverse effects on organizational operations, organizational assets, individuals, other organizations, or the Nation.",
    key="VH",
)


RISK_LEVEL = NistDecisionPoint(
    name="Risk Level",
    description="Assessment scale for level of risk based on NIST SP 800-30 Revision 1",
    key="RL",
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
    RISK_LEVEL,
]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
