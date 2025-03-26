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

X_PFX = "x_"
"""The prefix for extension namespaces. Extension namespaces must start with this prefix."""

# pattern to match
# `(?=.{3,25}$)`: 3-25 characters long
# `^(x_)`: `x_` prefix is optional
# `[a-z0-9]{3,4}`:  must start with 3-4 alphanumeric characters
# `[/.-]?`: only one punctuation character is allowed between alphanumeric characters
# `[a-z0-9]+`: at least one alphanumeric character is required after the punctuation character
# `([/.-]?[a-z0-9]+){0,22}`: zero to 22 occurrences of the punctuation character followed by at least one alphanumeric character
# (note that the total limit will kick in at or before this point)
# `$`: end of the string
NS_PATTERN = re.compile(r"^(?=.{3,25}$)(x_)?[a-z0-9]{3}([/.-]?[a-z0-9]+){0,22}$")
"""The regular expression pattern for validating namespaces.

Note: 
    Namespace values must 
    
    - be 3-25 characters long
    - contain only lowercase alphanumeric characters and limited punctuation characters (`/`,`.` and `-`)
    - have only one punctuation character in a row
    - start with 3-4 alphanumeric characters after the optional extension prefix
    - end with an alphanumeric character
    
    See examples in the `NameSpace` enum.
"""


class NameSpace(StrEnum):
    """
    Defines the official namespaces for SSVC.

    The namespace value must be one of the members of this enum or start with the prefix specified in X_PFX.
    Namespaces must be 3-25 lowercase characters long and must start with 3-4 alphanumeric characters after the optional prefix.
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
