#!/usr/bin/env python

"""
Provides the Supplier Cardinality decision point and its values.
"""
#  Copyright (c) 2025 Carnegie Mellon University and Contributors.
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

from ssvc.decision_points.base import SsvcDecisionPoint, SsvcDecisionPointValue

MULTIPLE = SsvcDecisionPointValue(
    name="Multiple",
    key="M",
    description="There are multiple suppliers of the vulnerable component.",
)

ONE = SsvcDecisionPointValue(
    name="One",
    key="O",
    description="There is only one supplier of the vulnerable component.",
)

SUPPLIER_CARDINALITY_1 = SsvcDecisionPoint(
    name="Supplier Cardinality",
    description="How many suppliers are responsible for the vulnerable component and its remediation or mitigation plan?",
    key="SC",
    version="1.0.0",
    values=(
        ONE,
        MULTIPLE,
    ),
)


def main():
    print(SUPPLIER_CARDINALITY_1.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
