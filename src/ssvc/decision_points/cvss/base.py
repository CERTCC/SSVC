#!/usr/bin/env python
"""
Provides a base class for modeling CVSS vector metrics as SSVC decision points.
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
