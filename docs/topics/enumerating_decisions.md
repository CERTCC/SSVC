# Enumerating Decisions

Stakeholders with different responsibilities in vulnerability management have very different decisions to make.
This section focuses on the differences among organizations based on their vulnerability management responsibilities.
Some decision makers may have different responsibilities in relation to different software.

!!! example "Example: Different Responsibilities for Different Software"

    For example, an Android app developer is a developer of the app, but is a deployer for any changes to the Android OS API.
    This situation is true for libraries in general:
    
    - A web browser developer makes decisions about applying patches to DNS lookup libraries and transport layer security (TLS) libraries.
    - A video game developer makes decisions about applying patches released to the Unreal Engine.
    - A medical device developer makes decisions about applying patches to the Linux kernel.
   


One might view applying patches as including some development and distribution of the updated product.
Or one might take the converse view, that development includes updating libraries.
Either way, in each of these examples (mobile device apps, web browsers, video games, medical devices),
we recommend that the professionals making genuine decisions do three things:

!!! example inline end "Bootstrapping SSVC"

    We provide a more detailed process for SSVC adoption in [Bootstrapping SSVC](../howto/bootstrap/index.md).

1. identify the decisions explicitly
2. describe how they view their role(s)
3. identify which software projects their decision relates to

SSVC models the decision of
“With what priority should the organization take action on a given vulnerability management work unit?”
to be agnostic to whether or not a patch is available.
If their decisions are explicit, then the decision makers can use the recommendations from this documentation that are relevant to them.


!!! tip "The Stakeholder Role / Decision Identity"

    As we have continued to develop SSVC and received feedback from SSVC implementers, we've found that similar
    stakeholders making similar decisions can often use the same set of decision points to model their decisions.
    Organizations might use the same structure of decision points but have different priority levels they need to map to
    their decisions. For example, one organization might need to map their decisions to three priority levels, while another
    might need to map their decisions to five priority levels.

    Variation can also arise from different organization goals or risk tolerance that alters the policy mapping the
    decision points to priority outcomes. The decision points themselves are often the same for the 
    stakeholder-decision pairing, but the policy that maps the decision points to priority outcomes is different.

    The salient information required to make a specific kind of decision in a specific context is often the same across
    organizations.
    For this reason, we have found it useful to think of the identity of a decision model as the combination of the
    _stakeholder role_ and the _decision_ being modeled. We've provided a few examples of different stakeholders' decision models
    in the [_SSVC How-To_](../howto/index.md) section:

    - [Supplier deciding whether to create a patch](../howto/supplier_tree.md)
    - [Deployer deciding whether to deploy a patch](../howto/deployer_tree.md)
    - [Coordinator deciding whether to coordinate a case](../howto/coordination_triage_decision.md)
    - [Coordinator deciding whether to publish about a case](../howto/publication_decision.md)

    
## Enumerating Vulnerability Management Units of Work

!!! example inline end "Stakeholder Units of Work"

    We provide a few examples of different stakeholders' units of work in the [_SSVC How-To_](../howto/index.md) section.
    See the _Units of Work_ section of each stakeholder's decision model for more information.
    
    - [Supplier](../howto/supplier_tree.md)
    - [Deployer](../howto/deployer_tree.md)
    - [Coordinator Triage](../howto/coordination_triage_decision.md)
    - [Coordinator Publication](../howto/publication_decision.md)

A unit of work means either remediating the vulnerability—such as applying a patch—or deploying a mitigation.
Both remediation and mitigations often address multiple identified vulnerabilities.
The unit of work may be different for different stakeholders: a supplier might be selecting individual vulnerabilities to fix,
while a deployer is choosing whether or not to deploy a patch bundle that fixes multiple vulnerabilities.

The units of work can also change as the vulnerability response progresses through a stakeholder's process.
Coordinators might make triage decisions on individual reports, but then make publication decisions on a set of related cases at once.

### Aggregation of SSVC Across Units of Work

SSVC users should answer the suggested questions for whatever discrete unit of work they are considering. 
There is not necessarily a reliable function to aggregate a recommendation about remediation out of its constituent 
vulnerabilities. 
For the sake of simplicity of examples, we treat the remediation as a patch of one vulnerability, and comment on any
difficulty in generalizing our advice to a more complex patch where appropriate.

!!! info "Remediation and Mitigation"

    To further clarify terms, we use the definitions from 
    [DoD Instruction 8530.01](https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/853001p.pdf) 
    _Cybersecurity Activities Support to DoD Information Network Operations_ (DODI 8530.01).
    
    - **Remediation** occurs when the vulnerability is eliminated or removed.
    - **Mitigation** occurs when the impact of the vulnerability is decreased without reducing or eliminating the vulnerability

    Examples of remediation include applying patches, fixes and upgrades; or removing the vulnerable software or system from operation.
    Mitigating actions may include software configuration changes, adding firewall ACLs, or otherwise limiting the system's
    exposure to reduce the risk of the impact of the vulnerability; or accepting the risk.



## Enumerating Action Priority

!!! example inline end "Decision Outcomes and Action Priority"

    We provide examples of different stakeholders' action priorities in the [_SSVC How-To_](../howto/index.md) section.
    See the _Decision Outcomes_ section of each stakeholder's decision model for more information.
    
    - [Supplier](../howto/supplier_tree.md)
    - [Deployer](../howto/deployer_tree.md)
    - [Coordinator Triage](../howto/coordination_triage_decision.md)
    - [Coordinator Publication](../howto/publication_decision.md)

Structuring decisions about vulnerability management action priority is a core concept of SSVC.
However, we also recognize that each stakeholder has different responsibilities and therefore different decisions to make.
Furthermore, even when stakeholders are making similar decisions, they may have different goals and constraints, which
lead to different priorities.

For example, some suppliers might need to map their vulnerability response decisions onto a specific set of service
level expectations (SLEs) set by their contractual obligations to their customers. Similarly, deployers might need to integrate
their decisions into a broader risk management framework or 
[IT Service Management](https://en.wikipedia.org/wiki/IT_service_management) (ITSM) process.


!!! example "SSVC, Vulnerability Response, and Risk Management Processes"

    A few examples from the US Government of organizational process requirements that can affect the decision 
    modeling process in SSVC adoption include:

    - [CISA Binding Operational Directive (BOD) 22-01](https://www.cisa.gov/news-events/directives/bod-22-01-reducing-significant-risk-known-exploited-vulnerabilities),
      _Reducing the Significant Risk of Known Exploited Vulnerabilities_, sets service level expectations for federal agencies to remediate vulnerabilities based on the exploitation status of the vulnerability.
    - [DoDI 8510.01](https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/851001p.pdf), _Risk Management Framework for DoD Systems_,
      includes multiple steps involving prioritization of impact levels (Task P-6), stakeholder assets (Task P-10), and
      security requirements (Task P-15).

    SSVC implementers in organizations subject to requirements like these may need to adapt their decision models to
    ensure that they are consistent with the requirements of the organization's broader risk management and ITSM processes.



