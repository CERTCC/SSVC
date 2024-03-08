#!/usr/bin/env python
"""
file: _basics
author: adh
created_at: 9/20/23 4:51 PM
"""
#  Copyright (c) 2023 Carnegie Mellon University and Contributors.
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

from dataclasses import dataclass, field
from typing import Optional

from dataclasses_json import config, dataclass_json


@dataclass_json
@dataclass(kw_only=True)
class _Versioned:
    """
    Mixin class for versioned SSVC objects.
    """

    version: str = "0.0.0"


@dataclass_json
@dataclass(kw_only=True)
class _Namespaced:
    """
    Mixin class for namespaced SSVC objects.
    """

    namespace: str = "ssvc"


@dataclass_json
@dataclass(kw_only=True)
class _Keyed:
    """
    Mixin class for keyed SSVC objects.
    """

    key: str


def exclude_if_none(value):
    return value is None


@dataclass_json
@dataclass(kw_only=True)
class _Commented:
    """
    Mixin class for commented SSVC objects.
    """

    _comment: Optional[str] = field(
        default=None, metadata=config(exclude=exclude_if_none)
    )


@dataclass_json
@dataclass(kw_only=True)
class _Base:
    """
    Base class for SSVC objects.
    """

    name: str
    description: str


def main():
    pass


if __name__ == "__main__":
    main()
