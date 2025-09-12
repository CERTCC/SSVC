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
from typing import ClassVar, Literal

import pandas as pd
from pydantic import BaseModel, Field, field_validator, model_validator

from ssvc._mixins import (
    _Commented,
    _GenericSsvcObject,
    _Registered,
    _SchemaVersioned,
)
from ssvc.decision_points.base import DecisionPoint
from ssvc.registry import get_registry
from ssvc.utils.field_specs import DecisionPointDict
from ssvc.utils.misc import obfuscate_dict
from ssvc.utils.toposort import dplist_to_toposort

logger = logging.getLogger(__name__)


def dpdict_to_combination_list(
    dpdict: dict[str, DecisionPoint],
    exclude: list[str] = [],
) -> list[dict[str, str]]:
    """
    Generate all combinations of decision point values as dictionaries.
    Each combination is a dictionary with decision point IDs as keys and value keys as values.
    """
    dpg_vals = []
    for dp in dpdict.values():
        if dp.id in exclude:
            # skip this decision point if it is in the exclude list
            continue
        vals = []
        for value in dp.values:
            row = {dp.id: value.key}
            vals.append(row)
        dpg_vals.append(vals)

    # now we have a list of lists of dicts, we need to the combinations
    combos = []
    for prod in product(*dpg_vals):
        # prod is a tuple of dicts, we need to merge them
        merged = {}
        for d in prod:
            merged.update(d)
        combos.append(merged)
    return combos


SCHEMA_VERSION: str = "2.0.0"


