#!/usr/bin/env python
"""
Provides a Policy Generator class for SSVC decision point groups.

"""
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

import itertools
import logging
import math
from typing import List, Tuple

import networkx as nx
import pandas as pd

from ssvc import csv_analyzer
from ssvc.dp_groups.base import SsvcDecisionPointGroup
from ssvc.outcomes.base import OutcomeGroup

logger = logging.getLogger(__name__)


class PolicyGenerator:
    """
    Generates a policy for a given decision point group and outcome group.

    An SSVC policy is represented as a table of decision point values and outcomes.
    Each row of the table represents a specific set of decision point values, and the outcome that results from those values.

    Internally, the PolicyGenerator represents a policy as a directed graph.
    Each node in the graph corresponds to a specific set of decision point values.
    Each edge in the graph indicates an ordering between two states.
    Taken together, the graph represents a partial ordering of the decision point values mapped to outcomes.
    """

    def __init__(
        self,
        dp_group: SsvcDecisionPointGroup = None,
        outcomes: OutcomeGroup = None,
        outcome_weights: List[float] = None,
        validate: bool = False,
    ):
        """
        Create a policy generator.

        If outcome weights are unspecified, then the weights are evenly distributed across the outcomes.

        Args:
            dp_group: The decision point group to generate a policy for.
            outcomes: The outcome group to generate a policy for.
            outcome_weights: The relative weights of the outcomes (optional)

        Raises:
            ValueError: If dp_group or outcomes are None.
        """
        if dp_group is None:
            raise ValueError("dp_group is required")
        else:
            self.dpg: SsvcDecisionPointGroup = dp_group

        if outcomes is None:
            raise ValueError("outcomes is required")
        else:
            self.outcomes: OutcomeGroup = outcomes

        if outcome_weights is None:
            weight = 1.0 / len(list(self.outcomes))
            self.outcome_weights = [weight for _ in self.outcomes]
        else:
            # validate the number of outcome weights
            if len(outcome_weights) != len(list(self.outcomes)):
                raise ValueError(
                    f"Outcome weights must have {len(list(self.outcomes))} elements, but has {len(outcome_weights)}"
                )

            # validate that the outcome weights sum to 1.0
            total = sum(outcome_weights)
            if not math.isclose(total, 1.0):
                raise ValueError(f"Outcome weights must sum to 1.0, but sum to {total}")

            self.outcome_weights = outcome_weights

        logger.debug(f"Outcome weights: {self.outcome_weights}")

        self.policy: pd.DataFrame = None
        self.G: nx.DiGraph = nx.DiGraph()
        self.top: Tuple[int] = None
        self.bottom: Tuple[int] = None

        self._enumerated_vec = None
        self._check_valid_paths = validate

    def __enter__(self) -> "PolicyGenerator":
        """
        Sets up a policy generator runtime context.

        The runtime context performs the following steps in order:

        1. Converts the decision point group to a vector
        representation.
        2. Adds nodes to the graph. A node is represented as a tuple of decision point values as
        integers. E.g., `(0,1,0,2)`, `(1,2,1,3)`
        3. Adds edges to the graph where each edge $(u,v)$ indicates that $u < v$.
        4. Assigns outcomes to each node in the graph according to the outcome weights.
        5. Validates that the graph
        meets the requirement that outcome ordering is consistent with node ordering.
        6. Converts the graph to a policy table. The policy table is a dataframe where each row represents a node in
        the graph.

        !!! note "Node ordering"

            A node $u$ is considered less than another node $v$ if $u[i] <= v[i]$ for all $i$.


        Example:
            ```python
            with PolicyGenerator(dp_group, outcomes) as pg:
                pg.emit_policy()
            ```

        Returns:
            The policy generator context.
        """
        self._setup()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def _setup(self):
        """
        Convert the decision point group to a vector representation.
        """

        self._enumerate_dp_values()
        self._add_nodes()
        self._add_edges()
        self._assign_outcomes()
        if self._check_valid_paths:
            self._validate_paths()
        self._create_policy()

    def _validate_paths(self):
        for path in nx.all_simple_paths(self.G, self.bottom, self.top):
            for start, end in zip(path[:-1], path[1:]):
                u = self.G.nodes[start]["outcome"]
                v = self.G.nodes[end]["outcome"]
                if u > v:
                    raise (ValueError(f"Invalid path: {u} !<= {v} in {path}"))

    def _create_policy(self):
        rows = []
        for node in self.G.nodes:
            row = {}
            for i in range(len(node)):
                # turn the numerical indexes back into decision point names
                col1 = f"{self.dpg.decision_points[i].name}"
                row[col1] = self.dpg.decision_points[i].values[node[i]].name
                # numerical values
                col2 = f"idx_{self.dpg.decision_points[i].name}"
                row[col2] = node[i]

            oc_idx = self.G.nodes[node]["outcome"]
            row["outcome"] = self.outcomes.outcomes[oc_idx].name

            row["idx_outcome"] = oc_idx
            rows.append(row)

        self.policy = pd.DataFrame(rows)

    def clean_policy(self) -> pd.DataFrame:
        df = self.policy.copy()
        print_cols = [c for c in df.columns if not c.startswith("idx_")]
        for c in print_cols:
            df[c] = df[c].str.lower()

        return pd.DataFrame(df[print_cols])

    def emit_policy(self) -> None:
        """
        Prints the policy to stdout in CSV format.
        """
        df = self.clean_policy()

        print(df.to_csv(index=False))

    def _assign_outcomes(self):
        node_count = len(self.G.nodes)
        outcomes = [outcome.name for outcome in self.outcomes.outcomes]
        logger.debug(f"Outcomes: {outcomes}")

        layers = list(nx.topological_generations(self.G))
        logger.debug(f"Layer count: {len(layers)}")
        logger.debug(f"Layer sizes: {[len(layer) for layer in layers]}")

        outcome_counts = [round(node_count * weight) for weight in self.outcome_weights]

        toposort = list(nx.topological_sort(self.G))
        logger.debug(f"Toposort: {toposort[:4]}...{toposort[-4:]}")

        outcome_idx = 0
        assigned_counts = [0 for _ in self.outcomes.outcomes]
        for node in toposort:
            # step through the nodes in topological order
            # and assign outcomes to each node
            self.G.nodes[node]["outcome"] = outcome_idx
            assigned_counts[outcome_idx] += 1

            # if we've assigned enough of this outcome, move on to the next outcome
            if (
                outcome_idx < (len(self.outcomes.outcomes))
                and outcome_counts[outcome_idx] <= assigned_counts[outcome_idx]
            ):
                outcome_idx += 1

        logger.debug(f"Expected counts: {dict(zip(outcomes,outcome_counts))}")
        logger.debug(f"Assigned counts: {dict(zip(outcomes,assigned_counts))}")

    def _add_edges(self):
        # for each node, create an edge to the next node if the next node is strictly greater than the current node
        for u, v in itertools.product(self.G.nodes, self.G.nodes):
            if u == v:
                # don't create an edge from a node to itself
                continue

            # if the next node has at least one value greater than the current node
            if all(u[i] <= v[i] for i in range(len(u))):
                # then create an edge from the current node to the next node
                self.G.add_edge(u, v)

        # the previous loop creates a much larger graph than we need
        # so replace it with the transitive reduction of the graph
        logger.debug(f"Edge count (pre-reduction): {len(self.G.edges)}")
        self.G = nx.transitive_reduction(self.G)
        logger.info(f"Edge count: {len(self.G.edges)}")

    def _add_nodes(self):
        # then get the cartesian product of the values
        # so [[0,1,2],[0,1],[0,1,2]] becomes
        # [[0,0,0],[0,0,1],[0,0,2],[0,1,0],[0,1,1],[0,1,2]]
        vec = self._enumerated_vec

        self.bottom = tuple([min(t) for t in vec])
        self.top = tuple([max(t) for t in vec])

        logger.debug(f"Top node: {self.top}")
        logger.debug(f"Bottom node: {self.bottom}")

        # add a node for each cartesian product of the elements of vec
        for node in itertools.product(*vec):
            node = tuple(node)
            self.G.add_node(node)

        node_count = len(self.G.nodes)
        logger.info(f"Node count: {node_count}")
        return node_count

    def _enumerate_dp_values(self):
        # for each decision point in the group, get an enumeration of the values
        # so [[a,b,c],[d,e],[f,g,h]] becomes [[0,1,2],[0,1],[0,1,2]]
        vec = []
        for dp in self.dpg.decision_points:
            vec.append(tuple(range(len(dp.values))))

        logger.debug(f"Enumerated vector: {vec}")

        self._enumerated_vec = vec


def main():
    from ssvc.decision_points.automatable import AUTOMATABLE_1
    from ssvc.decision_points.exploitation import EXPLOITATION_1
    from ssvc.decision_points.human_impact import HUMAN_IMPACT_1
    from ssvc.decision_points.system_exposure import SYSTEM_EXPOSURE_1_0_1
    from ssvc.outcomes.groups import DSOI

    # set up logging
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    hdlr = logging.StreamHandler()
    logger.addHandler(hdlr)

    dpg = SsvcDecisionPointGroup(
        name="Dummy Decision Point Group",
        description="Dummy decision point group",
        version="1.0.0",
        decision_points=[
            EXPLOITATION_1,
            SYSTEM_EXPOSURE_1_0_1,
            AUTOMATABLE_1,
            HUMAN_IMPACT_1,
        ],
    )

    with PolicyGenerator(
        dp_group=dpg, outcomes=DSOI, outcome_weights=[0.097, 0.583, 0.278, 0.042]
    ) as pg:
        pg.emit_policy()

    # check policy against csv_analyzer
    df = pg.clean_policy()
    imp = csv_analyzer.drop_col_feature_importance(df, "outcome")

    print(imp)


if __name__ == "__main__":
    main()
