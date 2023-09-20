#!/usr/bin/env python
"""
file: remediation_level
author: adh
created_at: 9/20/23 1:47 PM
"""
from copy import deepcopy

from ssvc.decision_points.base import SsvcValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint

REMEDIATION_LEVEL_1 = CvssDecisionPoint(
    name="Remediation Level",
    description="This metric measures the remediation status of a vulnerability.",
    key="RL",
    version="1.0.0",
    values=[
        SsvcValue(
            name="Official Fix",
            key="OF",
            description="A complete vendor solution is available. Either the vendor has issued the final, official patch which eliminates the vulnerability or an upgrade that is not vulnerable is available.",
        ),
        SsvcValue(
            name="Temporary Fix",
            key="TF",
            description="There is an official but temporary fix available. This includes instances where the vendor issues a temporary hotfix, tool or official workaround.",
        ),
        SsvcValue(
            name="Workaround",
            key="W",
            description="There is an unofficial, non-vendor solution available. In some cases, users of the affected technology will create a patch of their own or provide steps to work around or otherwise mitigate against the vulnerability. When it is generally accepted that these unofficial fixes are adequate in plugging the hole for the mean time and no official remediation is available, this value can be set.",
        ),
        SsvcValue(
            name="Unavailable",
            key="U",
            description="There is either no solution available or it is impossible to apply.",
        ),
    ],
)


REMEDIATION_LEVEL_1_1 = deepcopy(REMEDIATION_LEVEL_1)
REMEDIATION_LEVEL_1_1.version = "1.1.0"
REMEDIATION_LEVEL_1_1.values = [
    SsvcValue(
        name="Official Fix",
        key="OF",
        description="A complete vendor solution is available. Either the vendor has issued the final, official patch which eliminates the vulnerability or an upgrade that is not vulnerable is available.",
    ),
    SsvcValue(
        name="Temporary Fix",
        key="TF",
        description="There is an official but temporary fix available. This includes instances where the vendor issues a temporary hotfix, tool or official workaround.",
    ),
    SsvcValue(
        name="Workaround",
        key="W",
        description="There is an unofficial, non-vendor solution available. In some cases, users of the affected technology will create a patch of their own or provide steps to work around or otherwise mitigate against the vulnerability. When it is generally accepted that these unofficial fixes are adequate in plugging the hole for the mean time and no official remediation is available, this value can be set.",
    ),
    SsvcValue(
        name="Unavailable",
        key="U",
        description="There is either no solution available or it is impossible to apply.",
    ),
    SsvcValue(
        name="Not Defined",
        key="ND",
        description="Assigning this value to the metric will not influence the score. It is a signal to the equation to skip this metric.",
    ),
]


def main():
    print(REMEDIATION_LEVEL_1.to_json(indent=2))
    print(REMEDIATION_LEVEL_1_1.to_json(indent=2))


if __name__ == "__main__":
    main()
