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

import semver

from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_points.cvss._not_defined import NOT_DEFINED_X
from ssvc.decision_points.cvss.base import (
    CvssDecisionPoint,
    CvssDecisionPoint as DecisionPoint,
)


def _modify_3(dp: DecisionPoint):
    _dp_dict = deepcopy(dp.model_dump())
    _dp_dict["name"] = f'Modified {_dp_dict["name"]}'
    _dp_dict["key"] = f'M{_dp_dict["key"]}'

    # if there is no value named "Not Defined" value, add it
    nd = NOT_DEFINED_X

    values = list(_dp_dict["values"])
    names = [v["name"] for v in values]
    if nd.name not in names:
        values.append(nd)
    _dp_dict["values"] = tuple(values)

    _dp = DecisionPoint(**_dp_dict)

    return _dp


def modify_3(dp: DecisionPoint):
    """
    Prepends "Modified " to the name and "M" to the key of the given object. Also adds a value of "Not Defined" to the
    values list.
    Args:
        dp: the decision point object to modify

    Returns:
        A modified copy of the given object
    """

    _dp = _modify_3(dp)
    DecisionPoint.model_validate(_dp)  # validate the modified object
    return _dp


def modify_4(dp: DecisionPoint):
    """
    Modifies a CVSS v4 Base Metric decision point object.

    Args:
        dp: the decision point object to modify

    Returns:
        A modified copy of the given object
    """

    _dp = _modify_3(dp)
    _dp = _modify_4(_dp)
    DecisionPoint.model_validate(_dp)  # validate the modified object

    return _dp


def _modify_4(dp: DecisionPoint):
    # note:
    # this method was split out for testing purposes
    # assumes you've already done the 3.0 modifications

    _dp_dict = deepcopy(dp.model_dump())
    key = _dp_dict["key"]
    if key in ["MSC", "MSI", "MSA"]:
        for v in _dp_dict["values"]:
            if v["key"] == "N":
                v["name"] = "Negligible"
                v["definition"] = v["definition"].replace(
                    " no ", " negligible "
                )
                # we need to bump the version for this change
                version = _dp_dict["version"]
                ver = semver.Version.parse(version)
                _dp_dict["version"] = str(semver.Version.bump_patch(ver))
                break

    # Note: For MSI and MSA, There is also a highest severity level, Safety (S), in addition to the same values as the
    # corresponding Base Metric (High, Medium, Low).
    if key in ["MSI", "MSA"]:
        _SAFETY = DecisionPointValue(
            name="Safety",
            key="S",
            definition="The Safety metric value measures the impact regarding the Safety of a human actor or "
            "participant that can be predictably injured as a result of the vulnerability being exploited.",
        )
        values = list(_dp_dict["values"])
        values.append(_SAFETY)
        _dp_dict["values"] = tuple(values)

    _dp = DecisionPoint(**_dp_dict)

    return _dp


def main():
    pass


if __name__ == "__main__":
    main()


def no_x(dp: CvssDecisionPoint) -> CvssDecisionPoint:
    """Create a version of the decision point without the Not Defined (X) option."""
    return CvssDecisionPoint(
        namespace=dp.namespace,
        key=f"{dp.key}_NoX",
        version=dp.version,
        name=f"{dp.name} (without Not Defined)",
        definition=(
            f"{dp.definition} This version does not include the Not Defined (X) option."
        ),
        values=tuple([v for v in dp.values if v.key != "X"]),
    )
