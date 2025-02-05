#!/usr/bin/env python

"""
Provides helper functions for working with SSVC decision points.
"""
#  Copyright (c) 2024-2025 Carnegie Mellon University and Contributors.
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

from typing import Sequence

from ssvc.decision_points import SsvcDecisionPoint


#  Copyright (c) 2023 Carnegie Mellon University and Contributors.
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


def dp_diff(dp1: SsvcDecisionPoint, dp2: SsvcDecisionPoint) -> list[str]:
    """
    Compares two decision points and returns a list of differences.

    Args:
        dp1: the first decision point to compare
        dp2: the second decision point to compare

    Returns:
        A list of differences between the two decision points
    """

    major = False
    maybe_major = False
    minor = False
    maybe_minor = False
    patch = False

    diffs = []

    name_change = False
    desc_change = False
    key_change = False

    # did the name change?
    if dp1.name != dp2.name:
        name_change = True

        # was it a big change?
        from thefuzz import fuzz

        # fuzz ratio is 100 when exact match, 0 when no match
        if fuzz.ratio(dp1.name, dp2.name) < 50:
            diffs.append(f"(minor) {dp2.name} name changed from {dp1.name}")
            minor = True
        else:
            diffs.append(
                f"(patch / maybe minor) {dp2.name} name changed from {dp1.name}"
            )
            # It was a small change so maybe minor but probably patch
            patch = True
            maybe_minor = True

    # did the description change?
    desc1 = dp1.description.strip()
    desc2 = dp2.description.strip()

    if desc1 != desc2:
        diffs.append(f"(patch) {dp2.name} v{dp2.version} description changed")
        patch = True
        desc_change = True
    else:
        diffs.append(f"{dp2.name} v{dp2.version} description did not change")

    # did the key change?
    key1 = dp1.key.strip()
    key2 = dp2.key.strip()

    if key1 != key2:
        diffs.append(f"(major) {dp2.name} v{dp2.version} key changed")
        major = True
        key_change = True
    else:
        diffs.append(f"{dp2.name} v{dp2.version} key did not change")

    maybe_new_obj = all([name_change, desc_change, key_change])

    # did the version change?
    version1 = dp1.version.strip()
    version2 = dp2.version.strip()

    if version1 != version2:
        diffs.append(f"{dp2.name} v{version2} version changed from {version1}")
    else:
        diffs.append(f"{dp2.name} version did not change")

    # did the values change?
    # did the value names change?
    dp1_names = set([v.name for v in dp1.values])
    dp2_names = set([v.name for v in dp2.values])

    intersection = dp1_names.intersection(dp2_names)

    if dp1_names == dp2_names:
        diffs.append(f"{dp2.name} v{dp2.version} value names did not change")

    # names removed from dp1 in dp2:
    for name in dp1_names.difference(dp2_names):
        diffs.append(f"(major) {dp2.name} v{dp2.version} removes value {name}")
        major = True

    for name in dp2_names.difference(dp1_names):
        diffs.append(
            f"(major or minor) {dp2.name} v{dp2.version} adds value {name}"
        )
        maybe_major = True
        maybe_minor = True

    # did the value keys change?
    for name in intersection:
        v1 = {
            value["name"]: value["key"] for value in dp1.model_dump()["values"]
        }
        v1 = v1[name]

        v2 = {
            value["name"]: value["key"] for value in dp2.model_dump()["values"]
        }
        v2 = v2[name]

        if v1 != v2:
            diffs.append(
                f"(minor) {dp2.name} v{dp2.version} value {name} key changed"
            )
            minor = True
        else:
            diffs.append(
                f"{dp2.name} v{dp2.version} value {name} key did not change"
            )

    # did the value descriptions change?
    for name in intersection:
        v1 = {
            value["name"]: value["description"]
            for value in dp1.model_dump()["values"]
        }
        v1 = v1[name]

        v2 = {
            value["name"]: value["description"]
            for value in dp2.model_dump()["values"]
        }
        v2 = v2[name]

        if v1 != v2:
            diffs.append(
                f"(patch) {dp2.name} v{dp2.version} value {name} description changed"
            )
            patch = True
        else:
            diffs.append(
                f"{dp2.name} v{dp2.version} value {name} description did not change"
            )

    if major:
        diffs.append(f"{dp2.name} v{dp2.version} appears to be a major change")
    elif minor:
        diffs.append(f"{dp2.name} v{dp2.version} appears to be a minor change")
    elif patch:
        diffs.append(f"{dp2.name} v{dp2.version} appears to be a patch change")

    if maybe_new_obj:
        diffs.append(
            f"(maybe_new_obj) {dp2.name} v{dp2.version} changed name, description, and key. Potentially new object "
            f"depending on context."
        )

    if not major:
        if maybe_major:
            diffs.append(
                f"{dp2.name} v{dp2.version} could be a major change depending on context"
            )
        if maybe_minor:
            diffs.append(
                f"{dp2.name} v{dp2.version} could be a minor change depending on context"
            )

    if not any([major, minor, patch, maybe_major, maybe_minor]):
        diffs.append(f"{dp2.name} v{dp2.version} appears to be a no-op change")

    return diffs


def show_diffs(versions: Sequence[SsvcDecisionPoint]) -> None:
    if len(versions) < 2:
        print("Not enough versions to compare")
        return

    for a, b in zip(versions[:-1], versions[1:]):
        diff = dp_diff(a, b)
        print("\n".join(diff))
        print()


def print_versions_and_diffs(versions: Sequence[SsvcDecisionPoint]) -> None:
    """
    Prints the json representation of each version and then shows the diffs between each version.

    Args:
        versions: a list of decision point versions

    Returns:
        None
    """
    for version in versions:
        print(version.model_dump_json(indent=2))
    show_diffs(versions)


def main():
    pass


if __name__ == "__main__":
    main()
