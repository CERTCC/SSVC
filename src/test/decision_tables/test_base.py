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


if __name__ == "__main__":
    unittest.main()
