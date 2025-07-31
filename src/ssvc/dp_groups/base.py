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

import itertools
from typing import Generator

from pydantic import BaseModel

from ssvc._mixins import _Base, _SchemaVersioned
from ssvc.decision_points.base import (
    DecisionPoint,
    ValueSummary,
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
        for combo in self.combinations():
            yield tuple(str(x) for x in combo)

    def combinations(self) -> Generator[tuple[ValueSummary, ...], None, None]:
        """
        Return a list of tuples of the value summaries for all combinations of the decision points.
        """
        value_tuples = [dp.value_summaries for dp in self.decision_points]
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
