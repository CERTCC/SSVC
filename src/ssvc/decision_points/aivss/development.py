#!/usr/bin/env python
"""
Models the AIVSS Development decision point.
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

# Development
#
# 0.0: Secure development environment with formal verification of code, strict access controls, and continuous monitoring for security threats.
# 0.1-0.3: Secure development lifecycle (SDL) practices followed, including code reviews, static analysis, and vulnerability scanning, with access controls on development resources.
# 0.4-0.6: Basic security measures in the development environment (e.g., developer workstations have antivirus software), some secure coding guidelines, but no formal secure development lifecycle (SDL).
# 0.7-1.0: Insecure development environment, no secure coding practices, no access controls on development resources.
# Examples:
# 0.0: Development environment is isolated and continuously monitored, with formal methods used to verify the security of critical code components.
# 0.2: SDL practices are followed, including code reviews, static analysis, and vulnerability scanning, with access to code repositories restricted based on roles.
# 0.5: Developers use company-provided laptops with basic security software, and some secure coding guidelines are in place.
# 0.8: Developers work on personal laptops with no security controls, and code is stored in a public repository without access restrictions.

FORMAL_VERIFICATION = DecisionPointValue(
    name="Formal Verification",
    key="F",
    description="Secure development environment with formal verification of code, strict access controls, and continuous monitoring for security threats.",
)

SDL_PRACTICES = DecisionPointValue(
    name="SDL Practices",
    key="S",
    description="Secure development lifecycle (SDL) practices followed, including code reviews, static analysis, and vulnerability scanning, with access controls on development resources.",
)

BASIC_SECURITY = DecisionPointValue(
    name="Basic Security Measures",
    key="B",
    description="Basic security measures in the development environment, some secure coding guidelines, but no formal SDL.",
)

INSECURE = DecisionPointValue(
    name="Insecure Environment",
    key="I",
    description="Insecure development environment, no secure coding practices, no access controls on development resources.",
)

DEVELOPMENT = AivssDecisionPoint(
    name="Development",
    key="DV",
    version="1.0.0",
    description="Degree to which secure development practices and environments are implemented.",
    values=(FORMAL_VERIFICATION, SDL_PRACTICES, BASIC_SECURITY, INSECURE),
)

VERSIONS = [DEVELOPMENT]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()

