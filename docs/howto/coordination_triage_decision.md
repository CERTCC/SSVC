# Prioritizing Vulnerability Coordination

In coordinated vulnerability disclosure (CVD), there are two available decisions modelled in SSVC.
The first is whether or not to coordinate a vulnerability report.
This decision is also known as triage.

!!! info "Coordination Triage Priority"

    As noted in [Enumerating Decisions](../topics/enumerating_decisions.md), the root of a decision model's identity is
    the combination of the stakeholder and the decision being modeled.
    In this case, the stakeholder is the **Coordinator** and the decision is 
    the **priority of coordinating a vulnerability report**.


## Coordinator Triage Units of Work 

!!! info inline end "Coordinator Unit of Work"

    The unit of work for a Coordinator is usually a single report to be coordinated.

Coordinator units of work tend to coincide with whatever arrives in a single report, which spans the range from a single
vulnerability affecting a specific version of an individual product from one Supplier all the way to fundamental design 
flaws in system specifications that could affect every Supplier and product that uses or implements the flawed specification.
Coordinators may need to reorganize reports (e.g., merge, split, expand, or contract) according to their workflow demands.
SSVC can be applied to either the initial report or to the results of such refinement.


## Coordinator Triage Decision Outcomes

We take three priority levels in our decision about whether and how to [coordinate](https://vuls.cert.org/confluence/display/CVD/1.1.+Coordinated+Vulnerability+Disclosure+is+a+Process%2C+Not+an+Event)
a vulnerability based on an incoming report:

!!! info "Coordinator Triage Priority"

    | Triage Priority | Description |
    | :---            | :----------  |
    | Decline         | Do not act on the report. |
    | Track           | Receive information about the vulnerability and monitor for status changes but do not take any overt actions. |
    | Coordinate      | Take action on the report. “Action” may include any one or more of: technical analysis, reproduction, notifying vendors, publication, and assist another party. |


 - *Decline* — Do not act on the report. May take different forms, including ignoring the report as well as an 
   acknowledgement to the reporter that we will not act and suggest the reporter to go to vendor or publish if unresponsive.
 - *Track* — Receive information about the vulnerability and monitor for status changes but do not take any overt actions.
 - *Coordinate* — Take action on the report. “Action” may include any one or more of: technical analysis, reproduction,
   notifying vendors, lead coordination (notify, communicate, and publish), publish only (amplify public message), 
   advise only, secondary coordinator (assist another lead coordinator).
   See the [FIRST CSIRT Services Framework](https://www.first.org/standards/frameworks/csirts/csirt_services_framework_v2.1#7-Service-Area-Vulnerability-Management)
   for additional vulnerability management services a coordinator may provide.


## Coordinator Triage Decision Points

!!! tip inline end "Prior CERT/CC Work on Prioritizing Coordination Decisions"

    [Vulnerability Response Decision Assistance](https://insights.sei.cmu.edu/library/vulnerability-response-decision-assistance-vrda/)
    (VRDA) provides a starting point for a decision model for this situation.
    VRDA is likely [adequate](https://insights.sei.cmu.edu/library/effectiveness-of-the-vulnerability-response-decision-assistance-vrda-framework/)
    for national-level CSIRTs that do general CVD, but other CSIRT types may have different needs.
    The [*CERT Guide to Coordinated Vulnerability Disclosure*](https://vuls.cert.org/confluence/display/CVD/6.10+Troubleshooting+Coordinated+Vulnerability+Disclosure+Table)
    provides something similar for those who are deciding how to report and disclose vulnerabilities they have discovered.

The coordination and publication decisions for CERT/CC are about the social and collaborative state of vulnerability management.
Our goal with the coordination decision is to base it on information that is available to the analyst when CERT/CC receives a vulnerability report.
In addition to using some of the decision points common to [Suppliers](supplier_tree.md) and [Deployers](deployer_tree.md)
([Utility](../reference/decision_points/utility.md) and [Public Safety Impact](../reference/decision_points/public_safety_impact.md)), we have added five new decision points for the coordination decision model.

The first two function as gating questions:

- [Report Public](../reference/decision_points/report_public.md): If a report is already public, then CERT/CC will decline the case unless there are multiple suppliers, [*super effective*](../reference/decision_points/system_exposure.md) [Utility](../reference/decision_points/utility.md), and [*significant*](../reference/decision_points/public_safety_impact.md) [Public Safety Impact](../reference/decision_points/public_safety_impact.md).
- [Supplier Contacted](../reference/decision_points/supplier_contacted.md): If no suppliers have been contacted, then CERT/CC will decline the case unless there are multiple suppliers, [*super effective*](../reference/decision_points/system_exposure.md) [Utility](../reference/decision_points/utility.md), and [*significant*](../reference/decision_points/public_safety_impact.md) [Public Safety Impact](../reference/decision_points/public_safety_impact.md). 
  In this case, CERT/CC may encourage the reporter to contact the supplier and submit a new case request if the supplier is unresponsive.

These two sets of exceptional circumstances mean that the seven decision points involved in the coordination triage 
tree can be compressed slightly, as the decision model below shows.

The remaining five decision points are:

- [Report Credibility](../reference/decision_points/report_credibility.md): If the report is not credible, then CERT/CC will decline the case.
- [Supplier Cardinality](../reference/decision_points/supplier_cardinality.md): Cases involving multiple suppliers can get complicated very quickly, so we are more likely to get involved in those cases. 
- [Supplier Engagement](../reference/decision_points/supplier_engagement.md): If the suppliers are already engaged in a case, there is usually less for a coordinator to do, making it less likely that we will coordinate a case.
- [Utility](../reference/decision_points/utility.md): If the vulnerability has high utility, then CERT/CC is more likely to coordinate the case.
- [Public Safety Impact](../reference/decision_points/public_safety_impact.md): If the vulnerability has significant 
   public safety impact, then CERT/CC is more likely to coordinate the case.

More detail about each of these decision points is provided at the links above, here we provide a brief summary of each.

{% include-markdown "../_generated/decision_points/report_public.md" %}
{% include-markdown "../_generated/decision_points/supplier_contacted.md" %}
{% include-markdown "../_generated/decision_points/report_credibility.md" %}
{% include-markdown "../_generated/decision_points/supplier_cardinality.md" %}
{% include-markdown "../_generated/decision_points/supplier_engagement.md" %}
{% include-markdown "../_generated/decision_points/utility.md" %}
{% include-markdown "../_generated/decision_points/public_safety_impact.md" %}

## Coordinator Triage Decision Model

The following example decision model is a policy that closely follows our own decision model at the CERT/CC.
Other coordinators should consider customizing the tree to their needs, as described in [Tree Construction and Customization Guidance](tree_customization.md).

!!! tip "SSVC Customization in Action: CISA"

    CISA has customized an SSVC decision model to suit their coordination needs.
    It is available at [https://www.cisa.gov/ssvc](https://www.cisa.gov/ssvc).

<embed src="../../pdf/ssvc_2_coord-triage.pdf" alt="Coordination Triage Tree" type="application/pdf"
style="width: 100%;"
height = "700" />

### Table of Values

<!-- relative to /data/csvs/ -->
{{ read_csv('coord-triage-options.csv') }}
