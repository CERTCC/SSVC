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
from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, Field, model_validator

from ssvc._mixins import VersionField
from ssvc.decision_points.base import DecisionPoint
from ssvc.namespaces import NamespaceString

SCHEMA_VERSION = "2.0.0"


class MinimalSelection(BaseModel):
    """
    A minimal selection object that contains the decision point ID and the selected options.
    This is used to transition from an SSVC decision point to a selection.
    """

    namespace: NamespaceString = Field(
        ...,
        description="The namespace of the decision point.",
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
        description="A list of selected value keys from the decision point values.",
        min_length=1,
        examples=[
            ["N", "Y"],
            ["A", "B", "C"],
        ],  # Example values
    )


class MinimalSelectionList(BaseModel):
    """
    A down-selection of SSVC Decision Points that represent an evaluation at a specific time of a Vulnerability evaluation.
    """

    model_config = ConfigDict(extra="allow")
    schemaVersion: Literal[SCHEMA_VERSION] = Field(
        ...,
        description="The schema version of this selection list.",
    )

    vulnerability_id: Optional[str] = Field(
        default=None,
        description="Optional vulnerability ID associated with the selections.",
        examples=["CVE-2025-0000", "VU#999999", "GHSA-0123-4567-89ab"],
        min_length=1,
    )
    selections: list[MinimalSelection] = Field(
        ...,
        description="List of minimal selections made from decision points.",
        min_length=1,
    )
    timestamp: datetime = Field(
        ...,
        description="Timestamp of when the selections were made, in RFC 3339 format.",
        examples=["2025-01-01T12:00:00Z", "2025-01-02T15:30:45-04:00"],
    )

    @model_validator(mode="before")
    def set_schema_version(cls, data):
        # If schemaVersion is missing, add it
        if "schemaVersion" not in data:
            data["schemaVersion"] = SCHEMA_VERSION
        return data

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

    a1 = selection_from_decision_point(dp1)
    a2 = selection_from_decision_point(dp2)
    selections = MinimalSelectionList(
        schemaVersion=SCHEMA_VERSION, selections=[a1, a2], timestamp=datetime.now()
    )

    print(selections.model_dump_json(indent=2, exclude_none=True))

    print("# Schema for MinimalSelectionList")
    schema = MinimalSelectionList.model_json_schema()

    # add schema extras
    schema.pop("title")
    schema["$schema"] = "https://json-schema.org/draft/2020-12/schema"
    schema["$id"] = (
        "https://certcc.github.io/SSVC/data/schema/v2/Decision_Point_Value_Selection-2-0-0.schema.json"
    )
    schema["description"] = (
        "This schema defines the structure for selecting SSVC Decision Points and their evaluated values for a given vulnerability. Each vulnerability can have multiple Decision Points, and each Decision Point can have multiple selected values when full certainty is not available."
    )

    # preferred order of fields, just setting for convention
    preferred_order = [
        "$schema",
        "$id",
        "title",
        "description",
        "schemaVersion",
        "type",
        "properties",
        "required",
        "additionalProperties",
        "$defs",
    ]

    # create a new dict with the preferred order of fields first
    ordered_fields = {k: schema[k] for k in preferred_order if k in schema}
    # add the rest of the fields in their original order
    for k in schema:
        if k not in ordered_fields:
            ordered_fields[k] = schema[k]

    print(json.dumps(ordered_fields, indent=2))

    # find local path to this file
    import os

    current_dir = os.path.dirname(os.path.abspath(__file__))
    # construct the path to the schema file
    schema_path = (
        "../../data/schema/v2/Decision_Point_Value_Selection-2-0-0.schema.json"
    )
    schema_path = os.path.abspath(os.path.join(current_dir, schema_path))

    with open(schema_path, "w") as f:
        print(f"Writing schema to {schema_path}")
        json.dump(ordered_fields, f, indent=2)


if __name__ == "__main__":
    main()
