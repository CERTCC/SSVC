#!/usr/bin/env python
"""
Provides outcome group and outcome value classes for SSVC.
"""
from dataclasses import dataclass
from typing import Tuple

from dataclasses_json import dataclass_json

from ssvc._mixins import _Base, _Keyed


@dataclass_json
@dataclass(kw_only=True)
class OutcomeValue(_Base, _Keyed):
    """
    Models a single value option for an SSVC outcome.
    """


@dataclass_json
@dataclass(kw_only=True)
class OutcomeGroup(_Base):
    """
    Models an outcome group.
    """

    outcomes: Tuple[OutcomeValue]

    def __iter__(self):
        """
        Allow iteration over the outcomes in the group.
        """
        return iter(self.outcomes)

    # register all instances
