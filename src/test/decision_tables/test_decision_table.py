#  Copyright (c) 2025 Carnegie Mellon University and Contributors.
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
import tempfile
import unittest
from itertools import product

import pandas as pd

import ssvc.decision_points.ssvc_.base
from ssvc.decision_tables import base
from ssvc.decision_tables.base import name_to_key
from ssvc.dp_groups.base import SsvcDecisionPointGroup
from ssvc.outcomes.base import OutcomeGroup, OutcomeValue


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.tempdir_path = self.tempdir.name

        dps = []
        for i in range(3):
            dpvs = []
            for j in range(3):
                dpv = base.DecisionPointValue(
                    name=f"Value {i}{j}",
                    key=f"DP{i}V{j}",
                    description=f"Decision Point {i} Value {j} Description",
                )
                dpvs.append(dpv)

            dp = ssvc.decision_points.ssvc_.base.SsvcDecisionPoint(
                name=f"Decision Point {i}",
                key=f"DP{i}",
                description=f"Decision Point {i} Description",
                version="1.0.0",
                namespace="x_test",
                values=tuple(dpvs),
            )
            dps.append(dp)

        self.dpg = SsvcDecisionPointGroup(
            name="Decision Point Group",
            description="Decision Point Group description",
            decision_points=tuple(dps),
        )

        ogvs = []
        for i in range(3):
            ogv = OutcomeValue(
                name=f"Outcome Value {i}",
                key=f"ov{i}",
                description=f"Outcome Value {i} description",
            )
            ogvs.append(ogv)

        self.og = OutcomeGroup(
            name="Outcome Group",
            key="OG",
            description="Outcome Group description",
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

    def test_outcome_lookup(self):
        d = self.dt.outcome_lookup
        self.assertEqual(len(d), len(self.og.values))

        for i, v in enumerate(self.og.values):
            vname = name_to_key(v.name)
            self.assertEqual(d[vname], v)

    def test_dp_lookup(self):
        d = self.dt.dp_lookup
        self.assertEqual(len(d), len(self.dpg.decision_points))

        for i, dp in enumerate(self.dpg.decision_points):
            dpname = name_to_key(dp.name)
            self.assertEqual(d[dpname], dp)

    def test_dp_value_lookup(self):
        d = self.dt.dp_value_lookup
        for dp in self.dpg.decision_points:
            dpname = name_to_key(dp.name)
            self.assertEqual(len(d[dpname]), len(dp.values))

            for i, v in enumerate(dp.values):
                vname = name_to_key(v.name)
                self.assertEqual(d[dpname][vname], v)

    def test_populate_df(self):
        with self.subTest("df is set, no change"):
            data = {
                "a": [1, 2, 3],
                "b": [4, 5, 6],
                "c": [7, 8, 9],
            }
            df = pd.DataFrame(data)
            self.dt._df = df
            self.dt._populate_df()
            self.assertTrue(df.equals(self.dt._df))

        with self.subTest("df is None, populate"):
            self.dt._df = None
            self.dt._populate_df()
            self.assertFalse(df.equals(self.dt._df))
            self.assertIsNotNone(self.dt._df)
            self.assertIsInstance(self.dt._df, pd.DataFrame)

        with self.subTest("check df contents"):
            nrows = len(list(product(*[dp.values for dp in self.dpg.decision_points])))
            self.assertEqual(len(self.dt._df), nrows)
            ncols = len(self.dpg.decision_points) + 1
            self.assertEqual(len(self.dt._df.columns), ncols)

    def test_validate_mapping(self):
        with self.subTest("no problems"):
            self.dt.validate_mapping()

        with self.subTest("problems"):
            # set one of the outcomes out of order
            self.dt._df.iloc[0, -1] = self.og.values[-1].name
            with self.assertRaises(ValueError):
                self.dt.validate_mapping()


if __name__ == "__main__":
    unittest.main()
