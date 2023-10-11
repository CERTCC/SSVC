#!/usr/bin/env python
"""
file: _basics
author: adh
created_at: 9/20/23 4:51 PM
"""
from dataclasses import dataclass,field

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass(kw_only=True)
class _Versioned:
    """
    Mixin class for versioned SSVC objects.
    """

    version: str = field(default = "0.0.0", metadata = {'description': 'Version (a semantic version string) that identifies this object'})


@dataclass_json
@dataclass(kw_only=True)
class _Namespaced:
    """
    Mixin class for namespaced SSVC objects.
    """

    namespace: str = field(default = "ssvc", metadata = {'description': 'Namespace (a short, unique string): For example, "ssvc" or "cvss" to indicate the source of the decision point'})


@dataclass_json
@dataclass(kw_only=True)
class _Keyed:
    """
    Mixin class for keyed SSVC objects.
    """

    key: str = field(metadata = {'description': 'A key (a short, unique string) that can be used to identify the Decision Point/Decision Point value in a shorthand way'})


@dataclass_json
@dataclass(kw_only=True)
class _Base:
    """
    Base class for SSVC objects.
    """

    name: str = field(metadata = {'description': 'A short label that captures the description of the Decision Point or the Group of Decision Points.'})
    description: str = field(metadata = {'description': 'Description of the Decision Point or the Group of Decision Points.'})


def main():
    pass


if __name__ == "__main__":
    main()
