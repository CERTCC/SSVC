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
import secrets
from collections.abc import MutableMapping
from itertools import product

from pydantic import BaseModel, model_validator

from ssvc._mixins import _Base, _SchemaVersioned
from ssvc.decision_points.base import (
    DecisionPoint,
)


class DecisionPointGroup(_Base, _SchemaVersioned, BaseModel, MutableMapping):
    """
    Models a group of decision points as a dictionary, keyed by their ID.
    """

    decision_points: dict[str, DecisionPoint]

    @model_validator(mode="before")
    def transform_decision_points(cls, data):
        if isinstance(data, dict) and "decision_points" in data:
            # If decision_points is a list/tuple, convert to dictionary
            # this allows us to handle the older way of defining decision point groups
            dp_value = data["decision_points"]
            if isinstance(dp_value, (list, tuple)):
                data["decision_points"] = {dp.id: dp for dp in dp_value}
        return data

    # dunder methods to allow dict-like access in conjunction with MutableMapping abstract base class
    def __getitem__(self, key):
        return self.decision_points[key]

    def __setitem__(self, key, value):
        if not isinstance(value, DecisionPoint):
            raise TypeError("Value must be a DecisionPoint")
        self.decision_points[key] = value

    def __delitem__(self, key):
        del self.decision_points[key]

    def __iter__(self):
        return iter(self.decision_points)

    def __len__(self):
        return len(self.decision_points)

    def add(self, decision_point: DecisionPoint) -> None:
        """
        Add a decision point to the group.
        """
        if decision_point.id in self.decision_points:
            # are they the same?
            existing_dp = self.decision_points[decision_point.id]
            if existing_dp == decision_point:
                # this is a no-op, they are the same
                return
            # otherwise, raise an error
            raise ValueError(
                f"Decision point {decision_point.id} already exists in the group."
            )

        # set the decision point in the dictionary
        self.decision_points[decision_point.id] = decision_point

    def obfuscate(self) -> tuple["DecisionPointGroup", dict[str, str]]:
        """
        Returns a new DecisionPointGroup object, with the keys of the decision points dict obfuscated.

        Returns:
            tuple: A tuple containing the new DecisionPointGroup and a dictionary mapping old keys to new obfuscated keys.
        """
        token_len = 4
        new_dict = {}
        translator = {}
        for old_key in self.decision_points.keys():
            while True:
                new_key = secrets.token_hex(token_len)
                # make the new key match NNNN-NNNN...
                new_key = "-".join(
                    new_key[i : i + token_len]
                    for i in range(0, len(new_key), token_len)
                )
                # uppercase the new key
                new_key = new_key.upper()
                if new_key not in translator:
                    break
            # got a unique new_key
            translator[old_key] = new_key
            new_dict[new_key] = self.decision_points[old_key]

        new_group = self.copy(deep=True)
        new_group.decision_points = new_dict

        return (new_group, translator)

    def combination_strings(self) -> list[tuple[str, ...]]:
        """
        Generate all combinations of decision point values as strings.
        Each combination is a tuple of value keys, one for each decision point.
        """
        value_lists = []
        for dp in self.decision_points.values():
            if not dp.values:
                raise ValueError(
                    f"Decision point {dp.key} has no values defined, cannot generate combinations."
                )
            value_keys = list(dp.value_dict.keys())
            value_lists.append(value_keys)

        return list(product(*value_lists))

    def combination_list(self,exclude=str) -> list[dict[str, str]]:
        """
        Generate all combinations of decision point values as dictionaries.
        Each combination is a dictionary with decision point IDs as keys and value keys as values.
        """
        dpg_vals = []
        for dp in self.decision_points.values():
            if dp.id in exclude:
                # skip this decision point if it is in the exclude list
                continue
            vals = []
            for value in dp.values:
                row = {dp.id: value.key}
                vals.append(row)
            dpg_vals.append(vals)

        # now we have a list of lists of dicts, we need to the combinations
        combos = []
        for prod in product(*dpg_vals):
            # prod is a tuple of dicts, we need to merge them
            merged = {}
            for d in prod:
                merged.update(d)
            combos.append(merged)
        return combos


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
        for dp in group.decision_points.values():
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
