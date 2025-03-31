#!/usr/bin/env python
"""
file: md_gen
author: adh
created_at: 2/17/25 4:25 PM
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

import os


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


def cutfname(fname):
    # foo_bar_1_0_0 -> foo_bar
    parts = fname.split("_")
    parts_ = []

    for part in parts:
        if part.isnumeric():
            break
        parts_.append(part)

    return "_".join(parts_)


PAGE_TOP_TEMPLATE = """# {dp_name}

```python exec="true" idprefix=""
from ssvc.decision_points.cvss.{module} import LATEST
from ssvc.doc_helpers import example_block

print(example_block(LATEST))
```
"""

PAGE_BOTTOM_TEMPLATE = """## Previous Versions

```python exec="true" idprefix=""
from ssvc.decision_points.cvss.{module} import VERSIONS
from ssvc.doc_helpers import example_block

versions = VERSIONS[:-1]
for version in versions:
    print(example_block(version))
    print("\\n---\\n")
```
"""


def snake_to_title(s):
    return " ".join([w.capitalize() for w in s.split("_")])


def main():
    # add overwrite command line argument
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate decision point documentation"
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="overwrite existing files",
        default=False,
    )

    parser.add_argument(
        "--outdir",
        help="output directory",
        default="../../docs/reference/decision_points/cvss",
    )

    parser.add_argument(
        "--jsondir",
        help="json directory",
        default="../../data/json/decision_points/cvss",
    )

    args = parser.parse_args()

    json_dir = args.jsondir
    json_files = sorted(os.listdir(json_dir))
    print(json_files)

    dp_fnames = sorted(list(set([cutfname(f) for f in json_files])))
    print(dp_fnames)

    md_dir = args.outdir
    os.makedirs(md_dir, exist_ok=True)

    for dp_fname in dp_fnames:

        fname = dp_fname + ".md"
        path = os.path.join(md_dir, fname)

        if os.path.exists(path):
            if not args.overwrite:
                # skip if file already exists
                continue
            else:
                os.remove(path)

        # does the module exist?
        module = f"ssvc.decision_points.cvss.{dp_fname}"
        try:
            # try to import the module
            mod = __import__(module)
            print(f"Module {mod} exists")
        except ImportError:
            print(f"Module {module} does not exist")
            continue

        with open(os.path.join(md_dir, fname), "w") as f:
            f.write(
                PAGE_TOP_TEMPLATE.format(
                    dp_name=snake_to_title(dp_fname), module=dp_fname
                )
            )
            f.write("\n")
            if len(mod.VERSIONS) > 1:
                f.write("\n")
                f.write(PAGE_BOTTOM_TEMPLATE.format(module=dp_fname))
                f.write("\n")

    pass


if __name__ == "__main__":
    main()
