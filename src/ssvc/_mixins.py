#!/usr/bin/env python
"""
This module provides mixin classes for adding features to SSVC objects.
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

from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator
from semver import Version

from ssvc import _schemaVersion
from ssvc.namespaces import NameSpace
from ssvc.utils.defaults import DEFAULT_VERSION
from ssvc.utils.field_specs import NamespaceString, VersionString


class _Versioned(BaseModel):
    """
    Mixin class for versioned SSVC objects.
    """

    version: VersionString = Field(default=DEFAULT_VERSION)

    @field_validator("version")
    @classmethod
    def validate_version(cls, value: str) -> str:
        """
        Validate the version field.
        Args:
            value: a string representing a version number

        Returns:
            a fully qualified version number

        Raises:
            ValueError: if the value is not a valid version number
        """
        version = Version.parse(value, optional_minor_and_patch=True)
        return version.__str__()


class _SchemaVersioned(_Versioned, BaseModel):
    """
    Mixin class for version
    """

    schemaVersion: str = _schemaVersion


class _Namespaced(BaseModel):
    """
    Mixin class for namespaced SSVC objects.
    """

    # the field definition enforces the pattern for namespaces
    # additional validation is performed in the field_validator immediately after the pattern check
    namespace: NamespaceString

    @field_validator("namespace", mode="before")
    @classmethod
    def validate_namespace(cls, value: str) -> str:
        """
        Validate the namespace field.
        The value will have already been checked against the pattern in the field definition.
        The value must be one of the official namespaces or start with 'x_'.

        Args:
            value: a string representing a namespace

        Returns:
            the validated namespace value

        Raises:
            ValueError: if the value is not a valid namespace
        """

        return NameSpace.validate(value)


class _Keyed(BaseModel):
    """
    Mixin class for keyed SSVC objects.
    """

    key: str


class _Valued(BaseModel):
    """
    Mixin class for valued SSVC objects.
    """

    values: tuple

    def __iter__(self):
        """
        Allow iteration over the values in the object.
        """
        return iter(self.values)

    def __len__(self):
        """
        Allow len() to be called on the object.
        """
        return len(self.values)


def exclude_if_none(value):
    return value is None


class _Commented(BaseModel):
    """
    Mixin class for commented SSVC objects.
    """

    _comment: Optional[str] = None

    model_config = ConfigDict(json_encoders={Optional[str]: exclude_if_none})


class _Timestamped(BaseModel):
    """
    Mixin class for timestamped SSVC objects.
    """

    timestamp: datetime = Field(
        ...,
        description="Timestamp of the SSVC object, in RFC 3339 format.",
        examples=["2025-01-01T12:00:00Z", "2025-01-02T15:30:45-04:00"],
    )

    # set the default value to the current time
    @model_validator(mode="before")
    def set_timestamp(cls, data):
        """
        Set the timestamp to the current time if not provided.
        """
        if "timestamp" not in data:
            data["timestamp"] = datetime.now().astimezone(timezone.utc)
        return data


class _Base(BaseModel):
    """
    Base class for SSVC objects.
    """

    name: str
    description: str


def main():
    pass


if __name__ == "__main__":
    main()
