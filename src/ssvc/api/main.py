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
from ssvc.api.routers import (
    decision_point,
    decision_points,
    decision_table,
    decision_tables,
    keys,
    namespaces,
    objects,
    types,
    versions,
)
from ssvc.registry.base import (
    get_registry,
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
app.include_router(types.router)
app.include_router(namespaces.router)
app.include_router(keys.router)
app.include_router(versions.router)
app.include_router(objects.router)


# root should redirect to docs
# at least until we have something better to show
@app.get("/", include_in_schema=False)
async def redirect_root_to_docs():
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    from tabulate import tabulate

    rows = []
    for route in app.routes:
        methods = ",".join(sorted(route.methods - {"HEAD", "OPTIONS"}))
        response_model = getattr(route, "response_model", None)
        response_model_name = response_model.__name__ if response_model else ""
        description = getattr(route, "summary", "") or getattr(
            route, "description", ""
        )
        rows.append([route.path, methods, response_model_name, description])

    table = tabulate(
        rows,
        headers=["Path", "Methods", "Response Model", "Description"],
        tablefmt="github",
    )
    print(table)
