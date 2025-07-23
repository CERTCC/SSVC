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

from pydantic import (
    AnyUrl,
    BaseModel,
    ConfigDict,
    Field,
    field_validator,
    model_validator,
)

from ssvc._mixins import (
    _Base,
    _Keyed,
    _Namespaced,
    _Timestamped,
    _Valued,
    _Versioned,
)
from ssvc.decision_points.base import DecisionPoint
from ssvc.utils.field_specs import TargetIdList

SCHEMA_VERSION = "2.0.0"


class MinimalDecisionPointValue(_Base, _Keyed, BaseModel):
    """A minimal representation of a decision point value."""

    @model_validator(mode="before")
    def set_optional_fields(cls, data):
        if "name" not in data:
            data["name"] = ""
        if "description" not in data:
            data["description"] = ""

        return data


class Selection(_Valued, _Versioned, _Keyed, _Namespaced, _Base, BaseModel):
    """
    A minimal selection object that contains the decision point ID and the selected values.
    This is used to transition from an SSVC decision point to a selection.
    """

    model_config = ConfigDict(extra="forbid")

    values: tuple[MinimalDecisionPointValue, ...] = Field(
        ...,
        description="A list of selected value keys from the decision point values.",
        min_length=1,
        examples=[
            [{"key": "N"}, {"key": "Y"}],
            [{"key": "A"}, {"key": "B"}, {"key": "C"}],
        ],  # Example values
    )

    @model_validator(mode="before")
    def set_optional_fields(cls, data):
        if "name" not in data:
            data["name"] = ""
        if "description" not in data:
            data["description"] = ""
        return data

    def model_json_schema(cls, **kwargs):
        schema = super().model_json_schema(**kwargs)
        not_required = ["name", "description"]
        if "required" in schema and isinstance(schema["required"], list):
            # remove description from required list if it exists
            schema["required"] = [
                field for field in schema["required"] if field not in not_required
            ]
        return schema


class Reference(BaseModel):
    """A reference to a resource that provides additional context about the decision points or selections."""

    model_config = ConfigDict(extra="forbid")

    uri: AnyUrl
    description: str

    # override schema generation to ensure that description is not required
    def model_json_schema(cls, **kwargs):
        schema = super().model_json_schema(**kwargs)
        not_required = ["description"]
        if "required" in schema and isinstance(schema["required"], list):
            # remove description from required list if it exists
            schema["required"] = [
                field for field in schema["required"] if field not in not_required
            ]
        return schema


