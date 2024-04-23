# Vulnerability Coordination Decisions

Coordinators are facilitators within the vulnerability management ecosystem.
Since coordinators neither supply nor deploy the vulnerable component in question, their decisions are different from
[suppliers'](supplier_tree.md) or [deployers'](deployer_tree.md) decisions.
This section provides a window into CERT/CC's decisions as an example of how a coordinator might use SSVC to make its own decisions.


Coordinators vary quite a lot, and their use of SSVC may likewise vary.
A coordinator may want to gather and publish information about SSVC decision points that it does not use internally in order to assist its constituents.
Furthermore, a coordinator may only publish some of the information it uses to make decisions.
Consistent with other stakeholder perspectives (supplier and deployer), SSVC provides the priority with which a coordinator should take some defined action, but not how to do that action.
For more information about types of coordinators and their facilitation actions within vulnerability management, see
[The CERT Guide to Coordinated Vulnerability Disclosure](https://certcc.github.io/CERT-Guide-to-CVD/topics/roles/coordinator/)

The two decisions that CERT/CC makes as a coordinator that we will discuss in terms of SSVC are 

1. [Coordination Triage](coordination_triage_decision.md) - The initial triage of vulnerability reports. This initial coordination decision is a prioritization decision, but it 
   does not have the same values as prioritization by a [deployer](deployer_tree.md) or [supplier](supplier_tree.md).
2. [Publication](publication_decision.md) - Whether a publication about a vulnerability is warranted. The publication decision for us is a binary yes/no.

These two decisions are not the entirety of vulnerability coordination, but we leave further details of the process for future work.

!!! tip inline end "CISA and SSVC"

    For another example of how a coordinator is using SSVC, see the [CISA SSVC](https://www.cisa.gov/ssvc) website.


Different coordinators have different scopes and constituencies.
See [The CERT Guide to Coordinated Vulnerability Disclosure](https://certcc.github.io/CERT-Guide-to-CVD/topics/roles/coordinator/) for a listing of different coordinator types.
If a coordinator receives a report that is outside its own work scope or constituency, it should make an effort to route the report to a more suitable coordinator.
The decisions in this section assume the report or vulnerability in question is within the work scope or constituency for the coordinator.

