#!/usr/bin/env python
"""
Models the AIVSS Financial Impact decision point.
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

# Financial Impact
#
# 0.0: System designed to minimize financial risks, with real-time fraud prevention, anomaly detection, and comprehensive insurance coverage.
# 0.1-0.3: Robust financial controls and fraud detection mechanisms in place, regular audits conducted to identify and mitigate financial risks.
# 0.4-0.6: Some measures to mitigate financial risks (e.g., transaction limits), but no comprehensive risk assessment or fraud prevention mechanisms.
# 0.7-1.0: High risk of significant financial loss due to system errors or malicious attacks, no safeguards in place.
# Examples:
# 0.0: System has multiple layers of financial controls, real-time fraud prevention, and insurance against financial losses.
# 0.2: System uses advanced fraud detection algorithms and undergoes regular financial audits.
# 0.5: System has some transaction limits and basic fraud monitoring.
# 0.8: System errors could lead to large unauthorized transactions without any detection.

MINIMIZED_RISK = DecisionPointValue(
    name="Minimized Risk",
    key="M",
    description="System designed to minimize financial risks, with real-time fraud prevention, anomaly detection, and comprehensive insurance coverage.",
)

ROBUST_CONTROLS = DecisionPointValue(
    name="Robust Controls",
    key="R",
    description="Robust financial controls and fraud detection mechanisms in place, regular audits conducted to identify and mitigate financial risks.",
)

SOME_MEASURES = DecisionPointValue(
    name="Some Measures",
    key="S",
    description="Some measures to mitigate financial risks, but no comprehensive risk assessment or fraud prevention mechanisms.",
)

HIGH_RISK = DecisionPointValue(
    name="High Risk",
    key="H",
    description="High risk of significant financial loss due to system errors or malicious attacks, no safeguards in place.",
)

FINANCIAL_IMPACT = AivssDecisionPoint(
    name="Financial Impact",
    key="FI",
    version="1.0.0",
    description="Degree to which the system mitigates financial risks and incorporates financial safeguards.",
    values=(MINIMIZED_RISK, ROBUST_CONTROLS, SOME_MEASURES, HIGH_RISK),
)

VERSIONS = [FINANCIAL_IMPACT]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
