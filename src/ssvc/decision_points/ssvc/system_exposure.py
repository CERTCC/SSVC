#!/usr/bin/env python

"""
Provides the System Exposure decision point and its values.
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

from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_points.helpers import print_versions_and_diffs
from ssvc.decision_points.ssvc.base import SsvcDecisionPoint

EXP_UNAVOIDABLE = DecisionPointValue(
    name="Unavoidable",
    key="U",
    definition="Internet or another widely accessible network where access cannot plausibly be restricted or "
    "controlled (e.g., DNS servers, web servers, VOIP servers, email servers)",
)

EXP_CONTROLLED = DecisionPointValue(
    name="Controlled",
    key="C",
    definition="Networked service with some access restrictions or mitigations already in place (whether locally or on the network). "
    "A successful mitigation must reliably interrupt the adversary’s attack, which requires the attack is detectable "
    "both reliably and quickly enough to respond. Controlled covers the situation in which a vulnerability can be "
    "exploited through chaining it with other vulnerabilities. The assumption is that the number of steps in the "
    "attack path is relatively low; if the path is long enough that it is implausible for an adversary to reliably "
    "execute it, then exposure should be small.",
)

EXP_SMALL = DecisionPointValue(
    name="Small",
    key="S",
    definition="Local service or program; highly controlled network",
)


SYSTEM_EXPOSURE_1 = SsvcDecisionPoint(
    name="System Exposure",
    definition="The Accessible Attack Surface of the Affected System or Service",
    key="EXP",
    version="1.0.0",
    values=(
        EXP_SMALL,
        EXP_CONTROLLED,
        EXP_UNAVOIDABLE,
    ),
)

# EXP_OPEN is just a rename of EXP_UNAVOIDABLE
EXP_OPEN = DecisionPointValue(
    name="Open",
    key="O",
    definition="Internet or another widely accessible network where access cannot plausibly be restricted or "
    "controlled (e.g., DNS servers, web servers, VOIP servers, email servers)",
)


SYSTEM_EXPOSURE_1_0_1 = SsvcDecisionPoint(
    name="System Exposure",
    definition="The Accessible Attack Surface of the Affected System or Service",
    key="EXP",
    version="1.0.1",
    values=(
        EXP_SMALL,
        EXP_CONTROLLED,
        EXP_OPEN,
    ),
)

VERSIONS = (SYSTEM_EXPOSURE_1, SYSTEM_EXPOSURE_1_0_1)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
