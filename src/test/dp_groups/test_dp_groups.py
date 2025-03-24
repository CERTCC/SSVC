#  Copyright (c) 2023-2025 Carnegie Mellon University and Contributors.
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

import ssvc.decision_points.ssvc_.base
import ssvc.dp_groups.base as dpg
from ssvc.decision_points.base import DecisionPointValue


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.dps = []
        for i in range(10):
            dp = ssvc.decision_points.ssvc_.base.SsvcDecisionPoint(
                name=f"Decision Point {i}",
                key=f"DP_{i}",
                description=f"Description of Decision Point {i}",
                version="1.0.0",
                values=(
                    DecisionPointValue(name="foo", key="FOO", description="foo"),
                    DecisionPointValue(name="bar", key="BAR", description="bar"),
                    DecisionPointValue(name="baz", key="BAZ", description="baz"),
                ),
            )
            self.dps.append(dp)

    def tearDown(self) -> None:
        pass

    def test_iter(self):
        # add them to a decision point group
        g = dpg.SsvcDecisionPointGroup(
            name="Test Group",
            description="Test Group",
            decision_points=self.dps,
        )

        self.assertTrue(hasattr(g, "__iter__"))

        # iterate over the group
        for dp in g:
            self.assertIn(dp, self.dps)

    def test_len(self):
        # add them to a decision point group
        g = dpg.SsvcDecisionPointGroup(
            name="Test Group",
            description="Test Group",
            decision_points=self.dps,
        )

        self.assertGreater(len(self.dps), 0)
        self.assertEqual(len(self.dps), len(list(g.decision_points)))
        self.assertEqual(len(self.dps), len(g))

    def test_combo_strings(self):
        # add them to a decision point group
        g = dpg.SsvcDecisionPointGroup(
            name="Test Group",
            description="Test Group",
            decision_points=self.dps,
        )

        # get all the combinations
        combos = list(g.combination_strings())

        # assert that the number of combinations is the product of the number of values
        # for each decision point
        n_combos = 1
        for dp in self.dps:
            n_combos *= len(dp.values)
        self.assertEqual(n_combos, len(combos))

        # assert that each combination is a tuple
        for combo in combos:
            self.assertEqual(len(self.dps), len(combo))
            self.assertIsInstance(combo, tuple)
            # assert that each value in the combination is a string
            for value in combo:
                self.assertIsInstance(value, str)
            # foo, bar, and baz should be in each combination to some degree
            foo_count = sum(1 for v in combo if v.endswith("FOO"))
            bar_count = sum(1 for v in combo if v.endswith("BAR"))
            baz_count = sum(1 for v in combo if v.endswith("BAZ"))
            for count in (foo_count, bar_count, baz_count):
                # each count should be greater than or equal to 0
                self.assertGreaterEqual(count, 0)
                # each count should be less than or equal to the length of the combination
                self.assertLessEqual(count, len(combo))
            # the total count of foo, bar, and baz should be the same as the length of the combination
            # indicating that no other values are present
            total = sum((foo_count, bar_count, baz_count))
            self.assertEqual(len(combo), total)

    def test_json_roundtrip(self):
        # add them to a decision point group
        g = dpg.SsvcDecisionPointGroup(
            name="Test Group",
            description="Test Group",
            decision_points=self.dps,
        )

        # serialize the group to json
        g_json = g.model_dump_json()

        # deserialize the json to a new group
        g2 = dpg.SsvcDecisionPointGroup.model_validate_json(g_json)
        # assert that the new group is the same as the old group
        self.assertEqual(g_json, g2.model_dump_json())


if __name__ == "__main__":
    unittest.main()
