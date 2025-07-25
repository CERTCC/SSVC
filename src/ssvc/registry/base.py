#!/usr/bin/env python
"""
Work in progress on an experimental registry object for SSVC."""

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
from typing import Any, Literal

from pydantic import BaseModel, Field, model_validator

from ssvc._mixins import _Base, _GenericSsvcObject, _KeyedBaseModel, _SchemaVersioned, _Valued
from ssvc.utils.field_specs import VersionString

logger = logging.getLogger(__name__)

SCHEMA_VERSION: str = "2.0.0"
logger.debug(f"Using schema version {SCHEMA_VERSION} for SsvcObjectRegistry.")

def lookup_type(module:str,type_name: str):
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
    objtype = "other" # default type if not recognized
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
    obj: _GenericSsvcObject

class ValuedVersion(BaseModel):
    version: VersionString
    obj: _GenericSsvcObject
    values: dict[str, _KeyedBaseModel] = Field(
        default_factory=dict,
        description="A dictionary mapping value keys to _Valued objects.",
    )

    @model_validator(mode="before")
    def _populate_values(cls, data):
        obj = data.get("obj")
        if not isinstance(obj, _Valued):
            raise ValueError("ValuedVersion must include an `obj` that subclasses `_Valued`")
        return data

    def model_post_init(self, __context: Any) -> None:
        # set the values dictionary from the obj
        self.values = {v.key: v for v in self.obj.values}
        return self


class Key(BaseModel):
    key: str
    versions: dict[str,NonValuedVersion|ValuedVersion] = Field(
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

    def lookup(self,objtype:str=None,namespace:str=None,key:str=None,version:str=None,value_key:str=None) -> _GenericSsvcObject | None:
        """
        Lookup an object in the registry by type, namespace, key, version, and value key.
        """
        if objtype not in self.types:
            return None
        if namespace not in self.types[objtype].namespaces:
            return None
        if key not in self.types[objtype].namespaces[namespace].keys:
            return None
        if version not in self.types[objtype].namespaces[namespace].keys[key].versions:
            return None
        if value_key is not None:
            if value_key not in self.types[objtype].namespaces[namespace].keys[key].versions[version].values:
                return None
            return self.types[objtype].namespaces[namespace].keys[key].versions[version].values[value_key]
        return self.types[objtype].namespaces[namespace].keys[key].versions[version].decision_point

    def lookup_dp(self, namespace: str, key: str, version: str) -> _GenericSsvcObject | None:
        """
        Lookup a DecisionPoint by its namespace, key, and version.
        Returns None if not found.
        """
        return self.lookup(objtype=DecisionPoint.__name__, namespace=namespace, key=key, version=version)


    def register(self, obj: _GenericSsvcObject) -> None:
        # extract the parts we need to register

        objtype = _get_obj_type(obj)
        ns = str(obj.namespace)  # explicitly cast to string
        k = obj.key
        ver = obj.version

        # start at the top of the registry and work down
        if not objtype in self.types:
            self.types[objtype] = NsType(type=objtype)

        d = self.types[objtype].namespaces

        if ns not in d:
            d[ns] = Namespace(namespace=ns)
        if k not in d[ns].keys:
            # versions will be created empty by the Key model
            d[ns].keys[k] = Key(key=k)

        if ver not in d[ns].keys[k].versions:
            if isinstance(obj,_Valued):
                d[ns].keys[k].versions[ver] = ValuedVersion(
                        version=ver,
                        obj=obj,
                        # values will be populated from the obj
                )
            else:
                d[ns].keys[k].versions[ver] = NonValuedVersion(
                        version=ver,
                        obj=obj,
                )

    def reset(self,force: bool = False) -> None:
        """
        Reset the registry to an empty state.
        If force is True, it will clear the registry even if it has objects.
        """
        if force or not self.types:
            self.types = NsTypesDict()
            logger.debug("Registry reset.")
        else:
            logger.warning("Registry not reset. Use force=True to clear it.")



