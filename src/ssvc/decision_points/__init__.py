#!/usr/bin/env python
"""
The ssvc.decision_points package provides a set of decision points for use in SSVC decision functions.

Decision points are the basic building blocks of SSVC decision functions. Individual decision points describe a
single aspect of the input to a decision function. Decision points should have the following characteristics:

- A name or label
- A description
- A version (a semantic version string)
- A namespace (a short, unique string): For example, "ssvc" or "cvss" to indicate the source of the decision point
- A key (a short, unique string) that can be used to identify the decision point in a shorthand way
- A short enumeration of possible values

In turn, each value should have the following characteristics:
- A name or label
- A description
- A key (a short, unique string) that can be used to identify the value in a shorthand way
"""
from .base import SsvcDecisionPoint, SsvcDecisionPointValue
