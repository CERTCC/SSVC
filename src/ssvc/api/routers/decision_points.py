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

"""Decision Points API Router."""
from fastapi import APIRouter

from ssvc.api.helpers import _404_on_none
from ssvc.api.response_models import (
    DecisionPointDictResponse,
    DecisionPointDictType,
    DecisionPointValueListResponse,
    DecisionPointValuesListType,
)
from ssvc.decision_points.base import DecisionPoint
from ssvc.registry.base import get_registry
from ssvc.registry.base import (
    lookup_key,
    lookup_latest,
    lookup_namespace,
    lookup_objtype,
    lookup_version,
)

r = get_registry()

router = APIRouter(prefix="/decision_points", tags=["Decision Points"])


@router.get(
    "/",
    summary="Get all decision points",
    description="Returns a dictionary of all DecisionPoint objects organized by their object id.",
    response_model=DecisionPointDictResponse,
)
async def get_all_decision_points() -> DecisionPointDictType:
    result = lookup_objtype(objtype="DecisionPoint", registry=r)
    _404_on_none(result)

    objs = {}
    # result has namespaces, namespaces have keys, keys have versions.
    for ns in result.namespaces:
        for k in result.namespaces[ns].keys:
            for ver in result.namespaces[ns].keys[k].versions:
                obj = result.namespaces[ns].keys[k].versions[ver].obj
                objs[obj.id] = obj
    return objs


@router.get(
    "/{namespace}",
    summary="Get all decision points for a namespace",
    description="Returns a dictionary of DecisionPoint objects for the given namespace organized by their object id.",
    response_model=DecisionPointDictResponse,
)
async def get_all_decision_points_for_namespace(
    namespace: str,
) -> DecisionPointDictType:
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
    return objs


@router.get(
    "/{namespace}/{key}",
    summary="Get all versions of a decision point for a key in a namespace",
    description="Returns a dictionary of DecisionPoint objects for the given namespace and key organized by their object id.",
    response_model=DecisionPointDictResponse,
)
async def get_all_versions_of_decision_points_for_key(
    namespace: str, key: str
) -> DecisionPointDictType:
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
    return objs


@router.get(
    "/{namespace}/{key}/latest",
    summary="Get the latest decision point for a key in a namespace",
    description="Returns the latest DecisionPoint object for the given namespace and key.",
    response_model=DecisionPoint,
)
async def get_latest_decision_point_for_key(
    namespace: str, key: str
) -> DecisionPoint:
    """Returns the latest DecisionPoint object for the given namespace and key."""
    result = lookup_latest(
        objtype="DecisionPoint", namespace=namespace, key=key, registry=r
    )
    _404_on_none(result)
    dp = result
    return dp


@router.get(
    "/{namespace}/{key}/{version}",
    summary="Get a specific version of a decision point",
    description="Returns a single DecisionPoint object for the given namespace, key, and version.",
    response_model=DecisionPoint,
)
async def get_decision_point_version(
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


@router.get(
    "/{namespace}/{key}/latest/values",
    summary="Get the latest decision point for a key in a namespace",
    description="Returns the latest DecisionPoint object for the given namespace and key.",
    response_model=DecisionPointValueListResponse,
)
async def get_latest_decision_point_for_key(
    namespace: str, key: str
) -> DecisionPointValuesListType:
    """Returns the latest DecisionPoint object for the given namespace and key."""
    result = lookup_latest(
        objtype="DecisionPoint", namespace=namespace, key=key, registry=r
    )
    _404_on_none(result)
    dp = result
    return list(dp.values)


@router.get(
    "/{namespace}/{key}/{version}/values",
    summary="Get the values of a decision point",
    description="Returns the list of values of a single DecisionPoint object for the given namespace, key, and version.",
    response_model=DecisionPointValueListResponse,
)
async def get_decision_point_values(
    namespace: str, key: str, version: str
) -> DecisionPointValuesListType:
    """Returns the values of a single DecisionPoint object for the given namespace, key, and version."""
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
