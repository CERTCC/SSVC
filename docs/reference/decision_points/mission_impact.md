# Mission Impact

```python exec="true" idprefix=""
from ssvc.decision_points.ssvc.mission_impact import LATEST
from ssvc.doc_helpers import example_block

print(example_block(LATEST))
```

!!! tip "Gathering Information about Mission Impact"

      See this [HowTo](../../howto/gathering_info/mission_impact.md) for advice on gathering information about the Mission Impact decision point.

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

## Prior Versions

```python exec="true" idprefix=""
from ssvc.decision_points.ssvc.mission_impact import VERSIONS
from ssvc.doc_helpers import example_block

versions = VERSIONS[:-1]
for version in versions:
    print(example_block(version))
    print("\n---\n")
```
