#!/usr/bin/env python
"""
file: cvss_dp
author: adh
created_at: 9/20/23 12:08 PM
"""


from dataclasses import dataclass
from dataclasses_json import dataclass_json

from ssvc.decision_points.base import SsvcDecisionPoint


@dataclass_json
@dataclass(kw_only=True)
class CvssDecisionPoint(SsvcDecisionPoint):
    """
    Models a single CVSS decision point as a list of values.
    """

    namespace: str = "cvss"
