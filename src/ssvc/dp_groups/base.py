#!/usr/bin/env python

#  Copyright (c) 2025 Carnegie Mellon University.
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

"""
Provides a DecisionPointGroup object for use in SSVC.
"""
from itertools import product
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

    def __iter__(self) -> Generator[DecisionPoint, None, None]:
        """
        Allow iteration over the decision points in the group.
        """
        return iter(self.decision_points)

    def __len__(self) -> int:
        """
        Allow len() to be called on the group.
        """
        return len(self.decision_points)

    @property
    def decision_points_dict(self) -> dict[str, DecisionPoint]:
        """
        Return a dictionary of decision points keyed by their name.
        """
        return {dp.id: dp for dp in self.decision_points}

    @property
    def decision_points_str(self) -> list[str]:
        """
        Return a list of decision point names.
        """
        return [dp.id for dp in self.decision_points]

    def combination_strings(self) -> list[tuple[str, ...]]:
        """
        Generate all combinations of decision point values as strings.
        Each combination is a tuple of value keys, one for each decision point.
        """
        value_lists = []
        for dp in self.decision_points:
            if not dp.values:
                raise ValueError(
                    f"Decision point {dp.key} has no values defined, cannot generate combinations."
                )
            value_keys = list(dp.value_dict.keys())
            value_lists.append(value_keys)

        return list(product(*value_lists))


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
