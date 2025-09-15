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
from typing import ClassVar, Literal, Optional

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
    _GenericSsvcObject,
    _Keyed,
    _SchemaVersioned,
    _Timestamped,
    _Valued,
)
from ssvc.decision_points.base import DecisionPoint
from ssvc.utils.field_specs import TargetIdList, VersionString
from ssvc.utils.misc import order_schema

SCHEMA_VERSION = "2.0.0"


class MinimalDecisionPointValue(_Keyed, _Base, BaseModel):
    """
    A minimal representation of a decision point value.
    Intended to parallel the DecisionPointValue object, but with fewer required fields.
    A decision point value is uniquely identified within a decision point by its key.
    Globally, the combination of Decision Point namespace, key, and version coupled with the value key
    uniquely identifies a value across all decision points and values.
    Other required fields in the DecisionPointValue object, such as name and description, are optional here.
    """

    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    def set_optional_fields(cls, data):
        if "name" not in data:
            data["name"] = ""
        if "description" not in data:
            data["definition"] = ""

        return data

    @model_validator(mode="after")
    def validate_values(cls, data):
        """
        If name or description are empty strings, set them to None so that
        they are not included in the JSON output when serialized using model_dump_json.
        """
        if not data.name:
            data.name = None
        if not data.definition:
            data.definition = None
        return data


class Selection(_Valued, _GenericSsvcObject, BaseModel):
    """
    A minimal selection object that contains the decision point ID and the selected values.
    While the Selection object parallels the DecisionPoint object, it is intentionally minimal, with
    fewer required fields and no additional metadata, as it is meant to represent a selection made from a
    previously defined decision point. The expectation is that a Selection object will usually have
    fewer values than the original decision point, as it represents a specific evaluation
    at a specific time and may therefore rule out some values that were previously considered.
    Other fields like name and description may be copied from the decision point, but are not required.
    """

    model_config = ConfigDict(extra="forbid")

    # _Versioned has a default value, but here we don't want to have a default
    version: VersionString

    values: tuple[MinimalDecisionPointValue, ...] = Field(
        ...,
        description="A list of selected value keys from the decision point values.",
        min_length=1,
        examples=[
            [{"key": "N"}, {"key": "Y"}],
            [{"key": "A"}, {"key": "B"}, {"key": "C"}],
        ],  # Example values
    )

    # class method to convert a decision point to a selection
    @classmethod
    def from_decision_point(
        cls, decision_point: DecisionPoint, include_optional: bool = False
    ) -> "Selection":
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
            "values": [
                MinimalDecisionPointValue(key=val.key)
                for val in decision_point.values
            ],
        }
        for attr in ("name", "description"):
            if hasattr(decision_point, attr):
                data[attr] = getattr(decision_point, attr)

        return cls(**data)

    @model_validator(mode="before")
    def set_optional_fields(cls, data):
        if "name" not in data:
            data["name"] = ""
        if "description" not in data:
            data["definition"] = ""
        return data

    @model_validator(mode="after")
    def validate_values(cls, data):
        if not data.name:
            data.name = None
        if not data.definition:
            data.definition = None
        return data

    def model_json_schema(cls, **kwargs):
        schema = super().model_json_schema(**kwargs)
        not_required = ["name", "definition"]
        if "required" in schema and isinstance(schema["required"], list):
            # remove description from required list if it exists
            schema["required"] = [
                field
                for field in schema["required"]
                if field not in not_required
            ]
        return schema


class Reference(BaseModel):
    """
    A reference to a resource that provides additional context about the decision points or selections.
    This object is intentionally minimal and contains only the URL and an optional description.
    """

    model_config = ConfigDict(extra="forbid")

    uri: AnyUrl
    summary: str

    # override schema generation to ensure that description is not required
    def model_json_schema(cls, **kwargs):
        schema = super().model_json_schema(**kwargs)
        not_required = ["summary"]
        if "required" in schema and isinstance(schema["required"], list):
            # remove description from required list if it exists
            schema["required"] = [
                field
                for field in schema["required"]
                if field not in not_required
            ]
        return schema


class SelectionList(_SchemaVersioned, _Timestamped, BaseModel):
    """
    A list decision point selections that represent an evaluation at a specific time of evaluation.
    Individual selections are derived from decision points, and each selection
    contains a minimal representation of the decision point and the selected values.

    A SelectionList requires a timestamp in RFC 3339 format, which indicates when the selections were made.

    Optional fields include

    - `target_ids`: If present, a non-empty list of identifiers for the item or items being evaluated.
    - `decision_point_resources`: If present, a non-empty list of resources that provide information related to the decision points
        found in this selection. Resources point to documentation, JSON files, or other relevant information that
        describe what the decision points are and how they should be interpreted.
    - `references`: If present, a non-empty list of resources that provide additional context about the specific values selected.
        References point to reports, advisories, or other relevant information that describe why the selected values were chosen.
    """

    model_config = ConfigDict(extra="forbid")
    _schema_version: ClassVar[str] = SCHEMA_VERSION
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
        json_schema_extra={"uniqueItems": True},
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
    decision_point_resources: list[Reference] = Field(
        default_factory=list,
        min_length=1,
        description="A list of resources that provide additional context about the decision points found in this selection.",
        examples=[
            [
                {
                    "uri": "https://example.com/decision_points",
                    "summary": "Documentation for a set of decision points",
                },
                {
                    "uri": "https://example.org/definitions/dp2.json",
                    "summary": "JSON representation of decision point 2",
                },
                {
                    "uri": "https://example.com/ssvc/x_com.example/decision_points.json",
                    "summary": "A JSON file containing extension decision points in the x_com.example namespace",
                },
            ],
        ],
    )
    references: list[Reference] = Field(
        default_factory=list,
        min_length=1,
        description="A list of references that provide additional context about the specific values selected.",
        examples=[
            [
                {
                    "uri": "https://example.com/report",
                    "summary": "A report on which the selections were based",
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
    def validate_target_ids(
        cls, value: Optional[list[str]]
    ) -> Optional[list[str]]:
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
        if len(value) != len(set(value)):
            raise ValueError("target_ids must not contain duplicates.")
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

        non_required_fields = [
            "name",
            "definition",
            "target_ids",
            "decision_point_resources",
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
                        r
                        for r in prop["required"]
                        if r not in non_required_fields
                    ]

        return order_schema(schema)


def main() -> None:
    print(
        "Please use doctools.py for schema generation and unit tests for verification"
    )


if __name__ == "__main__":
    main()
