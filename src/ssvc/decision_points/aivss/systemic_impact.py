#!/usr/bin/env python

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

"""
Provides TODO writeme
"""
from ssvc.decision_points.aivss.base import AivssDecisionPoint
from ssvc.decision_points.base import DecisionPointValue

# Decision Point 3: Systemic Impact
# This measures the mission-criticality and blast radius of the systems, data, and processes the agent can affect.
#
# Contained: The impact of a compromise is limited to the agent itself, a single user's data, or a non-critical system. The business or mission impact is negligible.
# Significant: A compromise would impact a major business function, a critical internal system, or cause cascading failures within a business unit. It could result in moderate financial loss, reputational damage, or operational disruption.
# Critical: A compromise would pose a threat to the entire organization's viability, public safety, or critical infrastructure. It could lead to severe financial loss, widespread data breach, regulatory failure, or physical harm.

CONTAINED = DecisionPointValue(
    key="C",
    name="Contained",
    definition="The impact of a compromise is limited to the agent itself, a single user's data, or a non-critical system. The business or mission impact is negligible.",
)
SIGNIFICANT = DecisionPointValue(
    key="S",
    name="Significant",
    definition="A compromise would impact a major business function, a critical internal system, or cause cascading failures within a business unit. It could result in moderate financial loss, reputational damage, or operational disruption.",
)
CRITICAL = DecisionPointValue(
    key="R",
    name="Critical",
    definition="A compromise would pose a threat to the entire organization's viability, public safety, or critical infrastructure. It could lead to severe financial loss, widespread data breach, regulatory failure, or physical harm.",
)
SYSTEMIC_IMPACT_01 = AivssDecisionPoint(
    key="SI",
    name="Systemic Impact",
    definition=(
        "Measures the mission-criticality and blast radius of the systems, data, and processes the agent can affect."
    ),
    version="1.0.0",
    values=(CONTAINED, SIGNIFICANT, CRITICAL),
)
VERSIONS = (SYSTEMIC_IMPACT_01,)
LATEST = VERSIONS[-1]


def main():
    from ssvc.decision_points.helpers import print_versions_and_diffs

    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
