#!/usr/bin/env python
"""
CVSS Subsequent System Integrity Impact Decision Point
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

from ssvc.decision_points.cvss.helpers import modify_4, no_x
from ssvc.decision_points.cvss.subsequent_integrity_impact import (
    SUBSEQUENT_INTEGRITY_IMPACT_1 as SI,
)

MSI = modify_4(SI)

MSI_NoX = no_x(MSI)


VERSIONS = (MSI,)
LATEST = VERSIONS[-1]


def main():
    from ssvc.decision_points.helpers import print_versions_and_diffs

    print_versions_and_diffs(VERSIONS)

    print_versions_and_diffs(
        [
            MSI_NoX,
        ]
    )


if __name__ == "__main__":
    main()
