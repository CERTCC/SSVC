# Representing Information for Decisions About Vulnerabilities

We propose that decisions about vulnerabilities—rather than their severity—are a more useful approach.
Our design goals for the decision-making process are to

- clearly define whose decisions are involved
- properly use evidentiary categories
- be based on reliably available evidence
- be transparent
- be explainable

Our inspiration and justification for these design goals are that they are the features of a satisfactory scientific enterprise [@spring2017why] adapted to the vulnerability management problem.

## Clearly Define Whose Decisions Are Involved

To consider decisions about managing the vulnerability rather than just its technical severity, one must be clear about whose decisions are involved.
Organizations that produce patches and fix software clearly have different decisions to make than those that deploy patches or other security mitigations.
For example, organizations in the aviation industry have different priorities than organizations that make word processors.
These differences indicate a requirement: any formalism must adequately capture the different decisions and priorities exhibited by different groups of stakeholders.
As a usability requirement, the number of stakeholder groups needs to be small enough to be manageable, both by those issuing scores and those seeking them.

The goal of adequacy is more appropriate than optimality.
Our search process need not be exhaustive; we are satisficing rather than optimizing [@simon1996sciences].
Finding any system that meets all of the desired criteria is enough.

## Properly Use Evidentiary Categories

Decisions are not numbers.
They are qualitative actions that an organization can take.
In many cases, numerical values can be directly converted to qualitative decisions.
For example, if your child’s temperature is 105°F (40.5°C), you decide to go to the hospital immediately.
Conversion from numerical to qualitative values can be complicated by measurement uncertainty and the design of the metrics.
For example, CVSS scores were designed to be accurate with +/- 0.5 points of the given score [@cvss_v3-1, section 7.5].
Therefore, under a Gaussian error distribution, 8.9 is really 60\% high and 40\% critical since the recommended dividing line is 9.0.
SSVC decisions should be distinct and crisp, without such statistical overlaps.

We avoid numerical representations for either inputs or outputs of a vulnerability management decision process.
Quantified metrics are more useful when

1. data for decision making is available, and
2. the stakeholders agree on how to measure.

Vulnerability management does not yet meet either criterion.
Furthermore, it is not clear to what extent measurements about a vulnerability can be informative about other vulnerabilities.
Each vulnerability has a potentially unique relationship to the socio-technical system in which it exists, including the Internet.

## Be Based on Reliably Available Evidence

Vulnerability management decisions are often contextual: given what is known at the time, the decision is to do X.
But what is known can change over time, which can and should influence the decision.
The context of the vulnerability, and the systems it impacts, are inextricably linked to managing it.
Some information about the context will be relatively static over time, such as the contribution of a system to an organization's mission.
Other information can change rapidly as events occur, such as the public release of an exploit or observation of attacks.
Temporal and environmental considerations should be primary, not optional as they are in CVSS.
We discuss the temporal aspects further in [Information Changes over Time](../howto/bootstrap/use.md).

## Be Transparent

We make the deliberation process as clear as is practical; therefore, we risk belaboring some points to ensure our assumptions and reasoning are explicit.
Transparency should improve trust in the results.

## Be Explainable

Finally, any result of a decision-making process should be **explainable**
Explainable is defined and used with its common meaning, not as it is used in the research area of explainable artificial intelligence.
An explanation should make the process intelligible to an interested, competent, non-expert person.
There are at least two reasons common explainability is important:

1. for troubleshooting and error correction and
2. for justifying proposed decisions.

## Summary

To summarize, the following are our design goals for a vulnerability
management process:

- Outputs are decisions.

- Pluralistic recommendations are made among a manageable number of
    stakeholder groups.

- Inputs are qualitative.

- Outputs are qualitative, and there are no (unjustified) shifts to
    quantitative calculations.

- Process justification is transparent.

- Results are explainable.
