#!/usr/bin/env python
"""
Provides a generic Not Define decision point value for CVSS decision points.
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


NOT_DEFINED_ND = SsvcDecisionPointValue(
    name="Not Defined",
    key="ND",
    description="This metric value is not defined. See CVSS documentation for details.",
)

NOT_DEFINED_X = SsvcDecisionPointValue(
    name="Not Defined",
    key="X",
    description="This metric value is not defined. See CVSS documentation for details.",
)
