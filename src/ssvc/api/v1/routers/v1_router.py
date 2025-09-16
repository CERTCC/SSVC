#!/usr/bin/env python
"""
API version 1 router for SSVC
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
from fastapi import APIRouter

from ssvc.api.v1.routers import (
    decision_point,
    decision_table,
    decision_tables,
    objects,
)
from ssvc.api.v1.routers import (
    decision_points,
    keys,
    namespaces,
    types,
    versions,
)

router_v1 = APIRouter(prefix="/v1", tags=["v1"])
router_v1.include_router(decision_point.router)
router_v1.include_router(decision_points.router)
router_v1.include_router(decision_table.router)
router_v1.include_router(decision_tables.router)
router_v1.include_router(types.router)
router_v1.include_router(namespaces.router)
router_v1.include_router(keys.router)
router_v1.include_router(versions.router)
router_v1.include_router(objects.router)


def main():
    pass


if __name__ == "__main__":
    main()
