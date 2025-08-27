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


# fmt: off
# --- the following section is generated with
#  abnf-to-regexp --format python-nested -i ssvc_namespace_pattern.abnf | \
#    sed 's/{,/{0,/g'
alnum = '[a-zA-Z0-9]'
lower = '[a-z]'
alnumlow = f'({lower}|[0-9])'
dash = '-'
alnumlowdash = f'({alnumlow}|{dash})'
label = f'{alnumlow}(({alnumlowdash}){{0,61}}{alnumlow})?'
reverse_dns = f'{label}(\\.{label})+'
dot = '\\.'
specialchar = f'({dot}|{dash})'
fragment_seg = f'({alnumlow})+({specialchar}({alnumlow})+)*'
x_name = f'{reverse_dns}\\#{fragment_seg}'
x_base = f'x_{x_name}'
ns_core = f'{lower}{alnumlow}(({specialchar})?({alnumlow})+)+'
reg_base = f'{ns_core}(\\#{fragment_seg})?'
base_ns = f'({x_base}|{reg_base})'
singleton = '[0-9A-WY-Za-wy-z]'
bcp47 = (
    '(([a-zA-Z]{2,3}(-[a-zA-Z]{3}(-[a-zA-Z]{3}){0,2})?|[a-z'
    'A-Z]{4,8})(-[a-zA-Z]{4})?(-([a-zA-Z]{2}|[0-9]{3}))?(-'
    f'(({alnum}){{5,8}}|[0-9]({alnum}){{3}}))*(-{singleton}(-'
    f'({alnum}){{2,8}})+)*(-[xX](-({alnum}){{2,8}})+)?|[xX](-'
    f'({alnum}){{2,8}})+|i-default|i-mingo)'
)
translation = f'\\.({reverse_dns}|{x_name})\\${bcp47}'
ext_seg = f'({bcp47}|\\.{x_name}|{translation})'
lang_ext = f'(/|/{bcp47})'
extensions = f'{lang_ext}((/{ext_seg})+)?'
namespace = f'{base_ns}({extensions})?'
# --- end of generated output
# fmt: on

# --- define base patterns to be compatible with previously existing tests
BASE_PATTERN = ns_core
BASE_NS_PATTERN = base_ns
EXT_SEGMENT_PATTERN = fragment_seg

# --- Combine all parts into the full namespace pattern ---
NS_PATTERN_STR = rf"^{LENGTH_CHECK_PATTERN}" rf"{namespace}$"

NS_PATTERN = re.compile(NS_PATTERN_STR)
