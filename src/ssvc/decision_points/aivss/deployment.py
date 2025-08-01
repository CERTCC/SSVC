#!/usr/bin/env python
"""
Models the AIVSS Deployment decision point.
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

# Deployment
#
# 0.0: Secure and isolated deployment environment with continuous monitoring, automated security patching, and formal verification of the deployment process.
# 0.1-0.3: Secure deployment environment with strong authentication and authorization, regular security updates, and intrusion detection systems.
# 0.4-0.6: Basic security measures in the deployment environment (e.g., model deployed behind a firewall), but no strong authentication or authorization mechanisms.
# 0.7-1.0: Insecure deployment environment, no access controls or security monitoring, model deployed on publicly accessible servers without any protection.
# Examples:
# 0.0: Model is deployed in a secure enclave with strict access controls, continuous monitoring, and automated security patching.
# 0.2: Model is deployed in a secure cloud environment with strong authentication, authorization, and regular security updates.
# 0.5: Model is deployed behind a firewall, but API keys are shared among multiple users.
# 0.8: Model is deployed on a public server with no authentication required to access its API.

FORMAL_VERIFICATION = DecisionPointValue(
    name="Formal Verification",
    key="F",
    description="Secure and isolated deployment environment with continuous monitoring, automated security patching, and formal verification of the deployment process.",
)

SECURE_ENVIRONMENT = DecisionPointValue(
    name="Secure Environment",
    key="S",
    description="Secure deployment environment with strong authentication and authorization, regular security updates, and intrusion detection systems.",
)

BASIC_SECURITY = DecisionPointValue(
    name="Basic Security Measures",
    key="B",
    description="Basic security measures in the deployment environment, but no strong authentication or authorization mechanisms.",
)

INSECURE = DecisionPointValue(
    name="Insecure Environment",
    key="I",
    description="Insecure deployment environment, no access controls or security monitoring, model deployed on publicly accessible servers without any protection.",
)

DEPLOYMENT = AivssDecisionPoint(
    name="Deployment",
    key="DPY",
    version="1.0.0",
    description="Degree to which secure practices are implemented in the deployment environment and process.",
    values=(FORMAL_VERIFICATION, SECURE_ENVIRONMENT, BASIC_SECURITY, INSECURE),
)

VERSIONS = [DEPLOYMENT]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()

