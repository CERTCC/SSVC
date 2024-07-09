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

import random

from ssvc.decision_points.automatable import AUTOMATABLE_2
from ssvc.decision_points.exploitation import EXPLOITATION_1_1_0
from ssvc.decision_points.technical_impact import TECHNICAL_IMPACT_1
from ssvc.dp_groups.base import SsvcDecisionPointGroup
from ssvc.selections import SsvcDecisionPointGroupSelection, SsvcDecisionPointSelection

group = SsvcDecisionPointGroup(
    decision_points=[EXPLOITATION_1_1_0, AUTOMATABLE_2, TECHNICAL_IMPACT_1],
    name="Test Group",
    description="This is a test group",
)


def make_random_selections(group: SsvcDecisionPointGroup):
    selections = SsvcDecisionPointGroupSelection(selections=[])
    for dp in group.decision_points:
        select = SsvcDecisionPointSelection(
            namespace=dp.namespace, name=dp.name, version=dp.version, values=[]
        )
        # choose one value at random
        value = random.choice(dp.values)
        # get the name of the value
        select.values.append(value.name)
        selections.selections.append(select)
    return selections


def main():
    selections = make_random_selections(group)

    print("######################")
    print("### Output example ###")
    print("######################")

    print(selections.to_json(indent=2))

    with open(
        "../../data/schema_examples/Decision_Point_Group_Selection.json", "w"
    ) as f:
        f.write(selections.to_json(indent=2))


if __name__ == "__main__":
    main()
