# Using SSVC

!!! tip inline end "Prerequisites"

    The [Using SSVC](index.md) section assumes that you have
    
    - An interest in using SSVC in a vulnerability management process
    - Basic familiarity with SSVC

    If you are unfamiliar with SSVC, we suggest you start with the [Learning SSVC](../tutorials/index.md) section.
    [Understanding SSVC](../topics/index.md) provides necessary background detail.
    For technical reference, see [Reference](../reference/index.md).

<!--
What should go here?

    Advice for practitioners looking to integrate SSVC into their vulnerability management process.
    
    - example trees showing how decision points are used to model decisions
    - how to model new decisions
    - how to create more decision points
    - how to modify or adapt existing decision points
    - how to analyze trees for quality/parsimony
    - how to integrate SSVC into existing processes
    - how to integrate data sources into SSVC decision points
-->

SSVC is a methodology for prioritizing vulnerability response based on the needs of various stakeholders.
At its core are the concepts of:

- [**Stakeholder Roles**](../topics/enumerating_stakeholders.md): Different participants in the vulnerability response process have different needs and priorities.
  Roles can include patch suppliers, deployers, coordinators, and others.
- [**Decisions**](../topics/enumerating_decisions.md): Each stakeholder role has a set of decisions to make about how to respond to vulnerabilities.
  For a supplier, the decision might be about how to prioritize the creation of patches. For a deployer, the 
  decision might be about how to prioritize the deployment of patches. Coordinators usually need to decide whether
  to coordinate a response, and whether to publish information about a vulnerability they've coordinated.
- [**Decision Points**](../reference/decision_points/index.md): Each decision is made based on a set of inputs, or decision points. These are the factors
  that influence the decision. For example, a decision about whether to deploy a patch might be influenced by the
  severity of the vulnerability, the availability of an exploit, and the impact of the vulnerability on the system.
- [**Outcomes**](../topics/enumerating_decisions.md): Each decision has a set of possible outcomes. These are the possible results of the decision.
  For example, a decision about whether to deploy a patch might have outcomes like "immediate", "scheduled", "deferred",
  and "out-of-cycle".

Given these concepts, we can combine them into decision models to help stakeholders make decisions about the priority 
with which to act.
The definition of choices can take a logical form, such as:

 - IF
    
     - ([*Exploitation*](../reference/decision_points/exploitation.md) IS *Public PoC*) AND
     - ([*System Exposure*](../reference/decision_points/system_exposure.md) IS *controlled*) AND
     - ([*Automatable*](../reference/decision_points/automatable.md) IS *no*) AND
     - ([*Human Impact*](../reference/decision_points/human_impact.md) IS *medium*)

 - THEN priority is *scheduled*.

This example logical statement is captured in [line 35 of the deployer `.csv` file](https://github.com/CERTCC/SSVC/blob/main/data/csvs/deployer-options.csv#L35).

There are different formats for capturing these prioritization decisions depending on how and where they are going to be used.
In this documentation, we primarily represent a full set of guidance on how one stakeholder will make a decision as a **decision tree**.

This section presents example decision models for various stakeholders, followed by guidance on how to adapt and customize SSVC to
fit your organization's needs.

<div class="grid cards" markdown>

- :material-stairs: [Bootstrapping SSVC](bootstrap/index.md)
- :material-factory: [Supplier Decision Model](supplier_tree.md)
- :material-server-network: [Deployer Decision Model](deployer_tree.md)
- :material-steering: [Coordinator Decision Models](coordination_intro.md)
- :material-hand-saw: [Customizing SSVC](tree_customization.md)
- :material-slope-uphill: [Acuity Ramp](acuity_ramp.md)

</div>
