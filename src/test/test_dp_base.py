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

import ssvc.decision_points.base as base


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.original_registry = base.REGISTERED_DECISION_POINTS.copy()

        # add multiple values
        self.values = []
        for i in range(3):
            self.values.append(
                base.SsvcDecisionPointValue(
                    name=f"foo{i}", key=f"bar{i}", description=f"baz{i}"
                )
            )

        self.dp = base.SsvcDecisionPoint(
            name="foo",
            key="bar",
            description="baz",
            version="1.0.0",
            namespace="x_test",
            values=tuple(self.values),
        )

    def tearDown(self) -> None:
        # restore the original registry
        base._reset_registered()

    def test_decision_point_basics(self):
        from ssvc._mixins import _Base, _Keyed, _Namespaced, _Valued, _Versioned

        # inherits from mixins
        mixins = [_Valued, _Base, _Keyed, _Versioned, _Namespaced]
        for mixin in mixins:
            self.assertIsInstance(self.dp, mixin)

    def test_registry(self):
        # just by creating the objects, they should be registered
        self.assertIn(self.dp, base.REGISTERED_DECISION_POINTS)

        dp2 = base.SsvcDecisionPoint(
            name="asdfad",
            key="asdfasdf",
            description="asdfasdf",
            version="1.33.1",
            namespace="asdfasdf",
            values=tuple(self.values),
        )

    def test_registry(self):
        # just by creating the objects, they should be registered
        self.assertIn(self.dp, base.REGISTERED_DECISION_POINTS)

        dp2 = base.SsvcDecisionPoint(
            name="asdfad",
            key="asdfasdf",
            description="asdfasdf",
            version="1.33.1",
            namespace="x_test",
            values=self.values,
        )

        dp2._comment = "asdfasdfasdf"

        self.assertIn(dp2, base.REGISTERED_DECISION_POINTS)

    def test_ssvc_value(self):
        for i, obj in enumerate(self.values):
            # should have name, key, description
            self.assertEqual(obj.name, f"foo{i}")
            self.assertEqual(obj.key, f"bar{i}")
            self.assertEqual(obj.description, f"baz{i}")

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
        self.assertEqual(obj.namespace, "x_test")
        self.assertEqual(len(self.values), len(obj.values))

    def test_ssvc_value_json_roundtrip(self):
        for i, obj in enumerate(self.values):
            json = obj.model_dump_json()
            self.assertIsInstance(json, str)
            self.assertGreater(len(json), 0)

            obj2 = base.SsvcDecisionPointValue.model_validate_json(json)
            self.assertEqual(obj, obj2)

    def test_ssvc_decision_point_json_roundtrip(self):
        obj = self.dp

        json = obj.model_dump_json()
        self.assertIsInstance(json, str)
        self.assertGreater(len(json), 0)

        obj2 = base.SsvcDecisionPoint.model_validate_json(json)

        # the objects should be equal
        self.assertEqual(obj, obj2)
        self.assertEqual(obj.model_dump(), obj2.model_dump())


if __name__ == "__main__":
    unittest.main()
