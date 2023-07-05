

# Future Work

We intend SSVC to offer a workable baseline from which to improve and refine a vulnerability-prioritization methodology.
We are working to improve SSVC.
Several of the future work items in this section have issues associated with them on the SSVC GitHub page (https://github.com/CERTCC/SSVC/issues), which is a good place to go to check on progress or help.
Plans for future work focus on further requirements gathering, analysis of types of risk, and further testing of the reliability of the decision process.

## Requirements Gathering via Sociological Research

The community should know what users of a vulnerability prioritization system want.
To explore their needs, it is important to understand how people actually use CVSS and what they think it tells them.
In general, such empirical, grounded evidence about what practitioners and decision makers want from vulnerability scoring is lacking. We have based this paper’s methodology on multiple decades of professional experience and myriad informal conversations with practitioners. Such evidence is not a bad place to start, but it does not lend itself to examination and validation by others. The purpose of understanding practitioner expectations is to inform what a vulnerability-prioritization methodology should actually provide by matching it to what people want or expect. The method this future work should take is long-form, structured interviews. We do not expect anyone to have access to enough consumers of CVSS to get statistically valid results out of a short survey, nor to pilot a long survey.

Coordinators in particular are likely to be heterogeneous.
While the FIRST service frameworks for PSIRTs and CSIRTs differentiate two broad classes of coordinators, we have focused on CSIRTs here.
PSIRTs may have somewhat different concerns.
Investigating the extent to which SSVC should be customized for this group is future work as well.

## Types of Risks

SSVC estimates the relative risk created by a vulnerability in an information system.
The priority of acting to mitigate or remediate a vulnerability goes up as this vulnerability risk goes up.
SSVC does not currently take into account the change risk due to applying a mitigation or remediation.

One way to view what SSVC currently provides is that it tells you how urgently a stakeholder should analyze overall risk due to a vulnerability.
For all but the most dire vulnerabilities, what the stakeholder chooses to do may include accepting the vulnerability risk because the change risk or other costs of mitigation or remediation are too high.
Future work should attempt to provide a method for [evaluating change risk or cost](https://github.com/CERTCC/SSVC/issues/35) relative to vulnerability risk.

[Tree Construction and Customization Guidance](#tree-construction-and-customization-guidance) discusses how the prioritization labels in an SSVC tree reflect risk appetite or risk tolerance.
Specifically, these reflect vulnerability risk appetite.
Appetite for vulnerability risk may be negatively correlated with change risk; future work could explore this relationship.
Furthermore, future work could examine suggested practices for connecting tree customization to risk management.

[Reasoning Steps Forward](#reasoning-steps-forward) states the scope of SSVC analysis is “consider credible effects based on known use cases of the software system as a part of cyber-physical systems.”
The unit of prioritization in SSVC should be work items.
For deployers, a work item is often applying a patch that addresses multiple vulnerabilities.
The “credible effects” to consider are those of all vulnerabilities remediated by the patch.
How exactly to aggregate these different effects is not currently specified except to say that the unit of analysis is the whole work item.
Future work should provide some examples of how this holistic analysis of multiple vulnerabilities remediated in one patch should be conducted.


## Further Decision Tree Testing

More testing with diverse analysts is necessary before the decision trees are reliable. In this context, **reliable** means that two analysts, given the same vulnerability description and decision process description, will reach the same decision. Such reliability is important if scores and priorities are going to be useful. If they are not reliable, they will vary widely over time and among analysts. Such variability makes it impossible to tell whether a difference in scores is really due to one vulnerability being higher priority than other.

The SSVC version 1 pilot study provides a methodology for measuring and evaluating reliability of the decision process description based on the agreement measure *k*.
This study methodology should be repeated with different analyst groups, from different sectors and with different experience, using the results to make changes in the decision process description until the agreement measure is adequately close to 1.

Internationalization and localization of SSVC will also need to be considered and tested in future work.
It is not clear how best to consider translating SSVC decision points, if at all.
And at [a very practical level](https://github.com/CERTCC/SSVC/issues/123), the [Abbreviated Format](#abbreviated-format) would have to define a new algorithm for creating initialisms that is not dependent an an alphabet for languages based on syllabaries or ideograms.
But a more actionable item of future work would be to include non-native English speakers in future usability studies.

A different approach to testing the [*Utility*](#utility) decision point could be based on [Alternative Utility Outputs](#alternative-utility-outputs).
Namely, future work could example exploit resale markets and compare the value of exploits to the [*Utility*](#utility) score of the exploited vulnerability.
There are some limitations to this approach, since exploit markets target certain adversary groups (such as those with lots of resources) and may not be representative of all adversary types.
However, such analysis would provide some information as to whether the definition of [*Utility*](#utility) is reasonable.
