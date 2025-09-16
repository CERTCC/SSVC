#!/usr/bin/env python
"""
Models the CVSS Report Confidence metric as an SSVC decision point.
"""

#  Copyright (c) 2023-2025 Carnegie Mellon University.
#  NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE
#  ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS.
#  CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND,
#  EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT
#  NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR
#  MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE
#  OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE
#  ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM
#  PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
#  Licensed under a MIT (SEI)-style license, please see LICENSE or contact
#  permission@sei.cmu.edu for full terms.
#  [DISTRIBUTION STATEMENT A] This material has been approved for
#  public release and unlimited distribution. Please see Copyright notice
#  for non-US Government use and distribution.
#  This Software includes and/or makes use of Third-Party Software each
#  subject to its own license.
#  DM24-0278

from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_points.cvss._not_defined import (
    NOT_DEFINED_ND,
    NOT_DEFINED_X,
)
from ssvc.decision_points.cvss.base import CvssDecisionPoint
from ssvc.decision_points.helpers import print_versions_and_diffs

_CONFIRMED_2 = DecisionPointValue(
    name="Confirmed",
    key="C",
    definition="Detailed reports exist, or functional reproduction is possible (functional exploits may provide "
    "this). Source code is available to independently verify the assertions of the research, "
    "or the author or vendor of the affected code has confirmed the presence of the vulnerability.",
)

_REASONABLE = DecisionPointValue(
    name="Reasonable",
    key="R",
    definition="Significant details are published, but researchers either do not have full confidence in the root "
    "cause, or do not have access to source code to fully confirm all of the interactions that may lead "
    "to the result. Reasonable confidence exists, however, that the bug is reproducible and at least one "
    "impact is able to be verified (proof-of-concept exploits may provide this).",
)

_UNKNOWN = DecisionPointValue(
    name="Unknown",
    key="U",
    definition="There are reports of impacts that indicate a vulnerability is present. The reports indicate that the "
    "cause of the vulnerability is unknown, or reports may differ on the cause or impacts of the "
    "vulnerability. Reporters are uncertain of the true nature of the vulnerability, and there is little "
    "confidence in the validity of the reports or whether a static Base score can be applied given the "
    "differences described.",
)

_CONFIRMED = DecisionPointValue(
    name="Confirmed",
    key="C",
    definition="Vendor or author of the affected technology has acknowledged that the vulnerability exists. This "
    "value may also be set when existence of a vulnerability is confirmed with absolute confidence "
    "through some other event, such as publication of functional proof of concept exploit code or "
    "widespread exploitation.",
)

_UNCORROBORATED = DecisionPointValue(
    name="Uncorroborated",
    key="UR",
    definition="Multiple non-official sources; possibily including independent security companies or research "
    "organizations. At this point there may be conflicting technical details or some other lingering "
    "ambiguity.",
)

_UNCONFIRMED = DecisionPointValue(
    name="Unconfirmed",
    key="UC",
    definition="A single unconfirmed source or possibly several conflicting reports. There is little confidence in "
    "the validity of the report.",
)

REPORT_CONFIDENCE_1 = CvssDecisionPoint(
    name="Report Confidence",
    definition="This metric measures the degree of confidence in the existence of the vulnerability and the "
    "credibility of the known technical details.",
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
    definition="This metric measures the degree of confidence in the existence of the vulnerability and the "
    "credibility of the known technical details.",
    key="RC",
    version="1.1.0",
    values=(
        _UNCONFIRMED,
        _UNCORROBORATED,
        _CONFIRMED,
        NOT_DEFINED_ND,
    ),
)
"""
Adds Not Defined to the CVSS Report Confidence decision point.
"""

REPORT_CONFIDENCE_2 = CvssDecisionPoint(
    name="Report Confidence",
    definition="This metric measures the degree of confidence in the existence of the vulnerability and the "
    "credibility of the known technical details.",
    key="RC",
    version="2.0.0",
    values=(
        _UNKNOWN,
        _REASONABLE,
        _CONFIRMED_2,
        NOT_DEFINED_X,
    ),
)
"""
Replaces Unconfirmed and Uncorroborated with Unknown and Reasonable. Updated Confirmed. Retains Not Defined.
"""


VERSIONS = (
    REPORT_CONFIDENCE_1,
    REPORT_CONFIDENCE_1_1,
    REPORT_CONFIDENCE_2,
)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
