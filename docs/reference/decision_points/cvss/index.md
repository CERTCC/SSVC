# CVSS Decision Points

!!! tip inline end "For more information"

    For more information on the CVSS specification, please refer to the
    [CVSS Specifications](https://www.first.org/cvss/).

For convenience, we have provide a list of decision points that are based
on the CVSS specification. These decision points can be used to model various
decisions based on CVSS vector elements.

## Decision Points

The following list of CVSS vector elements have been modeled as SSVC decision
points for use in vulnerability response and security decision modeling.
We have organized them into groups according to where they belong in the
[CVSS v4.0 specification document](https://www.first.org/cvss/v4.0/specification-document).

!!! info "About CVSS Decision Point Versions"

    We have modeled our CVSS-based decision points using the SSVC versioning scheme.
    Therefore, some decision points may have multiple versions as the concepts have
    been refined over different versions of the CVSS specification. These versions
    do _not_ correspond the CVSS specification versions (2.0, 3.0, 3.1, 4.0 etc.).

### Base Metrics

<div class="grid cards" markdown>
- [Attack Vector](attack_vector.md)
- [Attack Complexity](attack_complexity.md)
- [Attack Requirements](attack_requirements.md)
- [Privileges Required](privileges_required.md)
- [User Interaction](user_interaction.md)
- [Confidentiality Impact](confidentiality_impact.md)
- [Subsequent Confidentiality Impact](subsequent_confidentiality_impact.md)
- [Integrity Impact](integrity_impact.md)
- [Subsequent Integrity Impact](subsequent_integrity_impact.md)
- [Availability Impact](availability_impact.md)
- [Subsequent Availability Impact](subsequent_availability_impact.md)
</div>

### Threat Metrics

<div class="grid cards" markdown>
- [Exploit Maturity](exploit_maturity.md)
</div>

### Environmental Metrics

<div class="grid cards" markdown>
- [Confidentiality Requirement](confidentiality_requirement.md)
- [Integrity Requirement](integrity_requirement.md)
- [Availability Requirement](availability_requirement.md)
</div>

### Supplemental Metrics

<div class="grid cards" markdown>
- [Safety](safety.md)
- [Automatable](automatable.md)
- [Provider Urgency](provider_urgency.md)
- [Recovery](recovery.md)
- [Value Density](value_density.md)
- [Vulnerability Response Effort](vulnerability_response_effort.md)
</div>

### Older Metrics

<div class="grid cards" markdown>
- [Authentication](authentication.md)
- [Collateral Damage Potential](collateral_damage_potential.md)
- [Impact Bias](impact_bias.md)
- [Remediation Level](remediation_level.md)
- [Report Confidence](report_confidence.md)
- [Scope](scope.md)
- [Target Distribution](target_distribution.md)
</div>
