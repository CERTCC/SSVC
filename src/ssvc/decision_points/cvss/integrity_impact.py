#!/usr/bin/env python
"""
file: integrity_impact
author: adh
created_at: 9/20/23 1:46 PM
"""
from copy import deepcopy

from ssvc.decision_points.base import SsvcDecisionPointValue

from ssvc.decision_points.cvss.base import CvssDecisionPoint

II_HIGH = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="There is a total loss of integrity, or a complete loss of protection. For example, the attacker is able to modify any/all files protected by the impacted component. Alternatively, only some files can be modified, but malicious modification would present a direct, serious consequence to the impacted component.",
)

II_LOW = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="Modification of data is possible, but the attacker does not have control over the consequence of a modification, or the amount of modification is constrained. The data modification does not have a direct, serious impact on the impacted component.",
)

II_NONE_2 = SsvcDecisionPointValue(
    name="None",
    key="N",
    description="There is no impact to the integrity of the system.",
)
COMPLETE = SsvcDecisionPointValue(
    name="Complete",
    key="C",
    description="A total compromise of system integrity. There is a complete loss of system protection resulting in the entire system being compromised. The attacker has sovereign control to modify any system files.",
)

PARTIAL = SsvcDecisionPointValue(
    name="Partial",
    key="P",
    description="Considerable breach in integrity. Modification of critical system files or information is possible, but the attacker does not have control over what can be modified, or the scope of what the attacker can affect is constrained. For example, key system or program files may be overwritten or modified, but at random or in a limited context or scope.",
)

II_NONE = SsvcDecisionPointValue(
    name="None", key="N", description="No impact on integrity."
)

INTEGRITY_IMPACT_1 = CvssDecisionPoint(
    name="Integrity Impact",
    description="This metric measures the impact on integrity a successful exploit of the vulnerability will have on the target system.",
    key="I",
    version="1.0.0",
    values=(
        II_NONE,
        PARTIAL,
        COMPLETE,
    ),
)

INTEGRITY_IMPACT_2 = deepcopy(INTEGRITY_IMPACT_1)
INTEGRITY_IMPACT_2.version = "2.0.0"
INTEGRITY_IMPACT_2.values = (
    II_NONE_2,
    II_LOW,
    II_HIGH,
)


def main():
    print(INTEGRITY_IMPACT_1.to_json(indent=2))
    print(INTEGRITY_IMPACT_2.to_json(indent=2))


if __name__ == "__main__":
    main()
