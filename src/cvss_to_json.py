#!/usr/bin/python3"
mods = ["attack_complexity", "attack_requirements", "attack_vector",
        "authentication", "availability_impact", "availability_requirement",
        "collateral_damage_potential", "confidentiality_impact",
        "confidentiality_requirement", "exploitability", "helpers",
        "impact_bias", "integrity_impact", "integrity_requirement",
        "privileges_required", "remediation_level", "report_confidence",
        "scope", "subsequent_availability_impact",
        "subsequent_confidentiality_impact", "subsequent_integrity_impact",
        "target_distribution", "user_interaction"]
for mod in mods:
    module = getattr(__import__('ssvc.decision_points.cvss', fromlist=[mod]),
                     mod)
    for dp in dir(module):
        if dp.upper().find(mod.upper()) > -1:
        #user_interaction USER_INTERACTION_2
            print(mod, dp)
            sdp = getattr(module, dp)
            with open(f"../data/json/decision_points/cvss/{dp.lower()}.json", "w") as f:
                f.write(sdp.to_json())

    
