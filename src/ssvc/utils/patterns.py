#!/usr/bin/env python
"""
Provides python regular expressions and utility functions for SSVC-related patterns.
"""

#  Copyright (c) 2026 Carnegie Mellon University.
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
from io import StringIO
from pathlib import Path

from abnf_to_regexp.main import run as run_abnf_to_regexp, Params, Format

# from https://semver.org/
VERSION_PATTERN = r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"
"""A regular expression pattern for semantic versioning (semver)."""

# from https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html
BCP_47_PATTERN = r"(([A-Za-z]{2,3}(-[A-Za-z]{3}(-[A-Za-z]{3}){0,2})?|[A-Za-z]{4,8})(-[A-Za-z]{4})?(-([A-Za-z]{2}|[0-9]{3}))?(-([A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(-[A-WY-Za-wy-z0-9](-[A-Za-z0-9]{2,8})+)*(-[Xx](-[A-Za-z0-9]{1,8})+)?|[Xx](-[A-Za-z0-9]{1,8})+|[Ii]-[Dd][Ee][Ff][Aa][Uu][Ll][Tt]|[Ii]-[Mm][Ii][Nn][Gg][Oo])"
"""A regular expression pattern for BCP-47 language tags."""


# --- Namespace Regex Components ---

# --- Length constraint ---
LENGTH_CHECK_PATTERN = r"(?=.{3,1000}$)"


# use abnf-to-regexp as library to catch the output str of the equivalent of
#  abnf-to-regexp --format python-nested -i ssvc_namespace_pattern.abnf
# and execute it as python code

_abnf_python_code = StringIO()
_err = StringIO()
_input_pth = Path(__file__).parent / "ssvc_namespace_pattern.abnf"
_params = Params(
    input_path=_input_pth,
    output_path=None,
    fmt=Format.PYTHON_NESTED,
)

if (
    run_abnf_to_regexp(params=_params, stdout=_abnf_python_code, stderr=_err)
    > 0
):
    raise RuntimeError(
        f"Reading of {_input_pth} failed with {_err.getvalue()}"
    )

exec(_abnf_python_code.getvalue())

#  we do not need them anymore
del _abnf_python_code
del _err

# --- define base patterns to be compatible with previously existing tests
BASE_PATTERN = ns_core
BASE_NS_PATTERN = base_ns
EXT_SEGMENT_PATTERN = fragment_seg

# --- Combine all parts into the full namespace pattern ---
NS_PATTERN_STR = rf"^{namespace}$"
