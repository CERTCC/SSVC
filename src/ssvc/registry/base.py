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
from typing import Any, ClassVar, Literal, Optional, Union

import semver
from pydantic import BaseModel, Field

from ssvc._mixins import (
    _Base,
    _GenericSsvcObject,
    _KeyedBaseModel,
    _SchemaVersioned,
)
from ssvc.decision_points.base import DecisionPoint, DecisionPointValue
from ssvc.decision_tables.base import DecisionTable
from ssvc.registry import get_registry
from ssvc.utils.field_specs import VersionString

logger = logging.getLogger(__name__)

SCHEMA_VERSION: str = "2.0.0"
logger.debug(f"Using schema version {SCHEMA_VERSION} for SsvcObjectRegistry.")

# Define the types we can register
_Registerable = (DecisionPoint, DecisionTable)
_RegisterableClass = Union[_Registerable]


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


class _ValuedVersion(BaseModel):
    version: VersionString
    obj: DecisionPoint
    values: dict[str, DecisionPointValue] = Field(
        default_factory=dict,
        description="A dictionary mapping value keys to DecisionPointValue objects.",
    )

    def model_post_init(self, __context: Any) -> None:
        if not self.values:
            # if the object is valued, we should set the values dictionary
            self.values = {v.key: v for v in self.obj.values}


class _NonValuedVersion(BaseModel):
    version: VersionString
    obj: DecisionTable


_Version = Union[_ValuedVersion, _NonValuedVersion]


class _Key(BaseModel):
    key: str
    versions: dict[str, _Version] = Field(
        default_factory=dict,
        description="A dictionary mapping version strings to versioned objects.",
    )


class _Namespace(BaseModel):
    namespace: str
    keys: dict[str, _Key] = Field(
        default_factory=dict,
        description="A dictionary mapping keys to Key objects within this namespace.",
    )


class _NsType(BaseModel):
    type: str
    namespaces: dict[str, _Namespace] = Field(
        default_factory=dict,
        description="A dictionary mapping obj types to Namespace objects.",
    )


class SsvcObjectRegistry(_SchemaVersioned, _Base, BaseModel):
    _schema_version: ClassVar[str] = SCHEMA_VERSION
    schemaVersion: Literal[SCHEMA_VERSION] = Field(
        ...,
        description="The schema version of this selection list.",
    )

    types: dict[str, _NsType] = Field(
        default_factory=dict,
        description="A dictionary mapping type names to NsType objects.",
    )

    def register(self, obj: _GenericSsvcObject) -> None:
        """
        Register an object in the SSVC object registry.
        If the object already exists, it will compare the new object with the existing one.
        If they differ, it will raise a ValueError.

        Args:
            obj: The object to register.

        Returns:
            None
        """
        return register(obj=obj, registry=self)

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

    def lookup(
        self,
        objtype: Optional[str] = None,
        namespace: Optional[str] = None,
        key: Optional[str] = None,
        version: Optional[str] = None,
        value_key: Optional[str] = None,
    ) -> Union[DecisionPoint, DecisionPointValue, DecisionTable, None]:
        """
        Lookup an object in the registry by type, namespace, key, version, and value key.

        Args:
            objtype (str): The name of the object type.
            namespace (str): The name of the namespace.
            key (str): The key to lookup.
            version (str): The version string to lookup.
            value_key (str): The key of the value to lookup.

        Returns:
            DecisionPoint | DecisionPointValue | DecisionTable | None: The object if found, otherwise None.
        """
        return lookup(
            objtype=objtype,
            namespace=namespace,
            key=key,
            version=version,
            value_key=value_key,
            registry=self,
        )

    def lookup_by_id(
        self, objtype: str, objid: str
    ) -> Union[DecisionPoint, DecisionPointValue, DecisionTable, None]:
        """
        Lookup an object by its ID in the registry.

        Args:
            objtype (str): The type of the object.
            objid (str): The ID of the object in the format "namespace:key:version[:value_key]".

        Returns:
            DecisionPoint | DecisionPointValue | DecisionTable | None: The object if found, otherwise None.
        """
        return lookup_by_id(objtype=objtype, objid=objid, registry=self)


