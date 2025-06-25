#!/usr/bin/env python
"""
DecisionTable: A flexible, serializable SSVC decision table model.
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

    def __len__(self) -> int:
        """
        Return the number of values in the combo.
        """
        return len(self.values)


class MappingRow(BaseModel):
    decision_point_values: ValueCombo
    outcome: Optional[ValueSummary]


class DecisionTable(_SchemaVersioned, _Namespaced, _Base, _Commented, BaseModel):
    """
    DecisionTable: A flexible, serializable SSVC decision table model.
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

        Example:
            Table values might look like:
            ```
            dp1ns:dp1k:1.0:dp1v1, dp2ns:dp2k:1.0:dp2v1, outcomens:outcomek:1.0:outcomev1
            dp1ns:dp1k:1.0:dp1v1, dp2ns:dp2k:1.0:dp2v2, outcomens:outcomek:1.0:outcomev2
            ```
            etc.

        Returns:
            str: CSV string representation of the decision table mapping.
        """
        if not self.mapping:
            raise ValueError("No mapping to export.")

        column_names = []
        for dp in self.decision_point_group.decision_points:
            col_name = f"{dp.namespace}:{dp.key}:{dp.version}"
            column_names.append(col_name)
        outcome_col_name = f"{self.outcome_group.namespace}:{self.outcome_group.key}:{self.outcome_group.version}"
        column_names.append(outcome_col_name)

        data = []
        for row in self.mapping:
            # row is a MappingRow
            # with attributes: decision_point_values (ValueCombo), outcome (ValueSummary or None)
            row_data = {}
            for vc in row.decision_point_values.values:
                key = f"{vc.namespace}:{vc.key}:{vc.version}"
                row_data[key] = str(vc.value)
            if row.outcome:
                outcome_key = (
                    f"{row.outcome.namespace}:{row.outcome.key}:{row.outcome.version}"
                )
                row_data[outcome_col_name] = str(row.outcome.value)
            else:
                row_data[outcome_col_name] = ""
            data.append(row_data)
        df = pd.DataFrame(data, columns=column_names)
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

        outcome_values = getattr(self.outcome_group, "value_summaries", None)
        if outcome_values is None:
            raise ValueError(
                "Outcome group must have value_summaries to distribute outcomes."
            )

        self.mapping = distribute_outcomes_evenly(self.mapping, outcome_values)


def generate_full_mapping(decision_table: "DecisionTable") -> list[MappingRow]:
    """
    Generate a full mapping for the decision table, with every possible combination of decision point values.
    Each MappingRow will have a ValueCombo of ValueSummary objects, and outcome=None.

    Args:
        decision_table (DecisionTable): The decision table to generate the mapping for.
    Returns:
        list[MappingRow]: A list of MappingRow objects representing the full mapping. Note that the outcome field will be None.

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
    Overwrites the outcome field in each MappingRow with the corresponding outcome value.
    The earliest mappings get the lowest outcome, the latest get the highest.
    If the mapping count is not divisible by the number of outcomes, the last outcome(s) get the remainder.
    Returns a new list of MappingRow with outcomes assigned.

    Args:
        mapping (list[MappingRow]): The mapping rows to distribute outcomes across.
        outcome_values (list[ValueSummary]): The outcome values to distribute.
    Returns:
        list[MappingRow]: A new list of MappingRow with outcomes assigned.
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
    from ssvc.dp_groups.ssvc.coordinator_publication import LATEST as dpg
    from ssvc.outcomes.x_basic.mscw import LATEST as outcomes

    table = DecisionTable(
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

    # print(table.mapping)


if __name__ == "__main__":
    main()
