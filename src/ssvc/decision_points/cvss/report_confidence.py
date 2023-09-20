#!/usr/bin/env python
"""
file: report_confidence
author: adh
created_at: 9/20/23 1:48 PM
"""
from copy import deepcopy

from ssvc.decision_points.base import SsvcValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint

REPORT_CONFIDENCE_1 = CvssDecisionPoint(
    name="Report Confidence",
    description="This metric measures the degree of confidence in the existence of the vulnerability and the credibility of the known technical details.",
    key="RC",
    version="1.0.0",
    values=[
        SsvcValue(
            name="Unconfirmed",
            key="UC",
            description="A single unconfirmed source or possibly several conflicting reports. There is little confidence in the validity of the report. For example, a rumor that surfaces from the hacker underground.",
        ),
        SsvcValue(
            name="Uncorroborated",
            key="UR",
            description="Multiple non-official sources; possibily including independent security companies or research organizations. At this point there may be conflicting technical details or some other lingering ambiguity.",
        ),
        SsvcValue(
            name="Confirmed",
            key="C",
            description="Vendor or author of the affected technology has acknowledged that the vulnerability exists. This value may also be set when existence of a vulnerability is confirmed with absolute confidence through some other event, such as publication of functional proof of concept exploit code or widespread exploitation.",
        ),
    ],
)

# CVSS v2 added Not Defined.
REPORT_CONFIDENCE_1_1 = deepcopy(REPORT_CONFIDENCE_1)
REPORT_CONFIDENCE_1_1.version = "1.1.0"
nd = SsvcValue(
    name="Not Defined",
    key="ND",
    description="Assigning this value to the metric will not influence the score. It is a signal to the equation to skip this metric.",
)
REPORT_CONFIDENCE_1_1.values.append(nd)

# CVSS v3 changed names and descriptions for this metric.
REPORT_CONFIDENCE_2 = deepcopy(REPORT_CONFIDENCE_1_1)
REPORT_CONFIDENCE_2.version = "2.0.0"
REPORT_CONFIDENCE_2.values = [
    SsvcValue(
        name="Unknown",
        key="U",
        description="There are reports of impacts that indicate a vulnerability is present. The reports indicate that the cause of the vulnerability is unknown, or reports may differ on the cause or impacts of the vulnerability. Reporters are uncertain of the true nature of the vulnerability, and there is little confidence in the validity of the reports or whether a static Base score can be applied given the differences described. An example is a bug report which notes that an intermittent but non-reproducible crash occurs, with evidence of memory corruption suggesting that denial of service, or possible more serious impacts, may result.",
    ),
    SsvcValue(
        name="Reasonable",
        key="R",
        description="Significant details are published, but researchers either do not have full confidence in the root cause, or do not have access to source code to fully confirm all of the interactions that may lead to the result. Reasonable confidence exists, however, that the bug is reproducible and at least one impact is able to be verified (proof-of-concept exploits may provide this). An example is a detailed write-up of research into a vulnerability with an explanation (possibly obfuscated or 'left as an exercise to the reader') that gives assurances on how to reproduce the results.",
    ),
    SsvcValue(
        name="Confirmed",
        key="C",
        description="Detailed reports exist, or functional reproduction is possible (functional exploits may provide this). Source code is available to independently verify the assertions of the research, or the author or vendor of the affected code has confirmed the presence of the vulnerability.",
    ),
    deepcopy(nd),
]


def main():
    print(REPORT_CONFIDENCE_1.to_json(indent=2))
    print(REPORT_CONFIDENCE_1_1.to_json(indent=2))
    print(REPORT_CONFIDENCE_2.to_json(indent=2))


if __name__ == "__main__":
    main()
