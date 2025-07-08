#!/usr/bin/env python
"""
Provides a decision point for assessing the relevance of threat events based on Table E-4 from NIST SP 800-30 Revision 1.
RELEVANCE OF THREAT EVENTS
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
from ssvc.decision_points.nist.base import NistDecisionPoint

CONFIRMED = DecisionPointValue(
    name="Confirmed",
    description="The threat event or TTP has been seen by the organization.",
    key="C",
)
EXPECTED = DecisionPointValue(
    name="Expected",
    description="The threat event or TTP has been seen by the organization’s peers or partners.",
    key="E",
)
ANTICIPATED = DecisionPointValue(
    name="Anticipated",
    description="The threat event or TTP has been reported by a trusted source.",
    key="A",
)
PREDICTED = DecisionPointValue(
    name="Predicted",
    description="The threat event or TTP has been predicted by a trusted source.",
    key="P",
)
POSSIBLE = DecisionPointValue(
    name="Possible",
    description="The threat event or TTP has been described by a somewhat credible source.",
    key="PS",
)
NOT_APPLICABLE = DecisionPointValue(
    name="N/A",
    description="The threat event or TTP is not currently applicable. For example, a threat event or TTP could assume "
    "specific technologies, architectures, or processes that are not present in the organization, "
    "mission/business process, EA segment, or information system; or predisposing conditions that are not "
    "present (e.g., location in a flood plain). Alternately, if the organization is using detailed or "
    "specific threat information, a threat event or TTP could be deemed inapplicable because information "
    "indicates that no adversary is expected to initiate the threat event or use the TTP.",
    key="NA",
)

THREAT_EVENT_RELEVANCE = NistDecisionPoint(
    name="Threat Event Relevance",
    description="Relevance of threat events",
    key="TER",
    version="1.0.0",
    values=(
        NOT_APPLICABLE,
        POSSIBLE,
        PREDICTED,
        ANTICIPATED,
        EXPECTED,
        CONFIRMED,
    ),
)

VERSIONS = [
    THREAT_EVENT_RELEVANCE,
]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
