"""Types Router."""

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

from ssvc.api.response_models import (
    ListOfStringsResponse,
    StringsListType,
    TypesDictResponse,
)
from ssvc.api.response_models._type_defs import TypesDictType
from ssvc.registry.base import get_registry

r = get_registry()

router = APIRouter(prefix="/objtypes", tags=["SSVC Object Types"])


@router.get(
    "/",
    summary="Get all object types",
    description="Returns a dictionary containing a list of all object types available in the SSVC registry.",
    response_model=TypesDictResponse,
)
async def get_object_types() -> TypesDictType:
    """Returns a dictionary of all object types in the registry."""
    response = {"types": sorted(list(r.types.keys()))}
    return response


@router.get(
    "/list",
    summary="Retrieve a list of available object types",
    description="Returns a sorted list (without the enclosing dict) of all object types available in the SSVC registry.",
    response_model=ListOfStringsResponse,
)
async def get_object_type_list() -> StringsListType:
    """Returns a list of all object types in the registry."""
    return sorted(list(r.types.keys()))
