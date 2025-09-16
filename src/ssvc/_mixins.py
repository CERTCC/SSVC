#!/usr/bin/env python
"""
This module provides mixin classes for adding features to SSVC objects.
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

import os
from datetime import datetime, timezone
from typing import Any, ClassVar, Optional
from urllib.parse import urljoin

import semver
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator,
    model_validator,
)
from semver import Version

from ssvc.namespaces import NameSpace
from ssvc.registry.events import notify_registration
from ssvc.utils.defaults import (
    DEFAULT_VERSION,
    SCHEMA_BASE_URL,
    SCHEMA_VERSION,
)
from ssvc.utils.field_specs import NamespaceString, VersionString
from ssvc.utils.misc import filename_friendly, order_schema


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


class _SchemaVersioned(BaseModel):
    """
    Mixin class for version
    """

    _schema_version: ClassVar[str] = SCHEMA_VERSION
    schemaVersion: str = Field(
        ..., description="Schema version of the SSVC object"
    )

    @model_validator(mode="before")
    def set_schema_version(cls, data):
        """
        Set the schema version to the default if not provided.
        """
        if "schemaVersion" not in data:
            data["schemaVersion"] = cls._schema_version
        return data

    @classmethod
    def model_json_schema(cls, **kwargs):
        """
        Overrides schema generation to ensure it's the way we want it
        """
        schema = super().model_json_schema(**kwargs)

        schema["$schema"] = "https://json-schema.org/draft/2020-12/schema"
        schema["$id"] = cls.schema_url()
        schema["description"] = (
            f"This schema defines the structure to represent an SSVC {cls.__name__} object."
        )

        return order_schema(schema)

    @classmethod
    def schema_version_relpath(cls):
        """
        Return the schema version relative path for the object.
        """
        ver = semver.Version.parse(cls._schema_version)
        verpath = f"v{ver.major}/"

        return verpath

    @classmethod
    def schema_filename(cls):
        """
        Return the schema filename for the object.
        """
        ver = semver.Version.parse(cls._schema_version)

        # construct the filename
        filename_base = f"{cls.__name__}-{str(ver)}"
        filename_base = filename_friendly(filename_base, to_lower=False)
        ext = ".schema.json"
        filename = f"{filename_base}{ext}"
        return filename

    @classmethod
    def schema_relpath(cls):
        """
        Return the schema relative path for the object.
        """
        verpath = cls.schema_version_relpath()
        filename = cls.schema_filename()

        relpath = os.path.join(verpath, filename)
        return relpath

    @classmethod
    def schema_url(cls) -> str:
        """
        Return the schema URL for the object.
        """
        base_url = SCHEMA_BASE_URL
        id_url = urljoin(base_url, cls.schema_relpath())
        return id_url


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

    # should start with uppercase alphanumeric followed by any case alphanumeric or underscores, no spaces
    key: str = Field(
        ...,
        description="A short, non-empty string identifier for the object. Keys must start with an alphanumeric, contain only alphanumerics and `_`, and end with an alphanumeric."
        "(`T*` is explicitly grandfathered in as a valid key, but should not be used for new objects.)",
        pattern=r"^(([a-zA-Z0-9])|([a-zA-Z0-9][a-zA-Z0-9_]*[a-zA-Z0-9])|(T\*))$",
        min_length=1,
        examples=[
            "E",
            "A",
            "SI",
            "L",
            "M",
            "H",
            "Mixed_case_OK",
            "alph4num3ric",
        ],
    )


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
    definition: str


class _KeyedBaseModel(_Base, _Keyed, BaseModel):
    pass


class _GenericSsvcObject(_Base, _Versioned, _Keyed, _Namespaced, BaseModel):
    """
    Generic mixin class for SSVC objects that need to be namespaced, keyed, and versioned.
    """

    pass


class _Registered(BaseModel):
    registered: bool = Field(
        default=True, exclude=True, json_schema_extra={"exclude": True}
    )

    model_config = ConfigDict(json_schema_mode_override="serialization")

    def model_post_init(self, __context: Any, /) -> None:
        if hasattr(super(), "model_post_init"):
            super().model_post_init(__context)

        if self.registered:
            self._register()

    def _register(self) -> None:
        """Register the object."""
        notify_registration(self)


def main():
    pass


if __name__ == "__main__":
    main()
