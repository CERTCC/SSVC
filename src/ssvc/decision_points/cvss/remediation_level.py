#!/usr/bin/env python
"""
Models the CVSS Remediation Level metric as an SSVC decision point.
"""

#  Copyright (c) 2023-2025 Carnegie Mellon University and Contributors.
#  - see Contributors.md for a full list of Contributors
#  - see ContributionInstructions.md for information on how you can Contribute to this project
#  Stakeholder Specific Vulnerability Categorization (SSVC) is
#  licensed under a MIT (SEI)-style license, please see LICENSE.md distributed
#  with this Software or contact permission@sei.cmu.edu for full terms.
#  Created, in part, with funding and support from the United States Government
#  (see Acknowledgments file). This program may include and/or can make use of
#  certain third party source code, object code, documentation and other files
#  (“Third Party Software”). See LICENSE.md for more details.
#  Carnegie Mellon®, CERT® and CERT Coordination Center® are registered in the
#  U.S. Patent and Trademark Office by Carnegie Mellon University

from ssvc.decision_points.base import SsvcDecisionPointValue
from ssvc.decision_points.cvss._not_defined import NOT_DEFINED_X
from ssvc.decision_points.cvss.base import CvssDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs


_UNAVAILABLE = SsvcDecisionPointValue(
    name="Unavailable",
    key="U",
    description="There is either no solution available or it is impossible to apply.",
)

_WORKAROUND = SsvcDecisionPointValue(
    name="Workaround",
    key="W",
    description="There is an unofficial, non-vendor solution available. In some cases, users of the affected "
    "technology will create a patch of their own or provide steps to work around or otherwise mitigate "
    "against the vulnerability. When it is generally accepted that these unofficial fixes are adequate in "
    "plugging the hole for the mean time and no official remediation is available, this value can be set.",
)

_TEMPORARY_FIX = SsvcDecisionPointValue(
    name="Temporary Fix",
    key="TF",
    description="There is an official but temporary fix available. This includes instances where the vendor issues a "
    "temporary hotfix, tool or official workaround.",
)

_OFFICIAL_FIX = SsvcDecisionPointValue(
    name="Official Fix",
    key="OF",
    description="A complete vendor solution is available. Either the vendor has issued the final, official patch "
    "which eliminates the vulnerability or an upgrade that is not vulnerable is available.",
)

REMEDIATION_LEVEL_1 = CvssDecisionPoint(
    name="Remediation Level",
    description="This metric measures the remediation status of a vulnerability.",
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
    description="This metric measures the remediation status of a vulnerability.",
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

versions = [REMEDIATION_LEVEL_1, REMEDIATION_LEVEL_1_1]


def main():
    print_versions_and_diffs(versions)


if __name__ == "__main__":
    main()
