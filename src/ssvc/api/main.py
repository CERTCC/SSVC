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

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

import ssvc  # noqa: F401
from ssvc.api.helpers import _404_on_none
from ssvc.api.routers import (
    decision_point,
    decision_points,
    decision_table,
    decision_tables,
    namespaces,
)
from ssvc.registry.base import (
    get_registry,
    lookup_key,
    lookup_namespace,
    lookup_objtype,
)

r = get_registry()

app = FastAPI(
    title="SSVC Object Registry API",
    description="An API for accessing SSVC decision points and decision tables.",
    version="0.1.0",
    contact={
        "name": "CERT/CC SSVC Team",
        "url": "https://certcc.github.io/SSVC/",
        "email": "cert@cert.org",
    },
)
app.include_router(decision_point.router)
app.include_router(decision_points.router)
app.include_router(decision_table.router)
app.include_router(decision_tables.router)
app.include_router(namespaces.router)


# root should redirect to docs
# at least until we have something better to show
@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")


@app.get("/types", response_model=list[str])
def get_type_list() -> list[str]:
    """Returns a list of all object types in the registry."""
    return sorted(list(r.types.keys()))


@app.get("/namespaces/{type}", response_model=list[str])
def get_namespace_list_for_type(type: str) -> list[str]:
    """Returns a list of all namespaces for a given object type in the registry."""
    objtype = lookup_objtype(objtype=type, registry=r)
    _404_on_none(objtype)
    return sorted(list(objtype.namespaces.keys()))


@app.get("/keys/{type}/{namespace}", response_model=list[str])
def get_key_list_for_namespace(type: str, namespace: str) -> list[str]:
    """Returns a list of all keys for a given object type and namespace in the registry."""
    ns = lookup_namespace(objtype=type, namespace=namespace, registry=r)
    _404_on_none(ns)
    return sorted(list(ns.keys.keys()))


@app.get("/versions/{type}/{namespace}/{key}", response_model=list[str])
def get_version_list_for_key(type: str, namespace: str, key: str) -> list[str]:
    """Returns a list of all versions for a given object type, namespace, and key in the registry."""
    k = lookup_key(objtype=type, namespace=namespace, key=key, registry=r)
    _404_on_none(k)
    return sorted(list(k.versions.keys()))
