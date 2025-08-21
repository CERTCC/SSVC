#!/usr/bin/env python
"""
Provides custom data types for use in SSVC objects.
"""

#  Copyright (c) 2025 Carnegie Mellon University.
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

from typing import Annotated

from pydantic import Field

from ssvc.utils.defaults import MAX_NS_LENGTH, MIN_NS_LENGTH
from ssvc.utils.patterns import NS_PATTERN, VERSION_PATTERN

VersionString = Annotated[
    str,
    Field(
        description="The version of the SSVC object. This must be a valid semantic version string.",
        examples=["1.0.0", "2.1.3"],
        pattern=VERSION_PATTERN,
        min_length=5,
    ),
]
"""A string datatype for version values, for use in Pydantic models."""

NamespaceString = Annotated[
    str,
    Field(
        description="The namespace of the SSVC object.",
        examples=[
            "ssvc",
            "cisa",
            "x_example.test#test//.example.test#private-extension",
            "ssvc/de-DE/.example.organization#reference-arch-1",
        ],
        pattern=NS_PATTERN,
        min_length=MIN_NS_LENGTH,
        max_length=MAX_NS_LENGTH,
    ),
]
"""A string datatype for namespace values, for use in Pydantic models."""

TargetIdList = Annotated[list[str], Field(min_length=1)]
"""A list of target IDs, for use in Pydantic models."""

DecisionPointDict = Annotated[
    dict[str, "DecisionPoint"],
    Field(
        ...,
        description="A non-empty dictionary of decision points Decision point IDs are recommended as keys.",
        min_length=1,
    ),
]
"""A dictionary of decision points, for use in Pydantic models."""


def main():
    pass


if __name__ == "__main__":
    main()
