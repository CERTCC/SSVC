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
from dataclasses import dataclass

from dataclasses_json import dataclass_json

from ssvc._mixins import _Base, _Keyed, _Versioned, _Namespaced


class TestMixins(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = _Base(name="foo", description="baz")

    def test_ssvc_base_create(self):
        obj = _Base(name="foo", description="baz")
        self.assertEqual(obj.name, "foo")
        self.assertEqual(obj.description, "baz")

        # empty
        self.assertRaises(TypeError, _Base)
        # no name
        self.assertRaises(TypeError, _Base, description="baz")
        # no description
        self.assertRaises(TypeError, _Base, name="foo")

    def test_json_roundtrip(self):
        obj = self.obj
        json = obj.to_json()
        # is it a string?
        self.assertIsInstance(json, str)
        # does it look right?
        self.assertEqual(json, '{"name": "foo", "description": "baz"}')

        # modify the raw json string
        json = json.replace("foo", "quux")
        self.assertEqual(json, '{"name": "quux", "description": "baz"}')

        # does it load?
        obj2 = _Base.from_json(json)
        self.assertEqual(obj2.name, "quux")
        self.assertEqual(obj2.description, "baz")

    def test_asdict_roundtrip(self):
        from dataclasses import asdict

        obj = self.obj
        d = asdict(obj)

        self.assertIsInstance(d, dict)
        self.assertEqual(d["name"], "foo")
        self.assertEqual(d["description"], "baz")

        # modify the dict
        d["name"] = "quux"

        # does it load?
        obj2 = _Base(**d)
        self.assertEqual(obj2.name, "quux")
        self.assertEqual(obj2.description, "baz")

    def test_namespaced_create(self):
        obj = _Namespaced()
        self.assertEqual(obj.namespace, "ssvc")

        obj = _Namespaced(namespace="quux")
        self.assertEqual(obj.namespace, "quux")

    def test_versioned_create(self):
        obj = _Versioned()
        self.assertEqual(obj.version, "0.0.0")

        obj = _Versioned(version="1.2.3")
        self.assertEqual(obj.version, "1.2.3")

    def test_keyed_create(self):
        obj = _Keyed(key="foo")
        self.assertEqual(obj.key, "foo")

        self.assertRaises(TypeError, _Keyed)

    def test_mixin_combos(self):
        # We need to test all the combinations
        mixins = [
            {"class": _Keyed, "args": {"key": "fizz"}, "has_default": False},
            {"class": _Namespaced, "args": {"namespace": "buzz"}, "has_default": True},
            {"class": _Versioned, "args": {"version": "1.2.3"}, "has_default": True},
        ]
        keys_with_defaults = [x["args"].keys() for x in mixins if x["has_default"]]
        # flatten the list
        keys_with_defaults = [
            item for sublist in keys_with_defaults for item in sublist
        ]

        import itertools

        max_len = len(mixins)
        for i in range(max_len):
            for combo in itertools.combinations(mixins, i + 1):
                classes = [x["class"] for x in combo]
                args = {k: v for x in combo for k, v in x["args"].items()}

                # create an object with the mixins
                @dataclass_json
                @dataclass(kw_only=True)
                class Foo(_Base, *classes):
                    pass

                # make sure it breaks if we leave out a required arg
                for k in args.keys():
                    args_copy = args.copy()
                    del args_copy[k]

                    if k in keys_with_defaults:
                        # expect success
                        obj = Foo(name="foo", description="baz", **args_copy)
                        # make sure the key is defaulted
                        self.assertEqual(getattr(Foo, k), getattr(obj, k))
                    else:
                        self.assertRaises(
                            TypeError, Foo, name="foo", description="baz", **args_copy
                        )

                # instantiate the object
                obj = Foo(name="foo", description="baz", **args)
                self.assertEqual(obj.name, "foo")
                self.assertEqual(obj.description, "baz")
                # make sure the args are set
                for k, v in args.items():
                    self.assertEqual(getattr(obj, k), v)

                # test json roundtrip
                json = obj.to_json()
                # is it a string?
                self.assertIsInstance(json, str)
                # does it look right?
                self.assertIn('"name": "foo"', json)
                self.assertIn('"description": "baz"', json)
                for k, v in args.items():
                    self.assertIn(f'"{k}": "{v}"', json)
                # change the name and description
                json = json.replace("foo", "quux")
                json = json.replace("baz", "fizz")
                # does it load?
                obj2 = Foo.from_json(json)
                self.assertEqual(obj2.name, "quux")
                self.assertEqual(obj2.description, "fizz")
                # make sure the args are set
                for k, v in args.items():
                    self.assertEqual(getattr(obj2, k), v)
                # make sure unchanged attributes match from the original object
                for k in args.keys():
                    self.assertEqual(getattr(obj2, k), getattr(obj, k))


if __name__ == "__main__":
    unittest.main()