class DecisionTable(
    _Registered, _SchemaVersioned, _GenericSsvcObject, _Commented, BaseModel
):
    """
    DecisionTable: A flexible, serializable SSVC decision table model.

    This model represents a decision table that can be used to map combinations of decision point values
    to outcomes. It allows for flexible mapping and can be used with helper methods to generate DataFrame and CSV representations
    of the decision table.

    Attributes:
    """

    key_prefix: ClassVar[str] = "DT"
    _schema_version: ClassVar[str] = SCHEMA_VERSION
    schemaVersion: Literal[SCHEMA_VERSION]

    decision_points: DecisionPointDict

    outcome: str = Field(
        ...,
        description="The key of the decision point in `self.decision_points` that represents the outcome of the decision table.",
        min_length=1,
    )

    # default to empty mapping list
    mapping: list[dict[str, str]] = Field(
        default_factory=list,
        description="Mapping of decision point values to outcomes.",
    )

    @property
    def id(self):
        return f"{self.namespace}:{self.name}:{self.version}"

    @field_validator("key", mode="before")
    @classmethod
    def validate_key(cls, value: str) -> str:
        if value.startswith(f"{cls.key_prefix}_"):
            return value

        # prepend the key prefix if it is not already present
        key = f"{cls.key_prefix}_{value}"
        return key

    @model_validator(mode="after")
    def populate_mapping_if_empty(self):
        """
        Populate the mapping if it is not already set.

        Returns:
            self: The DecisionTable instance with the mapping populated if it was not set. If the mapping is already set, it returns the instance unchanged.
        """
        # short-circuit if mapping is already set
        if self.mapping:
            # mapping is already set, no need to populate
            logger.debug("Mapping is already set, skipping population.")
            return self

        outcome_key = self.outcome

        dps = [
            dp
            for dpid, dp in self.decision_points.items()
            if dpid != outcome_key
        ]
        mapping = dplist_to_toposort(dps)

        # mapping is a list of dicts
        # but mapping doesn't have the outcome key yet
        # add the key with None as the value
        for row in mapping:
            # row is a dict with decision point values
            # we need to add the outcome key
            if outcome_key in row:
                # if the outcome key is already in the row, we should not overwrite it
                logger.warning(
                    f"Outcome key '{outcome_key}' already exists in row, skipping."
                )
            row[outcome_key] = None

        # distribute outcomes evenly across the mapping
        og: DecisionPoint = self.decision_points[outcome_key]

        mapping = distribute_outcomes_evenly(mapping, og)

        # set the mapping
        self.mapping = mapping
        return self

    @model_validator(mode="after")
    def check_mapping_keys(self):
        """
        Validate that each item in the mapping has the correct keys.
        Keys for each item should match the keys of the decision point group.

        Returns:
            self: The DecisionTable instance with validated mapping keys.
        Raises:
            TypeError: If any item in the mapping is not a dictionary.
            ValueError: If any item in the mapping does not have the expected keys.
        """
        # we expect the keys of each item in the mapping to match the decision point group keys
        expected = set(self.decision_points.keys())

        for i, d in enumerate(self.mapping):
            if not isinstance(d, dict):
                raise TypeError(f"Item {i} is not a dict")
            actual_keys = set(d.keys())
            if actual_keys != expected:
                raise ValueError(
                    f"Item {i} has keys {actual_keys}, expected {expected}"
                )
        return self

    @model_validator(mode="after")
    def remove_duplicate_mapping_rows(self):
        seen = dict()
        new_mapping = []
        for row in self.mapping:
            value_tuple = tuple(v for k, v in row.items() if k != self.outcome)
            if value_tuple in seen:
                # we have a duplicate, but is it same or different?
                if seen[value_tuple][self.outcome] == row[self.outcome]:
                    # if it's a match, just log it and move on
                    logger.warning(
                        f"Duplicate mapping found (removed automatically): {row}"
                    )
                else:
                    # they don't match
                    raise ValueError(
                        f"Conflicting mappings found: {seen[value_tuple]} != {row}"
                    )
            else:
                # not a duplicate, add it to the new mapping
                seen[value_tuple] = row
                new_mapping.append(row)
        # set the new mapping (with duplicates removed)
        self.mapping = new_mapping
        return self

    @model_validator(mode="after")
    def check_mapping_coverage(self):
        counts = {}
        all_combos = dpdict_to_combination_list(
            self.decision_points, exclude=[self.outcome]
        )
        # all_combos is a dict of all possible combinations of decision point values
        # keyed by decision point ID, with value keys as values.
        # initialize counts for all input combinations to 0
        for combo in all_combos:
            value_tuple = tuple(combo.values())
            counts[value_tuple] = counts.get(value_tuple, 0)

        # counts now has all possible input combinations set to count 0

        for row in self.mapping:
            value_tuple = tuple(v for k, v in row.items() if k != self.outcome)
            counts[value_tuple] += 1

        # check if all combinations are covered
        for k, v in counts.items():
            if v == 1:
                # ok, proceed
                continue
            elif v == 0:
                # missing combination
                raise ValueError(
                    f"Mapping is incomplete: No mapping found for decision point combination: {k}."
                )
            elif v > 1:
                # duplicate. remove duplicate mapping rows should have caught this already
                raise ValueError(
                    f"Duplicate mapping found for decision point combination: {k}."
                )
            else:
                raise ValueError(
                    f"Unexpected count in mapping coverage check.{k}: {v}"
                )

        # if you made it to here, all the counts were 1, so we're good

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
        if not self.mapping:
            raise ValueError("Mapping must be set before validation.")

        # Check that each MappingRow has the correct number of decision point values
        for row in self.mapping:
            if set(row.keys()) != set(self.decision_points.keys()):
                raise ValueError(
                    "MappingRow does not have the correct keys. "
                    "Keys must match the decision point group keys."
                )

        # Verify the topological order of the decision points (if u<v then u_outcome <= v_outcome)
        problems = check_topological_order(self)
        if len(problems) > 0:
            logger.warning("Topological order check found problems:")
            for problem in problems:
                logger.warning(f"Problem: {problem}")
            raise ValueError(
                "Topological order check failed. See logs for details."
            )
        else:
            logger.debug("Topological order check passed with no problems.")

        # if there's only one decision point mapping to the outcome, we can stop here
        input_cols = [
            dp for dp in self.decision_points.values() if dp.id != self.outcome
        ]
        if len(input_cols) <= 1:
            return self

        # reject if any irrelevant columns are present in the mapping
        fi = feature_importance(self)
        irrelevant_features = fi[fi["feature_importance"] <= 0]
        if not irrelevant_features.empty:
            logger.warning(
                "Mapping contains irrelevant features: "
                f"{', '.join(irrelevant_features['feature'].tolist())}"
            )
            raise ValueError(
                "Mapping contains irrelevant features. "
                "Please remove them before proceeding."
            )

        return self

    def obfuscate(self) -> "DecisionTable":
        """
        Obfuscate the decision table by renaming the dict keys.
        """
        obfuscated_dpdict, translator = obfuscate_dict(self.decision_points)

        new_table = self.model_copy(deep=True)
        new_table.decision_points = obfuscated_dpdict
        new_table.outcome = translator.get(self.outcome, self.outcome)
        # replace all the keys in mapping dicts
        new_table.mapping = []
        for row in self.mapping:
            new_row = {}
            for key in row.keys():
                new_key = translator[key]
                new_row[new_key] = row[key]
            new_table.mapping.append(new_row)

        return new_table


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
        ssvc:SINV:1.0.0,ssvc:E:1.0.0,ssvc:PVA:1.0.0,basic:MSCW:1.0.0
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
    if not dt.mapping:
        raise ValueError("Decision Table has no mapping to export.")

    df = pd.DataFrame(dt.mapping)
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


