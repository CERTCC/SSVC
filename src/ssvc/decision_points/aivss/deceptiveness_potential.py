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

"""
Provides a decision point to assess the deceptiveness potential of a vulnerability report.
"""
# ## 4. Deceptiveness Potential
# - **Plain** — structured, non-persona output.
# - **Fluent** — natural language output, but not convincingly human.
# - **Persuasive** — persona mimicry, deepfakes, or social-engineering capability.

from ssvc.decision_points.aivss.base import AivssDecisionPoint
from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_points.helpers import print_versions_and_diffs

PLAIN = DecisionPointValue(
    key="P",
    name="Plain",
    definition="Structured, non-persona output.",
)
FLUENT = DecisionPointValue(
    key="F",
    name="Fluent",
    definition="Natural language output, but not convincingly human.",
)
PERSUASIVE = DecisionPointValue(
    key="S",
    name="Persuasive",
    definition="Persona mimicry, deepfakes, or social-engineering capability.",
)

DECEPTIVENESS_POTENTIAL_01 = AivssDecisionPoint(
    key="DP",
    name="Deceptiveness Potential",
    definition=(
        "Assesses the potential for AI-generated vulnerability reports to be deceptive, "
        "ranging from plain structured output to highly persuasive content."
    ),
    version="1.0.0",
    values=(PLAIN, FLUENT, PERSUASIVE),
)

VERSIONS = (DECEPTIVENESS_POTENTIAL_01,)

LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
