#!/usr/bin/env python
"""
Models the AIVSS Training decision point.
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

# Training
#
# 0.0: Secure and isolated training environment with formal verification of the training process, strict access controls, and continuous monitoring for intrusions and anomalies.
# 0.1-0.3: Secure training environment with access controls, data encryption at rest and in transit, and regular security audits.
# 0.4-0.6: Basic security measures in the training environment (e.g., training data stored on a password-protected server), but no encryption or strict access controls.
# 0.7-1.0: Insecure training environment, no data security or access controls, training data stored and processed on unsecured systems.
# Examples:
# 0.0: Training is performed in a secure enclave with strict access controls, continuous monitoring, and formal verification of the training process.
# 0.2: Training data is encrypted at rest and in transit, access is restricted based on roles, and the training environment is regularly audited for security.
# 0.5: Training data is stored on a password-protected server, but access is not strictly controlled.
# 0.8: Training data is stored on a public cloud server without any encryption or access controls.

FORMAL_VERIFICATION = DecisionPointValue(
    name="Formal Verification",
    key="F",
    description="Secure and isolated training environment with formal verification of the training process, strict access controls, and continuous monitoring for intrusions and anomalies.",
)

SECURE_ENVIRONMENT = DecisionPointValue(
    name="Secure Environment",
    key="S",
    description="Secure training environment with access controls, data encryption at rest and in transit, and regular security audits.",
)

BASIC_SECURITY = DecisionPointValue(
    name="Basic Security Measures",
    key="B",
    description="Basic security measures in the training environment, but no encryption or strict access controls.",
)

INSECURE = DecisionPointValue(
    name="Insecure Environment",
    key="I",
    description="Insecure training environment, no data security or access controls, training data stored and processed on unsecured systems.",
)

TRAINING = AivssDecisionPoint(
    name="Training",
    key="TR",
    version="1.0.0",
    description="Degree to which secure practices are implemented in the training environment and process.",
    values=(FORMAL_VERIFICATION, SECURE_ENVIRONMENT, BASIC_SECURITY, INSECURE),
)

VERSIONS = [TRAINING]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
