#!/usr/bin/env python
"""
file: supplier_involvement
author: adh
created_at: 9/21/23 11:28 AM
"""

from ssvc.decision_points.base import SsvcDecisionPoint, SsvcDecisionPointValue

UNCOOPERATIVE = SsvcDecisionPointValue(
    name="Uncooperative/Unresponsive",
    key="UU",
    description="The supplier has not responded, declined to generate a remediation, or no longer exists.",
)

COOPERATIVE = SsvcDecisionPointValue(
    name="Cooperative",
    key="C",
    description="The supplier is actively generating a patch or fix; they may or may not have provided a mitigation or work-around in the mean time.",
)

FIX_READY = SsvcDecisionPointValue(
    name="Fix Ready",
    key="FR",
    description="The supplier has provided a patch or fix.",
)

SUPPLIER_INVOLVEMENT_1 = SsvcDecisionPoint(
    name="Supplier Involvement",
    description="What is the state of the supplier’s work on addressing the vulnerability?",
    key="SI",
    version="1.0.0",
    values=(
        FIX_READY,
        COOPERATIVE,
        UNCOOPERATIVE,
    ),
)


def main():
    print(SUPPLIER_INVOLVEMENT_1.to_json(indent=2))


if __name__ == "__main__":
    main()
