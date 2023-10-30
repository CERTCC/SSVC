#!/usr/bin/env python
"""
Provides a Policy Generator class for SSVC decision point groups
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
from typing import List, Tuple

import networkx as nx
import pandas as pd

from ssvc.dp_groups.base import SsvcDecisionPointGroup
from ssvc.outcomes.base import OutcomeGroup

logger = logging.getLogger(__name__)


class PolicyGenerator:
    def __init__(
        self,
        dp_group: SsvcDecisionPointGroup = None,
        outcomes: OutcomeGroup = None,
        outcome_weights: List[float] = None,
    ):
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
            self.outcome_weights = outcome_weights
        logger.debug(f"Outcome weights: {self.outcome_weights}")

        self.policy: pd.DataFrame = None
        self.G: nx.DiGraph = nx.DiGraph()
        self.top: Tuple[int] = None
        self.bottom: Tuple[int] = None

        self._enumerated_vec = None

    def __enter__(self) -> "PolicyGenerator":
        """
        Set up the policy generator.

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

    def emit_policy(self):
        df = self.policy.copy()
        print_cols = [c for c in df.columns if not c.startswith("idx_")]
        for c in print_cols:
            df[c] = df[c].str.lower()

        print(df[print_cols].to_csv(index=False))

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
    from ssvc.outcomes.groups import DSIO

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
        dp_group=dpg, outcomes=DSIO, outcome_weights=[0.097, 0.583, 0.278, 0.042]
    ) as pg:
        pg.emit_policy()


if __name__ == "__main__":
    main()
