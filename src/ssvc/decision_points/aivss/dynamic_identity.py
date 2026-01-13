#!/usr/bin/env python

"""
Provides the AIVSS Dynamic Identity Decision Point for SSVC.
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

from ssvc.decision_points.aivss.base import AivssDecisionPoint
from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_points.helpers import print_versions_and_diffs

# ## 4. Dynamic Identity
# - Fixed — single, constant identity.
# - Scoped Roles — limited role changes tied to specific tools or contexts.
# - Assumed Identity — cross-tenant, impersonation-like, or elevated role adoption.

FIXED = DecisionPointValue(
    key="F",
    name="Fixed",
    definition="Single, constant identity.",
)

SCOPED_ROLES = DecisionPointValue(
    key="S",
    name="Scoped Roles",
    definition="Limited role changes tied to specific tools or contexts.",
)

ASSUMED_IDENTITY = DecisionPointValue(
    key="A",
    name="Assumed Identity",
    definition="Cross-tenant, impersonation-like, or elevated role adoption.",
)

DYNAMIC_IDENTITY_01 = AivssDecisionPoint(
    key="DI",
    name="Dynamic Identity",
    definition=(
        "Describes how an AI system's identity and authorization context may change at runtime, "
        "including whether it can assume roles beyond a fixed identity."
    ),
    version="1.0.0",
    values=(FIXED, SCOPED_ROLES, ASSUMED_IDENTITY),
)

VERSIONS = (DYNAMIC_IDENTITY_01,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
