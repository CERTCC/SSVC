#!/usr/bin/python3"
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

mods = [
    "attack_complexity",
    "attack_requirements",
    "attack_vector",
    "authentication",
    "availability_impact",
    "availability_requirement",
    "collateral_damage_potential",
    "confidentiality_impact",
    "confidentiality_requirement",
    "exploitability",
    "helpers",
    "impact_bias",
    "integrity_impact",
    "integrity_requirement",
    "privileges_required",
    "remediation_level",
    "report_confidence",
    "scope",
    "subsequent_availability_impact",
    "subsequent_confidentiality_impact",
    "subsequent_integrity_impact",
    "target_distribution",
    "user_interaction",
]


def main():
    for mod in mods:
        module = getattr(__import__("ssvc.decision_points.cvss", fromlist=[mod]), mod)
        for dp in dir(module):
            if dp.upper().find(mod.upper()) > -1:
                # user_interaction USER_INTERACTION_2
                print(mod, dp)
                sdp = getattr(module, dp)
                with open(
                    f"../data/json/decision_points/cvss/{dp.lower()}.json", "w"
                ) as f:
                    f.write(sdp.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
