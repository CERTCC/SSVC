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

from ssvc.api.helpers import _404_on_none
from ssvc.api.response_models import (
    KeyDictResponse,
    ListOfStringsResponse,
    StringsListType,
)
from ssvc.registry.base import get_registry, lookup_namespace

router = APIRouter(prefix="/keys", tags=["SSVC Keys"])
r = get_registry()


@router.get(
    "/",
    summary="Get Key Dictionary",
    description="Returns a dictionary of all keys in the registry, grouped by object type and namespace",
    response_model=KeyDictResponse,
)
async def get_key_dict() -> dict:
    """Returns a dictionary of all keys in the registry, grouped by object type and namespace."""
    response = {}
    response["types"] = {}

    for object_type in r.types.keys():
        response["types"][object_type] = {"namespaces": {}}

        for namespace in r.types[object_type].namespaces.keys():
            ns = lookup_namespace(
                objtype=object_type, namespace=namespace, registry=r
            )
            if ns is not None:
                response["types"][object_type]["namespaces"][namespace] = {}
                response["types"][object_type]["namespaces"][namespace][
                    "keys"
                ] = sorted(list(ns.keys.keys()))
    return response


@router.get(
    "/{objtype}",
    summary="Get Key Dictionary for Type",
    description="Returns a dictionary of all keys for a given object type in the registry, grouped by object type and namespace",
    response_model=KeyDictResponse,
)
async def get_key_dict_for_type(objtype: str) -> dict:
    """Returns a dictionary of all keys for a given object type in the registry, grouped by object type and namespace."""
    object_type = r.types.get(objtype)
    _404_on_none(object_type)
    response = {"types": {objtype: {"namespaces": {}}}}
    for namespace in object_type.namespaces:
        ns = lookup_namespace(objtype=objtype, namespace=namespace, registry=r)
        if ns:
            response["types"][objtype]["namespaces"][namespace] = {
                "keys": (sorted(list(ns.keys.keys())))
            }
    return response


@router.get(
    "/{objtype}/{namespace}",
    summary="Get Key Dictionary for Type and Namespace",
    description="Returns a dictionary of all keys for a given object type and namespace in the registry, grouped by object type and namespace",
    response_model=KeyDictResponse,
)
async def get_key_dict_for_type_and_namespace(
    objtype: str, namespace: str
) -> dict:
    """Returns a dictionary of all keys for a given object type and namespace in the registry, grouped by object type and namespace."""
    ns = lookup_namespace(objtype=objtype, namespace=namespace, registry=r)
    _404_on_none(ns)

    response = {
        "types": {
            objtype: {
                "namespaces": {
                    namespace: {"keys": sorted(list(ns.keys.keys()))}
                }
            }
        }
    }
    return response


@router.get(
    "/{objtype}/{namespace}/list",
    summary="Get Key Dictionary for Type and Namespace",
    description="Returns a list (without the enclosing dict) of all keys for a given object type and namespace in the registry",
    response_model=ListOfStringsResponse,
)
async def get_key_list_for_type_and_namespace(
    objtype: str, namespace: str
) -> StringsListType:
    """Returns a list of all keys for a given object type and namespace in the registry."""
    ns = lookup_namespace(objtype=objtype, namespace=namespace, registry=r)
    _404_on_none(ns)

    response = sorted(list(ns.keys.keys()))
    return response
