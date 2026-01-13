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
import itertools

from pydantic import BaseModel

from ssvc.decision_tables.base import DecisionTable


class Rule(BaseModel):
    """
    Describes a rule for determining an outcome based on decision point values.
    Assumes integer indexes of decision point values to simplify matching.

    - value: The decision point value to match.
    - value_count: The minimum number of times the value must appear in the combination.
    - outcome: The outcome to assign if the rule matches.
    """

    value: int
    value_count: int
    outcome: int


class RuleSet(BaseModel):
    """
    A set of rules for determining outcomes based on decision point values.
    Always evaluated in order; first match applies.
    """

    rules: list[Rule]


_ruleset = RuleSet(
    rules=[
        # Highest severity first
        Rule(value=2, value_count=2, outcome=2),
        Rule(value=2, value_count=1, outcome=1),
        Rule(value=1, value_count=2, outcome=1),
        Rule(value=0, value_count=0, outcome=0),
    ]
)


def _get_outcome(
    combo: tuple[tuple[int, int], tuple[int, int]], ruleset: RuleSet
) -> int:
    """
    Determine the outcome for a given combination of decision point values based on the provided ruleset.
    Args:
        combo: the combination of decision point values (an integer tuple)
        ruleset: the ruleset to evaluate against

    Returns:
        The integer outcome value from the first matching rule.
    """
    for rule in ruleset.rules:
        count = sum(1 for v in combo if v == rule.value)
        if count >= rule.value_count:
            return rule.outcome
    # if you got here, nothing matched
    # default outcome is lowest severity
    return 0


def _shape_rules(
    dt: DecisionTable, ruleset: RuleSet
) -> list[tuple[tuple[int], int]]:
    """
    Generate all possible combinations of decision point values and their corresponding outcomes.

    Args:
        dt:

    Returns:

    """
    # get the shape of the decision table
    value_counts = [
        len(dp.values)
        for dp in dt.decision_points.values()
        if dp.id != dt.outcome
    ]

    combos = []
    outcomes = []
    for combo in itertools.product(
        *[list(range(count)) for count in value_counts]
    ):
        combos.append(combo)
        outcomes.append(_get_outcome(combo, ruleset))

    rows = list(zip(combos, outcomes))
    return rows


def rules_mapping(
    dt: DecisionTable, ruleset: RuleSet | None = None
) -> list[dict[str, str]]:

    if ruleset is None:
        ruleset = _ruleset

    rows = _shape_rules(dt, ruleset)

    dp_value_lookup = [
        {str(i): v.key for i, v in enumerate(dp.values)}
        for dp in dt.decision_points.values()
        if dp.id != dt.outcome
    ]
    dp_outcome_lookup = {
        str(i): v.key
        for i, v in enumerate(dt.decision_points[dt.outcome].values)
    }

    mapping_rows = []
    for row in rows:
        # translate to keys
        inputs = {
            dp.id: dp_value_lookup[i][str(v)]
            for i, (dp, v) in enumerate(
                zip(dt.decision_points.values(), row[0])
            )
            if dp.id != dt.outcome
        }
        outcome = dp_outcome_lookup[str(row[1])]
        mapping_row = dict(inputs)
        mapping_row.update({dt.outcome: outcome})
        mapping_rows.append(mapping_row)

    return mapping_rows
