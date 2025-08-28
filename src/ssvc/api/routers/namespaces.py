"""Namespace Router."""

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
from ssvc.api.response_models import (ListOfStringsResponse, NamespaceDictResponse, NamespaceDictType, StringsListType)
from ssvc.registry.base import get_registry, lookup_objtype

router = APIRouter(
    prefix="/namespaces",
    tags=["SSVC Namespaces"],
)

r = get_registry()


@router.get(
    "/",
    summary="Get all object types and their namespaces",
    description="Returns a dictionary of namespaces organized by object type.",
    response_model=NamespaceDictResponse,
)
async def get_object_type_namespaces() -> (
    dict[str, dict[str, dict[str, list[str]]]]
):
    """Returns a dictionary of object types and their namespaces."""
    response = {}
    response["types"] = {}
    for objtype in r.types:
        response["types"][objtype] = {}
        response["types"][objtype]["namespaces"] = sorted(
            list(r.types[objtype].namespaces.keys())
        )
    return response


@router.get(
    "/list",
    summary="Get a list (without the enclosing dict) of all namespaces in the registry (regardless of object type)",
    description="Returns a list of all namespaces in the registry.",
    response_model=ListOfStringsResponse,
)
async def get_namespace_list() -> StringsListType:
    """Returns a list of all namespaces in the registry."""
    namespaces = set()
    for objtype in r.types:
        for namespace in r.types[objtype].namespaces:
            namespaces.add(namespace)
    return sorted(list(namespaces))


@router.get(
    "/{objtype}",
    summary="Get the namespaces in the registry for a given object type",
    description="Returns a dictionary containing a list of namespaces for a given object type in the registry, organized by object type.",
    response_model=NamespaceDictResponse,
)
async def get_namespace_list_for_type(objtype: str) -> NamespaceDictType:
    """Returns a dict of all namespaces for a given object type in the registry."""
    result = lookup_objtype(objtype=objtype, registry=r)
    _404_on_none(result)
    response = {"types": {}}
    response["types"][objtype] = {}
    response["types"][objtype]["namespaces"] = sorted(
        list(r.types[objtype].namespaces.keys())
    )

    return response


@router.get(
    "/{objtype}/list",
    summary="Get a list of namespaces for a given object type",
    description="Returns a list of namespaces (without the enclosing dict) for a given object type in the registry.",
    response_model=ListOfStringsResponse,
)
async def get_namespace_list_for_type(objtype: str) -> list[str]:
    """Returns a list of all namespaces for a given object type in the registry."""
    result = lookup_objtype(objtype=objtype, registry=r)
    _404_on_none(result)
    return sorted(list(result.namespaces.keys()))
