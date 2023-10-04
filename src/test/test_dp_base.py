import unittest
import ssvc.decision_points.base as base


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
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
        self.assertEqual(obj, obj2)


if __name__ == "__main__":
    unittest.main()
