# Human Impact

{% include-markdown "../../_generated/decision_points/human_impact.md" %}

!!! tip "See also"

    *Human Impact* is a combination of [Safety Impact](./safety_impact.md) and
    [Mission Impact](./mission_impact.md)

Note: This is a compound decision point[^1], therefore it is a notational convenience.

*Human Impact* is a combination of how a vulnerability can affect an organization's mission essential functions as well as
safety considerations, whether for the organization's personnel or the public at large. 
We observe that the day-to-day operations of an organization often have already built in a degree of tolerance to small-scale variance in mission impacts.
Thus in our opinion we need only concern ourselves with discriminating well at the upper end of the scale.
Therefore we combine the two lesser mission impacts of degraded and MEF support crippled into a single category, while retaining the distinction between MEF Failure and Mission Failure at the extreme.
This gives us three levels of mission impact to work with.
On the other hand, most organizations tend to have lower tolerance for variance in safety.
Even small deviations in safety are unlikely to go unnoticed or unaddressed.
We suspect that the presence of regulatory oversight for safety issues and its absence at the lower end of the mission impact scale influences this behavior.
Because of this higher sensitivity to safety concerns, we chose to retain a four-level resolution for the safety dimension.
We then combine Mission Impact with Situated Safety impact and map them onto a 4-tiered scale (Low, Medium, High, Very High).
The mapping is shown in the table above.

[^1]: In pilot implementations of SSVC, we received feedback that organizations tend to think of mission and safety impacts as
if they were combined into a single factor: in other words, the priority increases regardless which of the two  impact factors was increased.
We therefore combine [Safety Impact](safety_impact.md) and
[Mission Impact](mission_impact.md) for deployers into a single _Human Impact_ factor
as a dimension reduction step.


## Safety and Mission Impact Decision Points for Industry Sectors

We expect to encounter diversity in both safety and mission impacts across different organizations.
However, we also anticipate a degree of commonality of impacts to arise across organizations within a given industry sector.
For example, different industry sectors may have different use cases for the same software.
Therefore, vulnerability information providers&mdash;that is, vulnerability databases,
Information Sharing and Analysis Organizations (ISAOs), or Information Sharing and Analysis Centers (ISACs)&mdash;may
provide SSVC information tailored as appropriate to their constituency's safety and mission concerns.
For considerations on how organizations might communicate SSVC information to their constituents,
see [Guidance on Communicating Results](../../howto/bootstrap/use.md).


## Prior Versions

{% include-markdown "../../_generated/decision_points/human_impact_2_0_0.md" %}

{% include-markdown "../../_generated/decision_points/mission_and_well-being_impact_1_0_0.md" %}
