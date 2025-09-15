#  Copyright (c) 2023-2025 Carnegie Mellon University.
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

import unittest
from collections import Counter
from itertools import product

import networkx as nx
import pandas as pd

from ssvc.decision_points.base import DecisionPoint, DecisionPointValue
from ssvc.dp_groups.base import DecisionPointGroup
from ssvc.policy_generator import PolicyGenerator


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.og_names = ["Never", "Someday", "Today", "Now"]
        self.dp_values = ["Yes", "No"]
        self.dp_names = ["Who", "What", "When", "Where"]

        self.og = DecisionPoint(
            name="test",
            definition="test",
            key="TEST",
            namespace="test",
            values=tuple(
                [
                    DecisionPointValue(key=c, name=c, definition=c)
                    for c in self.og_names
                ]
            ),
        )
        self.dpg = DecisionPointGroup(
            name="test",
            definition="test",
            decision_points=tuple(
                [
                    DecisionPoint(
                        name=c,
                        definition=c,
                        key=c,
                        namespace="test",
                        values=tuple(
                            [
                                DecisionPointValue(name=v, key=v, definition=v)
                                for v in self.dp_values
                            ]
                        ),
                    )
                    for c in self.dp_names
                ]
            ),
        )

    def test_pg_init(self):
        self.assertEqual(4, len(self.dpg.decision_points))
        self.assertEqual(4, len(self.og.values))

        pg = PolicyGenerator(dp_group=self.dpg, outcomes=self.og)
        for w in pg.outcome_weights:
            self.assertEqual(0.25, w)

        self.assertIsInstance(
            pg.G,
            nx.DiGraph,
        )
        self.assertIsNone(pg.policy)
        self.assertIsNone(pg.top)
        self.assertIsNone(pg.bottom)

    def test_pg_context(self):
        with PolicyGenerator(dp_group=self.dpg, outcomes=self.og) as pg:
            self.assertIsInstance(
                pg.G,
                nx.DiGraph,
            )
            self.assertIsNotNone(pg.policy)
            self.assertIsNotNone(pg.top)
            self.assertIsNotNone(pg.bottom)

    def test_enumerate_dp_values(self):
        pg = PolicyGenerator(dp_group=self.dpg, outcomes=self.og)

        self.assertIsNone(pg._enumerated_vec)

        pg._enumerate_dp_values()
        self.assertEqual(4, len(pg._enumerated_vec))

        for t in pg._enumerated_vec:
            self.assertEqual(2, len(t))
            self.assertEqual((0, 1), t)

    def test_add_nodes(self):
        pg = PolicyGenerator(dp_group=self.dpg, outcomes=self.og)
        pg._enumerated_vec = [(0, 1), (0, 1, 2), (0, 1), (0, 1, 2, 3)]

        self.assertIsNone(pg.bottom)
        self.assertIsNone(pg.top)
        self.assertEqual(0, len(pg.G.nodes))

        pg._add_nodes()

        prod = 1
        for t in pg._enumerated_vec:
            prod *= len(t)

        self.assertEqual(prod, len(pg.G.nodes))

        self.assertEqual((0, 0, 0, 0), pg.bottom)
        self.assertEqual((1, 2, 1, 3), pg.top)

        self.assertIn(pg.bottom, pg.G.nodes)
        self.assertIn(pg.top, pg.G.nodes)

        for i in range(2):
            for j in range(3):
                for k in range(2):
                    for l in range(4):
                        self.assertIn((i, j, k, l), pg.G.nodes)

        self.assertNotIn((2, 0, 0, 0), pg.G.nodes)
        self.assertNotIn((0, 3, 0, 0), pg.G.nodes)
        self.assertNotIn((0, 0, 2, 0), pg.G.nodes)
        self.assertNotIn((0, 0, 0, 4), pg.G.nodes)

    def test_add_edges(self):
        pg = PolicyGenerator(dp_group=self.dpg, outcomes=self.og)
        for i, j, k in product(range(2), range(3), range(2)):
            pg.G.add_node((i, j, k))

        self.assertEqual(0, len(pg.G.edges))

        pg._add_edges()

        expect_edges = [
            ((0, 0, 0), (1, 0, 0)),
            ((0, 0, 0), (0, 1, 0)),
            ((0, 0, 0), (0, 0, 1)),
            ((0, 0, 1), (1, 0, 1)),
            ((0, 0, 1), (0, 1, 1)),
            ((0, 1, 0), (1, 1, 0)),
            ((0, 1, 0), (0, 2, 0)),
            ((0, 1, 0), (0, 1, 1)),
            ((0, 1, 1), (0, 2, 1)),
            ((0, 1, 1), (1, 1, 1)),
            ((0, 2, 0), (0, 2, 1)),
            ((0, 2, 0), (1, 2, 0)),
            ((0, 2, 1), (1, 2, 1)),
            ((1, 0, 0), (1, 0, 1)),
            ((1, 0, 0), (1, 1, 0)),
            ((1, 0, 1), (1, 1, 1)),
            ((1, 1, 0), (1, 1, 1)),
            ((1, 1, 0), (1, 2, 0)),
            ((1, 1, 1), (1, 2, 1)),
            ((1, 2, 0), (1, 2, 1)),
        ]
        self.assertEqual(len(expect_edges), len(pg.G.edges))

        for u, v in expect_edges:
            self.assertIn(u, pg.G.nodes)
            self.assertIn(v, pg.G.nodes)
            self.assertIn((u, v), pg.G.edges)

    def test_assign_outcomes(self):
        pg = PolicyGenerator(dp_group=self.dpg, outcomes=self.og)
        pg._enumerate_dp_values()
        pg._add_nodes()
        pg._add_edges()

        self.assertEqual(16, len(pg.G.nodes))
        self.assertEqual(32, len(pg.G.edges))

        for node, data in pg.G.nodes.items():
            self.assertNotIn("outcome", data)

        pg._assign_outcomes()

        outcomes = []
        for node, data in pg.G.nodes.items():
            self.assertIn("outcome", data)
            outcomes.append(data["outcome"])

        # count outcomes
        counts = Counter(outcomes)
        self.assertEqual(len(self.og), len(counts))

        # they should be evenly distributed
        self.assertTrue(all([v == 4 for v in counts.values()]))

    def test_assign_weighted_outcomes(self):
        pg = PolicyGenerator(
            dp_group=self.dpg,
            outcomes=self.og,
            outcome_weights=[0.5, 0.25, 0.125, 0.125],
        )
        pg._enumerate_dp_values()
        pg._add_nodes()
        pg._add_edges()

        self.assertEqual(16, len(pg.G.nodes))
        self.assertEqual(32, len(pg.G.edges))

        for node, data in pg.G.nodes.items():
            self.assertNotIn("outcome", data)

        pg._assign_outcomes()

        outcomes = []
        for node, data in pg.G.nodes.items():
            self.assertIn("outcome", data)
            outcomes.append(data["outcome"])

        # count outcomes
        counts = Counter(outcomes)
        self.assertEqual(len(self.og), len(counts))

        # they should be evenly distributed
        self.assertEqual({0: 8, 1: 4, 2: 2, 3: 2}, counts)

    def test_emit_policy(self):
        with PolicyGenerator(dp_group=self.dpg, outcomes=self.og) as pg:
            # capture stdout
            import io
            import contextlib

            f = io.StringIO()
            with contextlib.redirect_stdout(f):
                pg.emit_policy()

            stdout = f.getvalue()

            for dpg in pg.dpg.decision_points.values():
                self.assertIn(dpg.name, stdout)
            for og in pg.outcomes.values:
                self.assertIn(og.name, stdout)

    def test_create_policy(self):
        pg = PolicyGenerator(
            dp_group=self.dpg,
            outcomes=self.og,
            outcome_weights=[0.5, 0.25, 0.125, 0.125],
        )
        pg._enumerate_dp_values()
        pg._add_nodes()
        pg._add_edges()
        pg._assign_outcomes()
        pg._validate_paths()

        self.assertIsNone(pg.policy)

        pg._create_policy()

        self.assertIsNotNone(pg.policy)
        self.assertIsInstance(pg.policy, pd.DataFrame)
        self.assertEqual(16, len(pg.policy))

        idx_cols = [col for col in pg.policy.columns if col.startswith("idx_")]
        other_cols = [
            col for col in pg.policy.columns if not col.startswith("idx_")
        ]

        for c in self.dp_names:

            self.assertTrue(any([c in col for col in other_cols]))
            self.assertTrue(any([c in col for col in idx_cols]))

        self.assertIn("outcome", pg.policy.columns)
        self.assertIn("idx_outcome", pg.policy.columns)

        for outcome in self.og_names:
            self.assertTrue(
                any([outcome in val for val in pg.policy.outcome.values])
            )

    def test_validate_paths(self):
        pg = PolicyGenerator(
            dp_group=self.dpg,
            outcomes=self.og,
            outcome_weights=[0.5, 0.25, 0.125, 0.125],
        )
        pg._enumerate_dp_values()
        pg._add_nodes()
        pg._add_edges()
        pg._assign_outcomes()

        # should work fine and return None
        self.assertIsNone(pg._validate_paths())

        # unless we add a bad outcome value
        pg.G.nodes[(0, 0, 0, 0)]["outcome"] = 5

        with self.assertRaises(ValueError):
            pg._validate_paths()

    def test_is_topological_order(self):
        pg = PolicyGenerator(
            dp_group=self.dpg,
            outcomes=self.og,
        )
        # just replace the graph with one we make up here
        # 0 - 1 - 2 - 4 - 5
        #      \- 3 -/

        pg.G = nx.DiGraph()
        pg.G.add_edges_from([(0, 1), (1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])

        self.assertTrue(pg._is_topological_order([0, 1, 2, 3, 4, 5]))
        self.assertTrue(pg._is_topological_order([0, 1, 3, 2, 4, 5]))
        self.assertFalse(pg._is_topological_order([0, 1, 2, 4, 3, 5]))
        self.assertFalse(pg._is_topological_order([0, 1, 2, 3, 5]))

    def test_confirm_topological_order(self):
        pg = PolicyGenerator(
            dp_group=self.dpg,
            outcomes=self.og,
        )
        # just replace the graph with one we make up here
        # 0 - 1 - 2 - 4 - 5
        #      \- 3 -/

        pg.G = nx.DiGraph()
        pg.G.add_edges_from([(0, 1), (1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])

        self.assertIsNone(pg._confirm_topological_order([0, 1, 2, 3, 4, 5]))
        self.assertIsNone(pg._confirm_topological_order([0, 1, 3, 2, 4, 5]))
        self.assertRaises(
            ValueError, pg._confirm_topological_order, [0, 1, 2, 4, 3, 5]
        )
        self.assertRaises(
            ValueError, pg._confirm_topological_order, [0, 1, 2, 3, 5]
        )


if __name__ == "__main__":
    unittest.main()
