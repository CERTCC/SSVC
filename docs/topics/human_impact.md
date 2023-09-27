# Human Impact

!!! note "Human Impact"

    Combined Situated Safety and Mission Impact

    | Situated Safety Impact | Mission Impact | Combined Value (Human Impact) |
    | -----:                 | :-----         | :---:          |
    |  None/Minor         | Degraded/Crippled | Low       |
    |  None/Minor         | MEF Failure       | Medium         |
    |  None/Minor         | Mission Failure   | Very High      |
    |  Major              | Degraded/Crippled | Medium    |
    |  Major              | MEF Failure       | High           |
    |  Major              | Mission Failure   | Very High      |
    |  Hazardous          | Degraded/Crippled | High      |
    |  Hazardous          | MEF Failure       | High           |
    |  Hazardous          | Mission Failure   | Very High      |
    |  Catastrophic       | Degraded/Crippled | Very High |
    |  Catastrophic       | MEF Failure       | Very High      |
    |  Catastrophic       | Mission Failure   | Very High      |

{== TODO note that this is a compound decision point, therefore it is a notational convenience ==}

In pilot implementations of SSVC, we received feedback that organizations tend to think of mission and safety impacts as
if they were combined into a single factor: in other words, the priority increases regardless which of the two  impact factors was increased.
We therefore combine [Safety Impact](../reference/decision_points/safety_impact.md) and
[Mission Impact](../reference/decision_points/mission_impact.md) for deployers into a single _Human Impact_ factor
as a dimension reduction step as follows.
We observe that the day-to-day operations of an organization often have already built in a degree of tolerance to small-scale variance in mission impacts.
Thus in our opinion we need only concern ourselves with discriminating well at the upper end of the scale.
Therefore we combine the two lesser mission impacts of degraded and MEF support crippled into a single category, while retaining the distinction between MEF Failure and Mission Failure at the extreme.
This gives us three levels of mission impact to work with.

On the other hand, most organizations tend to have lower tolerance for variance in safety.
Even small deviations in safety are unlikely to go unnoticed or unaddressed.
We suspect that the presence of regulatory oversight for safety issues and its absence at the lower end of the mission impact scale influences this behavior.
Because of this higher sensitivity to safety concerns, we chose to retain a four-level resolution for the safety dimension.
We then combine Mission Impact with Situated Safety impact and map them onto a 4-tiered scale (Low, Medium, High, Very High).
The mapping is shown in the following table.

## Safety and Mission Impact Decision Points for Industry Sectors

We expect to encounter diversity in both safety and mission impacts across different organizations.
However, we also anticipate a degree of commonality of impacts to arise across organizations within a given industry sector.
For example, different industry sectors may have different use cases for the same software.
Therefore, vulnerability information providers&mdash;that is, vulnerability databases,
Information Sharing and Analysis Organizations (ISAOs), or Information Sharing and Analysis Centers (ISACs)&mdash;may
provide SSVC information tailored as appropriate to their constituency's safety and mission concerns.
For considerations on how organizations might communicate SSVC information to their constituents,
see [Guidance on Communicating Results](../howto/communicating_results.md).


