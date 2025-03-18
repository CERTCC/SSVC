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

import unittest

import pandas as pd

from ssvc.decision_points.exploitation import LATEST as exploitation_dp
from ssvc.decision_points.safety_impact import LATEST as safety_dp
from ssvc.decision_points.system_exposure import LATEST as exposure_dp
from ssvc.decision_tables.base import DecisionTable
from ssvc.dp_groups.base import SsvcDecisionPointGroup
from ssvc.outcomes.groups import DSOI as dsoi_og


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.framework = DecisionTable(
            name="Test Prioritization Framework",
            description="Test Prioritization Framework Description",
            version="1.0.0",
            decision_point_group=SsvcDecisionPointGroup(
                name="Test Decision Point Group",
                description="Test Decision Point Group Description",
                decision_points=[exploitation_dp, exposure_dp, safety_dp],
            ),
            outcome_group=dsoi_og,
            mapping={},
        )

        pass

    def tearDown(self):
        pass

    def test_create(self):
        self.assertEqual(self.framework.name, "Test Prioritization Framework")
        self.assertEqual(3, len(self.framework.decision_point_group))
        # mapping should not be empty
        self.assertGreater(len(self.framework.mapping), 0)

    def test_generate_mapping(self):
        result = self.framework.generate_df()

        # there should be one row in result for each combination of decision points
        combo_count = len(list(self.framework.decision_point_group.combinations()))
        self.assertEqual(len(result), combo_count)

        # the length of each key should be the number of decision points
        for key in result.keys():
            parts = key.split(",")
            self.assertEqual(len(parts), 3)
            for i, keypart in enumerate(parts):
                dp_namespace, dp_key, dp_value_key = keypart.split(":")

                dp = self.framework.decision_point_group.decision_points[i]
                self.assertEqual(dp_namespace, dp.namespace)
                self.assertEqual(dp_key, dp.key)
                value_keys = [v.key for v in dp.values]
                self.assertIn(dp_value_key, value_keys)

    def test_mapping_to_table(self):
        d = {
            "ssvc:One:A,ssvc:Two:B,ssvc:Three:C": "og:One",
            "ssvc:One:A,ssvc:Two:B,ssvc:Three:D": "og:Two",
        }
        table = self.framework.mapping_to_table(d)

        # is it a DataFrame?
        self.assertIsInstance(table, pd.DataFrame)
        self.assertEqual(2, len(table))
        self.assertEqual(4, len(table.columns))

        # does it have the right columns?
        self.assertEqual(["one", "two", "three", "og"], list(table.columns))
        # does it have the right values?
        for i, (k, v) in enumerate(d.items()):
            k = k.lower()
            v = v.lower()

            parts = k.split(",")
            for part in parts:
                (ns, dp, val) = part.split(":")
                self.assertEqual(val, table.iloc[i][dp])


if __name__ == "__main__":
    unittest.main()
