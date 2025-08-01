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

import ssvc.decision_points.base as base
import ssvc.decision_points.ssvc.base
import ssvc.registry
from ssvc.decision_points.base import FIELD_DELIMITER


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        from ssvc.registry import REGISTRY

        self.original_registry = list(REGISTRY.get_all("DecisionPoint"))

        # reset the registry
        REGISTRY.reset()

        # add multiple values
        self.values = []
        for i in range(3):
            self.values.append(
                base.DecisionPointValue(
                    name=f"foo{i}", key=f"bar{i}", description=f"baz{i}"
                )
            )

        self.dp = ssvc.decision_points.ssvc.base.SsvcDecisionPoint(
            name="foo",
            key="bar",
            description="baz",
            version="1.0.0",
            namespace="x_example.test",
            values=tuple(self.values),
        )

    def tearDown(self) -> None:
        # restore the original registry
        from ssvc.registry import REGISTRY

        REGISTRY.reset()

    def test_decision_point_basics(self):
        from ssvc._mixins import _Base, _Keyed, _Namespaced, _Valued, _Versioned

        # inherits from mixins
        mixins = [_Valued, _Base, _Keyed, _Versioned, _Namespaced]
        for mixin in mixins:
            self.assertIsInstance(self.dp, mixin)

    def test_registry(self):
        # just by creating the objects, they should be registered
        self.assertIn(self.dp, base.REGISTERED_DECISION_POINTS)

        dp2 = ssvc.decision_points.ssvc.base.SsvcDecisionPoint(
            name="asdfad",
            key="asdfasdf",
            description="asdfasdf",
            version="1.33.1",
            namespace="asdfasdf",
            values=tuple(self.values),
        )
        self.assertIn(dp2, base.REGISTERED_DECISION_POINTS)

    def test_registry(self):
        from ssvc.registry import REGISTRY

        # just by creating the objects, they should be registered
        self.assertIsNotNone(REGISTRY.lookup_by_id("DecisionPoint", self.dp.id))

        dp2 = ssvc.decision_points.ssvc.base.SsvcDecisionPoint(
            name="asdfad",
            key="asdfasdf",
            description="asdfasdf",
            version="1.33.1",
            namespace="x_example.test",
            values=self.values,
        )

        dp2._comment = "asdfasdfasdf"

        self.assertIsNotNone(REGISTRY.lookup_by_id("DecisionPoint", dp2.id))

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
        self.assertEqual(obj.namespace, "x_example.test")
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

        obj2 = ssvc.decision_points.ssvc.base.SsvcDecisionPoint.model_validate_json(
            json
        )

        # the objects should be equal
        self.assertEqual(obj, obj2)
        self.assertEqual(obj.model_dump(), obj2.model_dump())

    def test_value_dict(self):
        obj = self.dp

        value_dict = obj.value_dict

        self.assertIsInstance(value_dict, dict)
        self.assertEqual(len(value_dict), len(obj.values))

        # the value_dict should have the dp.id:v.key as the key
        # and the DecisionPointValue as the value
        for value in obj.values:
            expected_key = FIELD_DELIMITER.join((obj.id, value.key))
            self.assertIn(expected_key, value_dict)
            self.assertEqual(value_dict[expected_key], value)

    def test_value_summaries(self):
        obj = self.dp
        # summaries are just the keys of the value_dict
        summaries = obj.value_summaries

        # should be a list
        self.assertIsInstance(summaries, list)
        self.assertEqual(len(summaries), len(obj.values))

        for summary in summaries:
            # each summary should be a string
            self.assertIsInstance(summary, str)
            # each summary should be the key of a value
            self.assertIn(summary, obj.value_dict)


if __name__ == "__main__":
    unittest.main()
