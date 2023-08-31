# Coordinator Decision Points

Our goal with the coordination decision is to base it on information that is available to the analyst when CERT/CC receives a vulnerability report.
In addition to using some of the decision points in [Likely Decision Points](#likely-decision-points-and-relevant-data); coordination makes use of [Utility](#utility) and [Public Safety Impact](#public-safety-impact) decision points.
The coordination and publication decisions for CERT/CC are about the social and collaborative state of vulnerability management.
To assess this, the decision involves five new decision points.

!!! note "Report Public"

    Is a viable report of the details of the vulnerability already publicly available?
    
    | Value | Description |
    | :---: | :--- |
    | Yes | A viable report of the details of the vulnerability is already publicly available. |
    | No | A viable report of the details of the vulnerability is not already publicly available. |


!!! tip inline end "Quality Contact Method"

    A quality contact method is a publicly posted known good email address, public portal on vendor website, etc.


!!! note "Supplier Contacted"

    Has the reporter made a good-faith effort to contact the supplier of the vulnerable component using a quality contact method?

    | Value | Description |
    | :---: | :--- |
    | Yes | The reporter has made a good-faith effort to contact the supplier of the vulnerable component using a quality contact method. |
    | No | The reporter has not made a good-faith effort to contact the supplier of the vulnerable component using a quality contact method. |


!!! note "Supplier Cardinality"

    How many suppliers are responsible for the vulnerable component and its remediation or mitigation plan?

    | Value | Description |
    | :---: | :--- |
    | One | One supplier is responsible for the vulnerable component and its remediation or mitigation plan. |
    | Multiple | Multiple suppliers are responsible for the vulnerable component and its remediation or mitigation plan. |

!!! note "Supplier Engagement"

    Is the supplier responding to the reporter's contact effort and actively participating in the coordination effort?

    | Value | Description |
    | :---: | :--- |
    | Active | The supplier is responding to the reporter's contact effort and actively participating in the coordination effort. |
    | Unresponsive | The supplier is not responding to the reporter's contact effort and is not actively participating in the coordination effort. |


!!! tip inline end "Presumption of Credibility"

    An analyst should start with a presumption of credibility and proceed toward disqualification.
    The reason for this is that, as a coordinator, occasionally doing a bit of extra work on a bad report is preferable to rejecting legitimate reports.
    This is essentially stating a preference for false positives over false negatives with respect to credibility determination.

    Guidance on assessing credibility is available in [Credibility Indicators](../../topics/credibility_indicators.md).
    There are no ironclad rules for this assessment, and other coordinators may find other guidance works for them.
    Credibility assessment topics include indicators for and against credibility, perspective, topic, and relationship to report scope.


!!! note "Report Credibility"

    Assessing the credibility of a report is complex, but the assessment must reach a conclusion of either:

    | Value | Description |
    | :---: | :--- |
    | Credible | The report is credible. |
    | Not credible | The report is not credible. |





