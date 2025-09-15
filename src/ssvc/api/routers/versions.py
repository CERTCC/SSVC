"""Versions API Router."""

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
    ListOfStringsResponse,
    StringsListType,
    VersionDictResponse,
    VersionDictType,
)
from ssvc.registry.base import get_registry, lookup_key

router = APIRouter(prefix="/versions", tags=["SSVC Versions"])
r = get_registry()


@router.get(
    "/{objtype}/{namespace}/{key}",
    summary="Get the version strings for a given object type, namespace, and key.",
    description="Returns a dict for a specific object type, namespace, and key in the SSVC registry containing a list of version strings available.",
    response_model=VersionDictResponse,
)
async def get_version_dict_for_key(
    objtype: str, namespace: str, key: str
) -> VersionDictType:
    """Returns a dictionary of all versions for a given object type, namespace, and key in the registry."""
    k = lookup_key(objtype=objtype, namespace=namespace, key=key, registry=r)
    _404_on_none(k)

    response = {
        "types": {objtype: {"namespaces": {namespace: {"keys": {key: {}}}}}}
    }
    response["types"][objtype]["namespaces"][namespace]["keys"][key][
        "versions"
    ] = sorted(list(k.versions.keys()))

    return response


@router.get(
    "/{objtype}/{namespace}/{key}/list",
    summary="Get the list (without the enclosing dict) of version strings for a given object type, namespace, and key.",
    description="Returns a sorted list of version strings available for the specified object type, namespace, and key in the SSVC registry.",
    response_model=ListOfStringsResponse,
)
async def get_version_list_for_key(
    objtype: str, namespace: str, key: str
) -> StringsListType:
    """Returns a list of all versions for a given object type, namespace, and key in the registry."""
    k = lookup_key(objtype=objtype, namespace=namespace, key=key, registry=r)
    _404_on_none(k)
    return sorted(list(k.versions.keys()))
