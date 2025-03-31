#!/usr/bin/env python
"""
Provides helpers for working with CVSS decision points.
"""
#  Copyright (c) 2023-2025 Carnegie Mellon University.
#  NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE
#  ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS.
#  CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND,
#  EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT
#  NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR
#  MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE
#  OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE
#  ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM
#  PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
#  Licensed under a MIT (SEI)-style license, please see LICENSE or contact
#  permission@sei.cmu.edu for full terms.
#  [DISTRIBUTION STATEMENT A] This material has been approved for
#  public release and unlimited distribution. Please see Copyright notice
#  for non-US Government use and distribution.
#  This Software includes and/or makes use of Third-Party Software each
#  subject to its own license.
#  DM24-0278

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
    _dp.values = list(values)

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
        _dp.values = list(values)

    return _dp


def main():
    pass


if __name__ == "__main__":
    main()
