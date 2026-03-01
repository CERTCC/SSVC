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

import itertools
import math
import unittest
from unittest.mock import patch

import networkx as nx

import ssvc.utils.graph_labeling


def _diff(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:

    if len(a) != len(b):
        raise ValueError("Tuples must be of the same length")

    d = [x - y for x, y in zip(a, b)]
    return tuple(d)


def _all_but_one_zero(t: tuple[int, ...]) -> bool:
    """
    Check if all elements in the tuple are zero except for one element.
    """
    non_zero_count = sum(1 for x in t if x != 0)
    return non_zero_count == 1 and len(t) > 1


def _exactly_one_one(t: tuple[int, ...]) -> bool:
    """
    Check if exactly one element in the tuple is one.
    """
    one_count = sum(1 for x in t if x == 1)
    return one_count == 1 and len(t) > 1


def _off_by_one(t: tuple[int, ...]) -> bool:
    """
    Returns true if exactly one element in the tuple is one and all others are zero.
    Args:
        t: the tuple to check

    Returns:
        bool: True if the tuple is off by one, False otherwise

    """
    if _all_but_one_zero(t) and _exactly_one_one(t):
        return True
    return False


class MyTestCase(unittest.TestCase):
    def setUp(self):
        from ssvc.decision_points.base import DecisionPoint, DecisionPointValue

        self.dp1 = DecisionPoint(
            namespace="test",
            name="Decision Point 1",
            key="DP1",
            version="1.0.0",
            definition="Test DP 1",
            values=[
                DecisionPointValue(
                    name="Value 1", key="V1", definition="value 1 description"
                ),
                DecisionPointValue(
                    name="Value 2", key="V2", definition="value 2 description"
                ),
            ],
        )
        self.dp2 = DecisionPoint(
            namespace="test",
            name="Decision Point 2",
            key="DP2",
            version="1.0.0",
            definition="Test DP 2",
            values=[
                DecisionPointValue(
                    name="Value A", key="VA", definition="value A description"
                ),
                DecisionPointValue(
                    name="Value B", key="VB", definition="value B description"
                ),
            ],
        )

        self.decision_points = [self.dp1, self.dp2]

    def tearDown(self):
        pass

    def test_diff(self):
        a = (1, 2, 3)
        b = (3, 2, 1)
        expected = (-2, 0, 2)
        result = _diff(a, b)
        self.assertIsInstance(result, tuple)
        self.assertEqual(result, expected)

    def test_diff_length_mismatch(self):
        a = (1, 2)
        b = (3, 2, 1)
        with self.assertRaises(ValueError):
            _diff(a, b)

    def test_all_but_one_zero(self):
        t1 = (0, 0, 1)
        t2 = (0, 0, 0)
        t3 = (1, 0, 0)
        t4 = (1, 1, 0)
        self.assertTrue(_all_but_one_zero(t1))
        self.assertFalse(_all_but_one_zero(t2))
        self.assertTrue(_all_but_one_zero(t3))
        self.assertFalse(_all_but_one_zero(t4))

    def test_exactly_one_one(self):
        t1 = (0, 0, 1)
        t2 = (0, 0, 0)
        t3 = (1, 0, 0)
        t4 = (1, 1, 0)
        self.assertTrue(_exactly_one_one(t1))
        self.assertFalse(_exactly_one_one(t2))
        self.assertTrue(_exactly_one_one(t3))
        self.assertFalse(_exactly_one_one(t4))

    def test_off_by_one(self):
        t1 = (0, 0, 1)
        t2 = (0, 0, 0)
        t3 = (1, 0, 0)
        t4 = (1, 1, 0)
        t5 = (2, 0, 0)
        self.assertTrue(_off_by_one(t1))
        self.assertFalse(_off_by_one(t2))
        self.assertTrue(_off_by_one(t3))
        self.assertFalse(_off_by_one(t4))
        self.assertFalse(_off_by_one(t5))

    def test_normalize_columns(self):
        import numpy as np
        from itertools import product

        column_1 = [0, 1]
        column_2 = [0, 1, 2]
        column_3 = [0, 1, 2, 3]
        column_4 = [0, 1, 2, 3, 4]
        columns = [column_1, column_2, column_3, column_4]

        data = np.array(list(product(*columns)))

        # confirm shape is as expected before normalization
        from math import prod

        n_rows = prod([len(c) for c in columns])
        n_cols = len(columns)
        self.assertEqual(data.shape, (n_rows, n_cols))

        normalized = ssvc.utils.graph_labeling._normalize_columns(data)

        # confirm normalized shape is the same
        self.assertEqual(normalized.shape, data.shape)

        # confirm normalized is an array of floats
        self.assertEqual(normalized.dtype, float)

        # confirm min of each column is 0.0
        np.testing.assert_array_almost_equal(
            normalized.min(axis=0), np.zeros(n_cols)
        )

        # confirm max of each column is 1.0
        np.testing.assert_array_almost_equal(
            normalized.max(axis=0), np.ones(n_cols)
        )

        expected = np.array(
            list(
                product(
                    [0.0, 1.0],
                    [0.0, 0.5, 1.0],
                    [0.0, 0.33333333, 0.66666667, 1.0],
                    [0.0, 0.25, 0.5, 0.75, 1.0],
                )
            )
        )
        self.assertEqual(data.shape, expected.shape)

        # confirm values are almost equal
        np.testing.assert_array_almost_equal(normalized, expected)

    def test_magnitude_quantile_labels_from_graph(self):

        value_ranges = [3, 2, 4]  # keep these small for testing
        values = [tuple(range(r)) for r in value_ranges]

        G = ssvc.utils.graph_labeling.graph_from_value_tuples(values)

        K = 4  # number of quantiles

        expected_node_count = math.prod(value_ranges)
        self.assertEqual(len(G.nodes), expected_node_count)

        min_node = tuple(0 for _ in values)
        max_node = tuple(len(v) - 1 for v in values)

        self.assertIn(min_node, G.nodes)
        self.assertIn(max_node, G.nodes)

        # in-degree of min_node should be 0
        self.assertEqual(G.in_degree(min_node), 0)
        # out-degree of min_node should be > 0
        self.assertGreater(G.out_degree(min_node), 0)

        # in-degree of max_node should be > 0
        self.assertGreater(G.in_degree(max_node), 0)
        # out-degree of max_node should be 0
        self.assertEqual(G.out_degree(max_node), 0)

        labels = (
            ssvc.utils.graph_labeling._magnitude_quantile_labels_from_graph(
                G=G,
                K=K,
                norm_func=ssvc.utils.graph_labeling.euclidean_distances,
            )
        )

        self.assertIsInstance(labels, dict)
        self.assertEqual(len(labels), len(G.nodes))

        # check that all labels are in the expected range
        for node, label in labels.items():
            self.assertIn(node, G.nodes)
            self.assertIsInstance(label, int)
            self.assertGreaterEqual(label, 0)
            self.assertLess(label, K)

        # for each pair of nodes, check that if one is off by one from the other,
        # the label of the one with the higher magnitude is greater than or equal to the other
        for u, v in itertools.product(G.nodes(), G.nodes()):
            if _off_by_one(_diff(u, v)):
                mag_u = math.sqrt(sum(x**2 for x in u))
                mag_v = math.sqrt(sum(x**2 for x in v))
                if mag_u >= mag_v:
                    self.assertGreaterEqual(
                        labels[u],
                        labels[v],
                        f"Expected label of {u} ({labels[u]}) to be >= label of {v} ({labels[v]})",
                    )
                else:
                    self.assertGreaterEqual(
                        labels[v],
                        labels[u],
                        f"Expected label of {v} ({labels[v]}) to be >= label of {u} ({labels[u]})",
                    )

        # every path through G should have non-decreasing labels
        for path in nx.all_simple_paths(G, source=min_node, target=max_node):
            path_labels = [labels[node] for node in path]
            for i in range(len(path_labels) - 1):
                self.assertLessEqual(
                    path_labels[i],
                    path_labels[i + 1],
                    f"Expected non-decreasing labels along path, but found {path_labels[i]} > {path_labels[i + 1]}",
                )

    @patch("ssvc.utils.graph_labeling.graph_from_value_tuples")
    def test_graph_from_dplist(self, mock_graph_from_value_tuples):
        mock_graph_from_value_tuples.return_value = nx.DiGraph()

        result = ssvc.utils.graph_labeling.graph_from_dplist(
            self.decision_points
        )

        self.assertIsInstance(result, nx.DiGraph)

        mock_graph_from_value_tuples.assert_called_once_with(
            [
                tuple(range(len(self.dp1.values))),
                tuple(range(len(self.dp2.values))),
            ]
        )

        pass

    def test_graph_from_value_tuples(self):
        # keep these ranges small for testing
        # because we're going to do a full cartesian product
        # and then square that for testing edges
        # so (3 * 2 * 2) ** 2 = 144 edges
        values = [tuple(range(3)), tuple(range(2)), tuple(range(2))]

        node_count = math.prod([len(v) for v in values])

        G = ssvc.utils.graph_labeling.graph_from_value_tuples(values)
        self.assertIsInstance(G, nx.DiGraph)
        self.assertEqual(
            len(G.nodes), node_count
        )  # 3! = 6, 2! = 2, 2! = 2, total = 6 + 2 + 2 = 10

        for u, v in itertools.product(G.nodes(), G.nodes()):
            if _off_by_one(_diff(u, v)):
                # edges should point from v to u
                self.assertTrue(
                    G.has_edge(v, u),
                    f"Expected edge from {u} to {v} but it does not exist.",
                )
            else:
                # edges should not point from v to u
                self.assertFalse(
                    G.has_edge(v, u),
                    f"Expected no edge from {u} to {v} but it exists.",
                )

    def test_dplist_to_value_lookup(self):
        value_lookup = ssvc.utils.graph_labeling.dplist_to_value_lookup(
            self.decision_points
        )

        expected = [
            {0: self.dp1.values[0].key, 1: self.dp1.values[1].key},
            {0: self.dp2.values[0].key, 1: self.dp2.values[1].key},
        ]
        self.assertEqual(value_lookup, expected)


if __name__ == "__main__":
    unittest.main()
