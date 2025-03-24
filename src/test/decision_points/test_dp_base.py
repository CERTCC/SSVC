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
import ssvc.decision_points.ssvc_.base


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.original_registry = base.REGISTERED_DECISION_POINTS.copy()

        # add multiple values
        self.values = []
        for i in range(3):
            self.values.append(
                base.DecisionPointValue(
                    name=f"foo{i}", key=f"bar{i}", description=f"baz{i}"
                )
            )

        self.dp = ssvc.decision_points.ssvc_.base.SsvcDecisionPoint(
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

        dp2 = ssvc.decision_points.ssvc_.base.SsvcDecisionPoint(
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

        dp2 = ssvc.decision_points.ssvc_.base.SsvcDecisionPoint(
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

            obj2 = base.DecisionPointValue.model_validate_json(json)
            self.assertEqual(obj, obj2)

    def test_ssvc_decision_point_json_roundtrip(self):
        obj = self.dp

        json = obj.model_dump_json()
        self.assertIsInstance(json, str)
        self.assertGreater(len(json), 0)

        obj2 = ssvc.decision_points.ssvc_.base.SsvcDecisionPoint.model_validate_json(
            json
        )

        # the objects should be equal
        self.assertEqual(obj, obj2)
        self.assertEqual(obj.model_dump(), obj2.model_dump())

    def test_value_summaries_dict(self):
        obj = self.dp
        summaries = obj.value_summaries_dict

        # should be a dictionary
        self.assertIsInstance(summaries, dict)
        self.assertEqual(len(summaries), len(obj.values))

        # the summaries dict should have str(ValueSummary) as the key
        # and the ValueSummary as the value
        for key, summary in summaries.items():
            # confirm the key is the string representation of the ValueSummary
            self.assertEqual(key, str(summary))

            # confirm the attributes of the ValueSummary
            # key, version, and namespace come from the decision point
            self.assertEqual(summary.key, obj.key)
            self.assertEqual(summary.version, obj.version)
            self.assertEqual(summary.namespace, obj.namespace)
            # value comes from the list of values, and should be a key to one of the values
            value_keys = [v.key for v in obj.values]
            self.assertIn(summary.value, value_keys)

    def test_value_summaries_str(self):
        obj = self.dp
        summaries = obj.value_summaries_str

        # should be a list
        self.assertIsInstance(summaries, list)
        self.assertEqual(len(summaries), len(obj.values))

        # the summaries list should have str(ValueSummary) as the key
        for key in summaries:
            # confirm the key is the string representation of the ValueSummary
            self.assertIsInstance(key, str)

            # parse the key into its parts
            (ns, k, v, val) = key.split(":")
            # ns, k, v should come from the decision point
            self.assertEqual(ns, obj.namespace)
            self.assertEqual(k, obj.key)
            self.assertEqual(v, obj.version)
            # val should be a key to one of the values
            value_keys = [v.key for v in obj.values]
            self.assertIn(val, value_keys)

    def test_value_summaries(self):
        obj = self.dp
        summaries = obj.value_summaries

        # should be a list
        self.assertIsInstance(summaries, list)
        self.assertEqual(len(summaries), len(obj.values))

        # the summaries list should be ValueSummary objects
        for summary in summaries:
            self.assertIsInstance(summary, base.ValueSummary)
            # key, version, and namespace come from the decision point
            self.assertEqual(summary.key, obj.key)
            self.assertEqual(summary.version, obj.version)
            self.assertEqual(summary.namespace, obj.namespace)
            # value comes from the list of values, and should be a key to one of the values
            value_keys = [v.key for v in obj.values]
            self.assertIn(summary.value, value_keys)


if __name__ == "__main__":
    unittest.main()
