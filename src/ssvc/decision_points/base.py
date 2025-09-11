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
from typing import ClassVar, Literal

from pydantic import BaseModel, ConfigDict, model_validator

from ssvc._mixins import (
    _Commented,
    _GenericSsvcObject,
    _KeyedBaseModel,
    _Registered,
    _SchemaVersioned,
    _Valued,
)
from ssvc.utils.defaults import FIELD_DELIMITER

logger = logging.getLogger(__name__)

SCHEMA_VERSION = "2.0.0"


class DecisionPointValue(_Commented, _KeyedBaseModel, BaseModel):
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


class DecisionPoint(
    _Registered,
    _Valued,
    _SchemaVersioned,
    _GenericSsvcObject,
    _Commented,
    BaseModel,
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
    _schema_version: ClassVar[str] = SCHEMA_VERSION
    schemaVersion: Literal[SCHEMA_VERSION]
    values: tuple[DecisionPointValue, ...]
    model_config = ConfigDict(revalidate_instances="always")

    def __str__(self):
        return FIELD_DELIMITER.join([self.namespace, self.key, self.version])

    @property
    def id(self) -> str:
        f"""
        Return an identity string for the DecisionPoint, combining namespace, key, and version into a global unique identifier.
        
        Returns:
            str: A string representation of the DecisionPoint in the format "namespace{FIELD_DELIMITER}key{FIELD_DELIMITER}version".
        """
        id_parts = (self.namespace, self.key, self.version)

        return FIELD_DELIMITER.join(id_parts)

    @property
    def value_dict(self) -> dict[str, DecisionPointValue]:
        """
        Return a list of value IDs for the DecisionPoint.

        Returns:
            list: A list of strings, each representing a value ID in the format "namespace:key:version:value".

        """
        value_dict = {}
        for value in self.values:
            value_id = FIELD_DELIMITER.join([self.id, value.key])
            value_dict[value_id] = value
        return value_dict

    @property
    def str(self) -> str:
        """
        Return the DecisionPoint represented as a short string.

        Returns:
            str: A string representation of the DecisionPoint, in the format "namespace:key:version".

        """
        return self.__str__()

    @model_validator(mode="before")
    def _set_schema_version(cls, data: dict) -> dict:
        """
        Set the schema version to the default if not provided.
        """
        if "schemaVersion" not in data:
            data["schemaVersion"] = SCHEMA_VERSION
        return data

    @model_validator(mode="after")
    def _validate_values(self):
        # confirm that value keys are unique
        seen = dict()
        for value in self.values:
            if value.key in seen:
                raise ValueError(
                    f"Duplicate key found in {self.id}: {value.key} ({value.name} and {seen[value.key]})"
                )
            else:
                seen[value.key] = value.name

        # if we got here, all good
        return self

    @property
    def value_summaries(self) -> list[str]:
        """
        Return a list of value summaries.
        """
        return list(self.value_dict.keys())



def main():
    print(
        "Please use doctools.py for schema generation and unit tests for verification"
    )


if __name__ == "__main__":
    main()
