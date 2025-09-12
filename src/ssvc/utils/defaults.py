#!/usr/bin/env python
"""
Provides default values and constants for use in SSVC objects.
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

DEFAULT_VERSION = "0.0.1"
"""The default version for SSVC objects, used when no version is specified at object creation."""

X_PFX = "x_"
"""The prefix for extension namespaces. Extension namespaces must start with this prefix."""

MIN_NS_LENGTH = 3
"""The minimum length of a namespace string."""

MAX_NS_LENGTH = 1000
"""The maximum length of a namespace string."""

NS_LENGTH_INTERVAL = MAX_NS_LENGTH - MIN_NS_LENGTH
"""The interval between the minimum and maximum lengths of a namespace string."""

FIELD_DELIMITER = ":"
"""The delimiter used to separate fields in SSVC object IDs."""

SCHEMA_ORDER = (
    "title",
    "$schema",
    "$id",
    "description",
    "schemaVersion",
    "type",
    "$defs",
    "properties",
    "required",
    "additionalProperties",
)
"""Preferred order of fields in SSVC JSON Schema objects."""


SCHEMA_VERSION = "2.0.0"

SCHEMA_BASE_URL = "https://certcc.github.io/SSVC/data/schema/"

IMPORTABLES = [
    "ssvc.decision_points",
    "ssvc.outcomes",
    "ssvc.decision_tables",
    "ssvc.dp_groups",
]


def main():
    pass


if __name__ == "__main__":
    main()
