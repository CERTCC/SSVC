#!/usr/bin/env python
"""
SSVC objects use namespaces to distinguish between objects that arise from different
stakeholders or analytical category sources. This module defines the official namespaces
for SSVC and provides a method to validate namespace values.
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

import re
from enum import StrEnum, auto
from typing import Annotated

from pydantic import Field

X_PFX = "x_"
"""The prefix for extension namespaces. Extension namespaces must start with this prefix."""

MIN_NS_LENGTH = 3
MAX_NS_LENGTH = 1000
NS_LENGTH_INTERVAL = MAX_NS_LENGTH - MIN_NS_LENGTH

LENGTH_CHECK_PATTERN = rf"(?=.{{{MIN_NS_LENGTH},{MAX_NS_LENGTH}}}$)"
"""Ensures the string is between MIN_NS_LENGTH and MAX_NS_LENGTH characters long."""

PREFIX_CHECK_PATTERN = rf"(x_)?[a-z0-9]{{{MIN_NS_LENGTH}}}"
"""Ensures the string starts with an optional prefix followed by at least 3 alphanumeric characters."""

REMAINDER_CHECK_PATTERN = rf"([/.-]?[a-z0-9]+){{0,{NS_LENGTH_INTERVAL}}}$"
"""Ensures that the string contains only lowercase alphanumeric characters and limited punctuation characters (`/`, `.`, `-`),"""


# pattern to match
# NOTE: be careful with this regex. We're using f-strings to insert the min and max lengths, so we need to ensure that
# literal { and } characters are escaped properly (doubled up) so they appear in as single braces in the final regex.
NS_PATTERN = re.compile(
    rf"^{LENGTH_CHECK_PATTERN}{PREFIX_CHECK_PATTERN}{REMAINDER_CHECK_PATTERN}$"
)
f"""The regular expression pattern for validating namespaces.

!!! note "Namespace Validation Rules"

    Namespace values must 
    
    - be {MIN_NS_LENGTH}-{MAX_NS_LENGTH} characters long
    - contain only lowercase alphanumeric characters and limited punctuation characters (`/`,`.` and `-`)
    - have only one punctuation character in a row
    - start with 3 alphanumeric characters after the optional extension prefix
    - end with an alphanumeric character
    
"""

NamespaceString = Annotated[
    str,
    Field(
        description="The namespace of the SSVC object.",
        examples=["ssvc", "cisa", "x_private-test", "ssvc/de-DE/reference-arch-1"],
        pattern=NS_PATTERN,
        min_length=MIN_NS_LENGTH,
        max_length=MAX_NS_LENGTH,
    ),
]
"""A string datatype for namespace values, for use in Pydantic models."""


class NameSpace(StrEnum):
    f"""
    Defines the official namespaces for SSVC.

    The namespace value must be one of the members of this enum or start with the prefix specified in X_PFX.
    Namespaces must be {MIN_NS_LENGTH}-{MAX_NS_LENGTH} lowercase characters long and must start with 3-4 
    alphanumeric characters after the optional prefix.
    Limited punctuation characters (/.-) are allowed between alphanumeric characters, but only one at a time.

    Example:
        Following are examples of valid and invalid namespace values:

        - `ssvc` is *valid* because it is present in the enum
        - `custom` is *invalid* because it does not start with the experimental prefix and is not in the enum
        - `x_custom` is *valid* because it starts with the experimental prefix and meets the pattern requirements
        - `x_custom/extension` is *valid* because it starts with the experimental prefix and meets the pattern requirements
        - `x_custom/extension/with/multiple/segments` is *invalid* because it exceeds the maximum length
        - `x_custom//extension` is *invalid* because it has multiple punctuation characters in a row
        - `x_custom.extension.` is *invalid* because it does not end with an alphanumeric character
        - `x_custom.extension.9` is *valid* because it meets the pattern requirements
    """

    # auto() is used to automatically assign values to the members.
    # when used in a StrEnum, auto() assigns the lowercase name of the member as the value
    SSVC = auto()
    CVSS = auto()
    CISA = auto()

    @classmethod
    def validate(cls, value: str) -> str:
        """
        Validate the namespace value. Valid values are members of the enum or start with the experimental prefix and
        meet the specified pattern requirements.

        Args:
            value: the namespace value to validate

        Returns:
            the validated namespace value

        Raises:
            ValueError: if the value is not a valid namespace

        """
        if value in cls.__members__.values():
            return value
        if value.startswith(X_PFX) and NS_PATTERN.match(value):
            return value
        raise ValueError(
            f"Invalid namespace: {value}. Must be one of {[ns.value for ns in cls]} or start with '{X_PFX}'."
        )


def main():
    for ns in NameSpace:
        print(ns)


if __name__ == "__main__":
    main()
