#  Copyright (c) 2024 Carnegie Mellon University and Contributors.
#  - see Contributors.md for a full list of Contributors
#  - see ContributionInstructions.md for information on how you can Contribute to this project
#  Stakeholder Specific Vulnerability Categorization (SSVC) is
#  licensed under a MIT (SEI)-style license, please see LICENSE.md distributed
#  with this Software or contact permission@sei.cmu.edu for full terms.
#  Created, in part, with funding and support from the United States Government
#  (see Acknowledgments file). This program may include and/or can make use of
#  certain third party source code, object code, documentation and other files
#  (“Third Party Software”). See LICENSE.md for more details.
#  Carnegie Mellon®, CERT® and CERT Coordination Center® are registered in the
#  U.S. Patent and Trademark Office by Carnegie Mellon University

from ssvc.decision_points import SsvcDecisionPoint, SsvcDecisionPointValue
from ssvc.decision_points.helpers import print_versions_and_diffs

MINIMAL = SsvcDecisionPointValue(
    name="Minimal",
    key="M",
    description="Neither Support nor Essential apply. "
    "The vulnerable component may be used within the entities, but it is not used as a mission-essential component, nor does it provide impactful support to mission-essential functions.",
)

SUPPORT = SsvcDecisionPointValue(
    name="Support",
    key="S",
    description="The vulnerable component only supports MEFs for two or more entities.",
)

ESSENTIAL = SsvcDecisionPointValue(
    name="Essential",
    key="E",
    description="The vulnerable component directly provides capabilities that constitute at least one MEF for at least one entity; component failure may (but does not necessarily) lead to overall mission failure.",
)


MISSION_PREVALENCE = SsvcDecisionPoint(
    name="Mission Prevalence",
    description="Prevalence of the mission essential functions",
    key="MP",
    version="1.0.0",
    values=(
        MINIMAL,
        SUPPORT,
        ESSENTIAL,
    ),
)

if __name__ == "__main__":
    versions = (MISSION_PREVALENCE,)

    print_versions_and_diffs(versions)
