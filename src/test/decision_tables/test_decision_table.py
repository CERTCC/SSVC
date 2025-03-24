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

from ssvc.decision_points.base import DecisionPoint, DecisionPointValue
from ssvc.decision_tables import base
from ssvc.dp_groups.base import DecisionPointGroup
from ssvc.outcomes.base import OutcomeValue


class TestDecisionTables(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.tempdir_path = self.tempdir.name

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


if __name__ == "__main__":
    unittest.main()
