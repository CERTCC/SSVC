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
from typing import List, Optional

import pandas as pd
from pydantic import BaseModel, model_validator

from ssvc._mixins import _Base, _Commented, _Namespaced, _SchemaVersioned
from ssvc.decision_points.base import DPV_REGISTRY, DP_REGISTRY
from ssvc.dp_groups.base import DecisionPointGroup
from ssvc.outcomes.base import OutcomeGroup

logger = logging.getLogger(__name__)


class MappingRow(BaseModel):
    decision_point_values: list[str]
    outcome: Optional[str]


class DecisionTable(_SchemaVersioned, _Namespaced, _Base, _Commented, BaseModel):
    """
    DecisionTable: A flexible, serializable SSVC decision table model.

    This model represents a decision table that can be used to map combinations of decision point values
    to outcomes. It allows for flexible mapping and can be used with helper methods to generate DataFrame and CSV representations
    of the decision table.

    Attributes:
        decision_point_group (DecisionPointGroup): The group of decision points that this table uses.
        outcome_group (OutcomeGroup): The group of outcomes that this table maps to.
        mapping (Optional[List[MappingRow]]): A list of MappingRow objects representing the mapping of decision point values to outcomes.
            If not provided or `None`, it will be populated automatically after validation.
    """

    decision_point_group: DecisionPointGroup
    outcome_group: OutcomeGroup
    mapping: Optional[List[MappingRow]] = None

    @model_validator(mode="after")
    def populate_mapping_if_none(self):
        """
        Populate the mapping if it is not already set.

        Returns:
            self: The DecisionTable instance with the mapping populated if it was not set. If the mapping is already set, it returns the instance unchanged.
        """

        if self.mapping is not None:
            # short-circuit if mapping is already set
            return self

        dpg = self.decision_point_group
        og = self.outcome_group

        if dpg is None or og is None:
            raise ValueError(
                "DecisionTable must have both decision_point_group and outcome_group set."
            )
        empty_mapping = generate_full_mapping(dt=self)
        mapping = distribute_outcomes_evenly(empty_mapping, og.value_summaries)

        # set the mapping
        self.mapping = mapping
        return self

    @model_validator(mode="after")
    def validate_mapping(self):
        """
        Validate the mapping after it has been populated.

        This method checks that the mapping is consistent with the decision points and outcomes defined in the table.
        It raises a ValueError if the mapping is not valid.

        Returns:
            self: The DecisionTable instance with validated mapping.
        """
        if self.mapping is None:
            raise ValueError("Mapping must be set before validation.")

        # Check that each MappingRow has the correct number of decision point values
        for row in self.mapping:
            if len(row.decision_point_values) != len(self.decision_point_group):
                raise ValueError(
                    "MappingRow does not have the correct number of decision point values."
                )

        # TODO: Check the consistency of the Hasse diagram graph
        # This is a placeholder for future validation logic, based on what appears in the Policy Generator module.

        return self


def decision_table_to_df(dt: DecisionTable, longform=False) -> pd.DataFrame:
    """
    Export the decision table to a pandas DataFrame.

    This is just a wrapper around the shortform and longform export functions.

    Args:
        dt (DecisionTable): The decision table to export.
        longform (bool): Whether to export in long form or short form. Defaults to False (short form).
    Returns:
        pd.DataFrame: The mapping table as a pandas DataFrame.

    """
    if longform:
        return decision_table_to_longform_df(dt)
    return decision_table_to_shortform_df(dt)


def decision_table_to_shortform_df(dt: DecisionTable) -> pd.DataFrame:
    """
    Export the mapping to pandas DataFrame.

    Columns: one per decision point, one for outcome. Column names are namespace:key:version.
    Individual decision point and outcome values are represented by their value key.

    Example:
        Table values might look like:

        ```csv
        ssvc:SINV:1.0.0,ssvc:E:1.0.0,ssvc:PVA:1.0.0,x_basic:MSCW:1.0.0
        FR,N,L,W
        FR,N,A,W
        FR,N,P,W
        FR,P,L,W
        FR,P,A,W
        FR,P,P,W
        FR,A,L,W
        FR,A,A,C
        ```
        etc.

    Returns:
        df: pd.DataFrame: The mapping as a pandas DataFrame.

    Raises:
        ValueError: If the decision table has no mapping to export.
    """
    if dt.mapping is None:
        raise ValueError("Decision Table has no mapping to export.")

    column_names = []
    for dp in dt.decision_point_group.decision_points:
        col_name = f"{dp.namespace}:{dp.key}:{dp.version}"
        column_names.append(col_name)

    outcome_col_name = f"{dt.outcome_group.namespace}:{dt.outcome_group.key}:{dt.outcome_group.version}"
    column_names.append(outcome_col_name)

    data = []
    for row in dt.mapping:
        # row is a MappingRow
        # with attributes: decision_point_values (ValueCombo), outcome (ValueSummary or None)
        row_data = {}
        for vc in row.decision_point_values:
            (ns, dpk, dpv, vk) = vc.split(":")

            col_name = f"{ns}:{dpk}:{dpv}"

            row_data[col_name] = vk
        if row.outcome:
            # outcome is a value_key too
            (ns, ok, ov, ovk) = row.outcome.split(":")
            row_data[outcome_col_name] = ovk
        else:
            row_data[outcome_col_name] = ""
        data.append(row_data)

    df = pd.DataFrame(data, columns=column_names)
    return df


