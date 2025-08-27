#!/usr/bin/env python
"""
Models the CVSS Remediation Level metric as an SSVC decision point.
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
from ssvc.decision_points.cvss._not_defined import NOT_DEFINED_X
from ssvc.decision_points.cvss.base import CvssDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs


_UNAVAILABLE = DecisionPointValue(
    name="Unavailable",
    key="U",
    definition="There is either no solution available or it is impossible to apply.",
)

_WORKAROUND = DecisionPointValue(
    name="Workaround",
    key="W",
    definition="There is an unofficial, non-vendor solution available. In some cases, users of the affected "
    "technology will create a patch of their own or provide steps to work around or otherwise mitigate "
    "against the vulnerability. When it is generally accepted that these unofficial fixes are adequate in "
    "plugging the hole for the mean time and no official remediation is available, this value can be set.",
)

_TEMPORARY_FIX = DecisionPointValue(
    name="Temporary Fix",
    key="TF",
    definition="There is an official but temporary fix available. This includes instances where the vendor issues a "
    "temporary hotfix, tool or official workaround.",
)

_OFFICIAL_FIX = DecisionPointValue(
    name="Official Fix",
    key="OF",
    definition="A complete vendor solution is available. Either the vendor has issued the final, official patch "
    "which eliminates the vulnerability or an upgrade that is not vulnerable is available.",
)

REMEDIATION_LEVEL_1 = CvssDecisionPoint(
    name="Remediation Level",
    definition="This metric measures the remediation status of a vulnerability.",
    key="RL",
    version="1.0.0",
    values=(
        _OFFICIAL_FIX,
        _TEMPORARY_FIX,
        _WORKAROUND,
        _UNAVAILABLE,
    ),
)
"""
Defines Official Fix, Temporary Fix, Workaround, and Unavailable values for CVSS Remediation Level.
"""

REMEDIATION_LEVEL_1_1 = CvssDecisionPoint(
    name="Remediation Level",
    definition="This metric measures the remediation status of a vulnerability.",
    key="RL",
    version="1.1.0",
    values=(
        _OFFICIAL_FIX,
        _TEMPORARY_FIX,
        _WORKAROUND,
        _UNAVAILABLE,
        NOT_DEFINED_X,
    ),
)
"""
Adds Not Defined to the CVSS Remediation Level decision point.
"""

VERSIONS = (REMEDIATION_LEVEL_1, REMEDIATION_LEVEL_1_1)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
