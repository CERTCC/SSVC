#!/usr/bin/env python
"""
Models the CVSS Remediation Level metric as an SSVC decision point.
"""

from ssvc.decision_points.base import SsvcDecisionPointValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint

_NOT_DEFINED = SsvcDecisionPointValue(
    name="Not Defined",
    key="ND",
    description="Assigning this value to the metric will not influence the score. It is a signal to the equation to skip this metric.",
)

_UNAVAILABLE = SsvcDecisionPointValue(
    name="Unavailable",
    key="U",
    description="There is either no solution available or it is impossible to apply.",
)

_WORKAROUND = SsvcDecisionPointValue(
    name="Workaround",
    key="W",
    description="There is an unofficial, non-vendor solution available. In some cases, users of the affected technology will create a patch of their own or provide steps to work around or otherwise mitigate against the vulnerability. When it is generally accepted that these unofficial fixes are adequate in plugging the hole for the mean time and no official remediation is available, this value can be set.",
)

_TEMPORARY_FIX = SsvcDecisionPointValue(
    name="Temporary Fix",
    key="TF",
    description="There is an official but temporary fix available. This includes instances where the vendor issues a temporary hotfix, tool or official workaround.",
)

_OFFICIAL_FIX = SsvcDecisionPointValue(
    name="Official Fix",
    key="OF",
    description="A complete vendor solution is available. Either the vendor has issued the final, official patch which eliminates the vulnerability or an upgrade that is not vulnerable is available.",
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
        _NOT_DEFINED,
    ),
)
"""
Adds Not Defined to the CVSS Remediation Level decision point.
"""


def main():
    print(REMEDIATION_LEVEL_1.to_json(indent=2))
    print(REMEDIATION_LEVEL_1_1.to_json(indent=2))


if __name__ == "__main__":
    main()
