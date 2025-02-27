# Risk Tolerance and Response Priority

SSVC enables stakeholders to balance and manage their risks themselves.
We follow the risk management vocabulary from [ISO 31073:2022(en)
Risk management — Vocabulary](https://www.iso.org/obp/ui/#iso:std:iso:31073:ed-1:v1:en) and define risk as “effect of uncertainty on objectives;”
see the original document for notes on the terms in the definition.
A successful vulnerability management practice must balance at least two risks:

!!! tip inline end "Contextualizing Risk"

    To place these risks in context, we follow the SEI's
    [Taxonomy of Operational Cyber Security Risks](https://insights.sei.cmu.edu/library/a-taxonomy-of-operational-cyber-security-risks/).
    **Change risk** can be characterized as a combination of Class 2 and/or Class 3 risks.
    
    - Class 2: Systems and Technology Failures includes hardware, software, and systems risks.
    - Class 3: Failed Internal Processes can arise from process design, process execution, process controls, or supporting processes.

    Meanwhile, **vulnerability risk** falls into Subclass 1.2: Actions of People: Deliberate.

1. **Change risk**: the potential costs of deploying remediation, which include testing and deployment in addition to any
   problems that could arise from making changes to production systems.
2. **Vulnerability risk**: the potential costs of incidents resulting from exploitation of vulnerable systems

In developing the decision trees in this document, we had in mind stakeholders with a moderate tolerance for risk. The resulting trees reflect that assumption. Organizations may of course be more or less conservative in their own vulnerability management practices, and we cannot presume to determine how an organization should balance their risk.

We therefore remind our readers that the labels on the trees (defer, immediate, etc.) can and should be customized to
suit the needs of individual stakeholders wherever necessary and appropriate.

<!-- hr for vertical space -->
---

!!! example "Risk Tolerance Influences Response Priority"

    - An organization with a high aversion to change risk might choose to accept more vulnerability risk by
    lowering the overall response labels for many branches in the trees, resulting in fewer vulnerabilities attaining
    the most urgent response.
    - On the other hand, an organization with a high aversion to vulnerability risk could elevate the priority of many 
    branches to ensure fixes are deployed quickly.
