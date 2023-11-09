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

import ssvc.decision_points.base as base


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.original_registry = base.REGISTERED_DECISION_POINTS.copy()

        self.value = base.SsvcDecisionPointValue(
            name="foo", key="bar", description="baz"
        )

        self.dp = base.SsvcDecisionPoint(
            name="foo",
            key="bar",
            description="baz",
            version="1.0.0",
            namespace="ns",
            values=(self.value,),
        )

    def tearDown(self) -> None:
        # restore the original registry
        base.REGISTERED_DECISION_POINTS = self.original_registry

    def test_registry(self):
        # just by creating the objects, they should be registered
        self.assertIn(self.dp, base.REGISTERED_DECISION_POINTS)

        dp2 = base.SsvcDecisionPoint(
            name="asdfad",
            key="asdfasdf",
            description="asdfasdf",
            version="1.33.1",
            namespace="asdfasdf",
            values=(
                self.value,
                self.value,
            ),
        )

        dp2._comment = "asdfasdfasdf"

        self.assertIn(dp2, base.REGISTERED_DECISION_POINTS)

    def test_ssvc_value(self):
        obj = self.value
        # should have name, key, description
        self.assertEqual(obj.name, "foo")
        self.assertEqual(obj.key, "bar")
        self.assertEqual(obj.description, "baz")

        # should not have namespace, version
        self.assertFalse(hasattr(obj, "namespace"))
        self.assertFalse(hasattr(obj, "version"))

    def test_ssvc_decision_point(self):
        obj = self.dp
        # should have name, key, description, values, version, namespace
        self.assertEqual(obj.name, "foo")
        self.assertEqual(obj.key, "bar")
        self.assertEqual(obj.description, "baz")
        self.assertEqual(obj.version, "1.0.0")
        self.assertEqual(obj.namespace, "ns")
        self.assertEqual(len(obj.values), 1)

    def test_ssvc_value_json_roundtrip(self):
        obj = self.value

        json = obj.to_json()
        self.assertIsInstance(json, str)
        self.assertGreater(len(json), 0)

        obj2 = base.SsvcDecisionPointValue.from_json(json)
        self.assertEqual(obj, obj2)

    def test_ssvc_decision_point_json_roundtrip(self):
        obj = self.dp

        json = obj.to_json()
        self.assertIsInstance(json, str)
        self.assertGreater(len(json), 0)

        obj2 = base.SsvcDecisionPoint.from_json(json)
        self.assertEqual(obj.to_dict(), obj2.to_dict())

    def test_dp_to_table(self):
        obj = self.dp

        table = base.dp_to_table(obj)

        self.assertIn(obj.description, table)
        self.assertIn("Value", table)
        self.assertIn("Key", table)
        self.assertIn("Description", table)
        self.assertIn(obj.name, table)
        self.assertIn(obj.key, table)


if __name__ == "__main__":
    unittest.main()
