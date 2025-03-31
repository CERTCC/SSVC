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
import tempfile
import unittest

import pandas as pd
from pandas import DataFrame

from ssvc.decision_points.base import (
    DP_REGISTRY,
    DecisionPoint,
    DecisionPointValue,
)
from ssvc.decision_tables import base
from ssvc.dp_groups.base import DecisionPointGroup
from ssvc.outcomes.base import OutcomeValue


class TestDecisionTable(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.tempdir_path = self.tempdir.name

        DP_REGISTRY.clear()

        dps = []
        for i in range(3):
            dpvs = []
            for j in range(3):
                dpv = DecisionPointValue(
                    name=f"Value {i}{j}",
                    key=f"DP{i}V{j}",
                    description=f"Decision Point {i} Value {j} Description",
                )
                dpvs.append(dpv)

            dp = DecisionPoint(
                name=f"Decision Point {i}",
                key=f"DP{i}",
                description=f"Decision Point {i} Description",
                version="1.0.0",
                namespace="x_test",
                values=tuple(dpvs),
            )
            dps.append(dp)

        self.dpg = DecisionPointGroup(
            name="Decision Point Group",
            description="Decision Point Group description",
            decision_points=tuple(dps),
        )

        ogvs = []
        for i in range(3):
            ogv = OutcomeValue(
                name=f"Outcome Value {i}",
                key=f"OV{i}",
                description=f"Outcome Value {i} description",
            )
            ogvs.append(ogv)

        self.og = DecisionPoint(
            name="Outcome Group",
            key="OG",
            description="Outcome Group description",
            namespace="x_test",
            values=tuple(ogvs),
        )

        self.dt = base.DecisionTable(
            name="foo",
            description="foo description",
            namespace="x_test",
            decision_point_group=self.dpg,
            outcome_group=self.og,
        )

    def tearDown(self):
        self.tempdir.cleanup()

    def test_create(self):
        # self.dt exists in setUp
        self.assertEqual(self.dt.name, "foo")
        self.assertEqual(self.dt.description, "foo description")
        self.assertEqual(self.dt.namespace, "x_test")
        self.assertEqual(self.dt.decision_point_group, self.dpg)
        self.assertEqual(self.dt.outcome_group, self.og)

    def test_get_mapping_df(self):
        df = self.dt.get_mapping_df()
        self.assertIsInstance(df, DataFrame)

        # df is not empty
        self.assertFalse(df.empty)
        # df has some rows
        self.assertGreater(len(df), 0)
        # df has the same number of rows as the product of the number of decision points and their values
        combos = list(self.dpg.combination_strings())
        self.assertGreater(len(combos), 0)
        self.assertEqual(len(df), len(combos))

        # column names are the decision point strings and the outcome group string
        for i, dp in enumerate(self.dpg.decision_points):
            self.assertEqual(dp.str, df.columns[i])
        self.assertEqual(self.og.str, df.columns[-1])

        for col in df.columns:
            # col is in the registry
            self.assertIn(col, DP_REGISTRY)

            dp = DP_REGISTRY[col]

            uniq = df[col].unique()

            # all values in the decision point should be in the column at least once
            for vsum in dp.value_summaries_str:
                self.assertIn(vsum, uniq)

    def test_dataframe_to_tuple_list(self):
        df = pd.DataFrame(
            [
                {"a": 1, "b": 2, "c": 3},
                {"a": 4, "b": 5, "c": 6},
                {"a": 7, "b": 8, "c": 9},
            ]
        )

        tuple_list = self.dt.dataframe_to_tuple_list(df)

        self.assertEqual(len(tuple_list), len(df))

        for row in tuple_list:
            self.assertIsInstance(row, tuple)
            self.assertEqual(len(row), 2)
            self.assertIsInstance(row[0], tuple)
            self.assertIsInstance(row[1], tuple)

        # manually check the structure of the tuple list
        self.assertEqual((1, 2), tuple_list[0][0])
        self.assertEqual((3,), tuple_list[0][1])
        self.assertEqual((4, 5), tuple_list[1][0])
        self.assertEqual((6,), tuple_list[1][1])
        self.assertEqual((7, 8), tuple_list[2][0])
        self.assertEqual((9,), tuple_list[2][1])

    def test_set_mapping(self):
        df = pd.DataFrame(
            {
                "a": ["x", "y", "z"],
                "b": ["one", "two", "three"],
                "c": ["apple", "orange", "pear"],
            }
        )

        result = self.dt.set_mapping(df)

        self.assertIn((("x", "one"), ("apple",)), result)
        self.assertIn((("y", "two"), ("orange",)), result)
        self.assertIn((("z", "three"), ("pear",)), result)

        self.assertEqual(result, self.dt.mapping)

    @unittest.skip("Test not implemented")
    def test_consistency_check_mapping(self):
        pass

    @unittest.skip("Test not implemented")
    def test_check_decision_boundaries(self):
        pass

    @unittest.skip("Test not implemented")
    def test_find_decision_boundaries(self):
        pass

    @unittest.skip("Test not implemented")
    def test_int_node_to_str(self):
        pass

    @unittest.skip("Test not implemented")
    def test_check_graph(self):
        pass

    @unittest.skip("Test not implemented")
    def test_add_nodes(self):
        pass

    @unittest.skip("Test not implemented")
    def test_add_edges(self):
        pass

    def test_mapping_to_csv_str(self):
        df = self.dt.get_mapping_df()
        self.dt.set_mapping(df)

        csv_str = self.dt.mapping_to_csv_str()
        self.assertIsInstance(csv_str, str)

        lines = csv_str.strip().split("\n")

        # first line is the header
        self.assertEqual(
            lines[0],
            ",".join([dp.str for dp in self.dpg.decision_points] + [self.og.str]),
        )

        combinations = list(self.dpg.combination_strings())

        # there should be one line for each combination after the header
        self.assertEqual(len(lines[1:]), len(combinations))

        # each line after the header starts with a combination of decision point values
        for combo, line in zip(combinations, lines[1:]):
            # there are as many commas in the line as there are combos
            comma_count = line.count(",")
            self.assertEqual(comma_count, len(combo))

            for dpv_str in combo:
                self.assertIn(dpv_str, line)

            # the last thing in the line is the outcome group value
            og_value = line.split(",")[-1]
            self.assertIn(og_value, self.og.value_summaries_str)

    @unittest.skip("Test not implemented")
    def test_load_from_csv_str(self):
        pass


if __name__ == "__main__":
    unittest.main()
