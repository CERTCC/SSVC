# Safety Impact

```python exec="true" idprefix=""
from ssvc.decision_points.safety_impact import LATEST
from ssvc.doc_helpers import example_block

print(example_block(LATEST))
```

{% include-markdown "../../_includes/safety_cvss_ssvc.md" %}

!!! tip "See also"

    - Safety Impact combines with [Mission Impact](./mission_impact.md) to 
      inform [Human Impact](./human_impact.md).

We take an expansive view of safety, in which a safety violation is a violation of what the United States [Centers for Disease Control (CDC)](https://www.cdc.gov/hrqol/wellbeing.htm) calls **well-being**. Physical well-being violations are common safety violations, but we also consider economic, social, emotional, and psychological well-being to be important. Weighing fine differences among these categories is probably not possible, so we will not try. Each decision option lists examples of the effects that qualify for that value/answer in the various types of violations of well-being. These examples should not be considered comprehensive or exhaustive, but rather as suggestive.
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

## Gathering Information About Safety Impact

The factors that influence the safety impact level are diverse.
This paper does not exhaustively discuss how a stakeholder should answer a question; that is a topic for future work.
At a minimum, understanding safety impact should include gathering information about survivability of the vulnerable component, determining available operator actions to compensate for the vulnerable component, understanding relevant insurance, and determining the viability of existing backup measures.
Because each of these information items depends heavily on domain-specific knowledge, it is out of the scope of this paper to give a general-purpose strategy for how they should be included.
For example, viable manual backup mechanisms are likely to be important in assessing the safety impact of an industrial control system in a sewage plant, but in banking the insurance structures that prevent bankruptcies are more important.

The decision values for safety impact are based on the hazard categories for aircraft software [@DO-178C; @faa2000safety, Section 3.3.2].
To assign a value to [*Safety Impact*](safety_impact.md), at least one type of harm must reach that value. For example, for a [*Safety Impact*](safety_impact.md) of [*major*](safety_impact.md), at least one type of harm must reach [*major*](safety_impact.md) level.
All types of harm do not need to rise to the level of [*major*](safety_impact.md), just one type of harm does.

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

### Situated Safety Impact

Deployers are anticipated to have a more fine-grained perspective on the safety impacts broadly defined in *Safety Impact*.
We defer this topic for now because we combine it with [*Mission Impact*](mission_impact.md) to simplify implementation for deployers.

## Prior Versions

```python exec="true" idprefix=""
from ssvc.decision_points.safety_impact import VERSIONS
from ssvc.doc_helpers import example_block

versions = VERSIONS[:-1]
for version in versions:
    print(example_block(version))
    print("\n---\n")
```
