#!/usr/bin/env python
"""
file: base
author: adh
created_at: 9/20/23 4:47 PM
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

from pydantic import BaseModel

from ssvc._mixins import _Base, _Versioned
from ssvc.decision_points.base import SsvcDecisionPoint


class SsvcDecisionPointGroup(_Base, _Versioned, BaseModel):
    """
    Models a group of decision points.
    """

    decision_points: list[SsvcDecisionPoint]

    def __iter__(self):
        """
        Allow iteration over the decision points in the group.
        """
        return iter(self.decision_points)

    def __len__(self):
        """
        Allow len() to be called on the group.
        """
        dplist = list(self.decision_points)
        l = len(dplist)
        return l


def get_all_decision_points_from(
    *groups: list[SsvcDecisionPointGroup],
) -> list[SsvcDecisionPoint]:
    """
    Given a list of SsvcDecisionPointGroup objects, return a list of all
    the unique SsvcDecisionPoint objects contained in those groups.

    Args:
        groups (list): A list of SsvcDecisionPointGroup objects.

    Returns:
        list: A list of SsvcDecisionPoint objects.
    """
    dps = []
    seen = set()

    for group in groups:
        for dp in group.decision_points:
            if dp in dps:
                # skip duplicates
                continue
            key = (dp.name, dp.version)
            if key in seen:
                # skip duplicates
                continue
            # keep non-duplicates
            dps.append(dp)
            seen.add(key)

    return list(dps)


def main():
    pass


if __name__ == "__main__":
    main()
