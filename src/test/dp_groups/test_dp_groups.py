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

import ssvc.decision_points.ssvc.base
import ssvc.dp_groups.base as dpg
from ssvc.decision_points.base import DecisionPointValue


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.dps = []
        for i in range(10):
            dp = ssvc.decision_points.ssvc.base.DecisionPoint(
                name=f"Decision Point {i}",
                key=f"DP_{i}",
                namespace="test",
                definition=f"Description of Decision Point {i}",
                version="1.0.0",
                values=(
                    DecisionPointValue(
                        name="foo", key="FOO", definition="foo"
                    ),
                    DecisionPointValue(
                        name="bar", key="BAR", definition="bar"
                    ),
                    DecisionPointValue(
                        name="baz", key="BAZ", definition="baz"
                    ),
                ),
            )
            self.dps.append(dp)
        self.dp_ids = [dp.id for dp in self.dps]

    def tearDown(self) -> None:
        pass

    def test_iter(self):
        # add them to a decision point group
        g = dpg.DecisionPointGroup(
            name="Test Group",
            definition="Test Group",
            decision_points=self.dps,
        )

        self.assertTrue(hasattr(g, "__iter__"))

        # iterate over the group
        for dp in g:
            self.assertIn(dp, self.dp_ids)

    def test_len(self):
        # add them to a decision point group
        g = dpg.DecisionPointGroup(
            name="Test Group",
            definition="Test Group",
            decision_points=self.dps,
        )

        self.assertGreater(len(self.dps), 0)
        self.assertEqual(len(self.dps), len(list(g.decision_points)))
        self.assertEqual(len(self.dps), len(g))

    def test_json_roundtrip(self):
        # add them to a decision point group
        g = dpg.DecisionPointGroup(
            name="Test Group",
            definition="Test Group",
            decision_points=self.dps,
        )

        # serialize the group to json
        g_json = g.model_dump_json()

        # deserialize the json to a new group
        g2 = dpg.DecisionPointGroup.model_validate_json(g_json)
        # assert that the new group is the same as the old group
        self.assertEqual(g_json, g2.model_dump_json())

    def test_decision_points_dict(self):
        # add them to a decision point group
        g = dpg.DecisionPointGroup(
            name="Test Group",
            definition="Test Group",
            decision_points=self.dps,
        )

        # after init, g.decision_points should be a dict

        # get the decision points as a dictionary

        dp_dict = g.decision_points
        self.assertIsInstance(dp_dict, dict)

        # assert that the dictionary is the correct length
        self.assertEqual(len(self.dps), len(dp_dict))

        # assert that each decision point is in the dictionary
        for dp in self.dps:
            self.assertIn(dp.str, dp_dict)
            self.assertEqual(dp, dp_dict[dp.str])


if __name__ == "__main__":
    unittest.main()
