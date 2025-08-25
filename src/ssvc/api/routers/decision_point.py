#!/usr/bin/env python
"""
API Routes for decision_point
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

from fastapi import HTTPException

from ssvc.api.helpers import _404_on_none
from ssvc.decision_points.base import DecisionPoint
from ssvc.registry.base import get_registry
from ssvc.registry.base import lookup_version

r = get_registry()

from fastapi import APIRouter


router = APIRouter(prefix="/decision_point", tags=["Decision Point"])


@router.get("/", response_model=DecisionPoint)
async def get_decision_point_by_id(id: str) -> DecisionPoint:
    """Returns a single DecisionPoint object by its ID."""
    try:
        (namespace, key, version) = id.split(":")
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="ID must be in the format 'namespace:key:version'",
        )

    version = lookup_version(
        objtype="DecisionPoint",
        namespace=namespace,
        key=key,
        version=version,
        registry=r,
    )
    _404_on_none(version)
    return version.obj


def main():
    pass


if __name__ == "__main__":
    main()
