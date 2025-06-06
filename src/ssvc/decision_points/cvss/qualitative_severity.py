#!/usr/bin/env python
"""
Provides a decision point for the [CVSS Qualitative Severity Rating Scale](https://www.first.org/cvss/v4.0/specification-document#Qualitative-Severity-Rating-Scale).
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

from ssvc.decision_points import SsvcDecisionPointValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs

QS_NONE = SsvcDecisionPointValue(
    name="None",
    key="N",
    description="No severity rating (0.0)",
)

LOW = SsvcDecisionPointValue(
    name="Low",
    key="L",
    description="Low (0.1 - 3.9)",
)
MEDIUM = SsvcDecisionPointValue(
    name="Medium",
    key="M",
    description="Medium (4.0 - 6.9)",
)
HIGH = SsvcDecisionPointValue(
    name="High",
    key="H",
    description="High (7.0 - 8.9)",
)
CRITICAL = SsvcDecisionPointValue(
    name="Critical",
    key="C",
    description="Critical (9.0 - 10.0)",
)

QUALITATIVE_SEVERITY = CvssDecisionPoint(
    name="CVSS Qualitative Severity Rating Scale",
    key="QS",
    description="The CVSS Qualitative Severity Rating Scale provides "
    "a categorical representation of a CVSS Score.",
    version="1.0.0",
    values=(
        QS_NONE,
        LOW,
        MEDIUM,
        HIGH,
        CRITICAL,
    ),
)

VERSIONS = (QUALITATIVE_SEVERITY,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
