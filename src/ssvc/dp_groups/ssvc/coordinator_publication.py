#!/usr/bin/env python
"""
file: coordinator_publication
author: adh
created_at: 9/21/23 11:40 AM
"""
#  Copyright (c) 2023-2025 Carnegie Mellon University.
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

from ssvc.decision_points.ssvc.exploitation import EXPLOITATION_1
from ssvc.decision_points.ssvc.public_value_added import PUBLIC_VALUE_ADDED_1
from ssvc.decision_points.ssvc.supplier_involvement import (
    SUPPLIER_INVOLVEMENT_1,
)
from ssvc.dp_groups.base import DecisionPointGroup


COORDINATOR_PUBLICATION_1 = DecisionPointGroup(
    name="Coordinator Publication",
    definition="The decision points used by the coordinator during publication.",
    version="1.0.0",
    decision_points=(
        SUPPLIER_INVOLVEMENT_1,
        EXPLOITATION_1,
        PUBLIC_VALUE_ADDED_1,
    ),
)
"""
Added in SSVC v2, the Coordinator Publication v1.0.0 decision points are used by the coordinator during the publication process.

It includes decision points:

- Supplier Involvement v1.0.0
- Exploitation v1.0.0
- Public Value Added v1.0.0
"""

VERSIONS = (COORDINATOR_PUBLICATION_1,)
LATEST = VERSIONS[-1]


def main():
    for version in VERSIONS:
        print(version.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
