#!/usr/bin/env python
"""
Work in progress on an experimental registry object for SSVC.
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

import logging
from typing import Any, Literal, Optional

from pydantic import BaseModel, Field, model_validator

from ssvc._mixins import (
    _Base,
    _GenericSsvcObject,
    _KeyedBaseModel,
    _SchemaVersioned,
    _Valued,
)
from ssvc.utils.field_specs import VersionString

logger = logging.getLogger(__name__)

SCHEMA_VERSION: str = "2.0.0"
logger.debug(f"Using schema version {SCHEMA_VERSION} for SsvcObjectRegistry.")


def lookup_type(module: str, type_name: str):
    """
    Lookup a type by its name in the specified module.
    Args:
        module: The module to search in.
        type_name: The name of the type to lookup.

    Returns:
        The type if found, otherwise None.
    """
    import sys

    mod = sys.modules.get(module)
    if mod is None:
        return None
    return getattr(mod, type_name, None)


def _get_obj_type(obj: object) -> str:
    """
    Get the type of the object for registry purposes.
    Args:
        obj: The object to check.

    Returns:
        str: If the object is of a recognized type, return the name of the recognized type.
             Otherwise, return "other".
    """
    objtype = "other"  # default type if not recognized
    recognized_types = [
        lookup_type("ssvc.decision_points.base", "DecisionPoint"),
        lookup_type("ssvc.decision_tables.base", "DecisionTable"),
    ]
    for t in recognized_types:
        if t is not None and isinstance(obj, t):
            objtype = t.__name__
            break
    return objtype


class NonValuedVersion(BaseModel):
    version: VersionString
    obj: object


class ValuedVersion(BaseModel):
    version: VersionString
    obj: object
    values: dict[str, _KeyedBaseModel] = Field(
        default_factory=dict,
        description="A dictionary mapping value keys to _Valued objects.",
    )

    @model_validator(mode="before")
    def _populate_values(cls, data):
        obj = data.get("obj")
        if not isinstance(obj, _Valued):
            raise ValueError(
                "ValuedVersion must include an `obj` that subclasses `_Valued`"
            )
        return data

    def model_post_init(self, __context: Any) -> None:
        # set the values dictionary from the obj
        self.values = {v.key: v for v in self.obj.values}
        return self


class Key(BaseModel):
    key: str
    versions: dict[str, NonValuedVersion | ValuedVersion] = Field(
        default_factory=dict,
        description="A dictionary mapping version strings to versioned objects.",
    )


class Namespace(BaseModel):
    namespace: str
    keys: dict[str, Key] = Field(
        default_factory=dict,
        description="A dictionary mapping keys to Key objects within this namespace.",
    )


class NsType(BaseModel):
    type: str
    namespaces: dict[str, Namespace] = Field(
        default_factory=dict,
        description="A dictionary mapping namespace strings to Namespace objects.",
    )


class SsvcObjectRegistry(_SchemaVersioned, _Base, BaseModel):
    schemaVersion: Literal[SCHEMA_VERSION] = Field(
        ...,
        description="The schema version of this selection list.",
    )

    types: dict[str, NsType] = Field(
        default_factory=dict,
        description="A dictionary mapping type names to NsType objects.",
    )

    @model_validator(mode="before")
    def set_schema_version(cls, data):
        """
        Set the schema version to the default if not provided.
        """
        if "schemaVersion" not in data:
            data["schemaVersion"] = SCHEMA_VERSION
        return data

    def lookup_objtype(self, objtype: str) -> NsType | None:
        """
        Lookup an object type in the registry by its name.
        Returns None if the type is not found.

        Args:
            objtype (str): The name of the object type to lookup.
        Returns:
            NsType | None: The NsType object if found, otherwise None.
        """
        return self.types.get(objtype, None)

    def lookup_namespace(self, objtype: str, namespace: str) -> Namespace | None:
        """
        Lookup a namespace in the registry by object type and namespace name.
        Returns None if the namespace is not found.

        Args:
            objtype (str): The name of the object type.
            namespace (str): The name of the namespace to lookup.
        Returns:
            Namespace | None: The Namespace object if found, otherwise None.
        """
        otype = self.lookup_objtype(objtype)

        if otype is None:
            return None

        return otype.namespaces.get(namespace, None)

    def lookup_key(self, objtype: str, namespace: str, key: str) -> Key | None:
        """
        Lookup a key in the registry by object type, namespace, and key name.
        Returns None if the key is not found.

        Args:
            objtype (str): The name of the object type.
            namespace (str): The name of the namespace.
            key (str): The key to lookup.
        Returns:
            Key | None: The Key object if found, otherwise None.
        """
        ns = self.lookup_namespace(objtype, namespace)

        if ns is None:
            return None

        return ns.keys.get(key, None)

    def lookup_version(
        self, objtype: str, namespace: str, key: str, version: str
    ) -> NonValuedVersion | ValuedVersion | None:
        """
        Lookup a version in the registry by object type, namespace, key, and version string.
        Returns None if the version is not found.
        Args:
            objtype (str): The name of the object type.
            namespace (str): The name of the namespace.
            key (str): The key to lookup.
            version (str): The version string to lookup.
        Returns:
            NonValuedVersion | ValuedVersion | None: The version object if found, otherwise None.

        """
        key_obj = self.lookup_key(objtype, namespace, key)

        if key_obj is None:
            return None

        return key_obj.versions.get(version, None)

    def lookup_value(
        self, objtype: str, namespace: str, key: str, version: str, value_key: str
    ) -> _KeyedBaseModel | None:
        """
        Lookup a value in the registry by object type, namespace, key, version, and value key.
        Returns None if the value is not found.

        Args:
            objtype (str): The name of the object type.
            namespace (str): The name of the namespace.
            key (str): The key to lookup.
            version (str): The version string to lookup.
            value_key (str): The key of the value to lookup.
        Returns:
            _KeyedBaseModel | None: The value object if found, otherwise None.

        """
        version_obj = self.lookup_version(objtype, namespace, key, version)

        if version_obj is None:
            return None

        if isinstance(version_obj, ValuedVersion):
            return version_obj.values.get(value_key, None)

        logger.debug(f"Object type '{objtype}' does not support values.")
        return None

    def lookup(
        self,
        objtype: Optional[str] = None,
        namespace: Optional[str] = None,
        key: Optional[str] = None,
        version: Optional[str] = None,
        value_key: Optional[str] = None,
    ) -> _GenericSsvcObject | None:
        """
        Lookup an object in the registry by type, namespace, key, version, and value key.

        Args:
            objtype (str): The name of the object type.
            namespace (str): The name of the namespace.
            key (str): The key to lookup.
            version (str): The version string to lookup.
            value_key (str): The key of the value to lookup.
        Returns:
            _GenericSsvcObject | None: The object if found, otherwise None.

        """
        # everything None just returns the whole registry
        if all([x is None for x in [objtype, namespace, key, version, value_key]]):
            return self

        # start at the deepest level and work up
        if value_key is not None:
            return self.lookup_value(objtype, namespace, key, version, value_key)
        if version is not None:
            return self.lookup_version(objtype, namespace, key, version)
        if key is not None:
            return self.lookup_key(objtype, namespace, key)
        if namespace is not None:
            return self.lookup_namespace(objtype, namespace)
        if objtype is not None:
            return self.lookup_objtype(objtype)
        logger.debug("No parameters provided for lookup, returning None.")
        return None

    def lookup_by_id(self, objtype: str, objid: str) -> object | None:

        value_key = None
        parts = objid.split(":")
        ns, objid, version = parts[0:3]
        if len(parts) == 4:
            value_key = parts[3]

        if value_key is not None:
            return self.lookup_value(objtype, ns, objid, version, value_key)

        return self.lookup_version(objtype, ns, objid, version)

    def register(self, obj: _GenericSsvcObject) -> None:
        # extract the parts we need to register

        objtype = _get_obj_type(obj)
        ns = str(obj.namespace)  # explicitly cast to string
        k = obj.key
        ver = obj.version

        # if this object already exists in the registry, see if it matches
        found = self.lookup(objtype=objtype, namespace=ns, key=k, version=ver)
        if found is not None:
            logger.debug(f"Object {obj.id} already registered, skipping registration.")
            # if this is a different object with the same id, we should throw an error
            diffs = []
            should_be_version = False
            found_obj = found.obj
            if found_obj.name != obj.name:
                diffs.append(f"Name mismatch: {found_obj.name} != {obj.name}")
            else:
                should_be_version = True
            if found_obj.description != obj.description:
                diffs.append(
                    f"Description mismatch: {found_obj.description} != {obj.description}"
                )
            if isinstance(found_obj, _Valued):
                for a, b in zip(found_obj.values, obj.values):
                    if a != b:
                        diffs.append(f"Value mismatch: {a} != {b}")
            for d in diffs:
                logger.warning(f"Diff found when registering {obj.id}: {d}")

            if diffs:
                if should_be_version:
                    logger.error(
                        f"Object {obj.id} ({obj.name}) already registered with different attributes. Consider changing the version."
                    )
                else:
                    logger.error(
                        f"Object {obj.id} already registered with different attributes. "
                        f"Consider changing the key ({obj.key}) for '{obj.name}' to avoid collision with '{found_obj.name}'."
                    )
                raise ValueError(
                    f"Object {obj.id} already registered with different attributes: {', '.join(diffs)}"
                )
            # otherwise, we just return
            return

        # start at the top of the registry and work down
        if objtype not in self.types:
            logger.debug(f"Registering new object type '{objtype}'.")
            self.types[objtype] = NsType(type=objtype)

        if ns not in self.types[objtype].namespaces:
            logger.debug(
                f"Registering new namespace '{ns}' for object type '{objtype}'."
            )
            self.types[objtype].namespaces[ns] = Namespace(namespace=ns)

        if k not in self.types[objtype].namespaces[ns].keys:
            logger.debug(
                f"Registering new key '{k}' in namespace '{ns}' for object type '{objtype}'."
            )
            # versions will be created empty by the Key model
            self.types[objtype].namespaces[ns].keys[k] = Key(key=k)

        if ver not in self.types[objtype].namespaces[ns].keys[k].versions:
            logger.debug(
                f"Registering new version '{ver}' for key '{k}' in namespace '{ns}' of type '{objtype}'."
            )
            if isinstance(obj, _Valued):
                # values will be populated in the ValuedVersion model
                self.types[objtype].namespaces[ns].keys[k].versions[ver] = (
                    ValuedVersion(
                        version=ver,
                        obj=obj,
                    )
                )
            else:
                self.types[objtype].namespaces[ns].keys[k].versions[ver] = (
                    NonValuedVersion(
                        version=ver,
                        obj=obj,
                    )
                )

    def reset(self, force: bool = False) -> None:
        """
        Reset the registry to an empty state.
        If force is True, it will clear the registry even if it has objects.
        """
        if force or not self.types:
            self.types = dict()
            logger.debug("Registry reset.")
        else:
            logger.warning("Registry not reset. Use force=True to clear it.")

    def get_all(self, objtype: str) -> list[_GenericSsvcObject]:
        """
        Get all objects of a specific type from the registry.

        Args:
            objtype (str): The type of objects to retrieve.

        Returns:
            list[_GenericSsvcObject]: A list of objects of the specified type.
        """
        otype_ns = self.lookup_objtype(objtype)
        if otype_ns is None:
            return []

        all_objects = []

        for ns in otype_ns.namespaces.values():
            for key in ns.keys.values():
                for version in key.versions.values():
                    all_objects.append(version.obj)

        return all_objects
