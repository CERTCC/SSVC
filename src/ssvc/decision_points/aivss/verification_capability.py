#!/usr/bin/env python
"""
Provides the AIVSS Verification Capability Decision Point for SSVC.
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

PROVABLE = DecisionPointValue(
    key="P",
    name="Provable",
    definition="Critical safety or correctness invariants can be verified.",
)

KEY_INVARIANTS = DecisionPointValue(
    key="K",
    name="Key Invariants Verifiable",
    definition="Some critical properties can be verified, but not all.",
)

UNVERIFIABLE = DecisionPointValue(
    key="U",
    name="Unverifiable",
    definition="Cannot prove correctness or invariants in practice.",
)

VERIFICATION_CAPABILITY_01 = AivssDecisionPoint(
    key="VC",
    name="Verification Capability",
    definition="Indicates whether the system’s critical properties can be formally or practically verified.",
    version="1.0.0",
    values=(PROVABLE, KEY_INVARIANTS, UNVERIFIABLE),
)

VERSIONS = (VERIFICATION_CAPABILITY_01,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
