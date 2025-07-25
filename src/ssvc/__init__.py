#  Copyright (c) 2023-2025 Carnegie Mellon University.
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
"""
Provides SSVC modules.
"""

# import all submodules from ssvc.decision_points and ssvc.outcomes to populate the registries
# automatically walk through the decision_points and outcomes directories
# dive into each submodule and import all its parts
modules_to_import = [
    "ssvc.decision_points",
    "ssvc.outcomes",
]

# find all the python files in the directories
import pkgutil

# dynamically import all submodules in the specified modules
for module in modules_to_import:
    package = __import__(module, fromlist=["*"])
    for _, submodule_name, _ in pkgutil.walk_packages(
        package.__path__, package.__name__ + "."
    ):
        try:
            __import__(submodule_name, fromlist=["*"])
        except ImportError as e:
            raise ImportError(f"Failed to import submodule {submodule_name}: {e}")


if __name__ == "__main__":
    from ssvc.decision_points.base import DP_REGISTRY

    for key in DP_REGISTRY.keys():
        print(f"Registered Decision Point: {key}")
