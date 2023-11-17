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

from ssvc.decision_points import SsvcDecisionPoint, SsvcDecisionPointValue
from ssvc.decision_points.cvss._not_defined import NOT_DEFINED_X


def _modify_3(dp: SsvcDecisionPoint):
    _dp = deepcopy(dp)
    _dp.name = "Modified " + _dp.name
    _dp.key = "M" + _dp.key

    # if there is no value named "Not Defined" value, add it
    nd = NOT_DEFINED_X

    values = list(_dp.values)

    names = [v.name for v in values]
    if nd.name not in names:
        values.append(nd)
    _dp.values = tuple(values)

    return _dp


def modify_3(dp: SsvcDecisionPoint):
    """
    Prepends "Modified " to the name and "M" to the key of the given object. Also adds a value of "Not Defined" to the
    values list.
    Args:
        dp: the decision point object to modify

    Returns:
        A modified copy of the given object
    """

    _dp = _modify_3(dp)
    _dp.__post_init__()  # call post-init to update the key & register
    return _dp


def modify_4(dp: SsvcDecisionPoint):
    """
    Modifies a CVSS v4 Base Metric decision point object.

    Args:
        dp: the decision point object to modify

    Returns:
        A modified copy of the given object
    """

    _dp = _modify_3(dp)
    _dp = _modify_4(_dp)
    _dp.__post_init__()  # call post-init to update the key & register

    return _dp


def _modify_4(dp: SsvcDecisionPoint):
    # note:
    # this method was split out for testing purposes
    # assumes you've already done the 3.0 modifications

    _dp = deepcopy(dp)
    # Note: For MSC, MSI, and MSA, the lowest metric value is “Negligible” (N), not “None” (N).
    if _dp.key in ["MSC", "MSI", "MSA"]:
        for v in _dp.values:
            if v.key == "N":
                v.name = "Negligible"
                v.description.replace(" no ", " negligible ")
                break

    # Note: For MSI, There is also a highest severity level, Safety (S), in addition to the same values as the
    # corresponding Base Metric (High, Medium, Low).
    if _dp.key == "MSI":
        _SAFETY = SsvcDecisionPointValue(
            name="Safety",
            key="S",
            description="The Safety metric value measures the impact regarding the Safety of a human actor or "
            "participant that can be predictably injured as a result of the vulnerability being exploited.",
        )
        values = list(_dp.values)
        values.append(_SAFETY)
        _dp.values = tuple(values)

    return _dp


def main():
    pass


if __name__ == "__main__":
    main()
