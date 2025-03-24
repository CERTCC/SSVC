#  Copyright (c) 2023-2025 Carnegie Mellon University and Contributors.
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
"""
Provides SSVC outcome group objects.

SSVC outcome groups are functionally equivalent to Decision Points.
The only difference is that Outcome Groups are primarily intended to be used
as the outputs of a decision, whereas Decision Points are the inputs to a decision.
However, there are use cases where an outcome of one decision may feed into another
decision, so the distinction is somewhat arbitrary. Hence, we chose to use the same
data structure for both.

Outcome groups are organized by namespace.
"""
