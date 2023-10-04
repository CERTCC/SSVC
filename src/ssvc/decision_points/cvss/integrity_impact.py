#!/usr/bin/env python
"""
Models the CVSS Integrity Impact metric as an SSVC decision point.
"""

from ssvc.decision_points.base import SsvcDecisionPointValue

from ssvc.decision_points.cvss.base import CvssDecisionPoint

_II_HIGH = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="There is a total loss of integrity, or a complete loss of protection. For example, the attacker is able to modify any/all files protected by the impacted component. Alternatively, only some files can be modified, but malicious modification would present a direct, serious consequence to the impacted component.",
)

_II_LOW = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="Modification of data is possible, but the attacker does not have control over the consequence of a modification, or the amount of modification is constrained. The data modification does not have a direct, serious impact on the impacted component.",
)

_II_NONE_2 = SsvcDecisionPointValue(
    name="None",
    key="N",
    description="There is no impact to the integrity of the system.",
)
_COMPLETE = SsvcDecisionPointValue(
    name="Complete",
    key="C",
    description="A total compromise of system integrity. There is a complete loss of system protection resulting in the entire system being compromised. The attacker has sovereign control to modify any system files.",
)

_PARTIAL = SsvcDecisionPointValue(
    name="Partial",
    key="P",
    description="Considerable breach in integrity. Modification of critical system files or information is possible, but the attacker does not have control over what can be modified, or the scope of what the attacker can affect is constrained. For example, key system or program files may be overwritten or modified, but at random or in a limited context or scope.",
)

_II_NONE = SsvcDecisionPointValue(
    name="None", key="N", description="No impact on integrity."
)

INTEGRITY_IMPACT_1 = CvssDecisionPoint(
    name="Integrity Impact",
    description="This metric measures the impact on integrity a successful exploit of the vulnerability will have on the target system.",
    key="I",
    version="1.0.0",
    values=(
        _II_NONE,
        _PARTIAL,
        _COMPLETE,
    ),
)
"""
Defines None, Partial, and Complete values for CVSS Integrity Impact.
"""

INTEGRITY_IMPACT_2 = CvssDecisionPoint(
    name="Integrity Impact",
    description="This metric measures the impact to integrity of a successfully exploited vulnerability.",
    key="I",
    version="2.0.0",
    values=(
        _II_NONE_2,
        _II_LOW,
        _II_HIGH,
    ),
)
"""
Updates None. Removes Partial and Complete. Adds Low and High values for CVSS Integrity Impact.
"""


def main():
    print(INTEGRITY_IMPACT_1.to_json(indent=2))
    print(INTEGRITY_IMPACT_2.to_json(indent=2))


if __name__ == "__main__":
    main()
