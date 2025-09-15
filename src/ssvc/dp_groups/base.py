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

!!! warning "`ssvc.dp_groups` is deprecated"

    This module is *deprecated*. New development should focus on [`ssvc.decision_tables`](decision_tables.md).

"""
import warnings
from collections.abc import MutableMapping
from typing import ClassVar, Literal

from pydantic import BaseModel, model_validator

from ssvc._mixins import _Base, _SchemaVersioned, _Versioned
from ssvc.decision_points.base import (
    DecisionPoint,
)

SCHEMA_VERSION = "2.0.0"


class DecisionPointGroup(
    _Base, _SchemaVersioned, _Versioned, BaseModel, MutableMapping
):
    """
    **DEPRECATED:** `DecisionPointGroup` has been superseded by `DecisionTable`.
    New development should use `DecisionTable` instead.
    We are keeping this class around for backward compatibility, but it may be removed in future releases.

    Models a group of decision points as a dictionary, keyed by their ID.
    """

    decision_points: dict[str, DecisionPoint]
    _schema_version: ClassVar[str] = SCHEMA_VERSION
    schemaVersion: Literal[SCHEMA_VERSION]

    def __init__(self, *args, **kwargs):
        warnings.warn(
            f"{self.__class__.__name__} is deprecated; use `DecisionTable` instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        super().__init__(*args, **kwargs)

    @model_validator(mode="before")
    @classmethod
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

    @classmethod
    def model_json_schema(cls, **kwargs):
        """
        Overrides schema generation to ensure it's the way we want it
        """
        schema = super().model_json_schema(**kwargs)

        deprecation_warning = f"**DEPRECATED:** `{cls.__name__}` has been superseded by `DecisionTable`.\nNew development should use `DecisionTable` instead.\nWe are keeping this class around for backward compatibility, but it may be removed in future releases.\n\n"

        # append a deprecation warning to the description
        if "description" in schema:
            schema["description"] = (
                deprecation_warning + schema["description"].strip()
            )
        else:
            schema["description"] = deprecation_warning.strip()

        return schema


def get_all_decision_points_from(
    *groups: list[DecisionPointGroup],
) -> list[DecisionPoint]:
    """
    Given a list of DecisionPointGroup objects, return a list of all
    the unique DecisionPoint objects contained in those groups.

    Args:
        groups (list): A list of SsvcDecisionPointGroup objects.

    Returns:
        list: A list of unique SsvcDecisionPoint objects.
    """

    # each group has a decision_points dict, we need to collect all the decision points
    new_dict = {}
    for group in groups:
        # we could have just done a dict update, but want to ensure uniqueness
        # even if the decision point groups use non-standard keys for their
        # decision points dict. So we'll build a new dict with known consistent keys.
        for dp in group.decision_points.values():
            new_dict[dp.id] = dp
    # now we have a dictionary of all decision points, we can return them as a tuple
    return list(new_dict.values())


def main():
    pass


if __name__ == "__main__":
    main()
