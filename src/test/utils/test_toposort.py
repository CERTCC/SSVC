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

from ssvc.utils import toposort


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

    @patch("ssvc.utils.toposort.graph_from_value_tuples")
    def test_graph_from_dplist(self, mock_graph_from_value_tuples):
        mock_graph_from_value_tuples.return_value = nx.DiGraph()

        result = toposort.graph_from_dplist(self.decision_points)

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

        G = toposort.graph_from_value_tuples(values)
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
        value_lookup = toposort.dplist_to_value_lookup(self.decision_points)

        expected = [
            {0: self.dp1.values[0].key, 1: self.dp1.values[1].key},
            {0: self.dp2.values[0].key, 1: self.dp2.values[1].key},
        ]
        self.assertEqual(value_lookup, expected)

    def test_dplist_to_lookup(self):
        dp_lookup = toposort.dplist_to_lookup(self.decision_points)

        expected = {
            0: self.dp1.id,
            1: self.dp2.id,
        }
        self.assertEqual(dp_lookup, expected)

    def lookup_value(self):
        value_lookup = toposort.dplist_to_value_lookup(self.decision_points)
        t = (0, 1)
        result = toposort.lookup_value(t, value_lookup)
        expected = (self.dp1.values[0].key, self.dp2.values[1].key)
        self.assertEqual(result, expected)

    def test_tuple_to_dict(self):
        dp_lookup = toposort.dplist_to_lookup(self.decision_points)
        value_lookup = toposort.dplist_to_value_lookup(self.decision_points)

        nodes = list(
            itertools.product(
                range(len(self.dp1.values)), range(len(self.dp2.values))
            )
        )
        for node in nodes:
            node = tuple(node)
            vals = toposort.lookup_value(node, value_lookup)
            result = toposort.tuple_to_dict(vals, dp_lookup)

            expected = {
                self.dp1.id: self.dp1.values[node[0]].key,
                self.dp2.id: self.dp2.values[node[1]].key,
            }
            self.assertEqual(result, expected)

    def test_dplist_to_toposort(self):
        dplist = self.decision_points
        result = toposort.dplist_to_toposort(dplist)
        # result is a list of dicts of str:str
        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(item, dict) for item in result))
        self.assertTrue(
            all(
                isinstance(k, str) and isinstance(v, str)
                for item in result
                for k, v in item.items()
            )
        )

        # check the shape of the result
        # length of each dict should match the number of decision points
        self.assertTrue(all(len(item) == len(dplist) for item in result))
        # length of result should be the product of the number of values in each decision point
        expected_length = math.prod(len(dp.values) for dp in dplist)
        self.assertEqual(len(result), expected_length)

        # lowest item should be V1,VA
        expected_lowest = {
            self.dp1.id: self.dp1.values[0].key,
            self.dp2.id: self.dp2.values[0].key,
        }
        self.assertEqual(result[0], expected_lowest)

        # highest item should be V2,VB
        expected_highest = {
            self.dp1.id: self.dp1.values[-1].key,
            self.dp2.id: self.dp2.values[-1].key,
        }
        self.assertEqual(result[-1], expected_highest)


if __name__ == "__main__":
    unittest.main()
