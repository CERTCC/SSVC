#!/usr/bin/env python
"""
Provides a bulk importer for SSVC object modules.
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

import logging
import pkgutil


logger = logging.getLogger(__name__)

# import all submodules from ssvc.decision_points and ssvc.outcomes to populate the registries
# automatically walk through the decision_points and outcomes directories
# dive into each submodule and import all its parts


def import_module(module_name: str) -> object:
    logger.debug(f"Importing module: {module_name}")
    try:
        package = __import__(module_name, fromlist=["*"])
    except ImportError as e:
        raise ImportError(f"Failed to import submodule {module_name}: {e}")
    return package


def import_modules(modules: list[str], include_children=True) -> list[object]:
    """
    Import specified modules dynamically.

    Args:
        modules (list[str]): List of module names to import.
    """
    packages = []
    for module in modules:
        package = import_module(module)
        packages.append(package)

        if not include_children:
            # If we don't want to include children, just import the top-level module
            # and short-circuit the rest
            continue

        # dynamically import all submodules in the specified modules
        for _, submodule_name, _ in pkgutil.walk_packages(
            package.__path__, package.__name__ + "."
        ):
            subpkg = import_module(submodule_name)
            packages.append(subpkg)

    return packages


def main():
    from ssvc.utils.defaults import IMPORTABLES

    pkgs = import_modules(IMPORTABLES)

    for pkg in pkgs:
        logger.info(f"Imported package: {pkg.__name__}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
