#!/usr/bin/env python
"""
API for SSVC
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

from typing import Any, Dict

from fastapi import FastAPI, HTTPException
from pydantic import RootModel

from ssvc.decision_points.base import DecisionPoint, DecisionPointValue
from ssvc.decision_tables.base import DecisionTable
from ssvc.registry import get_registry
from ssvc.registry.base import (
    lookup_key,
    lookup_namespace,
    lookup_objtype,
    lookup_version,
)

app = FastAPI()

r = get_registry()


# TODO: move convenience object models to a separate module
class DecisionPointDict(RootModel[Dict[str, DecisionPoint]]):
    """A dictionary of DecisionPoint objects with keys as 'namespace:key:version'."""


class DecisionTableDict(RootModel[Dict[str, DecisionTable]]):
    """A dictionary of DecisionTable objects with keys as 'namespace:key:version'."""


@app.get("/")
def read_root():
    return {"Hello": "SSVC World"}


def _404_on_none(obj: Any):
    if obj is None:
        raise HTTPException(status_code=404, detail=f"Item not found")


@app.get("/decision_points", response_model=DecisionPointDict)
async def get_decision_points() -> DecisionPointDict:
    result = lookup_objtype(objtype="DecisionPoint", registry=r)
    _404_on_none(result)

    objs = {}
    # result has namespaces, namespaces have keys, keys have versions.
    for ns in result.namespaces:
        for k in result.namespaces[ns].keys:
            for ver in result.namespaces[ns].keys[k].versions:
                obj = result.namespaces[ns].keys[k].versions[ver].obj
                objs[obj.id] = obj
    return DecisionPointDict(**objs)


@app.get("/decision_points/{namespace}", response_model=DecisionPointDict)
async def get_decision_points(namespace: str) -> DecisionPointDict:
    result = lookup_namespace(
        objtype="DecisionPoint", namespace=namespace, registry=r
    )
    _404_on_none(result)

    objs = {}
    # result has keys, keys have versions, versions have objs.
    for k in result.keys:
        for ver in result.keys[k].versions:
            obj = result.keys[k].versions[ver].obj
            objs[obj.id] = obj
    return DecisionPointDict(**objs)


@app.get(
    "/decision_points/{namespace}/{key}", response_model=DecisionPointDict
)
async def get_decision_points(namespace: str, key: str) -> DecisionPointDict:
    """Returns a dictionary of DecisionPoint objects for the given namespace and key.
    Dictionary keys are namespace:key:version."""
    result = lookup_key(
        objtype="DecisionPoint", namespace=namespace, key=key, registry=r
    )
    _404_on_none(result)
    # result obj has versions.
    objs = {}
    for ver in result.versions:
        obj = result.versions[ver].obj
        objs[obj.id] = obj
    return DecisionPointDict(**objs)


@app.get(
    "/decision_points/{namespace}/{key}/{version}",
    response_model=DecisionPoint,
)
async def get_decision_points(
    namespace: str, key: str, version: str
) -> DecisionPoint:
    """Returns a single DecisionPoint object for the given namespace, key, and version."""
    result = lookup_version(
        objtype="DecisionPoint",
        namespace=namespace,
        key=key,
        version=version,
        registry=r,
    )
    _404_on_none(result)
    dp = result.obj
    return dp


@app.get(
    "/decision_points/{namespace}/{key}/{version}/values",
    response_model=list[DecisionPointValue],
)
async def get_decision_points(
    namespace: str, key: str, version: str
) -> DecisionPoint:
    """Returns a single DecisionPoint object for the given namespace, key, and version."""
    result = lookup_version(
        objtype="DecisionPoint",
        namespace=namespace,
        key=key,
        version=version,
        registry=r,
    )
    _404_on_none(result)
    dp = result.obj
    return list(dp.values)


@app.get("/decision_tables", response_model=DecisionTableDict)
async def get_decision_tables() -> DecisionTableDict:
    # load registry and return decision tables
    result = lookup_objtype(objtype="DecisionTable", registry=r)
    _404_on_none(result)
    # result obj has namespaces, namespaces have keys, keys have versions.
    objs = {}
    for ns in result.namespaces:
        for k in result.namespaces[ns].keys:
            for ver in result.namespaces[ns].keys[k].versions:
                obj = result.namespaces[ns].keys[k].versions[ver].obj
                objs[obj.id] = obj
    return DecisionTableDict(**objs)


@app.get("/decision_tables/{namespace}", response_model=DecisionTableDict)
async def get_decision_tables_namespace(
    namespace: str,
) -> DecisionTableDict:

    ns_obj = lookup_namespace(
        objtype="DecisionTable", namespace=namespace, registry=r
    )
    _404_on_none(ns_obj)
    # namespace obj has keys, keys have versions.
    objs = {}
    for k in ns_obj.keys:
        for ver in ns_obj.keys[k].versions:
            obj = ns_obj.keys[k].versions[ver].obj
            objs[obj.id] = obj
    return DecisionTableDict(**objs)


@app.get(
    "/decision_tables/{namespace}/{key}", response_model=DecisionTableDict
)
async def get_decision_tables_key(
    namespace: str, key: str
) -> DecisionTableDict:
    """Returns a dictionary of DecisionTable objects for the given namespace and key.
    Dictionary keys are version strings."""
    results = lookup_key(
        objtype="DecisionTable", namespace=namespace, key=key, registry=r
    )
    _404_on_none(results)

    objs = {}
    # results is a DecisionTableKey object with versions.
    # versions is a dict of version strings to DecisionTableVersion objects.
    # DecisionTableVersion objects have an obj attribute which is the DecisionTable.
    for ver in results.versions.values():
        obj = ver.obj
        objs[obj.id] = obj
    return DecisionTableDict(**objs)


@app.get(
    "/decision_tables/{namespace}/{key}/{version}",
    response_model=DecisionTable,
)
async def get_decision_tables_version(
    namespace: str, key: str, version: str
) -> DecisionTable:
    """Returns a single DecisionTable object for the given namespace, key, and version."""
    dt_version = lookup_version(
        objtype="DecisionTable",
        namespace=namespace,
        key=key,
        version=version,
        registry=r,
    )
    _404_on_none(dt_version)
    dt = dt_version.obj
    return dt


@app.get("/namespaces", response_model=list[str])
def get_namespaces() -> list[str]:
    namespaces = set()
    for objtype in r.types:
        for namespace in r.types[objtype].namespaces:
            namespaces.add(namespace)
    return sorted(list(namespaces))


@app.get("/types", response_model=list[str])
def get_types() -> list[str]:
    """Returns a list of all object types in the registry."""
    return sorted(list(r.types.keys()))


@app.get("/namespaces/{type}", response_model=list[str])
def get_types_namespaces(type: str) -> list[str]:
    """Returns a list of all namespaces for a given object type in the registry."""
    objtype = lookup_objtype(objtype=type, registry=r)
    _404_on_none(objtype)
    return sorted(list(objtype.namespaces.keys()))


@app.get("/keys/{type}/{namespace}", response_model=list[str])
def get_keys(type: str, namespace: str) -> list[str]:
    """Returns a list of all keys for a given object type and namespace in the registry."""
    ns = lookup_namespace(objtype=type, namespace=namespace, registry=r)
    _404_on_none(ns)
    return sorted(list(ns.keys.keys()))


@app.get("/versions/{type}/{namespace}/{key}", response_model=list[str])
def get_versions(type: str, namespace: str, key: str) -> list[str]:
    """Returns a list of all versions for a given object type, namespace, and key in the registry."""
    k = lookup_key(objtype=type, namespace=namespace, key=key, registry=r)
    _404_on_none(k)
    return sorted(list(k.versions.keys()))
