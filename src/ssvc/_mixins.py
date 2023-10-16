#!/usr/bin/env python
"""
file: _basics
author: adh
created_at: 9/20/23 4:51 PM
"""
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
class _Base:
    """
    Base class for SSVC objects.
    """

    name: str
    description: str
    _comment: Optional[str] = field(
        default=None, metadata=config(exclude=exclude_if_none)
    )


def main():
    pass


if __name__ == "__main__":
    main()
