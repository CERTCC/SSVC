"""Response Models for SSVC API."""

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

from pydantic import RootModel, model_validator

from ssvc.api.response_models._type_defs import (DecisionPointDictType, DecisionPointValuesListType,
                                                 DecisionTableDictType, KeyDictType, NamespaceDictType, StringsListType,
                                                 TypesDictType, VersionDictType)
from ssvc.decision_points.base import DecisionPoint, DecisionPointValue
from ssvc.decision_tables.base import DecisionTable


class DecisionPointListResponse(RootModel[list[DecisionPoint]]):
    """Response model for a list of DecisionPoint objects."""

    @model_validator(mode="before")
    @classmethod
    def model_validate(cls, value):
        if not isinstance(value, list):
            raise TypeError("Value must be a list")

        for item in value:
            if not isinstance(item, DecisionPoint):
                raise TypeError(
                    f"Item '{item}' must be a DecisionPoint object"
                )

        return value


class DecisionPointValueListResponse(RootModel[DecisionPointValuesListType]):
    """Response model for a list of DecisionPointValue objects."""

    @model_validator(mode="before")
    @classmethod
    def model_validate(cls, value):
        if not isinstance(value, list):
            raise TypeError("Value must be a list")

        for item in value:
            if not isinstance(item, DecisionPointValue):
                raise TypeError(
                    f"Item '{item}' must be a DecisionPointValue object"
                )

        return value


class DecisionPointDictResponse(RootModel[DecisionPointDictType]):
    """A dictionary of DecisionPoint objects with keys as 'namespace:key:version'."""

    @model_validator(mode="before")
    @classmethod
    def model_validate(cls, value):
        if not isinstance(value, dict):
            raise TypeError("Value must be a dictionary")

        for k, obj in value.items():
            if not isinstance(k, str):
                raise TypeError(f"Key '{k}' must be a string")
            if not isinstance(obj, DecisionPoint):
                raise TypeError(f"Value for key '{k}' must be a DecisionPoint")

            # key must be the value.id
            if k != obj.id:
                raise ValueError(
                    f"Key '{k}' does not match DecisionPoint id '{obj.id}'"
                )

        return value


class DecisionTableDictResponse(RootModel[DecisionTableDictType]):
    """A dictionary of DecisionTable objects with keys as 'namespace:key:version'."""

    @model_validator(mode="before")
    @classmethod
    def model_validate(cls, value):
        if not isinstance(value, dict):
            raise TypeError("Value must be a dictionary")

        for k, obj in value.items():
            if not isinstance(k, str):
                raise TypeError(f"Key '{k}' must be a string")
            if not isinstance(obj, DecisionTable):
                raise TypeError(f"Value for key '{k}' must be a DecisionTable")

            # key must be the value.id
            if k != obj.id:
                raise ValueError(
                    f"Key '{k}' does not match DecisionPoint id '{obj.id}'"
                )

        return value


class ListOfStringsResponse(RootModel[StringsListType]):
    """Response model for a list of strings."""

    @model_validator(mode="before")
    @classmethod
    def model_validate(cls, value):
        if not isinstance(value, list):
            raise TypeError("Value must be a list")

        for item in value:
            if not isinstance(item, str):
                raise TypeError(f"Item '{item}' must be a string")

        return value


class TypesDictResponse(RootModel[TypesDictType]):
    """Response model for the list of object types."""

    @model_validator(mode="before")
    @classmethod
    def model_validate(cls, value):
        if not isinstance(value, dict):
            raise TypeError("Value must be a dictionary")

        if "types" not in value:
            raise ValueError('Top-level key must be "types"')

        if not isinstance(value["types"], list):
            raise TypeError('"types" must be a list')

        for item in value["types"]:
            if not isinstance(item, str):
                raise TypeError(f'Object type "{item}" must be a string')

        return value


class NamespaceDictResponse(RootModel[NamespaceDictType]):
    """Response model for the namespaces of object types."""

    @model_validator(mode="before")
    @classmethod
    def model_validate(cls, value):
        # validators:
        # top key is "types"
        # then the keys of that dict are object types
        # then the keys of that dict is "namespaces"
        # and the value of that is a list of strings
        if not isinstance(value, dict):
            raise TypeError("Value must be a dictionary")

        if "types" not in value:
            raise ValueError('Top-level key must be "types"')

        if not isinstance(value["types"], dict):
            raise TypeError('"types" must be a dictionary')

        for objtype, obj in value["types"].items():
            if not isinstance(obj, dict):
                raise TypeError(
                    f'Value for object type "{objtype}" must be a dictionary'
                )

            if "namespaces" not in obj:
                raise ValueError(
                    f'Key "namespaces" missing for object type "{objtype}"'
                )

            if not isinstance(obj["namespaces"], list):
                raise TypeError(
                    f'"namespaces" for object type "{objtype}" must be a list'
                )

            for ns in obj["namespaces"]:
                if not isinstance(ns, str):
                    raise TypeError(
                        f'Namespace "{ns}" for object type "{objtype}" must be a string'
                    )

        return value


