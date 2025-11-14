#!/usr/bin/env python

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

"""
Provides TODO writeme
"""
import json

import yaml
from pydantic import BaseModel

from ssvc.decision_points.base import DecisionPoint
from ssvc.decision_tables.base import DecisionTable
from ssvc.registry import get_registry


class GhFormCheckboxOption(BaseModel):
    label: str
    required: bool | None = None


class GhFormCheckboxes(BaseModel):
    label: str
    description: str | None = None
    options: list[GhFormCheckboxOption]


class GhFormCheckboxesValidations(BaseModel):
    required: bool | None = None


class GhFormElement(BaseModel):
    type: str
    id: str | None = None
    attributes: GhFormCheckboxes
    validations: GhFormCheckboxesValidations | None = None


class GhForm(BaseModel):
    name: str
    description: str
    title: str | None = None
    body: list[GhFormElement] | str | None = None
    assignees: list[str] | None = None
    labels: list[str] | None = None
    type: str | None = None
    projects: list[str] | None = None


def to_checkboxes(decision_point) -> GhFormCheckboxes:
    """
    Given a decision point, return a github issue form compatible checkbox list
    Args:
        decision_point:

    Returns:
        GhFormCheckboxes: A github issue form compatible checkbox list
    """
    description = f"{decision_point.definition.strip()}\n"
    description += "\n".join(
        f"- (**{option.key.strip()}**) *{option.name.strip()}*: {option.definition.strip()}"
        for option in decision_point.values
    )

    cb = GhFormElement(
        type="checkboxes",
        attributes=GhFormCheckboxes(
            label=decision_point.name,
            description=description.strip(),
            options=[
                GhFormCheckboxOption(
                    label=f"{option.key} | {option.name}",
                )
                for option in decision_point.values
            ],
        ),
    )

    return cb


def json_to_yaml(json_str: str) -> str:
    data = json.loads(json_str)
    return yaml.dump(data, sort_keys=False)


def expand_dps(
    dt: DecisionTable, other_dts: list[DecisionTable]
) -> list[DecisionPoint]:
    """
    Recursively expand a decision table to a list of decision points.
    Skips the outcome decision point.

    Args:
        dt: DecisionTable to expand
        other_dts: A list of other DecisionTables to use for expansion

    Returns:
        list[DecisionPoint]: A list of DecisionPoints collected after expansion
    """

    dt_by_outcomes = {dt.outcome: dt for dt in other_dts}

    dps = []
    for dp in dt.decision_points.values():
        if dp.id == dt.outcome:
            # skip the outcome decision point
            continue

        if dp.id in dt_by_outcomes:
            # we have another decision table that defines this decision point as its outcome
            # so we need to expand that decision table too
            dps.extend(
                expand_dps(
                    dt_by_outcomes[dp.id],
                    [odt for odt in other_dts if odt.outcome != dp.id],
                )
            )
            continue

        # otherwise, just add the decision point to the list
        dps.append(dp)

    return dps


def main():
    # load one decision point
    # import registry

    registry = get_registry()

    from ssvc.decision_tables.ssvc.supplier_dt import LATEST as supplier_dt
    from ssvc.decision_tables.ssvc.utility import LATEST as utility_dt
    from ssvc.decision_tables.ssvc.public_safety_impact import (
        LATEST as public_safety_dt,
    )

    form = GhForm(
        name="SSVC Form Example",
        title="SSVC Supplier Decision Table Submission",
        description="Issue Form Containing SSVC Supplier Decision Table Form",
        body=[],
    )

    for dp in expand_dps(supplier_dt, [utility_dt, public_safety_dt]):

        cb = to_checkboxes(dp)
        form.body.append(cb)

    form_yaml = json_to_yaml(form.model_dump_json(indent=2, exclude_none=True))
    print(form_yaml)


if __name__ == "__main__":
    main()
