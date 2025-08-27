#!/usr/bin/env python

"""
Provides helper functions for working with SSVC decision points.
"""
#  Copyright (c) 2024-2025 Carnegie Mellon University.
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

from typing import Sequence

import semver

from ssvc.decision_points.base import DecisionPoint


def dp_diff(dp1: DecisionPoint, dp2: DecisionPoint) -> list[str]:
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
    desc1 = dp1.definition.strip()
    desc2 = dp2.definition.strip()

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
            value["name"]: value["definition"]
            for value in dp1.model_dump()["values"]
        }
        v1 = v1[name]

        v2 = {
            value["name"]: value["definition"]
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

    v1 = semver.VersionInfo.parse(dp1.version)
    v2 = semver.VersionInfo.parse(dp2.version)

    if major:
        diffs.append(f"{dp2.name} v{dp2.version} appears to be a major change")
        expected = v1.bump_major()
        if v2 != expected:
            diffs.append(
                f"Expected version to be bumped to {expected}, but was bumped to {v2}"
            )
    elif minor:
        diffs.append(f"{dp2.name} v{dp2.version} appears to be a minor change")
        expected = v1.bump_minor()
        if v2 != expected:
            diffs.append(
                f"Expected version to be bumped to {expected}, but was bumped to {v2}"
            )
    elif patch and not any([maybe_minor, maybe_major]):
        diffs.append(f"{dp2.name} v{dp2.version} appears to be a patch change")
        expected = v1.bump_patch()
        if v2 != expected:
            diffs.append(
                f"Expected version to be bumped to {expected}, but was bumped to {v2}"
            )

    if maybe_new_obj:
        diffs.append(
            f"(maybe_new_obj) {dp2.name} v{dp2.version} changed name, description, and key. Potentially new object "
            f"depending on context."
        )

    if not major:
        check_possible = False
        possible1 = v1.bump_major()
        possible2 = v1.bump_minor()
        if maybe_major:
            diffs.append(
                f"{dp2.name} v{dp2.version} could be a major change ({v1} -> {possible1}) depending on context"
            )
            check_possible = True
        if maybe_minor:
            diffs.append(
                f"{dp2.name} v{dp2.version} could be a minor change ({v1} -> {possible2}) depending on context"
            )
            check_possible = True
        # did one of possible1 or possible2 match v2?
        if check_possible and v2 not in [possible1, possible2]:
            diffs.append(
                f"Expected version to be bumped to {possible1} or {possible2}, but was bumped to {v2}"
            )

    if not any([major, minor, patch, maybe_major, maybe_minor]):
        diffs.append(f"{dp2.name} v{dp2.version} appears to be a no-op change")

    return diffs


def show_diffs(versions: Sequence[DecisionPoint]) -> None:
    if len(versions) < 2:
        print("Not enough versions to compare")
        return

    for a, b in zip(versions[:-1], versions[1:]):
        diff = dp_diff(a, b)
        print("\n".join(diff))
        print()


def print_versions_and_diffs(versions: Sequence[DecisionPoint]) -> None:
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
