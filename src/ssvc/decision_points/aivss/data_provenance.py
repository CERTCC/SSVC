#!/usr/bin/env python
"""
Models the AIVSS Data Provenance decision point.
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

# Data Provenance
#
# 0.0: Data provenance formally verified and auditable, with mechanisms to ensure the authenticity and trustworthiness of the data source.
# 0.1-0.3: Detailed data lineage tracked, including all transformations and processing steps, with a clear audit trail.
# 0.4-0.6: Basic information about data sources available, but lineage is incomplete or unclear.
# 0.7-1.0: No information about data origin, collection methods, or transformations.
# Examples:
# 0.0: Data provenance is cryptographically verified and tamper-proof.
# 0.2: Full data lineage is tracked, including all processing steps and data owners.
# 0.5: Data sources are documented, but the transformations applied are not clearly recorded.
# 0.9: Origin and collection method of the data are unknown.

FORMALLY_VERIFIED = DecisionPointValue(
    name="Formally Verified",
    key="F",
    description="Data provenance formally verified and auditable, with mechanisms to ensure authenticity and trustworthiness.",
)

DETAILED_LINEAGE = DecisionPointValue(
    name="Detailed Lineage",
    key="D",
    description="Detailed data lineage tracked, including all transformations and processing steps, with a clear audit trail.",
)

BASIC_INFO = DecisionPointValue(
    name="Basic Info",
    key="B",
    description="Basic information about data sources available, but lineage is incomplete or unclear.",
)

_NONE = DecisionPointValue(
    name="None",
    key="N",
    description="No information about data origin, collection methods, or transformations.",
)

DATA_PROVENANCE = AivssDecisionPoint(
    name="Data Provenance",
    key="DP",
    version="1.0.0",
    description="Degree to which the provenance of data is tracked, verified, and auditable.",
    values=(FORMALLY_VERIFIED, DETAILED_LINEAGE, BASIC_INFO, _NONE),
)

VERSIONS = [DATA_PROVENANCE]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