class KeyDictResponse(
    RootModel[KeyDictType],
):
    """Response model for key list grouped by object type and namespace."""

    # validators:
    # top key is "types"
    # then the keys of that dict are object types
    # then the keys of that dict is "namespaces"
    # then the keys of that dict are namespace strings
    # then the keys of that dict are "keys"
    # and the value of that is a list of strings
    @model_validator(mode="before")
    @classmethod
    def model_validate(cls, value):
        if not isinstance(value, dict):
            raise TypeError("Value must be a dictionary")

        if "types" not in value:
            raise ValueError('Top-level key must be "types"')

        if not isinstance(value["types"], dict):
            raise TypeError('"types" must be a dictionary')

        for objtype, obj in value["types"].items():
            if not isinstance(objtype, str):
                raise TypeError(f'Object type "{objtype}" must be a string')

            if not isinstance(obj, dict):
                raise TypeError(
                    f'Value for object type "{objtype}" must be a dictionary'
                )

            if "namespaces" not in obj:
                raise ValueError(
                    f'Key "namespaces" missing for object type "{objtype}"'
                )

            if not isinstance(obj["namespaces"], dict):
                raise TypeError(
                    f'"namespaces" for object type "{objtype}" must be a dictionary'
                )

            for namespace, ns in obj["namespaces"].items():
                if not isinstance(ns, dict):
                    raise TypeError(
                        f'Value for namespace "{namespace}" in object type "{objtype}" must be a dictionary'
                    )

                if "keys" not in ns:
                    raise ValueError(
                        f'Key "keys" missing for namespace "{namespace}" in object type "{objtype}"'
                    )

                if not isinstance(ns["keys"], list):
                    raise TypeError(
                        f'"keys" for namespace "{namespace}" in object type "{objtype}" must be a list'
                    )
                for key in ns["keys"]:
                    if not isinstance(key, str):
                        raise TypeError(
                            f'Key "{key}" in namespace "{namespace}" of object type "{objtype}" must be a string'
                        )

        return value


class VersionDictResponse(RootModel[VersionDictType]):
    """Response model for version list grouped by object type, namespace, and key."""

    @model_validator(mode="before")
    @classmethod
    def model_validate(cls, value):
        # validators:
        # top key is "types"
        # then the keys of that dict are object types
        # then the keys of that dict is "namespaces"
        # then the keys of that dict are namespace strings
        # then the keys of that dict are "keys"
        # then the keys of that dict are key strings
        # then the keys of that dict are "versions"
        # and the value of that is a list of strings
        if not isinstance(value, dict):
            raise TypeError("Value must be a dictionary")

        if "types" not in value:
            raise ValueError('Top-level key must be "types"')

        if not isinstance(value["types"], dict):
            raise TypeError('"types" must be a dictionary')

        for objtype, obj in value["types"].items():
            if not isinstance(objtype, str):
                raise TypeError(f'Object type "{objtype}" must be a string')

            if not isinstance(obj, dict):
                raise TypeError(
                    f'Value for object type "{objtype}" must be a dictionary'
                )

            if "namespaces" not in obj:
                raise ValueError(
                    f'Key "namespaces" missing for object type "{objtype}"'
                )

            if not isinstance(obj["namespaces"], dict):
                raise TypeError(
                    f'"namespaces" for object type "{objtype}" must be a dictionary'
                )

            for namespace, ns in obj["namespaces"].items():
                if not isinstance(ns, dict):
                    raise TypeError(
                        f'Value for namespace "{namespace}" in object type "{objtype}" must be a dictionary'
                    )

                if "keys" not in ns:
                    raise ValueError(
                        f'Key "keys" missing for namespace "{namespace}" in object type "{objtype}"'
                    )

                if not isinstance(ns["keys"], dict):
                    raise TypeError(
                        f'"keys" for namespace "{namespace}" in object type "{objtype}" must be a dictionary'
                    )

                for key, k in ns["keys"].items():
                    if not isinstance(k, dict):
                        raise TypeError(
                            f'Value for key "{key}" in namespace "{namespace}" of object type "{objtype}" must be a dictionary'
                        )
                    if "versions" not in k:
                        raise ValueError(
                            f'Key "versions" missing for key "{key}" in namespace "{namespace}" of object type "{objtype}"'
                        )
                    if not isinstance(k["versions"], list):
                        raise TypeError(
                            f'"versions" for key "{key}" in namespace "{namespace}" of object type "{objtype}" must be a list'
                        )
                    for version in k["versions"]:
                        if not isinstance(version, str):
                            raise TypeError(
                                f'Version "{version}" in key "{key}" of namespace "{namespace}" in object type "{objtype}" must be a string'
                            )

        return value
