#!/usr/bin/env python
"""
Provides helpers for working with CVSS decision points.
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

from copy import deepcopy

from ssvc.decision_points import SsvcDecisionPointValue


def modify(obj):
    """
    Prepends "Modified " to the name and "M" to the key of the given object. Also adds a value of "Not Defined" to the
    values list.
    Args:
        obj: the decision point object to modify

    Returns:
        A modified copy of the given object
    """
    o = deepcopy(obj)
    o.name = "Modified " + o.name
    o.key = "M" + o.key
    nd = SsvcDecisionPointValue(
        name="Not Defined", key="ND", description="Ignore this value"
    )
    values = list(o.values)
    # if there is no value named "Not Defined" value, add it
    names = [v.name for v in values]
    if nd.name not in names:
        values.append(nd)
    o.values = tuple(values)
    return o


def main():
    pass


if __name__ == "__main__":
    main()
