"""Decision Tables API Router."""

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

from fastapi import APIRouter

from ssvc.api.helpers import _404_on_none
from ssvc.api.response_models import (
    DecisionTableDictResponse,
    DecisionTableDictType,
)
from ssvc.decision_tables.base import DecisionTable
from ssvc.registry.base import get_registry
from ssvc.registry.base import (
    lookup_key,
    lookup_latest,
    lookup_namespace,
    lookup_objtype,
    lookup_version,
)

r = get_registry()
router = APIRouter(prefix="/decision_tables", tags=["Decision Tables"])


@router.get(
    "/",
    summary="Get all decision tables",
    description="Returns a dictionary of all decision tables in the registry organized by their object id.",
    response_model=DecisionTableDictResponse,
)
async def get_decision_tables() -> DecisionTableDictType:
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
    return objs


@router.get(
    "/{namespace}",
    summary="Get decision tables for a namespace",
    description="Returns a dictionary of DecisionTable objects for the given namespace organized by their object id.",
    response_model=DecisionTableDictResponse,
)
async def get_decision_tables_for_namespace(
    namespace: str,
) -> DecisionTableDictType:

    ns_obj = lookup_namespace(
        objtype="DecisionTable", namespace=namespace, registry=r
    )
    _404_on_none(ns_obj)
    # namespace obj has keys, keys have versions.
    objs = {}
    for k in ns_obj.keys.keys():
        for ver in ns_obj.keys[k].versions.keys():
            obj = ns_obj.keys[k].versions[ver].obj
            objs[obj.id] = obj
    return objs


@router.get(
    "/{namespace}/{key}",
    summary="Get decision tables for namespace and key",
    description="Returns a dictionary of DecisionTable objects for the given namespace and key organized by their object id.",
    response_model=DecisionTableDictResponse,
)
async def get_decision_tables_for_key(
    namespace: str, key: str
) -> DecisionTableDictType:
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
    return objs


@router.get(
    "/{namespace}/{key}/latest",
    summary="Get the latest decision table for a namespace and key",
    description="Returns the latest DecisionTable object for the given namespace and key.",
    response_model=DecisionTable,
)
async def get_latest_decision_table_for_key(
    namespace: str, key: str
) -> DecisionTable:
    """Returns the latest DecisionPoint object for the given namespace and key."""
    result = lookup_latest(
        objtype="DecisionTable", namespace=namespace, key=key, registry=r
    )
    _404_on_none(result)
    dt = result
    return dt


@router.get(
    "/{namespace}/{key}/{version}",
    summary="Get a specific version of a decision table",
    description="Returns a specific version of a DecisionTable object for the given namespace, key, and version.",
    response_model=DecisionTable,
)
async def get_decision_table_version(
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
