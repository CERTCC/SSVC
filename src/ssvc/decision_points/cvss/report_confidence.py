#!/usr/bin/env python
"""
Models the CVSS Report Confidence metric as an SSVC decision point.
"""

from ssvc.decision_points.base import SsvcDecisionPointValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint

_NOT_DEFINED = SsvcDecisionPointValue(
    name="Not Defined",
    key="ND",
    description="Assigning this value to the metric will not influence the score. It is a signal to the equation to skip this metric.",
)

_CONFIRMED_2 = SsvcDecisionPointValue(
    name="Confirmed",
    key="C",
    description="Detailed reports exist, or functional reproduction is possible (functional exploits may provide this). Source code is available to independently verify the assertions of the research, or the author or vendor of the affected code has confirmed the presence of the vulnerability.",
)

_REASONABLE = SsvcDecisionPointValue(
    name="Reasonable",
    key="R",
    description="Significant details are published, but researchers either do not have full confidence in the root cause, or do not have access to source code to fully confirm all of the interactions that may lead to the result. Reasonable confidence exists, however, that the bug is reproducible and at least one impact is able to be verified (proof-of-concept exploits may provide this). An example is a detailed write-up of research into a vulnerability with an explanation (possibly obfuscated or 'left as an exercise to the reader') that gives assurances on how to reproduce the results.",
)

_UNKNOWN = SsvcDecisionPointValue(
    name="Unknown",
    key="U",
    description="There are reports of impacts that indicate a vulnerability is present. The reports indicate that the cause of the vulnerability is unknown, or reports may differ on the cause or impacts of the vulnerability. Reporters are uncertain of the true nature of the vulnerability, and there is little confidence in the validity of the reports or whether a static Base score can be applied given the differences described. An example is a bug report which notes that an intermittent but non-reproducible crash occurs, with evidence of memory corruption suggesting that denial of service, or possible more serious impacts, may result.",
)

_CONFIRMED = SsvcDecisionPointValue(
    name="Confirmed",
    key="C",
    description="Vendor or author of the affected technology has acknowledged that the vulnerability exists. This value may also be set when existence of a vulnerability is confirmed with absolute confidence through some other event, such as publication of functional proof of concept exploit code or widespread exploitation.",
)

_UNCORROBORATED = SsvcDecisionPointValue(
    name="Uncorroborated",
    key="UR",
    description="Multiple non-official sources; possibily including independent security companies or research organizations. At this point there may be conflicting technical details or some other lingering ambiguity.",
)

_UNCONFIRMED = SsvcDecisionPointValue(
    name="Unconfirmed",
    key="UC",
    description="A single unconfirmed source or possibly several conflicting reports. There is little confidence in the validity of the report. For example, a rumor that surfaces from the hacker underground.",
)

REPORT_CONFIDENCE_1 = CvssDecisionPoint(
    name="Report Confidence",
    description="This metric measures the degree of confidence in the existence of the vulnerability and the credibility of the known technical details.",
    key="RC",
    version="1.0.0",
    values=(
        _UNCONFIRMED,
        _UNCORROBORATED,
        _CONFIRMED,
    ),
)
"""
Defines Unconfirmed, Uncorroborated, and Confirmed values for CVSS Report Confidence.
"""

REPORT_CONFIDENCE_1_1 = CvssDecisionPoint(
    name="Report Confidence",
    description="This metric measures the degree of confidence in the existence of the vulnerability and the credibility of the known technical details.",
    key="RC",
    version="1.1.0",
    values=(
        _UNCONFIRMED,
        _UNCORROBORATED,
        _CONFIRMED,
        _NOT_DEFINED,
    ),
)
"""
Adds Not Defined to the CVSS Report Confidence decision point.
"""

REPORT_CONFIDENCE_2 = CvssDecisionPoint(
    name="Report Confidence",
    description="This metric measures the degree of confidence in the existence of the vulnerability and the credibility of the known technical details.",
    key="RC",
    version="2.0.0",
    values=(
        _UNKNOWN,
        _REASONABLE,
        _CONFIRMED_2,
        _NOT_DEFINED,
    ),
)
"""
Replaces Unconfirmed and Uncorroborated with Unknown and Reasonable. Updated Confirmed. Retains Not Defined.
"""


def main():
    print(REPORT_CONFIDENCE_1.to_json(indent=2))
    print(REPORT_CONFIDENCE_1_1.to_json(indent=2))
    print(REPORT_CONFIDENCE_2.to_json(indent=2))


if __name__ == "__main__":
    main()
