#!/usr/bin/env python

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

"""
Provides a DecisionPointGroup object for use in SSVC.
"""

import itertools
from typing import Generator

from pydantic import BaseModel

from ssvc._mixins import _Base, _SchemaVersioned
from ssvc.decision_points.base import (
    DecisionPoint,
)


class DecisionPointGroup(_Base, _SchemaVersioned, BaseModel):
    """
    Models a group of decision points.
    """

    decision_points: tuple[DecisionPoint, ...]

    def __iter__(self):
        """
        Allow iteration over the decision points in the group.
        """
        return iter(self.decision_points)

    def __len__(self):
        """
        Allow len() to be called on the group.
        """
        return len(self.decision_points)

    @property
    def decision_points_dict(self) -> dict[str, DecisionPoint]:
        """
        Return a dictionary of decision points keyed by their name.
        """
        return {dp.str: dp for dp in self.decision_points}

    @property
    def decision_points_str(self) -> list[str]:
        """
        Return a list of decision point names.
        """
        return list(self.decision_points_dict.keys())

    def combination_strings(self) -> Generator[tuple[str, ...], None, None]:
        """
        Return a list of tuples of the value short strings for all combinations of the decision points.
        """
        value_tuples = [dp.value_summaries_str for dp in self.decision_points]
        for combo in itertools.product(*value_tuples):
            yield combo


def get_all_decision_points_from(
    *groups: list[DecisionPointGroup],
) -> tuple[DecisionPoint, ...]:
    """
    Given a list of DecisionPointGroup objects, return a list of all
    the unique DecisionPoint objects contained in those groups.

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

    return tuple(dps)


def main():
    pass


if __name__ == "__main__":
    main()
