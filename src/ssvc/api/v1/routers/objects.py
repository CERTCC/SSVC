"""Objects API Router."""

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
from ssvc.decision_points.base import DecisionPoint
from ssvc.decision_tables.base import DecisionTable
from ssvc.registry.base import get_registry, lookup_by_id

router = APIRouter(prefix="/objects", tags=["SSVC Objects"])
r = get_registry()

# generate endpoints for each object type
object_types = [DecisionPoint, DecisionTable]


@router.get(
    "/DecisionPoint/{namespace}/{key}/{version}",
    summary="Get an object by objtype, namespace, key, and version",
    response_model=DecisionPoint,
)
async def get_object(namespace: str, key: str, version: str) -> DecisionPoint:
    """
    Get an object by its type, namespace, key, and version.
    """
    obj_id = ":".join([namespace, key, version])
    ver_obj = lookup_by_id(objtype="DecisionPoint", objid=obj_id, registry=r)

    _404_on_none(ver_obj)
    obj = ver_obj.obj
    return obj


@router.get(
    "/DecisionTable/{namespace}/{key}/{version}",
    summary="Get an object by objtype, namespace, key, and version",
    response_model=DecisionTable,
)
async def get_object(namespace: str, key: str, version: str) -> DecisionTable:
    """
    Get an object by its type, namespace, key, and version.
    """
    obj_id = ":".join([namespace, key, version])
    ver_obj = lookup_by_id(objtype="DecisionTable", objid=obj_id, registry=r)

    _404_on_none(ver_obj)
    obj = ver_obj.obj
    return obj
