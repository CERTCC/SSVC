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

from enum import StrEnum

from ssvc.utils.defaults import MAX_NS_LENGTH, MIN_NS_LENGTH, X_PFX
from ssvc.utils.patterns import NS_PATTERN

EXT_SEP = "/"
FRAG_SEP = "#"

# The following namespace strings are RESERVED and cannot be used
# as the base of a namespace (i.e., before any fragment or extension),
# even if they otherwise meet the pattern requirements.
RESERVED_NS = ("invalid", "x_invalid")


class NameSpace(StrEnum):
    f"""Define the official namespaces for SSVC.

    The namespace value must be one of the members of this enum or start with
    the prefix specified in X_PFX.

    Namespaces must be {MIN_NS_LENGTH}-{MAX_NS_LENGTH} characters long.

    The accepted format is specified in ABNF,
    see file `src/ssvc/utils/ssvc_namespace_pattern.abnf`.

    Example:
        Following are examples of valid and invalid namespace values:

        - `ssvc` is *valid* because it is present in the enum
        - `custom` is *invalid* because it does not start with the experimental prefix and is not in the enum
        - `x_example.test#test` is *valid* because it starts with the experimental prefix and meets the pattern requirements
        - `x_example.test#test/en-US` is *valid* because it starts with the experimental prefix and meets the pattern requirements
        - `x_example.test#te..st` is *invalid* because it has multiple punctuation characters in a row
        - `x_example.test.#test` is *invalid* as the reverse dns does not match
        - `x_example.test#test9` is *valid* because it meets the pattern requirements
    """

    # auto() is used to automatically assign values to the members.
    # when used in a StrEnum, auto() assigns the lowercase name of the member as the value
    SSVC = "ssvc"
    CVSS = "cvss"
    CISA = "cisa"
    BASIC = "basic"
    EXAMPLE = "example"
    TEST = "test"
    NIST = "nist"

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
        valid = NS_PATTERN.match(value)

        if valid:
            # pattern matches, so we can proceed with further checks
            # partition always returns three parts: the part before the separator, the separator itself, and the part after the separator
            (base_ns, _, extension) = value.partition(EXT_SEP)
            # and we don't care about the extension beyond the pattern match above
            # so base_ns is either the full value or the part before the first slash

            # but base_ns might have a fragment
            # so we need to split that off if present
            # because partition always returns three parts, we can ignore the second and third parts here
            if "#" in base_ns:
                (base_ns, _, _) = base_ns.partition(FRAG_SEP)

            # reject reserved namespaces
            if base_ns in RESERVED_NS:
                raise ValueError(f"Invalid namespace: '{value}' is reserved.")

            if base_ns in cls.__members__.values():
                # base_ns is a registered namespaces
                return value

            elif base_ns.startswith(X_PFX):
                # base_ns might start with x_
                return value

        # if you got here, the value is not a valid namespace
        raise ValueError(
            f"Invalid namespace: '{value}' Must be one of {[ns.value for ns in cls]} or start with '{X_PFX}'."
        )


def main():
    for ns in NameSpace:
        print(ns)


if __name__ == "__main__":
    main()