class SelectionList(_Timestamped, BaseModel):
    """
    A down-selection of SSVC Decision Points that represent an evaluation at a specific time of a Vulnerability evaluation.
    """

    model_config = ConfigDict(extra="forbid")
    schemaVersion: Literal[SCHEMA_VERSION] = Field(
        ...,
        description="The schema version of this selection list.",
    )

    target_ids: TargetIdList = Field(
        default_factory=list,
        description="Optional list of identifiers for the item or items "
        "(vulnerabilities, reports, advisories, systems, assets, etc.) "
        "being evaluated by these selections.",
        examples=[
            ["CVE-1900-0000"],
            ["VU#999999", "GHSA-0123-4567-89ab"],
        ],
        min_length=1,
    )
    selections: list[Selection] = Field(
        ...,
        description="List of selections made from decision points. Each selection item corresponds to "
        "value keys contained in a specific decision point identified by its namespace, key, and version. "
        "Note that selection objects are deliberately minimal objects and do not contain the full decision point details.",
        min_length=1,
    )
    timestamp: datetime = Field(
        ...,
        description="Timestamp of the selections, in RFC 3339 format.",
        examples=["2025-01-01T12:00:00Z", "2025-01-02T15:30:45-04:00"],
    )
    resources: list[Reference] = Field(
        default_factory=list,
        min_length=1,
        description="A list of references to resources that provide additional context about the decision points found in this selection.",
        examples=[
            [
                {
                    "uri": "https://example.com/decision_points",
                    "description": "Documentation for a set of decision points",
                },
                {
                    "uri": "https://example.org/definitions/dp2.json",
                    "description": "JSON representation of decision point 2",
                },
                {
                    "uri": "https://example.com/ssvc/x_com.example/decision_points.json",
                    "description": "A JSON file containing extension decision points in the x_com.example namespace",
                },
            ],
        ],
    )
    references: list[Reference] = Field(
        default_factory=list,
        min_length=1,
        description="A list of references to resources that provide additional context about the specific values selected.",
        examples=[
            [
                {
                    "uri": "https://example.com/report",
                    "description": "A report on which the selections were based",
                },
            ]
        ],
    )

    @model_validator(mode="before")
    def set_schema_version(cls, data):
        if "schemaVersion" not in data:
            data["schemaVersion"] = SCHEMA_VERSION
        return data

    # target_ids should be a non-empty list if not None
    @field_validator("target_ids", mode="before")
    @classmethod
    def validate_target_ids(cls, value: Optional[list[str]]) -> Optional[list[str]]:
        """
        Validate the target_ids field.
        If target_ids is provided, it must be a non-empty list of strings.
        """
        if value is None:
            return []
        if not isinstance(value, list):
            raise ValueError("target_ids must be a list of strings.")
        if len(value) == 0:
            raise ValueError("target_ids must be a non-empty list of strings.")
        for item in value:
            if not isinstance(item, str):
                raise ValueError("Each target_id must be a string.")
        return value

    def add_selection(self, selection: Selection) -> None:
        """
        Adds a minimal selection to the list.

        Args:
            selection (Selection): The minimal selection to add.
        """
        self.selections.append(selection)

    # override schema generation to ensure it's the way we want it
    @classmethod
    def model_json_schema(cls, **kwargs):
        schema = super().model_json_schema(**kwargs)

        schema["title"] = "Decision Point Value Selection List"
        schema["$schema"] = "https://json-schema.org/draft/2020-12/schema"
        schema["$id"] = (
            "https://certcc.github.io/SSVC/data/schema/v2/Decision_Point_Value_Selection-2-0-0.schema.json"
        )
        schema["description"] = (
            "This schema defines the structure for selecting SSVC Decision Points and their evaluated values "
            "for a given vulnerability. Each vulnerability can have multiple Decision Points, and each "
            "Decision Point can have multiple selected values when full certainty is not available."
        )

        non_required_fields = [
            "name",
            "description",
            "target_ids",
            "resources",
            "references",
        ]

        # remove non-required fields from the required list
        if "required" in schema and isinstance(schema["required"], list):
            schema["required"] = [
                field
                for field in schema["required"]
                if field not in non_required_fields
            ]

        # dive in to find all the required lists in the schema
        # don't forget the defs
        if "$defs" in schema:
            for prop in schema["$defs"].values():
                if isinstance(prop, dict) and "required" in prop:
                    # remove non-required fields from the required list
                    prop["required"] = [
                        r for r in prop["required"] if r not in non_required_fields
                    ]

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

        return ordered_fields


def selection_from_decision_point(decision_point: DecisionPoint) -> Selection:
    """
    Converts a decision point to a minimal selection object.

    Args:
        decision_point (DecisionPoint): The decision point to convert.

    Returns:
        Selection: The resulting minimal selection object.
    """
    data = {
        "namespace": decision_point.namespace,
        "key": decision_point.key,
        "version": decision_point.version,
        "values": [{"key": val.key} for val in decision_point.values],
    }

    return Selection(**data)


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
    selections = SelectionList(
        schemaVersion=SCHEMA_VERSION,
        selections=[a1, a2],
        timestamp=datetime.now(),
        target_ids=["CVE-2025-0001", "GHSA-0123-4567-89ab"],
        references=[
            Reference(
                uri="https://example.com/report",
                description="A report on which the selections were based",
            )
        ],
    )

    print(selections.model_dump_json(indent=2, exclude_none=True, exclude_unset=True))

    print("# Schema for SelectionList")
    schema = SelectionList.model_json_schema()

    print(json.dumps(schema, indent=2))

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
        json.dump(schema, f, indent=2)


if __name__ == "__main__":
    main()
