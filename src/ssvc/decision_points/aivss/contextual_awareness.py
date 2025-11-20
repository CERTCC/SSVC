#!/usr/bin/env python

"""
Provides the AIVSS Contextual Awareness Decision Point for SSVC.
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

# ## 2. Contextual Awareness
# - Isolated — no external contextual signals.
# - Trusted-Signal — uses only vetted, narrow, structured signals.
# - Ambient — reacts to broad, open-ended environmental signals.

ISOLATED = DecisionPointValue(
    key="I",
    name="Isolated",
    definition="No external contextual signals.",
)

TRUSTED_SIGNAL = DecisionPointValue(
    key="T",
    name="Trusted-Signal",
    definition="Uses only vetted, narrow, structured signals.",
)

AMBIENT = DecisionPointValue(
    key="A",
    name="Ambient",
    definition="Reacts to broad, open-ended environmental signals.",
)

CONTEXTUAL_AWARENESS_01 = AivssDecisionPoint(
    key="CA",
    name="Contextual Awareness",
    definition=(
        "Determines the degree to which an AI system senses and incorporates context "
        "from its environment and external signals."
    ),
    version="1.0.0",
    values=(ISOLATED, TRUSTED_SIGNAL, AMBIENT),
)

VERSIONS = (CONTEXTUAL_AWARENESS_01,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
