# Using SSVC

!!! tip inline end "Prerequisites"

    The [Using SSVC](index.md) section assumes that you have
    
    - An interest in using SSVC in a vulnerability management process
    - Basic familiarity with SSVC

    If you are unfamiliar with SSVC, we suggest you start with the
    [Understanding SSVC](../topics/index.md) section, which provides necessary background detail.
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

Given a specific [stakeholder](../topics/enumerating_stakeholders.md) [decision](../topics/enumerating_decisions.md) 
and set of useful [decision points](../reference/decision_points/index.md), 
we are now in a position to combine them into a
comprehensive set of decisions about the priority with which to act.
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

This section presents example trees for various stakeholders, followed by guidance on how to adapt and customize SSVC to
fit your organization's needs.

<div class="grid cards" markdown>

- :material-factory: [Supplier Decision Model](supplier_tree.md)
- :material-server-network: [Deployer Decision Model](deployer_tree.md)
- :material-steering: [Coordinator Decision Models](coordination_intro.md)
- :material-stairs: [Bootstrapping SSVC](bootstrap/index.md)
- :material-hand-saw: [Customizing SSVC](tree_customization.md)
- :material-slope-uphill: [Acuity Ramp](acuity_ramp.md)

</div>
