#!/usr/bin/env python

"""
Defines the formatting for SSVC Decision Points.
"""
#  Copyright (c) 2023-2025 Carnegie Mellon University.
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

import logging

from pydantic import BaseModel, ConfigDict, Field, model_validator

from ssvc._mixins import (
    _Base,
    _Commented,
    _Keyed,
    _Namespaced,
    _SchemaVersioned,
    _Valued,
    _Versioned,
)

logger = logging.getLogger(__name__)


REGISTERED_DECISION_POINTS = []
FIELD_DELIMITER = ":"


class Registry(BaseModel):
    registry: dict[str, object] = Field(default_factory=dict)

    def __iter__(self) -> object:
        return iter(self.registry.values())

    def __getitem__(self, key: str) -> object:
        return self.registry[key]

    def __setitem__(self, key: str, value: object) -> None:

        if key in self.registry:
            # are the values the same?
            registered = self.registry[key].model_dump_json()
            value_dumped = value.model_dump_json()
            if registered == value_dumped:
                logger.warning(f"Duplicate key {key} with the same value, ignoring.")
                return

            logger.warning(f"Duplicate key {key}:")
            logger.warning(f"\t{registered}")
            logger.warning(f"\t{value_dumped}")
            raise KeyError(f"Duplicate key {key}")

        self.registry[key] = value

    def __contains__(self, key: str) -> bool:
        return key in self.registry

    def reset_registry(self) -> None:
        self.registry = {}

    # convenience alias
    def clear(self) -> None:
        self.reset_registry()


class DecisionPointRegistry(Registry, BaseModel):
    """
    A dictionary of decision points.
    """

    registry: dict[str, "DecisionPoint"] = Field(default_factory=dict)


class DecisionPointValueRegistry(Registry, BaseModel):
    """
    A dictionary of decision point values.
    """

    registry: dict[str, "DecisionPointValue"] = Field(default_factory=dict)


def register(dp):
    """
    Register a decision point.
    """

    # register the values
    for value_str, value_summary in dp.value_summaries_dict.items():
        DPV_REGISTRY[value_str] = value_summary

    key = dp.str
    DP_REGISTRY[key] = dp
    REGISTERED_DECISION_POINTS.append(dp)


def _reset_registered():
    """
    Reset the registered decision points.
    """
    global DPV_REGISTRY
    global DP_REGISTRY
    global REGISTERED_DECISION_POINTS

    DPV_REGISTRY.reset_registry()
    DP_REGISTRY.reset_registry()
    REGISTERED_DECISION_POINTS = []


class DecisionPointValue(_Base, _Keyed, _Commented, BaseModel):
    """
    Models a single value option for a decision point.

    Each value should have the following attributes:

    - name (str): A name
    - description (str): A description
    - key (str): A key (a short, unique string) that can be used to identify the value in a shorthand way
    - _comment (str): An optional comment that will be included in the object.
    """

    def __str__(self):
        return self.name


class ValueSummary(_Versioned, _Keyed, _Namespaced, BaseModel):
    """
    A ValueSummary is a simple object that represents a single value for a decision point.
    It includes the parent decision point's key, version, namespace, and the value key.
    These can be used to reference a specific value in a decision point.
    """

    value: str

    def __str__(self):
        s = FIELD_DELIMITER.join([self.namespace, self.key, self.version, self.value])
        return s

    @property
    def str(self):
        """
        Return the ValueSummary as a string.

        Returns:
            str: A string representation of the ValueSummary, in the format "namespace:key:version:value".

        """
        return self.__str__()


class DecisionPoint(
    _Valued, _Keyed, _SchemaVersioned, _Namespaced, _Base, _Commented, BaseModel
):
    """
    Models a single decision point as a list of values.

    Decision points should have the following attributes:

    - name (str): The name of the decision point
    - description (str): A description of the decision point
    - version (str): A semantic version string for the decision point
    - namespace (str): The namespace (a short, unique string): For example, "ssvc" or "cvss" to indicate the source of the decision point
    - key (str): A key (a short, unique string within the namespace) that can be used to identify the decision point in a shorthand way
    - values (tuple): A tuple of DecisionPointValue objects
    """

    values: tuple[DecisionPointValue, ...]

    model_config = ConfigDict(revalidate_instances="always")

    def __str__(self):
        return FIELD_DELIMITER.join([self.namespace, self.key, self.version])

    @property
    def str(self) -> str:
        """
        Return the DecisionPoint represented as a short string.

        Returns:
            str: A string representation of the DecisionPoint, in the format "namespace:key:version".

        """
        return self.__str__()

    @model_validator(mode="after")
    def _register(self):
        """
        Register the decision point.
        """
        register(self)
        return self

    @property
    def value_summaries(self) -> list[ValueSummary]:
        """
        Return a list of value summaries.
        """
        return list(self.value_summaries_dict.values())

    @property
    def value_summaries_dict(self) -> dict[str, ValueSummary]:
        """
        Return a dictionary of value summaries keyed by the value key.
        """
        summaries = {}
        for value in self.values:
            summary = ValueSummary(
                key=self.key,
                version=self.version,
                namespace=self.namespace,
                value=value.key,
            )
            key = summary.str
            summaries[key] = summary

        return summaries

    @property
    def value_summaries_str(self):
        """
        Return a list of value summaries as strings.

        Returns:
            list: A list of strings, each representing a value summary in the format "namespace:key:version:value".

        """
        return list(self.value_summaries_dict.keys())

    @property
    def enumerated_values(self) -> dict[int, str]:
        """
        Return a list of enumerated values.
        """
        return {i: v.str for i, v in enumerate(self.value_summaries)}


DP_REGISTRY = DecisionPointRegistry()
DPV_REGISTRY = DecisionPointRegistry()


def main():
    opt_none = DecisionPointValue(
        name="None", key="N", description="No exploit available"
    )
    opt_poc = DecisionPointValue(
        name="PoC", key="P", description="Proof of concept exploit available"
    )
    opt_active = DecisionPointValue(
        name="Active", key="A", description="Active exploitation observed"
    )
    opts = [opt_none, opt_poc, opt_active]

    dp = DecisionPoint(
        _comment="This is an optional comment that will be included in the object.",
        values=opts,
        name="Exploitation",
        description="Is there an exploit available?",
        key="E",
        version="1.0.0",
    )

    print(dp.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
