#!/usr/bin/env python
"""
The ssvc.decision_points package provides a set of decision points for use in SSVC decision functions.

Decision points are the basic building blocks of SSVC decision functions. Individual decision points describe a
single aspect of the input to a decision function. Decision points should have the following characteristics:

- A name or label
- A description
- A version (a semantic version string)
- A namespace (a short, unique string): For example, "ssvc" or "cvss" to indicate the source of the decision point
- A key (a short, unique string) that can be used to identify the decision point in a shorthand way
- A short enumeration of possible values

In turn, each value should have the following characteristics:
- A name or label
- A description
- A key (a short, unique string) that can be used to identify the value in a shorthand way
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

from .base import SsvcDecisionPoint, SsvcDecisionPointValue
