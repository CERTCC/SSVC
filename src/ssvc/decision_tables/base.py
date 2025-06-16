#!/usr/bin/env python
"""
DecisionTableBase: A flexible, serializable SSVC decision table model.
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
from itertools import product
from typing import List, Optional

import pandas as pd
from pydantic import BaseModel, model_validator

from ssvc._mixins import _Base, _Commented, _Namespaced, _SchemaVersioned
from ssvc.decision_points.base import ValueSummary
from ssvc.dp_groups.base import DecisionPointGroup
from ssvc.outcomes.base import OutcomeGroup

logger = logging.getLogger(__name__)


class ValueCombo(BaseModel):
    values: tuple[ValueSummary, ...]


class MappingRow(BaseModel):
    decision_point_values: ValueCombo
    outcome: Optional[ValueSummary]


class DecisionTableBase(_SchemaVersioned, _Namespaced, _Base, _Commented, BaseModel):
    """
    DecisionTableBase: A flexible, serializable SSVC decision table model.
    """

    decision_point_group: DecisionPointGroup
    outcome_group: OutcomeGroup
    mapping: Optional[List[MappingRow]] = None

    @model_validator(mode="after")
    def populate_mapping_if_none(self):

        if self.mapping is not None:
            # short-circuit if mapping is already set
            return self

        dpg = self.decision_point_group
        og = self.outcome_group
        if dpg is not None and og is not None:
            mapping = self.generate_full_mapping()
            outcome_values = getattr(og, "value_summaries", None)
            if outcome_values:
                mapping = distribute_outcomes_evenly(mapping, outcome_values)
            else:
                raise ValueError(
                    "Outcome group must have value_summaries to distribute outcomes."
                )
            self.mapping = mapping
        return self

    def to_csv(self) -> str:
        """
        Export the mapping to a CSV string. Columns: one per decision point (by name), one for outcome.
        Indiviual decision point and outcome values are represented as a colon-separated tuple
        consisting of the namespace, decision point key, decision point version, and value key.
        """
        if not self.mapping:
            raise ValueError("No mapping to export.")
        dp_names = [dp.name for dp in self.decision_point_group.decision_points]
        outcome_name = self.outcome_group.name
        rows = []
        for row in self.mapping:
            row_dict = {
                name: str(val)
                for name, val in zip(dp_names, row.decision_point_values.values)
            }
            row_dict[outcome_name] = str(row.outcome) if row.outcome else ""
            rows.append(row_dict)
        df = pd.DataFrame(rows, columns=dp_names + [outcome_name])
        return df.to_csv(index=False)

    def generate_full_mapping(self) -> List[MappingRow]:
        """
        Generate a full mapping for the decision table, with every possible combination of decision point values.
        Each MappingRow will have a ValueCombo of ValueSummary objects, and outcome=None.
        """
        if self.mapping is not None:
            # short-circuit if mapping is already set
            logger.warning("Mapping is already set, skipping full generation.")
            return self.mapping

        logger.debug("Generating full mapping.")
        self.mapping = generate_full_mapping(self)

        return self.mapping

    def distribute_outcomes_evenly(self, overwrite: bool = False) -> List[MappingRow]:
        """
        Distribute the given outcome_values across the mapping rows in sorted order.
        The earliest mappings get the lowest outcome, the latest get the highest.
        If the mapping count is not divisible by the number of outcomes, the last outcome(s) get the remainder.
        Returns a new list of MappingRow with outcomes assigned.
        """
        if self.mapping is not None:
            if not overwrite:
                # short-circuit if mapping is already set
                logger.warning("Mapping is already set, skipping distribution.")
                return self.mapping
            else:
                logger.info("Overwriting existing mapping with new distribution.")

        self.generate_full_mapping()

        outcome_values = getattr(self.outcome_group, "value_summaries", None)
        if outcome_values is None:
            raise ValueError(
                "Outcome group must have value_summaries to distribute outcomes."
            )

        if mapping is None:
            self.mapping = distribute_outcomes_evenly(outcome_values)


def generate_full_mapping(decision_table: "DecisionTableBase") -> list[MappingRow]:
    """
    Generate a full mapping for the decision table, with every possible combination of decision point values.
    Each MappingRow will have a ValueCombo of ValueSummary objects, and outcome=None.
    """
    dp_group = decision_table.decision_point_group
    # For each decision point, get its value summaries
    value_lists = [
        [
            ValueSummary(
                key=dp.key,
                version=dp.version,
                namespace=dp.namespace,
                value=val.key,
            )
            for val in dp.values
        ]
        for dp in dp_group.decision_points
    ]
    all_combos = product(*value_lists)
    mapping = [
        MappingRow(decision_point_values=ValueCombo(values=combo), outcome=None)
        for combo in all_combos
    ]
    return mapping


def distribute_outcomes_evenly(
    mapping: list[MappingRow], outcome_values: list[ValueSummary]
) -> list[MappingRow]:
    """
    Distribute the given outcome_values across the mapping rows in sorted order.
    The earliest mappings get the lowest outcome, the latest get the highest.
    If the mapping count is not divisible by the number of outcomes, the last outcome(s) get the remainder.
    Returns a new list of MappingRow with outcomes assigned.
    """
    if not outcome_values:
        raise ValueError("No outcome values provided for distribution.")
    n = len(mapping)
    k = len(outcome_values)
    base = n // k
    rem = n % k
    new_mapping = []
    idx = 0
    for i, outcome in enumerate(outcome_values):
        count = base + (1 if i < rem else 0)
        for _ in range(count):
            if idx >= n:
                break
            row = mapping[idx]
            new_mapping.append(
                MappingRow(
                    decision_point_values=row.decision_point_values, outcome=outcome
                )
            )
            idx += 1
    return new_mapping


def main() -> None:
    from ssvc.dp_groups.ssvc.coordinator_triage import LATEST as dpg
    from ssvc.outcomes.x_basic.mscw import LATEST as outcomes

    table = DecisionTableBase(
        name="Test Table",
        description="A test decision table",
        namespace="x_test",
        decision_point_group=dpg,
        outcome_group=outcomes,
    )
    table.mapping = generate_full_mapping(table)
    table.mapping = distribute_outcomes_evenly(table.mapping, outcomes.value_summaries)
    csv_str = table.to_csv()
    print(csv_str)


if __name__ == "__main__":
    main()
