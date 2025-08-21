"""Keys API Router."""

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
from pydantic import RootModel

from ssvc.api.helpers import _404_on_none
from ssvc.registry.base import get_registry, lookup_namespace

router = APIRouter(prefix="/keys", tags=["SSVC Keys"])
r = get_registry()


class KeyDictResponse(RootModel[dict[str, dict[str, list[str]]]]):
    """Response model for key list grouped by object type and namespace."""


@router.get("/", response_model=KeyDictResponse)
def get_key_list() -> dict:
    """Returns a list of all keys in the registry, grouped by object type and namespace."""
    response = {}
    for object_type in r.types.keys():
        response[object_type] = {}

        for namespace in r.types[object_type].namespaces.keys():
            ns = lookup_namespace(
                objtype=object_type, namespace=namespace, registry=r
            )
            if ns is not None:
                response[object_type][namespace] = sorted(list(ns.keys.keys()))
    return response


@router.get("/{objtype}", response_model=KeyDictResponse)
def get_key_list_for_type(objtype: str) -> dict:
    """Returns a list of all keys for a given object type in the registry, grouped by namespace."""
    object_type = r.types.get(objtype)
    _404_on_none(object_type)

    response = {objtype: {}}
    for namespace in object_type.namespaces:
        ns = lookup_namespace(objtype=objtype, namespace=namespace, registry=r)
        if ns:
            response[objtype][namespace] = sorted(list(ns.keys.keys()))
    return response


@router.get("/{objtype}/{namespace}", response_model=KeyDictResponse)
def get_key_list_for_type_and_namespace(objtype: str, namespace: str) -> dict:
    """Returns a list of all keys for a given object type and namespace in the registry."""
    ns = lookup_namespace(objtype=objtype, namespace=namespace, registry=r)
    _404_on_none(ns)

    response = {objtype: {namespace: sorted(list(ns.keys.keys()))}}
    return response
