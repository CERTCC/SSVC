#!/usr/bin/env python
"""
Provides an SSVC selection object and functions to facilitate transition from an SSVC decision point to a selection.
"""
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

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from ssvc._mixins import VersionField
from ssvc.decision_points.base import DecisionPoint


class MinimalSelection(BaseModel):
    """
    A minimal selection object that contains the decision point ID and the selected options.
    This is used to transition from an SSVC decision point to a selection.
    """

    decision_point_id: str = Field(
        ...,
        description="The ID (namespace:key:version) of the decision point from which the selection was made.",
    )
    namespace: str = Field(
        ...,
        description="The namespace of the decision point.",
        examples=["ssvc", "cisa", "certcc"],
        min_length=3,
    )
    key: str = Field(
        ...,
        description="The decision point key.",
        examples=["E", "A", "MI", "PSI"],
        min_length=1,
    )
    version: VersionField

    values: list[str] = Field(
        ...,
        description="A list of selected values keys from the decision point values.",
        min_length=1,
    )


class MinimalSelectionList(BaseModel):
    """
    A down-selection of SSVC Decision Points that represent an evaluation at a specific time of a Vulnerability evaluation.
    """

    schemaVersion: str = Field(
        "2.0.0", description="The schema version of this selection list."
    )

    vulnerability_id: Optional[str] = Field(
        default=None,
        description="Optional vulnerability ID associated with the selections.",
        examples=["CVE-2025-0000", "VU#999999", "GHSA-0123-4567-89ab"],
    )
    selections: list[MinimalSelection] = Field(
        default_factory=list,
        description="List of minimal selections made from decision points.",
    )
    timestamp: Optional[datetime] = Field(
        default=None, description="Timestamp of when the selections were made."
    )

    def add_selection(self, selection: MinimalSelection) -> None:
        """
        Adds a minimal selection to the list.

        Args:
            selection (MinimalSelection): The minimal selection to add.
        """
        self.selections.append(selection)


def selection_from_decision_point(decision_point: DecisionPoint) -> MinimalSelection:
    """
    Converts a decision point to a minimal selection object.

    Args:
        decision_point (DecisionPoint): The decision point to convert.

    Returns:
        MinimalSelection: The resulting minimal selection object.
    """
    data = {
        "decision_point_id": decision_point.id,
        "namespace": decision_point.namespace,
        "key": decision_point.key,
        "version": decision_point.version,
        "values": [val.key for val in decision_point.values],
    }

    return MinimalSelection(**data)


def main() -> None:
    """
    Prints example selections and their schema in JSON format.

    Returns:
        None
    """
    from ssvc.decision_points.ssvc.automatable import LATEST as dp1
    from ssvc.decision_points.ssvc.safety_impact import LATEST as dp2
    import json

    selections = MinimalSelectionList()
    selections.add_selection(selection_from_decision_point(dp1))
    selections.add_selection(selection_from_decision_point(dp2))
    selections.timestamp = datetime.now()

    print(selections.model_dump_json(indent=2, exclude_none=True))

    print("# Schema for MinimalSelectionList")
    schema = MinimalSelectionList.model_json_schema()

    # add schema extras
    schema.pop("title")
    schema["$schema"] = "https://json-schema.org/draft/2020-12/schema"
    schema["$id"] = (
        "https://certcc.github.io/SSVC/data/schema/v1/Decision_Point_Value_Selection-1-0-1.schema.json"
    )
    schema["description"] = (
        "This schema defines the structure for selecting SSVC Decision Points and their evaluated values for a given vulnerability. Each vulnerability can have multiple Decision Points, and each Decision Point can have multiple selected values when full certainty is not available."
    )

    print(json.dumps(schema, indent=2))

    schema_path = (
        "../../data/schema/v2/Decision_Point_Value_Selection-2-0-0.schema.json"
    )

    with open(schema_path, "w") as f:
        print(f"Writing schema to {schema_path}")
        json.dump(schema, f, indent=2)


if __name__ == "__main__":
    main()
