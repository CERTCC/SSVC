#!/usr/bin/env python
"""
This module provides mixin classes for adding features to SSVC objects.
"""
#  Copyright (c) 2023-2025 Carnegie Mellon University and Contributors.
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

from typing import Optional

from pydantic import BaseModel, ConfigDict

from . import _schemaVersion


class _Versioned(BaseModel):
    """
    Mixin class for versioned SSVC objects.
    """

    version: str = "0.0.0"
    schemaVersion: str = _schemaVersion


class _Namespaced(BaseModel):
    """
    Mixin class for namespaced SSVC objects.
    """

    namespace: str = "ssvc"


class _Keyed(BaseModel):
    """
    Mixin class for keyed SSVC objects.
    """

    key: str


def exclude_if_none(value):
    return value is None


class _Commented(BaseModel):
    """
    Mixin class for commented SSVC objects.
    """

    _comment: Optional[str] = None

    model_config = ConfigDict(json_encoders={Optional[str]: exclude_if_none})


class _Base(BaseModel):
    """
    Base class for SSVC objects.
    """

    name: str
    description: str


def main():
    pass


if __name__ == "__main__":
    main()
