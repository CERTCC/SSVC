import unittest
from dataclasses import dataclass

from dataclasses_json import dataclass_json

from ssvc._mixins import _Base, _Versioned, _Namespaced


class TestMixins(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = _Base(name="foo", key="bar", description="baz")

    def test_ssvc_base_bad_create(self):
        # empty
        self.assertRaises(TypeError, _Base)
        # no name
        self.assertRaises(TypeError, _Base, key="bar", description="baz")
        # no key
        self.assertRaises(TypeError, _Base, name="foo", description="baz")
        # no description
        self.assertRaises(TypeError, _Base, name="foo", key="bar")

    def test_ssvc_base_create(self):
        obj = self.obj
        self.assertEqual(obj.name, "foo")
        self.assertEqual(obj.key, "bar")
        self.assertEqual(obj.description, "baz")

    def test_json_roundtrip(self):
        obj = self.obj
        json = obj.to_json()
        # is it a string?
        self.assertIsInstance(json, str)
        # does it look right?
        self.assertEqual(json, '{"name": "foo", "description": "baz", "key": "bar"}')

        # modify the raw json string
        json = json.replace("foo", "quux")
        self.assertEqual(json, '{"name": "quux", "description": "baz", "key": "bar"}')

        # does it load?
        obj2 = _Base.from_json(json)
        self.assertEqual(obj2.name, "quux")
        self.assertEqual(obj2.key, "bar")
        self.assertEqual(obj2.description, "baz")

    def test_asdict_roundtrip(self):
        from dataclasses import asdict

        obj = self.obj
        d = asdict(obj)

        self.assertIsInstance(d, dict)
        self.assertEqual(d["name"], "foo")
        self.assertEqual(d["key"], "bar")
        self.assertEqual(d["description"], "baz")

        # modify the dict
        d["name"] = "quux"

        # does it load?
        obj2 = _Base(**d)
        self.assertEqual(obj2.name, "quux")
        self.assertEqual(obj2.key, "bar")
        self.assertEqual(obj2.description, "baz")

    def test_namespaced_create(self):
        obj = _Namespaced()
        self.assertEqual(obj.namespace, "ssvc")

        obj = _Namespaced(namespace="quux")
        self.assertEqual(obj.namespace, "quux")

    def test_base_namespaced_mix(self):
        # We need a dataclass to mix in with _Namespaced
        @dataclass_json
        @dataclass(kw_only=True)
        class Foo(_Base, _Namespaced):
            pass

        # empty
        self.assertRaises(TypeError, Foo)
        # no name
        self.assertRaises(TypeError, Foo, key="bar", description="baz")
        # no key
        self.assertRaises(TypeError, Foo, name="foo", description="baz")
        # no description
        self.assertRaises(TypeError, Foo, name="foo", key="bar")
        # no namespace (should default to ssvc)
        obj = Foo(name="foo", key="bar", description="baz")
        self.assertEqual(obj.namespace, "ssvc")

        # with namespace
        obj = Foo(name="foo", key="bar", description="baz", namespace="quux")
        self.assertEqual(obj.namespace, "quux")

    def test_versioned_create(self):
        obj = _Versioned()
        self.assertEqual(obj.version, "0.0.0")

        obj = _Versioned(version="1.2.3")
        self.assertEqual(obj.version, "1.2.3")

    def test_base_versioned_mix(self):
        # We need a dataclass to mix in with _Versioned
        @dataclass_json
        @dataclass(kw_only=True)
        class Foo(_Base, _Versioned):
            pass

        # empty
        self.assertRaises(TypeError, Foo)
        # no name
        self.assertRaises(TypeError, Foo, key="bar", description="baz")
        # no key
        self.assertRaises(TypeError, Foo, name="foo", description="baz")
        # no description
        self.assertRaises(TypeError, Foo, name="foo", key="bar")
        # no version (should default to 0.0.0)
        obj = Foo(name="foo", key="bar", description="baz")
        self.assertEqual(obj.version, "0.0.0")

        # with version
        obj = Foo(name="foo", key="bar", description="baz", version="1.2.3")
        self.assertEqual(obj.version, "1.2.3")

    def test_base_versioned_namespaced_mix(self):
        # We need a dataclass to mix in with _Versioned and _Namespaced
        @dataclass_json
        @dataclass(kw_only=True)
        class Foo(_Base, _Versioned, _Namespaced):
            pass

        # empty
        self.assertRaises(TypeError, Foo)
        # no name
        self.assertRaises(TypeError, Foo, key="bar", description="baz")
        # no key
        self.assertRaises(TypeError, Foo, name="foo", description="baz")
        # no description
        self.assertRaises(TypeError, Foo, name="foo", key="bar")
        # no version (should default to 0.0.0)
        obj = Foo(name="foo", key="bar", description="baz")
        self.assertEqual(obj.version, "0.0.0")
        # no namespace (should default to ssvc)
        self.assertEqual(obj.namespace, "ssvc")

        # with version
        obj = Foo(
            name="foo", key="bar", description="baz", version="1.2.3", namespace="quux"
        )
        self.assertEqual(obj.version, "1.2.3")
        self.assertEqual(obj.namespace, "quux")


if __name__ == "__main__":
    unittest.main()
