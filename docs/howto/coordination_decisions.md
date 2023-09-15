
# Decisions During Vulnerability Coordination

Coordinators are facilitators within the vulnerability management ecosystem.
Since coordinators neither supply nor deploy the vulnerable component in question, their decisions are different from suppliers' or deployers' decisions.
This section provides a window into CERT/CC's decisions as an example of how a coordinator might use SSVC to make its own decisions.

Coordinators vary quite a lot, and their use of SSVC may likewise vary.
A coordinator may want to gather and publish information about SSVC decision points that it does not use internally in order to assist its constituents.
Furthermore, a coordinator may only publish some of the information it uses to make decisions.
Consistent with other stakeholder perspectives (supplier and deployer), SSVC provides the priority with which a coordinator should take some defined action, but not how to do that action.
For more information about types of coordinators and their facilitation actions within vulnerability management, see [@householder2020cvd].

The two decisions that CERT/CC makes as a coordinator that we will discuss in terms of SSVC are the initial triage of vulnerability reports and whether a publication about a vulnerability is warranted.
The initial coordination decision is a prioritization decision, but it does not have the same values as prioritization by a deployer or supplier.
The publication decision for us is a binary yes/no.
These two decisions are not the entirety of vulnerability coordination, but we leave further details of the process for future work.

Different coordinators have different scopes and constituencies.
See [@householder2020cvd, 3.5] for a listing of different coordinator types.
If a coordinator receives a report that is outside its own work scope or constituency, it should make an effort to route the report to a more suitable coordinator.
The decisions in this section assume the report or vulnerability in question is in the work scope or constituency for the coordinator.



## Coordination Triage Decisions

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

{== TODO merge with [Coordinator Trees](coordinator_trees.md)? ==}