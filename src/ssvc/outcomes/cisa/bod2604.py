#  Copyright (c) 2026 Carnegie Mellon University.
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
"""
Provides the CISA BOD 26-04 outcome group for use in SSVC.
These are timelines, in calendar days, for agencies to remedy vulnerabilities.
"""

from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_points.cisa.base import CisaDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs

_FSU = DecisionPointValue(
    name="Fix on system upgrade",
    key="FSU",
    definition="The vulnerability should be remediated the next time the vulnerable asset receives a scheduled major upgrade or rebuild.",
)

_60D = DecisionPointValue(
    name="60 days",
    key="60D",
    definition="Remediate within 60 days.",
)

_14D = DecisionPointValue(
    name="14 days",
    key="14D",
    definition="Remediate within 14 days.",
)

_3D = DecisionPointValue(
    name="3 days",
    key="3D",
    definition="Remediate within 3 days.",
)

_3DF = DecisionPointValue(
    name="3 days & forensic investigation",
    key="3DF",
    definition="Remediate within 3 days and carry out a forensic triage of the asset to assess whether the system is compromised.",
)


BOD_26_04 = CisaDecisionPoint(
    name="CISA BOD 26-04 Remediation Timelines",
    key="BOD2604",
    definition="The CISA BOD 26-04 outcome group of remediation timelines for agencies to follow.",
    version="1.0.0",
    values=(_FSU, _60D, _14D, _3D, _3DF),
)
"""
The CISA BOD 26-04 outcome group. Based on CISA's customizations of the SSVC model.
"""

VERSIONS = (BOD_26_04,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