def register(
    obj: _RegisterableClass, registry: SsvcObjectRegistry = None
) -> None:
    """
    Register an object in the SSVC object registry.

    Args:
        obj: The object to register.
        registry: The SsvcObjectRegistry to use. If None, uses the global registry.

    Returns:
        None
    """
    if registry is None:
        registry = get_registry()

    _insert(new=obj, registry=registry)


def _get_keys(obj: _RegisterableClass) -> tuple[str, ...]:
    objtype = _get_obj_type(obj)
    ns = str(obj.namespace)  # explicitly cast to string
    k = obj.key
    ver = obj.version

    return (objtype, ns, k, ver)


def _insert(
    new: _RegisterableClass, registry: Optional[SsvcObjectRegistry] = None
) -> None:
    """
    Inserts a new object into the SSVC object registry.
    If the object is not registerable, it will raise a TypeError.
    If the object already exists, it will compare the new object with the existing one.
    If they differ, it will raise a ValueError.

    Args:
        new:
        registry:

    Returns:

    """
    if registry is None:
        registry = get_registry()

    if not isinstance(new, _Registerable):
        raise TypeError(f"Object {new} is not a registerable SSVC object.")

    (objtype, ns, k, ver) = _get_keys(new)

    # check to see if the type is already registered
    typesobj = registry.types.get(objtype)
    if typesobj is None:
        logger.debug(f"Registering new object type '{objtype}'.")
        typesobj = _NsType(type=objtype)
        registry.types[objtype] = typesobj

    # check to see if the namespace is already registered
    nsobj = typesobj.namespaces.get(ns)
    if nsobj is None:
        logger.debug(
            f"Registering new namespace '{ns}' for object type '{objtype}'."
        )
        nsobj = _Namespace(namespace=ns)
        registry.types[objtype].namespaces[ns] = nsobj

    # check to see if the key is already registered
    keyobj = nsobj.keys.get(k)
    if keyobj is None:
        logger.debug(
            f"Registering new key '{k}' in namespace '{ns}' for object type '{objtype}'."
        )
        keyobj = _Key(key=k)
        registry.types[objtype].namespaces[ns].keys[k] = keyobj

    #
    verobj = keyobj.versions.get(ver)
    if verobj is None:
        # if we got here, we need to register the new version
        logger.debug(
            f"Registering new version '{ver}' for key '{k}' in namespace '{ns}' of type '{objtype}'."
        )

        # use model_construct to create the versioned object
        # while avoiding recursion issues
        if isinstance(new, DecisionTable):
            # if this is a DecisionTable, we use the non-valued version
            verobj = _NonValuedVersion.model_construct(version=ver, obj=new)
        elif isinstance(new, DecisionPoint):
            # if this is a DecisionPoint, we use the valued version
            verobj = _ValuedVersion.model_construct(version=ver, obj=new)
        else:
            raise TypeError(
                f"Object {new} is not a recognized SSVC object type for registration."
            )
        keyobj.versions[ver] = verobj
    else:
        # if we got here, the version already exists, which is odd, but often benign
        logger.debug(f"Object {new.id} already registered with version {ver}.")
        # we should do a comparison to ensure it matches
        _compare(new=new, existing=verobj.obj)


