#!/usr/bin/env python
"""
Provides python regular expressions and utility functions for SSVC-related patterns.
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

from ssvc.utils.defaults import MAX_NS_LENGTH, MIN_NS_LENGTH, X_PFX

# from https://semver.org/
VERSION_PATTERN = r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"
"""A regular expression pattern for semantic versioning (semver)."""

# from https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html
BCP_47_PATTERN = r"(([A-Za-z]{2,3}(-[A-Za-z]{3}(-[A-Za-z]{3}){0,2})?|[A-Za-z]{4,8})(-[A-Za-z]{4})?(-([A-Za-z]{2}|[0-9]{3}))?(-([A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(-[A-WY-Za-wy-z0-9](-[A-Za-z0-9]{2,8})+)*(-[Xx](-[A-Za-z0-9]{1,8})+)?|[Xx](-[A-Za-z0-9]{1,8})+|[Ii]-[Dd][Ee][Ff][Aa][Uu][Ll][Tt]|[Ii]-[Mm][Ii][Nn][Gg][Oo])"
"""A regular expression pattern for BCP-47 language tags."""


# --- Namespace Regex Components ---

# Length check
LENGTH_CHECK_PATTERN = rf"(?=.{{{MIN_NS_LENGTH},{MAX_NS_LENGTH}}}$)"
"""Ensures the string is between MIN_NS_LENGTH and MAX_NS_LENGTH characters long."""

# Base namespace pattern (before any // or /lang/)
BASE_PATTERN = (
    r"(?!.*[.-]{2,})"  # no consecutive separators
    r"[a-z][a-z0-9]+"  # starts with a letter, followed by one or more alphanumeric chars
    r"(?:[.-][a-z0-9]+)*"  # then . or - followed by alphanumerics
)
"""The base pattern for namespaces."""

EXPERIMENTAL_BASE = rf"{X_PFX}{BASE_PATTERN}"
"""The base pattern for experimental namespaces with the x_ prefix."""

BASE_NS_PATTERN = rf"(?:{EXPERIMENTAL_BASE}|{BASE_PATTERN})"
"""The complete base namespace pattern."""

# --- Extension Segments ---

# Single extension segment between slashes.
# Requirements:
#   - Starts with a letter
#   - May contain '.', '-', or '#' as separators
#   - No consecutive '.' or '-'
#   - At most one '#'
EXT_SEGMENT_PATTERN = (
    r"(?!.*#.*#)"  # at most one hash
    r"(?!.*[.-]{2,})"  # no consecutive dots or hyphens
    r"[a-zA-Z][a-zA-Z0-9]*"  # must start with a letter
    r"(?:[.#-][a-zA-Z0-9]+)*"  # allowed separators with alphanumerics
)
"""The pattern for a single extension segment."""

# Language extension pattern: either // or /<BCP_47>/
LANG_EXT_PATTERN = rf"(?:/{BCP_47_PATTERN}/|//)"
"""The first extension segment, either empty (//) or a valid BCP-47 tag."""

# Subsequent extension segments (zero or more)
SUBSEQUENT_EXT_PATTERN = rf"{EXT_SEGMENT_PATTERN}(?:/{EXT_SEGMENT_PATTERN})*"
"""The pattern for all subsequent extension segments."""

# --- Full Namespace Pattern ---
NS_PATTERN = re.compile(
    rf"^{LENGTH_CHECK_PATTERN}{BASE_NS_PATTERN}(?:{LANG_EXT_PATTERN}{SUBSEQUENT_EXT_PATTERN})?$"
)
f"""The full regular expression pattern for validating namespaces.

!!! note "Length Requirements"

    - Namespaces must be between {MIN_NS_LENGTH} and {MAX_NS_LENGTH} characters long.

!!! note "Base Namespace Requirements"

    - Must start with a lowercase letter
    - Must contain at least 3 total characters in the base part (after the optional experimental/private prefix)
    - Must contain only lowercase letters, numbers, dots (`.`), and hyphens (`-`)
    - Must not contain consecutive dots or hyphens (no `..`, `--`, `.-`, `-.`, `---`, etc.)
    - May optionally start with the experimental/private prefix `{X_PFX}`.

!!! note "Extension Requirements (Optional)"

    - Extensions are optional
    - Extensions must be delineated by slashes (`/`)
    - If any extension segments are present, the following rules apply:
    - The first extension segment, must be a valid BCP-47 language tag or empty (i.e., `//`).
    - Subsequent extension segments:
        - must start with a letter (upper or lowercase)
        - may contain letters, numbers, dots (`.`), and hyphens (`-`)
        - must not start or end with a dot or hyphen
        - must not contain consecutive dots or hyphens (no `..`, `--`, `.-`, `-.`, `---`, etc.)
        - are separated by single forward slashes (`/`)
    - multiple extension segments are allowed

"""


def main():
    pass


if __name__ == "__main__":
    main()
