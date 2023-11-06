#!/usr/bin/env python
"""
CVSS v4 Equivalence Sets
"""
#  Copyright (c) 2023 Carnegie Mellon University and Contributors.
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

from ssvc.decision_points import SsvcDecisionPointValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint


# EQ1 → AV/PR/UI with 3 levels specified in Table 24
# Levels	Constraints	Highest Severity Vector(s)
# 0	AV:N and PR:N and UI:N	AV:N/PR:N/UI:N
# 1	(AV:N or PR:N or UI:N) and not (AV:N and PR:N and UI:N) and not AV:P	AV:A/PR:N/UI:N or AV:N/PR:L/UI:N or AV:N/PR:N:/UI:P
# 2	AV:P or not(AV:N or PR:N or UI:N)	AV:P/PR:N/UI:N or AV:A/PR:L/UI:P
EQ1 = CvssDecisionPoint(
    name="Equivalence Set 1",
    key="EQ1",
    description="AV/PR/UI with 3 levels specified in Table 24",
    version="1.0.0",
    values=[
        SsvcDecisionPointValue(
            name="Low",
            key="L",
            description="2: AV:P or not(AV:N or PR:N or UI:N)",
        ),
        SsvcDecisionPointValue(
            name="Medium",
            key="M",
            description="1: (AV:N or PR:N or UI:N) and not (AV:N and PR:N and UI:N) and not AV:P",
        ),
        SsvcDecisionPointValue(
            name="High",
            key="H",
            description="0: AV:N and PR:N and UI:N",
        ),
    ],
)

# EQ2 → AC/AT with 2 levels specified in Table 25
# Levels	Constraints	Highest Severity Vector(s)
# 0	AC:L and AT:N	AC:L/AT:N
# 1	not (AC:L and AT:N)	AC:L/AT:P or AC:H/AT:N
EQ2 = CvssDecisionPoint(
    name="Equivalence Set 2",
    key="EQ2",
    description="AC/AT with 2 levels specified in Table 25",
    version="1.0.0",
    values=[
        SsvcDecisionPointValue(
            name="Low",
            key="L",
            description="1: not (AC:L and AT:N)",
        ),
        SsvcDecisionPointValue(
            name="High",
            key="H",
            description="0: AC:L and AT:N",
        ),
    ],
)


# EQ3 → VC/VI/VA with 3 levels specified in Table 26
# Levels	Constraints	Highest Severity Vector(s)
# 0	VC:H and VI:H	VC:H/VI:H/VA:H
# 1	not (VC:H and VI:H) and (VC:H or VI:H or VA:H)	VC:L/VI:H/VA:H or VC:H/VI:L/VA:H
# 2	not (VC:H or VI:H or VA:H)	VC:L/VI:L/VA:L
EQ3 = CvssDecisionPoint(
    name="Equivalence Set 3",
    key="EQ3",
    description="VC/VI/VA with 3 levels specified in Table 26",
    version="1.0.0",
    values=[
        SsvcDecisionPointValue(
            name="Low",
            key="L",
            description="2: not (VC:H or VI:H or VA:H)",
        ),
        SsvcDecisionPointValue(
            name="Medium",
            key="M",
            description="1: not (VC:H and VI:H) and (VC:H or VI:H or VA:H)",
        ),
        SsvcDecisionPointValue(
            name="High",
            key="H",
            description="0: VC:H and VI:H",
        ),
    ],
)


# EQ4 → SC/SI/SA with 3 levels specified in Table 27
# 0	MSI:S or MSA:S	SC:H/SI:S/SA:S
# 1	not (MSI:S or MSA:S) and (SC:H or SI:H or SA:H)	SC:H/SI:H/SA:H
# 2	not (MSI:S or MSA:S) and not (SC:H or SI:H or SA:H)	SC:L/SI:L/SA:L
EQ4 = CvssDecisionPoint(
    name="Equivalence Set 4",
    key="EQ4",
    description="SC/SI/SA with 3 levels specified in Table 27",
    version="1.0.0",
    values=[
        SsvcDecisionPointValue(
            name="Low",
            key="L",
            description="2: not (MSI:S or MSA:S) and not (SC:H or SI:H or SA:H)",
        ),
        SsvcDecisionPointValue(
            name="Medium",
            key="M",
            description="1: not (MSI:S or MSA:S) and (SC:H or SI:H or SA:H)",
        ),
        SsvcDecisionPointValue(
            name="High",
            key="H",
            description="0: MSI:S or MSA:S",
        ),
    ],
)


# EQ5 → E with 3 levels specified in Table 28
# 0	E:A	E:A
# 1	E:P	E:P
# 2	E:U	E:U
EQ5 = CvssDecisionPoint(
    name="Equivalence Set 5",
    key="EQ5",
    description="E with 3 levels specified in Table 28",
    version="1.0.0",
    values=[
        SsvcDecisionPointValue(
            name="Low",
            key="L",
            description="2: E:U",
        ),
        SsvcDecisionPointValue(
            name="Medium",
            key="M",
            description="1: E:P",
        ),
        SsvcDecisionPointValue(
            name="High",
            key="H",
            description="0: E:A",
        ),
    ],
)

# EQ6 → VC/VI/VA+CR/CI/CA with 2 levels specified in Table 29
# 0	(CR:H and VC:H) or (IR:H and VI:H) or (AR:H and VA:H)	VC:H/VI:H/VA:H/CR:H/IR:H/AR:H
# 1	not (CR:H and VC:H) and not (IR:H and VI:H) and not (AR:H and VA:H)	VC:H/VI:H/VA:H/CR:M/IR:M/AR:M or VC:H/VI:H/VA:L/CR:M/IR:M/AR:H or VC:H/VI:L/VA:H/CR:M/IR:H/AR:M or VC:H/VI:L/VA:L/CR:M/IR:H/AR:H or VC:L/VI:H/VA:H/CR:H/IR:M/AR:M or VC:L/VI:H/VA:L/CR:H/IR:M/AR:H or VC:L/VI:L/VA:H/CR:H/IR:H/AR:M or VC:L/VI:L/VA:L/CR:H/IR:H/AR:H
EQ6 = CvssDecisionPoint(
    name="Equivalence Set 6",
    key="EQ6",
    description="VC/VI/VA+CR/CI/CA with 2 levels specified in Table 29",
    version="1.0.0",
    values=[
        SsvcDecisionPointValue(
            name="Low",
            key="L",
            description="1: not (CR:H and VC:H) and not (IR:H and VI:H) and not (AR:H and VA:H)",
        ),
        SsvcDecisionPointValue(
            name="High",
            key="H",
            description="0: (CR:H and VC:H) or (IR:H and VI:H) or (AR:H and VA:H)",
        ),
    ],
)


def main():
    for dp in [EQ1, EQ2, EQ3, EQ4, EQ5, EQ6]:
        print(dp.to_json(indent=2))


if __name__ == "__main__":
    main()
