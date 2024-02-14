# Using SSVC

!!! tip inline end "Prerequisites"

    The [Using SSVC](index.md) section assumes that you have
    
    - An interest in using SSVC in a vulnerability management process
    - Basic familiarity with SSVC

    If you are unfamiliar with SSVC, we suggest you start with the
    [Understanding SSVC](../topics/index.md) section, which provides necessary background detail.
    For technical reference, see [Reference](../reference/index.md).

!!! note "TODO: What should go here?"

    Advice for practitioners looking to integrate SSVC into their vulnerability management process.
    
    - example trees showing how decision points are used to model decisions
    - how to model new decisions
    - how to create more decision points
    - how to modify or adapt existing decision points
    - how to analyze trees for quality/parsimony
    - how to integrate SSVC into existing processes
    - how to integrate data sources into SSVC decision points

## Prioritization

Given a specific stakeholder decision and set of useful decision points, we are now in a position to combine them into a comprehensive set of decisions about the priority with which to act.
The definition of choices can take a logical form, such as:

 - IF
   - ([*Exploitation*](../reference/decision_points/exploitation.md) IS [PoC](../reference/decision_points/exploitation.md)) AND
   - ([Exposure](../reference/decision_points/system_exposure.md) IS [controlled](../reference/decision_points/exploitation.md)) AND
   - ([*Automatable*](../reference/decision_points/automatable.md) IS [no](../reference/decision_points/automatable.md)) AND
   - ([*Human Impact*](../reference/decision_points/human_impact.md) IS [medium](../reference/decision_points/human_impact.md))
 - THEN priority is *scheduled*.

This example logical statement is captured in (line 35 of the deployer `.csv` file)[https://github.com/CERTCC/SSVC/blob/main/data/csvs/deployer-options.csv#L35].

There are different formats for capturing these prioritization decisions depending on how and where they are going to be used.
In this paper, we primarily represent a full set of guidance on how one stakeholder will make a decision as a **decision tree**.
This section presents example trees for each stakeholder: supplier, deployer, and coordinator.
This section also provides some guidance on how to [construct and customize a decision tree](tree_customization.md) and [gather evidence](bootstrap/collect.md) to make decisions.
How this decision information might be stored or communicated is the topic of subsections on [Asset Management](../topics/asset_management.md) and [Communication](bootstrap/use.md).

