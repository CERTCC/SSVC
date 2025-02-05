#!/usr/bin/python3

#  Copyright (c) 2025 Carnegie Mellon University and Contributors.
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

from ssvc.outcomes import groups
from ssvc.outcomes.base import OutcomeGroup


def main():
    for x in dir(groups):
        outcome = getattr(groups, x)
        if type(outcome) == OutcomeGroup:
            with open(f"../data/json/outcomes/{x}.json", "w") as f:
                f.write(outcome.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
