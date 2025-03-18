#!/usr/bin/env python
"""
Provides a namespace enum
"""
#  Copyright (c) 2025 Carnegie Mellon University and Contributors.
#  - see Contributors.md for a full list of Contributors
#  - see ContributionInstructions.md for information on how you can Contribute to this project
#  Stakeholder Specific Vulnerability Categorization (SSVC) is
#  licensed under a MIT (SEI)-style license, please see LICENSE.md distributed
#  with this Software or contact permission@sei.cmu.edu for full terms.
#  Created, in part, with funding and support from the United States Government
#  (see Acknowledgments file). This program may include and/or can make use of
#  certain third party source code, object code, documentation and other files
#  (“Third Party Software”). See LICENSE.md for more details.
#  Carnegie Mellon®, CERT® and CERT Coordination Center® are registered in the
#  U.S. Patent and Trademark Office by Carnegie Mellon University

from enum import StrEnum, auto

# extensions / experimental namespaces should start with the following prefix
# this is to avoid conflicts with official namespaces
X_PFX = "x_"


class NameSpace(StrEnum):
    """
    Defines the official namespaces for SSVC.
    """

    # auto() is used to automatically assign values to the members.
    # when used in a StrEnum, auto() assigns the lowercase name of the member as the value
    SSVC = auto()
    CVSS = auto()
    NCISS = auto()


class NamespaceValidator:
    """Custom type for validating namespaces."""

    @classmethod
    def validate(cls, value: str) -> str:
        """
        Validate the namespace value. The value must be one of the official namespaces or start with 'x_'.

        Args:
            value: a string representing a namespace

        Returns:
            the validated namespace value

        Raises:
            ValueError: if the value is not a valid namespace

        """
        if value in NameSpace.__members__.values():
            return value
        if value.startswith(X_PFX):
            return value
        raise ValueError(
            f"Invalid namespace: {value}. Must be one of {[ns.value for ns in NameSpace]} or start with '{X_PFX}'."
        )

    def __get_validators__(cls):
        yield cls.validate


def main():
    for ns in NameSpace:
        print(ns)


if __name__ == "__main__":
    main()
