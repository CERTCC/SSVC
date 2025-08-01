#!/usr/bin/env python
"""
Models the AIVSS Auditing decision point.
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

# Auditing
#
# 0.0: Regular independent audits by reputable third parties, with formal verification of the system's security, fairness, and ethical performance.
# 0.1-0.3: Regular internal audits conducted, covering all aspects of the AI system lifecycle, with clear audit trails and documentation.
# 0.4-0.6: Infrequent or limited audits (e.g., only auditing code for security vulnerabilities), with no independent verification.
# 0.7-1.0: No auditing of the AI system's design, development, deployment, or operation.
# Examples:
# 0.0: Independent audits are conducted annually by a reputable third party, with the results publicly reported.
# 0.2: Regular internal audits are conducted, covering security, fairness, and performance, with detailed audit trails.
# 0.5: Code is audited for security vulnerabilities before deployment, but no other audits are conducted.
# 0.8: No audit logs are maintained, and no audits are performed.

INDEPENDENT = DecisionPointValue(
    name="Independent Audits",
    key="I",
    description="Regular independent audits by reputable third parties, with formal verification of the system's security, fairness, and ethical performance.",
)

INTERNAL = DecisionPointValue(
    name="Internal Audits",
    key="N",
    description="Regular internal audits conducted, covering all aspects of the AI system lifecycle, with clear audit trails and documentation.",
)

LIMITED = DecisionPointValue(
    name="Limited Audits",
    key="L",
    description="Infrequent or limited audits, with no independent verification.",
)

NONE = DecisionPointValue(
    name="None",
    key="O",
    description="No auditing of the AI system's design, development, deployment, or operation.",
)

AUDITING = AivssDecisionPoint(
    name="Auditing",
    key="AU",
    version="1.0.0",
    description="Degree to which the AI system is subject to regular, independent, and comprehensive audits.",
    values=(INDEPENDENT, INTERNAL, LIMITED, NONE),
)

VERSIONS = [AUDITING]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()

