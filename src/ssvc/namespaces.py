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


# from https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html
BCP_47_PATTERN = r"(([A-Za-z]{2,3}(-[A-Za-z]{3}(-[A-Za-z]{3}){0,2})?|[A-Za-z]{4,8})(-[A-Za-z]{4})?(-([A-Za-z]{2}|[0-9]{3}))?(-([A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(-[A-WY-Za-wy-z0-9](-[A-Za-z0-9]{2,8})+)*(-[Xx](-[A-Za-z0-9]{1,8})+)?|[Xx](-[A-Za-z0-9]{1,8})+|[Ii]-[Dd][Ee][Ff][Aa][Uu][Ll][Tt]|[Ii]-[Mm][Ii][Nn][Gg][Oo])"

LENGTH_CHECK_PATTERN = rf"(?=.{{{MIN_NS_LENGTH},{MAX_NS_LENGTH}}}$)"
"""Ensures the string is between MIN_NS_LENGTH and MAX_NS_LENGTH characters long."""

# Base namespace part (before any extensions) allows . and - with restrictions
BASE_PATTERN = (
    r"(?!.*[.-]{2,})"  # no consecutive separators
    r"[a-z][a-z0-9]{2,}"  # first part starts with a letter, followed by one or more alphanumeric characters
    r"(?:[.-][a-z0-9]+)*"  # remaining parts can have alphanumeric characters and single . or - separators
)

X_PFX = "x_"
EXPERIMENTAL_BASE = rf"{X_PFX}{BASE_PATTERN}"
BASE_NS_PATTERN = rf"({EXPERIMENTAL_BASE}|{BASE_PATTERN})"

# Extension segment pattern (alphanumeric + limited punctuation, no consecutive punctuation, ends with alphanumeric)
EXT_SEGMENT_PATTERN = (
    r"(?!.*[.-]{2,})"  # no consecutive separators
    r"[a-zA-Z0-9]+"  # first part starts with a letter, followed by one or more alphanumeric characters
    r"(?:[.-][a-zA-Z0-9]+)*"  # remaining parts can have alphanumeric characters and single ., -, / separators
)

# Language extension pattern (BCP-47 or empty for //)
LANG_EXT_PATTERN = rf"(/({BCP_47_PATTERN})|/)"

# Subsequent extension segments
SUBSEQUENT_EXT_PATTERN = rf"(/{EXT_SEGMENT_PATTERN})*"

# Complete pattern with length validation
NS_PATTERN = re.compile(
    rf"^{LENGTH_CHECK_PATTERN}{BASE_NS_PATTERN}({LANG_EXT_PATTERN}{SUBSEQUENT_EXT_PATTERN})?$"
)
f"""The regular expression pattern for validating namespaces.

!!! note "Namespace Validation Rules"

    Namespace values must 
    
    - be {MIN_NS_LENGTH}-{MAX_NS_LENGTH} characters long
    - optionally start with the experimental/private prefix `{X_PFX}`
    - after the optional experimental/private prefix, they must:
        - start with a letter
        - contain at least 3 alphanumeric characters (longer is permitted)
        - contain only lowercase alphanumeric characters and limited punctuation characters (`.`, `-`)
    - extensions are supported and optional, and are delineated by slashes (`/`)
    - more than one extension segment is allowed, however:
        - the first extension segment, if present, is reserved for a BCP-47 language tag, otherwise it must be empty
        - if no BCP-47 tag is present, the first extension segment must be empty (i.e., `//`)
        - double slashes (`//`) are *only* permitted in the *first segment* to indicate no BCP-47 tag
    - beyond the first extension segment, subsequent segments must:
        - contain only alphanumeric characters and limited punctuation characters (`.`, `-`)
        - have only one punctuation character in a row (no double dashes or dots)
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