def _compare(new: _RegisterableClass, existing: _RegisterableClass) -> None:
    """
    Compares two objects and raises an error if they are different.

    Args:
        new: the new object being registered
        existing: the existing object in the registry

    Returns:
        None: if the objects are the same

    Raises:
        ValueError: if the objects are different
    """
    # if this is a different object with the same id, we should throw an error
    diffs = []
    should_be_version = False

    if existing.name != new.name:
        diffs.append(f"Name mismatch: {existing.name} != {new.name}")
    else:
        should_be_version = True

    if existing.definition != new.definition:
        diffs.append(
            f"Description mismatch: {existing.definition} != {new.definition}"
        )

    if hasattr(existing, "values") and hasattr(new, "values"):
        if existing.values is None and new.values is not None:
            diffs.append(
                f"Existing object {existing.id} has no values, but new object {new.id} has values."
            )
        elif existing.values is not None and new.values is None:
            diffs.append(
                f"Existing object {existing.id} has values, but new object {new.id} has no values."
            )
        elif existing.values is not None and new.values is not None:
            for a, b in zip(existing.values, new.values):
                if a != b:
                    diffs.append(f"Value mismatch: {a} != {b}")

    if diffs:
        for d in diffs:
            logger.warning(f"Diff found when registering {new.id}: {d}")

        if should_be_version:
            logger.error(
                f"Object {new.id} ({new.name}) already registered with different attributes. Consider changing the version."
            )
        else:
            logger.error(
                f"Object {new.id} already registered with different attributes. "
                f"Consider changing the key ({new.key}) for '{new.name}' to avoid collision with '{existing.name}'."
            )
        raise ValueError(
            f"Object {new.id} already registered with different attributes: {', '.join(diffs)}"
        )

    # if you get here, no problems were found, this is just a benign duplicate
    logger.debug(
        f"Object {new.id} already registered with matching attributes. No action taken."
    )


def lookup_by_id(
    objtype: str, objid: str, registry: SsvcObjectRegistry
) -> DecisionPoint | DecisionPointValue | DecisionTable | None:

    parts = objid.split(":")
    args = {}
    args["objtype"] = objtype
    args["namespace"] = parts[0]
    args["key"] = parts[1]
    args["version"] = parts[2]
    try:
        args["value_key"] = parts[3]
    except IndexError:
        pass

    if "value_key" in args:
        return lookup_value(**args, registry=registry)

    # if you got here, we're just looking up a version
    return lookup_version(**args, registry=registry)


def get_all(
    objtype: str, registry: SsvcObjectRegistry
) -> list[_GenericSsvcObject]:
    """
    Get all objects of a specific type from the registry.

    Args:
        objtype (str): The type of objects to retrieve.

    Returns:
        list[_GenericSsvcObject]: A list of objects of the specified type.
    """

    all_objects = []

    otype_ns = lookup_objtype(objtype, registry)

    if otype_ns is None:
        return all_objects

    for ns in otype_ns.namespaces.values():
        for key in ns.keys.values():
            for version in key.versions.values():
                all_objects.append(version.obj)

    return all_objects


def lookup_objtype(
    objtype: str, registry: SsvcObjectRegistry
) -> _NsType | None:
    """
    Lookup an object type in the registry by its name.
    Returns None if the type is not found.

    Args:
        objtype (str): The name of the object type to lookup.
    Returns:
        _NsType | None: The NsType object if found, otherwise None.
    """
    return registry.types.get(objtype, None)


def lookup_namespace(
    objtype: str, namespace: str, registry: SsvcObjectRegistry
) -> _Namespace | None:
    """
    Lookup a namespace in the registry by object type and namespace name.
    Returns None if the namespace is not found.

    Args:
        objtype (str): The name of the object type.
        namespace (str): The name of the namespace to lookup.
    Returns:
        _Namespace | None: The Namespace object if found, otherwise None.
    """
    otype = lookup_objtype(objtype, registry)

    if otype is None:
        return None

    return otype.namespaces.get(namespace, None)


def lookup_key(
    objtype: str, namespace: str, key: str, registry: SsvcObjectRegistry
) -> _Key | None:
    """
    Lookup a key in the registry by object type, namespace, and key name.
    Returns None if the key is not found.

    Args:
        objtype (str): The name of the object type.
        namespace (str): The name of the namespace.
        key (str): The key to lookup.
    Returns:
        _Key | None: The Key object if found, otherwise None.
    """
    ns = lookup_namespace(objtype, namespace, registry)

    if ns is None:
        return None

    return ns.keys.get(key, None)


