#!/usr/bin/env python
"""
API for SSVC
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

from typing import Any

from fastapi import FastAPI, HTTPException

from ssvc.registry import get_registry
from ssvc.registry.base import (
    _Key,
    _Namespace,
    _NonValuedVersion,
    _NsType,
    _ValuedVersion,
    lookup_key,
    lookup_namespace,
    lookup_objtype,
    lookup_version,
)

app = FastAPI()

r = get_registry()


@app.get("/")
def read_root():
    return {"Hello": "SSVC World"}


def _404_on_none(obj: Any):
    if obj is None:
        raise HTTPException(status_code=404, detail=f"Item not found")
    return obj


@app.get("/decision_points")
async def get_decision_points() -> _NsType:
    decision_points = lookup_objtype(objtype="DecisionPoint", registry=r)
    _404_on_none(decision_points)
    return decision_points


@app.get("/decision_points/{namespace}")
async def get_decision_points(namespace: str) -> _Namespace:
    decision_points = lookup_namespace(
        objtype="DecisionPoint", namespace=namespace, registry=r
    )
    _404_on_none(decision_points)
    return decision_points


@app.get("/decision_points/{namespace}/{key}")
async def get_decision_points(namespace: str, key: str) -> _Key:
    decision_points = lookup_key(
        objtype="DecisionPoint", namespace=namespace, key=key, registry=r
    )
    _404_on_none(decision_points)
    return decision_points


@app.get("/decision_points/{namespace}/{key}/{version}")
async def get_decision_points(
    namespace: str, key: str, version: str
) -> _ValuedVersion:
    decision_points = lookup_version(
        objtype="DecisionPoint",
        namespace=namespace,
        key=key,
        version=version,
        registry=r,
    )
    _404_on_none(decision_points)
    return decision_points


@app.get("/decision_tables")
async def get_decision_tables() -> _NsType:
    # load registry and return decision tables
    decision_tables = lookup_objtype(objtype="DecisionTable", registry=r)
    _404_on_none(decision_tables)
    return decision_tables


@app.get("/decision_tables/{namespace}")
async def get_decision_tables_namespace(namespace: str) -> _Namespace:
    decision_tables = lookup_namespace(
        objtype="DecisionTable", namespace=namespace, registry=r
    )
    _404_on_none(decision_tables)
    return decision_tables


@app.get("/decision_tables/{namespace}/{key}")
async def get_decision_tables_key(namespace: str, key: str) -> _Key:
    decision_tables = lookup_key(
        objtype="DecisionTable", namespace=namespace, key=key, registry=r
    )
    _404_on_none(decision_tables)
    return decision_tables


@app.get("/decision_tables/{namespace}/{key}/{version}")
async def get_decision_tables_version(
    namespace: str, key: str, version: str
) -> _NonValuedVersion:
    decision_tables = lookup_version(
        objtype="DecisionTable",
        namespace=namespace,
        key=key,
        version=version,
        registry=r,
    )
    _404_on_none(decision_tables)
    return decision_tables