def distribute_outcomes_evenly(
    mapping: list[dict[str, str]], outcome_group: DecisionPoint
) -> list[dict[str, str]]:
    """
    Distribute the given outcome_values across the mapping item dicts in sorted order.
    Overwrites the outcome value in each mapping dict item with the corresponding outcome value.
    The earliest mappings get the lowest outcome value, the latest get the highest.
    If the mapping count is not divisible by the number of outcomes, the last outcome(s) get the remainder.
    Returns a new list of dicts with outcome values assigned.

    Args:
        mapping (list[dict[str,str]]): The mapping to distribute outcomes across.
        outcome_values (list[str]): The list of outcome values to distribute.
    Returns:
        list[dict[str,str]]: A new list of dicts with outcome values assigned.
    """
    outcome_values = [ov.key for ov in outcome_group.values]

    if not outcome_values:
        raise ValueError("No outcome values provided for distribution.")

    og_id = outcome_group.id

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
            row[og_id] = outcome
            new_mapping.append(row)
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
        row,Supplier Involvement v1.0.0,Exploitation v1.0.0,Public Value Added v1.0.0,MoSCoW v1.0.0 (basic)
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

    def _col_check(col: str) -> bool:
        """
        Check if the column is a valid decision point or outcome column.
        Args:
            col: a colon-separated string representing a decision point or outcome column in the format `namespace:dp_key:version`.

        Returns:
            bool: True if the column is a valid decision point or outcome column, False otherwise.

        """
        # late-binding import to avoid circular import issues
        registry = get_registry()

        ns, dp_key, version = col.split(":")

        return (
            registry.lookup(
                objtype="DecisionPoint",
                namespace=ns,
                key=dp_key,
                version=version,
            )
            is not None
        )

    # Replace cell values using DPV_REGISTRY
    for col in df.columns:
        logger.debug(f"Converting column: {col}")

        ns, dp_key, version = col.split(":")

        if _col_check(col):
            dp_id = col
            newcol = df[col].apply(_replace_value_keys, dp_id=dp_id)
            df[col] = newcol

    # lowercase all cell values
    df = df.apply(
        lambda col: col.map(lambda x: x.lower() if isinstance(x, str) else x)
    )

    # Rename columns using DP_REGISTRY

    rename_map = {
        col: _rename_column(col) for col in df.columns if _col_check(col)
    }

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

    objtype = "DecisionPoint"
    REGISTRY = get_registry()

    newval = REGISTRY.lookup_by_id(objtype, key)

    logger.debug(f"Replacing value key: {key} with {newval}")

    return newval.name


def _rename_column(col: str) -> str:
    """Helper function to rename a column based on the DP_REGISTRY.
    Args:
        col (str): The column name to rename.
    Returns:
        str: The renamed column.
    """
    registry = get_registry()

    # col should be in the format "namespace:dp_key:version"
    dp = registry.lookup_by_id(objtype="DecisionPoint", objid=col)

    if dp is None:
        raise KeyError(f"Column {col} not found in DP_REGISTRY.")

    dp = dp.obj

    new_col = f"{dp.name} v{dp.version}"

    # If the namespace is "ssvc", we don't include it in the column name
    if dp.namespace == "ssvc":
        return new_col

    # If the namespace is not "ssvc", include it in the column name
    return f"{new_col} ({dp.namespace})"


