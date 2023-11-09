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

import unittest

import ssvc.dp_groups.base as dpg
from ssvc.decision_points import SsvcDecisionPointValue


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.dps = []
        for i in range(10):
            dp = dpg.SsvcDecisionPoint(
                name=f"Decision Point {i}",
                key=f"DP_{i}",
                description=f"Description of Decision Point {i}",
                version="1.0.0",
                values=(
                    SsvcDecisionPointValue(name="foo", key="FOO", description="foo"),
                    SsvcDecisionPointValue(name="bar", key="BAR", description="bar"),
                    SsvcDecisionPointValue(name="baz", key="BAZ", description="baz"),
                ),
            )
            self.dps.append(dp)

    def tearDown(self) -> None:
        pass

    def test_iter(self):
        # add them to a decision point group
        g = dpg.SsvcDecisionPointGroup(
            name="Test Group", description="Test Group", decision_points=self.dps
        )

        self.assertTrue(hasattr(g, "__iter__"))

        # iterate over the group
        for dp in g:
            self.assertIn(dp, self.dps)

    def test_len(self):
        # add them to a decision point group
        g = dpg.SsvcDecisionPointGroup(
            name="Test Group", description="Test Group", decision_points=self.dps
        )

        self.assertEqual(len(self.dps), len(g.decision_points))
        self.assertEqual(len(self.dps), len(g))

    def test_json_roundtrip(self):
        # add them to a decision point group
        g = dpg.SsvcDecisionPointGroup(
            name="Test Group", description="Test Group", decision_points=self.dps
        )

        # serialize the group to json
        g_json = g.to_json()

        # deserialize the json to a new group
        g2 = dpg.SsvcDecisionPointGroup.from_json(g_json)
        # assert that the new group is the same as the old group
        self.assertEqual(g.to_dict(), g2.to_dict())


if __name__ == "__main__":
    unittest.main()
