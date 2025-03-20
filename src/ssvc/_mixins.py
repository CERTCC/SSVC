#!/usr/bin/env python
"""
This module provides mixin classes for adding features to SSVC objects.
"""
#  Copyright (c) 2023-2025 Carnegie Mellon University and Contributors.
#  - see Contributors.md for a full list of Contributors
#  - see ContributionInstructions.md for information on how you can Contribute to this project
#  Stakeholder Specific Vulnerability Categorization (SSVC) is
#  licensed under a MIT (SEI)-style license, please see LICENSE.md distributed
#  with this Software or contact permission@sei.cmu.edu for full terms.
#  Created, in part, with funding and support from the United States Government
#  (see Acknowledgments file). This program may include and/or can make use of
#  certain third party source code, object code, documentation and other files
#  (“Third Party Software”). See LICENSE.md for more details.
#  Carnegie Mellon®, CERT® and CERT Coordination Center® are registered in the
#  U.S. Patent and Trademark Office by Carnegie Mellon University

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator
from semver import Version

from ssvc.namespaces import NS_PATTERN, NameSpace
from . import _schemaVersion


class _Versioned(BaseModel):
    """
    Mixin class for versioned SSVC objects.
    """

    version: str = "0.0.0"
    schemaVersion: str = _schemaVersion

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


class _Namespaced(BaseModel):
    """
    Mixin class for namespaced SSVC objects.
    """

    # the field definition enforces the pattern for namespaces
    # additional validation is performed in the field_validator immediately after the pattern check
    namespace: str = Field(pattern=NS_PATTERN, min_length=3, max_length=25)

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
