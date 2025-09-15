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
from ssvc.decision_points.base import DecisionPointValue as DecisionPointValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs

_NONE = DecisionPointValue(name="None", key="N", definition="None (0.0)")

_LOW = DecisionPointValue(name="Low", key="L", definition="Low (0.1-3.9)")

_MEDIUM = DecisionPointValue(
    name="Medium", key="M", definition="Medium (4.0-6.9)"
)

_HIGH = DecisionPointValue(name="High", key="H", definition="High (7.0-8.9)")

_CRITICAL = DecisionPointValue(
    name="Critical", key="C", definition="Critical (9.0-10.0)"
)

LMHC = CvssDecisionPoint(
    name="CVSS Qualitative Severity Rating Scale",
    key="CVSS",
    definition="The CVSS Qualitative Severity Rating Scale group.",
    version="1.0.0",
    values=(
        _NONE,
        _LOW,
        _MEDIUM,
        _HIGH,
        _CRITICAL,
    ),
)
"""
The CVSS Qualitative Severity (N,L,M,H,C) Rating Scale outcome group.
"""

VERSIONS = (LMHC,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
