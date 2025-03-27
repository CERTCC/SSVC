#!/usr/bin/env python

"""
Defines the formatting for SSVC Decision Points.
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

import logging

from pydantic import BaseModel

from ssvc._mixins import _Base, _Keyed, _Namespaced, _Valued, _Versioned
from ssvc.namespaces import NameSpace

logger = logging.getLogger(__name__)


_RDP = {}
REGISTERED_DECISION_POINTS = []


def register(dp):
    """
    Register a decision point.
    """
    global _RDP

    key = (dp.namespace, dp.name, dp.key, dp.version)

    if key in _RDP:
        logger.warning(f"Duplicate decision point {key}")

    _RDP[key] = dp
    REGISTERED_DECISION_POINTS.append(dp)


def _reset_registered():
    """
    Reset the registered decision points.
    """
    global _RDP
    global REGISTERED_DECISION_POINTS

    _RDP = {}
    REGISTERED_DECISION_POINTS = []


class SsvcDecisionPointValue(_Base, _Keyed, BaseModel):
    """
    Models a single value option for a decision point.
    """


class SsvcDecisionPoint(_Valued, _Keyed, _Versioned, _Namespaced, _Base, BaseModel):
    """
    Models a single decision point as a list of values.
    """

    namespace: str = NameSpace.SSVC
    values: tuple[SsvcDecisionPointValue, ...]

    def __iter__(self):
        """
        Allow iteration over the decision points in the group.
        """
        return iter(self.values)

    def __init__(self, **data):
        super().__init__(**data)
        register(self)

    def __post_init__(self):
        register(self)


def main():
    opt_none = SsvcDecisionPointValue(
        name="None", key="N", description="No exploit available"
    )
    opt_poc = SsvcDecisionPointValue(
        name="PoC", key="P", description="Proof of concept exploit available"
    )
    opt_active = SsvcDecisionPointValue(
        name="Active", key="A", description="Active exploitation observed"
    )
    opts = [opt_none, opt_poc, opt_active]

    dp = SsvcDecisionPoint(
        _comment="This is an optional comment that will be included in the object.",
        values=opts,
        name="Exploitation",
        description="Is there an exploit available?",
        key="E",
        version="1.0.0",
    )

    print(dp.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
