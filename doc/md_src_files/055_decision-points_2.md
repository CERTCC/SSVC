## Safety Impact
> Safety Impacts of Affected System Compromise

We take an expansive view of safety, in which a safety violation is a violation of what the United States [Centers for Disease Control (CDC)](https://www.cdc.gov/hrqol/wellbeing.htm#three) calls **well-being**. Physical well-being violations are common safety violations, but we also consider economic, social, emotional, and psychological well-being to be important. Weighing fine differences among these categories is probably not possible, so we will not try. Each decision option lists examples of the effects that qualify for that value/answer in the various types of violations of well-being. These examples should not be considered comprehensive or exhaustive, but rather as suggestive.
<!--The CDC webpage is better called a lit review. It has 74 citations on well-being across various fields. The following citations could reasonably be cited directly, rather than just referencing the CDC page:
Frey BS, Stutzer A. Happiness and economics. Princeton, N.J.: Princeton University Press; 2002.
Andrews FM, Withey SB. Social indicators of well-being. NewYork: Plenum Press; 1976:63–106.
Diener E. Subjective well being: the science of happiness and a proposal for a national index. American Psychologist 2000;55(1):34–43.
Ryff CD, Keyes CLM. The structure of psychological well-being revisited. Journal of Personality and Social Psychology 1995;69(4):719–727.
Diener E, Suh E, Oishi S. Recent findings on subjective well-being. Indian Journal of Clinical Psychology 1997;24:25–41.
Veenhoven R. Sociological theories of subjective well-being. In: M Eid , RJ Larsen (eds). The science of subjective well-being. New York: Guilford Press; 2008:44–61.
Csikszentmihalyi M. Flow: The Psychology of Optimal Experience. New York, NY: Harper Perennial; 1991.
Diener E, Suh EM, Lucas R, Smith H. Subjective well-being: Three decades of progress. Psychological Bulletin 1999;125:276–302.
Larsen RJ, Eid M. Ed Diener and The Science of Subjective Well-Being. In: RJ Larsen and M Eid, (Eds.) The Science of Subjective Well-Being. New York: Guildford Press, 2008:1–12.
Kahneman D, Krueger AB, Schkade DA, Schwarz N, Stone AA. A survey method for characterizing daily life: the day reconstruction method. Science 2004;306:1776–1780.
Eid M. Measuring the Immeasurable: Psychometric modeling of subjective well-being data. In: Eid M, Larsen RJ (eds.) The science of subjective well-being. New York: Guilford Press; 2008:141–167.
Dupuy HJ (1978). Self-representations of general psychological well-being of American adults. Paper presented at the American Public Health Association Meeting, Los Angeles, October, 1978.
Fazio, A.F. (1977). A concurrent validational study of the NCHS General Well-Being Schedule. Hyattsville, MD: U.S. Department of Health, Education and Welfare, national Center for Health Statistics, 1977. Vital and Health Statistics Series 2, No. 73. DHEW Publication No. (HRA) 78-1347.
Kaplan RM, Anderson JP. The quality of well-being scale: Rationale for a single quality of life index. In: SR Walker, R Rosser (Eds.) Quality of Life: Assessment and Application. London: MTP Press; 1988:51–77.
Keyes CLM. The mental health continuum: from languishing to flourishing in life. J Health Soc Res 2002;43(6):207-222.
 -->

The stakeholder should consider the safety impact on the system operators (by “system operator,” we mean those who are professionally responsible for the proper operation of the cyber-physical system, as the term is used in the safety analysis literature) and users of the software they provide.
If software is repackaged and resold by a stakeholder to further downstream entities who will then sell a product, the initial stakeholder can only reasonably consider so many links in that supply chain.
However, a stakeholder should know its immediate consumers who are one step away in the supply chain.
Those consumers may repackage or build on the software and then provide that product further on.

We expect that a stakeholder should be aware of common usage of their software about one step away in the supply chain.
This expectation holds in both open source and proprietary contexts. Further steps along the supply chain are probably not reasonable for the stakeholder to consider consistently; however, this is not a license to willfully ignore common downstream uses of the stakeholder’s software.
If the stakeholder is contractually or legally responsible for safe operation of the software or cyber-physical system of which it is part, that also supersedes our rough supply-chain depth considerations.

For software used in a wide variety of sectors and deployments, the stakeholder may need to estimate an aggregate safety impact.
Aggregation suggests that the stakeholder’s response to this decision point cannot be less than the most severe credible safety impact, but we leave the specific aggregation method or function as a domain-specific extension for future work.

### Gathering Information About Safety Impact

The factors that influence the safety impact level are diverse.
This paper does not exhaustively discuss how a stakeholder should answer a question; that is a topic for future work.
At a minimum, understanding safety impact should include gathering information about survivability of the vulnerable component, determining available operator actions to compensate for the vulnerable component, understanding relevant insurance, and determining the viability of existing backup measures.
Because each of these information items depends heavily on domain-specific knowledge, it is out of the scope of this paper to give a general-purpose strategy for how they should be included.
For example, viable manual backup mechanisms are likely to be important in assessing the safety impact of an industrial control system in a sewage plant, but in banking the insurance structures that prevent bankruptcies are more important.

The decision values for safety impact are based on the hazard categories for aircraft software [@DO-178C; @faa2000safety, Section 3.3.2].
To assign a value to [*Safety Impact*](#safety-impact), at least one type of harm must reach that value. For example, for a [*Safety Impact*](#safety-impact) of [*major*](#safety-impact), at least one type of harm must reach [*major*](#safety-impact) level.
All types of harm do not need to rise to the level of [*major*](#safety-impact), just one type of harm does.

Table: Safety Impact Decision Values

| Value | Type of Harm  | Definition |
| --:          | :--            | :-----------   |
| None          | All           | Does *not* mean no impact *literally*; the effect is below the threshold for all aspects described in Minor |
| Minor         | Physical Harm | Physical discomfort for users of the system OR a minor occupational safety hazard OR reduction in physical system safety margins |
| Minor         | Environment   | Minor externalities (property damage, environmental damage, etc.) imposed on other parties |
| Minor         | Financial     | Financial losses, which are not readily absorbable, to multiple persons |
| Minor         | Psychological | Emotional or psychological harm, sufficient to be cause for counseling or therapy, to multiple persons |
| Major         | Physical Harm | Physical distress and injuries for users of the system OR a significant occupational safety hazard OR failure of physical system functional capabilities that support safe operation |
| Major         | Environment   | Major externalities (property damage, environmental damage, etc.) imposed on other parties |
| Major         | Financial     | Financial losses that likely lead to bankruptcy of multiple persons |
| Major         | Psychological | Widespread emotional or psychological harm, sufficient to be cause for counseling or therapy, to populations of people |
| Hazardous     | Physical Harm | Serious or fatal injuries, where fatalities are plausibly preventable via emergency services or other measures OR parts of the cyber-physical system that support safe operation break |
| Hazardous     | Environment   | Serious externalities (threat to life as well as property, widespread environmental damage, measurable public health risks, etc.) imposed on other parties |
| Hazardous     | Financial     | Socio-technical system (elections, financial grid, etc.) of which the affected component is a part is actively destabilized and enters unsafe state |
| Hazardous     | Psychological | N/A |
| Catastrophic  | Physical Harm | Multiple immediate fatalities (emergency response probably cannot save the victims.) |
| Catastrophic  | Environment   | Extreme externalities (immediate public health threat, environmental damage leading to small ecosystem collapse, etc.) imposed on other parties |
| Catastrophic  | Financial     | Social systems (elections, financial grid, etc.) supported by the software collapse |
| Catastrophic  | Psychological | N/A |


<!-- Literal HTML is only included by pandoc etc in HTML output, so the below is correct but not portable -->
<!--
<a name="table-safety-impact"></a> Safety Impact Decision Values

<table>
<thead>
<tr class="header">
<th><strong>Safety Impact</strong></th>
<th><strong>Type of Harm</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>None</td>
<td>All</td>
<td>Does not mean <em>no impact</em> literally; it just means that the effect is below the threshold for all aspects described in Minor</td>
</tr>
<tr class="even">
<td>Minor<br />
(Any one or more of these conditions hold.)</td>
<td>Physical harm</td>
<td>Physical discomfort for users (not operators) of the system</td>
</tr>
<tr class="odd">
<td></td>
<td>Operator<br />
resiliency</td>
<td>Requires action by system operator to maintain safe system state as a result of exploitation of the vulnerability where operator actions would be well within expected operator abilities; OR causes a minor occupational safety hazard</td>
</tr>
<tr class="even">
<td></td>
<td>System<br />
resiliency</td>
<td>Small reduction in built-in system safety margins; OR small reduction in system functional capabilities that support safe operation</td>
</tr>
<tr class="odd">
<td></td>
<td>Environment</td>
<td>Minor externalities (property damage, environmental damage, etc.) imposed on other parties</td>
</tr>
<tr class="even">
<td></td>
<td>Financial</td>
<td>Financial losses, which are not readily absorbable, to multiple persons</td>
</tr>
<tr class="odd">
<td></td>
<td>Psychological</td>
<td>Emotional or psychological harm, sufficient to be cause for counselling or therapy, to multiple persons</td>
</tr>
<tr class="even">
<td>Major<br />
(Any one or more of these conditions hold.)</td>
<td>Physical harm</td>
<td>Physical distress and injuries for users (not operators) of the system</td>
</tr>
<tr class="odd">
<td></td>
<td>Operator<br />
resiliency</td>
<td>Requires action by system operator to maintain safe system state as a result of exploitation of the vulnerability where operator actions would be within their capabilities but the actions require their full attention and effort; OR significant distraction or discomfort to operators; OR causes significant occupational safety hazard</td>
</tr>
<tr class="even">
<td></td>
<td>System<br />
resiliency</td>
<td>System safety margin effectively eliminated but no actual harm; OR failure of system functional capabilities that support safe operation</td>
</tr>
<tr class="odd">
<td></td>
<td>Environment</td>
<td>Major externalities (property damage, environmental damage, etc.) imposed on other parties</td>
</tr>
<tr class="even">
<td></td>
<td>Financial</td>
<td>Financial losses that likely lead to bankruptcy of multiple persons</td>
</tr>
<tr class="odd">
<td></td>
<td>Psychological</td>
<td>Widespread emotional or psychological harm, sufficient to be cause for counselling or therapy, to populations of people</td>
</tr>
<tr class="even">
<td>Hazardous<br />
(Any one or more of these conditions hold.)</td>
<td>Physical harm</td>
<td>Serious or fatal injuries, where fatalities are plausibly preventable via emergency services or other measures</td>
</tr>
<tr class="odd">
<td></td>
<td>Operator<br />
resiliency</td>
<td>Actions that would keep the system in a safe state are beyond system operator capabilities, resulting in adverse conditions; OR great physical distress to system operators such that they cannot be expected to operate the system properly</td>
</tr>
<tr class="even">
<td></td>
<td>System<br />
resiliency</td>
<td>Parts of the cyber-physical system break; system’s ability to recover lost functionality remains intact</td>
</tr>
<tr class="odd">
<td></td>
<td>Environment</td>
<td>Serious externalities (threat to life as well as property, widespread environmental damage, measurable public health risks, etc.) imposed on other parties</td>
</tr>
<tr class="even">
<td></td>
<td>Financial</td>
<td>Socio-technical system (elections, financial grid, etc.) of which the affected component is a part is actively destabilized and enters unsafe state</td>
</tr>
<tr class="odd">
<td></td>
<td>Psychological</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Catastrophic (Any one or more of these conditions hold.)</td>
<td>Physical harm</td>
<td>Multiple immediate fatalities (Emergency response probably cannot save the victims.)</td>
</tr>
<tr class="odd">
<td></td>
<td>Operator<br />
resiliency</td>
<td>Operator incapacitated (includes fatality or otherwise incapacitated)</td>
</tr>
<tr class="even">
<td></td>
<td>System resiliency</td>
<td>Total loss of whole cyber-physical system, of which the software is a part</td>
</tr>
<tr class="odd">
<td></td>
<td>Environment</td>
<td>Extreme externalities (immediate public health threat, environmental damage leading to small ecosystem collapse, etc.) imposed on other parties</td>
</tr>
<tr class="even">
<td></td>
<td>Financial</td>
<td>Social systems (elections, financial grid, etc.) supported by the software collapse</td>
</tr>
<tr class="odd">
<td></td>
<td>Psychological</td>
<td>N/A</td>
</tr>
</tbody>
</table>
-->

### Public Safety Impact

Suppliers necessarily have a rather coarse-grained perspective on the broadly defined safety impacts described above. Therefore we simplify the above into a binary categorization: _Significant_ is when any impact meets the criteria for an impact of Major, Hazardous, or Catastrophic in the above table. _Minimal_ is when none do.

Table: Public Safety Impact Decision Values

|   Value     | Definition |
| :--- | :--------- |
| Minimal     | Safety Impact of None or Minor                     |
| Significant | Safety Impact of Major, Hazardous, or Catastrophic |


### Situated Safety Impact

Deployers are anticipated to have a more fine-grained perspective on the safety impacts broadly defined in [Safety Impact](#table-safety-impact).
We defer this topic for now because we combine it with [*Mission Impact*](#mission-impact) to simplify implementation for deployers.


## Mission Impact
> Impact on Mission Essential Functions of the Organization

A **mission essential function (MEF)** is a function “directly related to accomplishing the organization’s mission as set forth in its statutory or executive charter” [@FCD2_2017, page A-1]. Identifying MEFs is part of business continuity planning or crisis planning. The rough difference between MEFs and non-essential functions is that an organization “must perform a\[n MEF\] during a disruption to normal operations” [@FCD2_2017, page B-2]. The mission is the reason an organization exists, and MEFs are how that mission is affected. Non-essential functions do not directly support the mission per se; however, they support the smooth delivery or success of MEFs. Financial losses—especially to publicly traded for-profit corporations—are covered here as a (legally mandated) mission of such corporations is financial performance.

Table:  Mission Impact Decision Values

| Value | Definition  |
| :--- | :---------- |
| Degraded | Little to no impact up to degradation of non-essential functions; chronic degradation would eventually harm essential functions                                                                     |
| MEF Support Crippled   | Activities that directly support essential functions are crippled; essential functions continue for a time                                                                |
| MEF Failure            | Any one mission essential function fails for period of time longer than acceptable; overall mission of the organization degraded but can still be accomplished for a time |
| Mission Failure        | Multiple or all mission essential functions fail; ability to recover those functions degraded; organization’s ability to deliver its overall mission fails                |

### Gathering Information About Mission Impact

The factors that influence the mission impact level are diverse. This paper does not exhaustively discuss how a stakeholder should answer a question; that is a topic for future work. At a minimum, understanding mission impact should include gathering information about the critical paths that involve vulnerable components, viability of contingency measures, and resiliency of the systems that support the mission. There are various sources of guidance on how to gather this information; see for example the FEMA guidance in Continuity Directive 2 [@FCD2_2017] or OCTAVE FORTE [@tucker2018octave]. This is part of risk management more broadly. It should require the vulnerability management team to interact with more senior management to understand mission priorities and other aspects of risk mitigation.

As a heuristic, [*Utility*](#utility) might constrain [*Mission Impact*](#mission-impact) if both are not used in the same decision tree.
For example, if the [*Utility*](#utility) is [*super effective*](#utility), then [*Mission Impact*](#mission-impact) is at least [*MEF support crippled*](#mission-impact).

## Human Impact
 > Combined Situated Safety and Mission Impact

In pilot implementations of SSVC, we received feedback that organizations tend to think of mission and safety impacts as if they were combined into a single factor: in other words, the priority increases regardless which of the two  impact factors was increased.
We therefore combine Situated Safety and Mission Impact for deployers into a single _Human Impact_ factor as a dimension reduction step as follows.
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

Table: Combining Mission and Situated Safety Impact into Human Impact

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

<!-- Literal HTML is only included by pandoc etc in HTML output, so the below is correct but not portable -->
<!--
<table>
<a name="table-mission-safety-combined"></a>
<thead>
<tr class="header">
<th colspan=5><strong>Combining Mission Impact and Situated Safety Impact into one result.</strong></th>
</tr>
</thead>
  <tr>
  <td> </td>
  <td> </td>
  <td colspan=3 style="text-align:center"> <b>Mission Impact</b> </td>
  </tr>
  <tr>
  <td> </td>
  <td> </td>
  <td> <em> Degraded/ Crippled </td>
  <td> <em> MEF Failure</td>
  <td> <em> Mission Failure</td>
  </tr>
  <tr>
  <td rowspan=4> <b>Situated Safety Impact </b></td>
  <td> <em> None/Minor</td>
  <td> Low </td>
  <td> Medium </td>
  <td> Very High </td>
  </tr>
  <tr>
  <td> <em> Major</td>
  <td> Medium </td>
  <td> High </td>
  <td> Very High </td>
  </tr>
  <tr>
  <td> <em> Hazardous</td>
  <td> High </td>
  <td> High </td>
  <td> Very High </td>
  </tr>
  <tr>
  <td> <em> Catastrophic</td>
  <td> Very High </td>
  <td> Very High </td>
  <td> Very High </td>
  </tr>
</table>
-->

### Safety and Mission Impact Decision Points for Industry Sectors

We expect to encounter diversity in both safety and mission impacts across different organizations. However, we also anticipate a degree of commonality of impacts to arise across organizations within a given industry sector. For example, different industry sectors may have different use cases for the same software.
Therefore, vulnerability information providers—that is, vulnerability databases, Information Sharing and Analysis Organizations (ISAOs), or Information Sharing and Analysis Centers (ISACs)—may provide SSVC information tailored as appropriate to their constituency's safety and mission concerns.
For considerations on how organizations might communicate SSVC information to their constituents, see [Guidance on Communicating Results](#guidance-on-communicating-results).


## System Exposure
> The Accessible Attack Surface of the Affected System or Service

Measuring the attack surface precisely is difficult, and we do not propose to perfectly delineate between small and controlled access.
Exposure should be judged against the system in its deployed context, which may differ from how it is commonly expected to be deployed.
For example, the exposure of a device on a vehicle's CAN bus will vary depending on the presence of a cellular telemetry device on the same bus.

If a vulnerability cannot be remediated, other mitigations may be used.
Usually, the effect of these mitigations is to reduce exposure of the vulnerable component.
Therefore, a deployer’s response to Exposure may change if such mitigations are put in place.
If a mitigation changes exposure and thereby reduces the priority of a vulnerability, that mitigation can be considered a success.
Whether that mitigation allows the deployer to defer further action varies according to each case.

Table: System Exposure Decision Values

| Value       | Definition |
| :---        | :------------ |
| Small       | Local service or program; highly controlled network       |
| Controlled  | Networked service with some access restrictions or mitigations already in place (whether locally or on the network). A successful mitigation must reliably interrupt the adversary’s attack, which requires the attack is detectable both reliably and quickly enough to respond. *Controlled* covers the situation in which a vulnerability can be exploited through chaining it with other vulnerabilities. The assumption is that the number of steps in the attack path is relatively low; if the path is long enough that it is implausible for an adversary to reliably execute it, then *exposure* should be *small*. |
| Open        | Internet or another widely accessible network where access cannot plausibly be restricted or controlled (e.g., DNS servers, web servers, VOIP servers, email servers)  |

### Gathering Information About System Exposure

[*System Exposure*](#system-exposure) is primarily used by Deployers, so the question is about whether some specific system is in fact exposed, not a hypothetical or aggregate question about systems of that type.
Therefore, it generally has a concrete answer, even though it may vary from vulnerable component to vulnerable component, based on their respective configurations.

[*System Exposure*](#system-exposure) can be readily informed by network scanning techniques.
For example, if the vulnerable component is visible on [Shodan](www.shodan.io) or by some other external scanning service, then it is [*open*](#system-exposure).
Network policy or diagrams are also useful information sources, especially for services intentionally open to the Internet such as public web servers.
An analyst should also choose [*open*](#system-exposure) for a phone or PC that connects to the web or email without the usual protections (IP and URL blocking, updated firewalls, etc.).

Distinguishing between [*small*](#system-exposure) and [*controlled*](#system-exposure) is more nuanced.
If [*open*](#system-exposure) has been ruled out, some suggested heuristics for differentiating the other two are as follows.
Apply these heuristics in order and stop when one of them applies.
 - If the system's networking and communication interfaces have been physically removed or disabled, choose [*small*](#system-exposure).
 - If [*Automatable*](#automatable) is [*yes*](#automatable), then choose [*controlled*](#system-exposure). The reasoning behind this heuristic is that if reconnaissance through exploitation is automatable, then the usual deployment scenario exposes the system sufficiently that access can be automated, which contradicts the expectations of [*small*](#system-exposure).
 - If the vulnerable component is on a network where other hosts can browse the web or receive email, choose [*controlled*](#system-exposure).

If you have suggestions for further heuristics, or potential counterexamples to these,  please describe the example and reasoning in an issue on the [SSVC GitHub](https://github.com/CERTCC/SSVC/issues).
