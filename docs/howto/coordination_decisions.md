# Coordination Triage Decisions

We take three priority levels in our decision about whether and how to coordinate a vulnerability [@householder2020cvd, 1.1] based on an incoming report:

 - *Decline*—Do not act on the report. May take different forms, including ignoring the report as well as an acknowledgement to the reporter that we will not act and suggest the reporter to go to vendor or publish if unresponsive.
 - *Track*—Receive information about the vulnerability and monitor for status changes but do not take any overt actions.
 - *Coordinate*—Take action on the report. “Action” may include any one or more of: technical analysis, reproduction, notifying vendors, lead coordination (notify, communicate, and publish), publish only (amplify public message), advise only, secondary coordinator (assist another lead coordinator). See [@csirtservices_v2] for additional vulnerability management services a coordinator may provide.


## Coordinator Decision Points

Our goal with the coordination decision is to base it on information that is available to the analyst when CERT/CC receives a vulnerability report.
In addition to using some of the decision points in [Likely Decision Points](#likely-decision-points-and-relevant-data); coordination makes use of [Utility](#utility) and [Public Safety Impact](#public-safety-impact) decision points.
The coordination and publication decisions for CERT/CC are about the social and collaborative state of vulnerability management.
To assess this, the decision involves five new decision points.

{== TODO link to specific decision points ==}




## Coordination Triage Decision Process

The decision tree for reaching a [Decision](#coordination-triage-decisions) involves seven decision points.
The first two function as gating questions:
 - If a report is already public, then CERT/CC will decline the case unless there are multiple suppliers, [*super effective*](#utility) [*Utility*](#utility), and [*significant*](#public-safety-impact) [Public Safety Impact](#public-safety-impact).
 - If no suppliers have been contacted, then CERT/CC will decline the case unless there are multiple suppliers, [*super effective*](#utility) [*Utility*](#utility), and [*significant*](#public-safety-impact) [Public Safety Impact](#public-safety-impact).

In the second case, CERT/CC may encourage the reporter to contact the supplier and submit a new case request if the supplier is unresponsive.

These two sets of exceptional circumstances mean that the seven decision points involved in the coordination triage tree can be compressed slightly, as the tree shows.
This tree's information is available as either a [CSV](https://github.com/CERTCC/SSVC/blob/main/data/ssvc_2_coord-triage.csv) or [PDF](https://github.com/CERTCC/SSVC/blob/main/doc/graphics/ssvc_2_coord-triage.pdf)

{% include-markdown './coordinator_trees.md' heading-offset=1 %}