def decision_table_to_csv(dt: DecisionTable, **kwargs) -> str:
    """Wrapper around to_df to export to CSV string.
    Args:
        dt (DecisionTable): The decision table to export.
        kwargs: Additional keyword arguments to pass to pandas.DataFrame.to_csv().

    Returns:
        str: The mapping table as a CSV string.
    """
    return decision_table_to_df(dt).to_csv(**kwargs)


def generate_full_mapping(dt: DecisionTable) -> list[MappingRow]:
    """
    Generate a full mapping for the decision table, with every possible combination of decision point values.
    Each MappingRow will have a list of strings, and outcome=None.

    Args:
        dt (DecisionTable): The decision table to generate the mapping for.
    Returns:
        list[MappingRow]: A list of MappingRow objects representing the full mapping. Note that the outcome field will be None.

    """
    dp_group = dt.decision_point_group

    combos = dp_group.combination_strings()

    mapping = []
    for combo in combos:
        row = MappingRow(decision_point_values=combo, outcome=None)
        mapping.append(row)

    return mapping


def distribute_outcomes_evenly(
    mapping: list[MappingRow], outcome_values: list[str]
) -> list[MappingRow]:
    """
    Distribute the given outcome_values across the mapping rows in sorted order.
    Overwrites the outcome field in each MappingRow with the corresponding outcome value.
    The earliest mappings get the lowest outcome, the latest get the highest.
    If the mapping count is not divisible by the number of outcomes, the last outcome(s) get the remainder.
    Returns a new list of MappingRow with outcomes assigned.

    Args:
        mapping (list[MappingRow]): The mapping rows to distribute outcomes across.
        outcome_values (list[str]): The outcome values to distribute.
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


def decision_table_to_longform_df(dt: DecisionTable) -> pd.DataFrame:
    """
    Given a DecisionTable, convert it to a long-form DataFrame.
    The DataFrame will have one row per decision point value combination, with columns for each decision point and the outcome.
    The column names will be the decision point names with their versions, and the values will be the value names.
    If the decsion point is from a namespace other than "ssvc", the column name will include the namespace in parentheses.


    Example:
        Column Heading format: `{decision_point_name} v{version} ({namespace})`

        ```csv
        row,Supplier Involvement v1.0.0,Exploitation v1.0.0,Public Value Added v1.0.0,MoSCoW v1.0.0 (x_basic)
        0,fix ready,none,limited,won't
        1,fix ready,none,ampliative,won't
        2,fix ready,none,precedence,won't
        ```

    Args:
        df (pd.DataFrame): The input DataFrame from `to_df()`.

    Returns:
        pd.DataFrame: The converted DataFrame.

    """

    df = decision_table_to_shortform_df(dt)

    # Replace cell values using DPV_REGISTRY
    for col in df.columns:
        logger.debug(f"Converting column: {col}")
        if col in DP_REGISTRY.registry:  # Ensure the column name is valid
            dp_id = col
            newcol = df[col].apply(_replace_value_keys, dp_id=dp_id)
            df[col] = newcol

    # lowercase all cell values
    df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    # Rename columns using DP_REGISTRY

    rename_map = {col: _rename_column(col) for col in df.columns if col in DP_REGISTRY}

    df = df.rename(
        columns=rename_map,
    )

    return df


def _replace_value_keys(value_key: str, dp_id: str) -> str:
    """Helper function to replace value keys with their names from DPV_REGISTRY.
    Args:
        value_key (str): The value key to replace.
        dp_id (str): The decision point ID to use for the lookup.
    Returns:
        str: The name of the value if found in DPV_REGISTRY
    Raises:
        KeyError: If the value_key is not found in DPV_REGISTRY for the given dp_id.
    """
    key = f"{dp_id}:{value_key}"

    newval = DPV_REGISTRY[key]
    logger.debug(f"Replacing value key: {key} with {newval}")

    return newval.name


def _rename_column(col: str) -> str:
    """Helper function to rename a column based on the DP_REGISTRY.
    Args:
        col (str): The column name to rename.
    Returns:
        str: The renamed column.
    """

    if col not in DP_REGISTRY.registry:
        raise KeyError(f"Column {col} not found in DP_REGISTRY.")

    dp = DP_REGISTRY[col]
    new_col = f"{dp.name} v{dp.version}"

    # If the namespace is "ssvc", we don't include it in the column name
    if dp.namespace == "ssvc":
        return new_col

    # If the namespace is not "ssvc", include it in the column name
    return f"{new_col} ({dp.namespace})"


def main() -> None:
    from ssvc.dp_groups.ssvc.coordinator_publication import LATEST as dpg
    from ssvc.outcomes.x_basic.mscw import LATEST as outcomes

    rootlogger = logging.getLogger()
    rootlogger.setLevel(logging.DEBUG)
    hdlr = logging.StreamHandler()
    rootlogger.addHandler(hdlr)

    table = DecisionTable(
        name="Test Table",
        description="A test decision table",
        namespace="x_test",
        decision_point_group=dpg,
        outcome_group=outcomes,
    )

    table.mapping = generate_full_mapping(table)
    table.mapping = distribute_outcomes_evenly(table.mapping, outcomes.value_summaries)
    csv_str = decision_table_to_csv(table)
    print(csv_str)

    converted_df = decision_table_to_longform_df(table)
    print(converted_df.to_csv(index=True, index_label="row"))


if __name__ == "__main__":
    main()
