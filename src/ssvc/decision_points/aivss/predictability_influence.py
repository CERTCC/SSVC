#!/usr/bin/env python

"""
Provides TODO writeme
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

# Verifiable
# Behavior is traceable, reproducible, and backed by strong logging or proofs.
# Outputs align with clear rules, and any action can be independently checked.
# Unexpected deviations are rare and easy to diagnose.
# Uncertain
# Behavior is generally well-structured but can deviate within known bounds.
# Some reasoning steps or interactions lack full visibility, making verification partial.
# Issues may be diagnosable but require effort or contextual reconstruction.
# Opaque
# Behavior is highly variable, difficult to trace, and resistant to verification.
# Key reasoning paths, external influences, or interactions are hidden or unpredictable.
# Actions may appear coherent but cannot be reliably reproduced or audited.

VERIFIABLE = DecisionPointValue(
    name="Verifiable",
    key="V",
    definition=(
        "Behavior is traceable, reproducible, and backed by strong logging or proofs. "
        "Outputs align with clear rules, and any action can be independently checked. "
        "Unexpected deviations are rare and easy to diagnose."
    ),
)
UNCERTAIN = DecisionPointValue(
    name="Uncertain",
    key="U",
    definition=(
        "Behavior is generally well-structured but can deviate within known bounds. "
        "Some reasoning steps or interactions lack full visibility, making verification partial. "
        "Issues may be diagnosable but require effort or contextual reconstruction."
    ),
)
OPAQUE = DecisionPointValue(
    name="Opaque",
    key="O",
    definition=(
        "Behavior is highly variable, difficult to trace, and resistant to verification. "
        "Key reasoning paths, external influences, or interactions are hidden or unpredictable. "
        "Actions may appear coherent but cannot be reliably reproduced or audited."
    ),
)

PREDICTABILITY_INFLUENCE_01 = AivssDecisionPoint(
    key="PI",
    name="Predictability and Influence",
    definition="TODO writeme",
    version="1.0.0",
    values=(VERIFIABLE, UNCERTAIN, OPAQUE),
)

VERSIONS = (PREDICTABILITY_INFLUENCE_01,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
