#!/usr/bin/env python
"""
file: report_credibility
author: adh
created_at: 9/21/23 11:24 AM
"""

from ssvc.decision_points.base import SsvcDecisionPoint, SsvcDecisionPointValue

NOT_CREDIBLE = SsvcDecisionPointValue(
    name="Not Credible",
    key="NC",
    description="The report is not credible.",
)

CREDIBLE = SsvcDecisionPointValue(
    name="Credible",
    key="C",
    description="The report is credible.",
)

REPORT_CREDIBILITY_1 = SsvcDecisionPoint(
    name="Report Credibility",
    description="Is the report credible?",
    key="RC",
    version="1.0.0",
    values=(
        CREDIBLE,
        NOT_CREDIBLE,
    ),
)


def main():
    print(REPORT_CREDIBILITY_1.to_json(indent=2))


if __name__ == "__main__":
    main()
