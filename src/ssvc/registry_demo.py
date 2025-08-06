#!/usr/bin/env python
"""
Demonstrates the SSVC registry and schema.
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

import logging

from ssvc.registry import get_registry
from ssvc.registry.base import SsvcObjectRegistry
from ssvc.utils.misc import order_schema

logger = logging.getLogger(__name__)


def main():
    # importing the ssvc module forces the registry to be initialized
    import ssvc  # noqa: F401

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    registry = get_registry()

    print(registry.model_dump_json(indent=2))

    print()
    print()
    import json

    schema = SsvcObjectRegistry.model_json_schema()
    schema = order_schema(schema)
    print(json.dumps(schema, indent=2))

    print()
    print("# Lookup demo")
    search_for = {
        "objtype": "DecisionPoint",
        "namespace": "ssvc",
        "key": "EXP",
    }

    dp = registry.lookup(**search_for)
    print(dp.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
