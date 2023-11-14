# Mission Impact

{% include-markdown "../../_generated/decision_points/mission_impact.md" %}

!!! tip "See also"

    Mission Impact combines with [Safety Impact](./safety_impact.md) to inform 
    [Human Impact](./human_impact.md)

A **mission essential function (MEF)** is a function “directly related to accomplishing the organization’s mission as set forth in its statutory or executive charter” [@FCD2_2017, page A-1]. 
Identification and prioritization of mission essential functions enables effective continuity planning or crisis planning. 
Mission Essential Functions are in effect critical activities within an organization that are used to identify key assets, supporting tasks, and resources that an organization requires to remain operational in a crises situation, and so must be included in its planning process.
During an event, key resources may be limited and personnel may be unavailable, so organizations must consider these factors and validate assumptions when identifying, validating, and prioritizing MEFs.

When reviewing the list of organizational functions, an organization must first identify whether a function is essential or non-essential. 
The distinction between these two categories is whether or not an organization must perform a function during a disruption to normal operations and must continue performance during emergencies [@FCD2_2017, page B-2]. 
Essential functions are both important and urgent.
Functions that can be deferred until after an emergency are identified as non-essential.
For example, DoD defines MEFs in [DoD Directive 3020.26 DoD Continuity Policy](https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodd/302026p.pdf) using similar terminology to [FCD-2](https://www.fema.gov/sites/default/files/2020-07/Federal_Continuity_Directive-2_June132017.pdf) [@dod3026_26_2018].

As mission essential functions are most clearly defined for government agencies, stakeholders in other sectors may be familiar with different terms of art from continuity planning. 
For example, infrastructure providers in the US may better align with [National Critical Functions](https://www.cisa.gov/national-critical-functions). 
Private sector businesses may better align with [operational and financial impacts](https://www.ready.gov/sites/default/files/2020-03/business-impact-analysis-worksheet.pdf) in a [business continuity plan](https://www.ready.gov/business-continuity-plan). 

While the processes, terminology, and audience for these different frameworks differ, they all can provide a sense of the criticality of an asset or assets within the scope of the stakeholder conducting the cyber vulnerability prioritization with SSVC.
In that sense they all function quite similarly within SSVC. Organizations should use whatever is most appropriate for their stakeholder context, with Mission Essential Function analysis serving as a fully worked example in the SSVC documents. 


## Gathering Information About Mission Impact

The factors that influence the mission impact level are diverse. 
This paper does not exhaustively discuss how a stakeholder should answer a question; that is a topic for future work. 
At a minimum, understanding mission impact should include gathering information about the critical paths that involve vulnerable components, viability of contingency measures, and resiliency of the systems that support the mission. 
There are various sources of guidance on how to gather this information; see for example the FEMA guidance in Continuity Directive 2 [@FCD2_2017] or OCTAVE FORTE [@tucker2018octave]. 
This is part of risk management more broadly.
It should require the vulnerability management team to interact with more senior management to understand mission priorities and other aspects of risk mitigation.

As a heuristic, [*Utility*](#utility) might constrain [*Mission Impact*](#mission-impact) if both are not used in the same decision tree.
For example, if the [*Utility*](#utility) is [*super effective*](#utility), then [*Mission Impact*](#mission-impact) is at least [*MEF support crippled*](#mission-impact).

## Prior Versions

{% include-markdown "../../_generated/decision_points/mission_impact_1_0_0.md" %}