def _get_target_column_name(colname: str) -> str:
    """
    Helper function to convert a column name to a target column name for use with older csv_analyzer functions.
    This function converts the column name to lowercase and replaces non-alphanumeric characters with underscores.
    """
    colname = colname.lower()
    colname = "".join(c if c.isalnum() else "_" for c in colname)
    return colname


def feature_importance(dt: DecisionTable) -> pd.DataFrame:
    """
    Calculate feature importance for the decision table.
    Args:
        dt:

    Returns:

    """
    from ssvc.csv_analyzer import drop_col_feature_importance

    logger.debug("Calculating feature importance for the decision table.")

    df = decision_table_to_shortform_df(dt)
    # target is the last column in the DataFrame, which is the outcome column
    target = _get_target_column_name(df.columns[-1])

    return drop_col_feature_importance(df, target=target)


def interpret_feature_importance(dt: DecisionTable) -> pd.DataFrame:
    """
    Interpret the feature importance for the decision table.
    This function is a wrapper around the feature_importance function to provide a more user-friendly output.
    It sorts the features by importance and adds a commentary column that describes the importance of each feature,
    calling out the most important features, those above median importance, low to medium importance features,
    low importance features, and irrelevant features. The commentary is based on the computed feature importance scores.

    This function is useful for understanding which decision points and their values are most influential in the decision-making process of the table,
    and can help in identifying which features can be considered for removal or further investigation.

    Args:
        dt (DecisionTable): The decision table to analyze.
    Returns:
        pd.DataFrame: A DataFrame containing the feature importance scores.
    """

    fi_df = feature_importance(dt)

    logger.debug("Interpreting feature importance for the decision table.")
    col = "feature_importance"
    fi_df = fi_df.sort_values(by=col, ascending=False)
    # add a column for commentary
    # low importance are those with importance< 0.1 * max(importance)
    # irrelevant features are those with importance <= 0
    max_importance = fi_df[col].max()
    logger.debug(f"Max importance: {max_importance}")
    median_importance = fi_df[col].median()
    logger.debug(f"Median importance: {median_importance}")
    low_threshold = 0.1 * fi_df[col].max()
    logger.debug(f"Low threshold: {low_threshold}")
    irrelevant_threshold = 0.0

    def _label_importance(importance: float) -> str:
        """
        Label the importance of a feature based on its importance score.
        The values are computed in relation to the
        Args:
            importance:

        Returns:

        """
        comments = []

        if importance == max_importance:
            comments.append("Most important feature")
        elif importance > median_importance:
            comments.append("Medium-high importance feature")
        elif importance == median_importance:
            comments.append("Median importance feature")
        elif low_threshold <= importance < median_importance:
            comments.append("Low-medium importance feature")
        elif irrelevant_threshold < importance < low_threshold:
            comments.append("Low importance feature")
        elif importance <= irrelevant_threshold:
            comments.append("Irrelevant feature")

        return "; ".join(comments)

    logger.debug("Adding feature importance commentary.")
    fi_df["Commentary"] = fi_df[col].apply(_label_importance)

    return fi_df.reset_index(drop=True)


def check_topological_order(dt: DecisionTable) -> list[dict]:
    """
    Check the topological order of the decision table.
    This function uses the `check_topological_order` function from the csv_analyzer module to verify the topological order of the decision table.
    It returns a list of dictionaries containing any problems found in the topological order check.

    Args:
        dt: DecisionTable: The decision table to check.

    Returns:
        list[dict]: A list of dictionaries containing any problems found in the topological order check.
        Problems are defined as any pair of mappings `(u,v)` where `u < v` but `u_outcome > v_outcome`.

        Each dictionary contains the following keys:
        "u": The lower decision point value
        "v": The higher decision point value
        "u_outcome": The outcome of the lower decision point value
        "v_outcome": The outcome of the higher decision point value

    """
    from ssvc.csv_analyzer import check_topological_order

    logger.debug("Checking topological order of the decision table.")
    df = decision_table_to_shortform_df(dt)
    target = _get_target_column_name(df.columns[-1])
    target_values = dt.decision_points[dt.outcome].values
    target_value_order = [v.key for v in target_values]
    return check_topological_order(
        df, target=target, target_value_order=target_value_order
    )
