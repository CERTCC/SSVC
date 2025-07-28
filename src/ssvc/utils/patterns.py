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

# from https://semver.org/
VERSION_PATTERN = r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"
"""A regular expression pattern for semantic versioning (semver)."""

# from https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html
BCP_47_PATTERN = r"(([A-Za-z]{2,3}(-[A-Za-z]{3}(-[A-Za-z]{3}){0,2})?|[A-Za-z]{4,8})(-[A-Za-z]{4})?(-([A-Za-z]{2}|[0-9]{3}))?(-([A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(-[A-WY-Za-wy-z0-9](-[A-Za-z0-9]{2,8})+)*(-[Xx](-[A-Za-z0-9]{1,8})+)?|[Xx](-[A-Za-z0-9]{1,8})+|[Ii]-[Dd][Ee][Ff][Aa][Uu][Ll][Tt]|[Ii]-[Mm][Ii][Nn][Gg][Oo])"
"""A regular expression pattern for BCP-47 language tags."""


# --- Namespace Regex Components ---

# --- Length constraint ---
LENGTH_CHECK_PATTERN = r"(?=.{3,1000}$)"

# --- Base namespace ---
NO_CONSECUTIVE_SEP = r"(?!.*[.-]{2,})"  # no consecutive '.' or '-'

BASE_PATTERN = (
    rf"{NO_CONSECUTIVE_SEP}"
    r"[a-z][a-z0-9]+"  # starts with lowercase letter + 1+ alnum
    r"(?:[.-][a-z0-9]+)*"  # optional dot or dash + alnum
)

BASE_NS_PATTERN = rf"(?:x_{BASE_PATTERN}|{BASE_PATTERN})"

# --- Extension segments ---
# A single ext-seg with at most one '#'
EXT_SEGMENT_PATTERN = (
    rf"{NO_CONSECUTIVE_SEP}"
    r"[a-zA-Z][a-zA-Z0-9]*"  # start with a letter
    r"(?:[.-][a-zA-Z0-9]+)*"  # dot or dash + alnum
    r"(?:#[a-zA-Z0-9]+(?:[.-][a-zA-Z0-9]+)*)?"  # optional single hash section
)

# Subsequent ext-seg(s)
SUBSEQUENT_EXT = rf"{EXT_SEGMENT_PATTERN}(?:/{EXT_SEGMENT_PATTERN})*"


# --- Language extension ---
LANG_EXT = rf"(?:/{BCP_47_PATTERN}/|//)"

# --- Combine all parts into the full namespace pattern ---
NS_PATTERN_STR = (
    rf"^{LENGTH_CHECK_PATTERN}"
    rf"{BASE_NS_PATTERN}"
    rf"(?:{LANG_EXT}{SUBSEQUENT_EXT})?$"
)

# Compile the regex with verbose flag for readability (if needed)
NS_PATTERN = re.compile(NS_PATTERN_STR)


def main():
    pass


if __name__ == "__main__":
    main()