def lookup_version(
    objtype: str,
    namespace: str,
    key: str,
    version: str,
    registry: SsvcObjectRegistry,
) -> _ValuedVersion | _NonValuedVersion | None:
    """
    Lookup a version in the registry by object type, namespace, key, and version string.
    Returns None if the version is not found.
    Args:
        registry: the SsvcObjectRegistry to use for lookup.
        objtype (str): The name of the object type.
        namespace (str): The name of the namespace.
        key (str): The key to lookup.
        version (str): The version string to lookup.
    Returns:
        NonValuedVersion | ValuedVersion | None: The version object if found, otherwise None.

    """
    key_obj = lookup_key(objtype, namespace, key, registry)

    if key_obj is None:
        return None

    return key_obj.versions.get(version, None)


def lookup_value(
    objtype: str,
    namespace: str,
    key: str,
    version: str,
    value_key: str,
    registry: SsvcObjectRegistry,
) -> DecisionPointValue | None:
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
    version_obj = lookup_version(objtype, namespace, key, version, registry)

    if version_obj is None:
        return None

    if version_obj.values is not None:
        return version_obj.values.get(value_key, None)

    logger.debug(f"Object type '{objtype}' does not support values.")
    return None


def lookup_latest(
    objtype: Optional[str] = None,
    namespace: Optional[str] = None,
    key: Optional[str] = None,
    registry: SsvcObjectRegistry = None,
) -> Union[_RegisterableClass, None]:
    if registry is None:
        registry = get_registry()

    keyobj = lookup_key(
        objtype=objtype, namespace=namespace, key=key, registry=registry
    )
    versions = keyobj.versions
    # now we have a dict of {version_string: version_object}

    if versions is None:
        return None

    def normalize_version(v: str) -> str:
        return semver.Version.parse(v, optional_minor_and_patch=True)

    def stringify_version(v: str) -> str:
        vers = normalize_version(v)
        return vers.__str__()

    # create a quick lookup for version strings
    version_lookup = {stringify_version(k): v.obj for k, v in versions.items()}

    parsed_version = [normalize_version(v) for v in list(versions.keys())]
    latest = sorted(parsed_version)[-1]
    # convert back to string
    latest_str = str(latest)

    # now lookup the version object
    version_obj = version_lookup[latest_str]

    return version_obj


def lookup(
    objtype: Optional[str] = None,
    namespace: Optional[str] = None,
    key: Optional[str] = None,
    version: Optional[str] = None,
    value_key: Optional[str] = None,
    registry: SsvcObjectRegistry = None,
) -> Union[_RegisterableClass, DecisionPointValue, None]:
    """
    Lookup an object in the registry by type, namespace, key, version, and value key.

    Args:
        objtype (str): The name of the object type.
        namespace (str): The name of the namespace.
        key (str): The key to lookup.
        version (str): The version string to lookup.
        value_key (str): The key of the value to lookup.
        registry (SsvcObjectRegistry): The SsvcObjectRegistry to use.

    Returns:
        DecisionPoint | DecisionPointValue | DecisionTable | None: The object if found, otherwise None.

    Raises:
        ValueError: If the registry is not provided or if all lookup parameters are None.

    """
    if registry is None:
        raise ValueError("Registry must be provided for lookup.")

    # start at the deepest level and work up
    if value_key is not None:
        return lookup_value(
            objtype, namespace, key, version, value_key, registry
        )

    if version is not None:
        return lookup_version(objtype, namespace, key, version, registry)

    if key is not None:
        return lookup_key(objtype, namespace, key, registry)

    if namespace is not None:
        return lookup_namespace(objtype, namespace, registry)

    if objtype is not None:
        return lookup_objtype(objtype, registry)

    raise ValueError(
        "All lookup parameters were None. Please provide at least one parameter to lookup an object."
    )
