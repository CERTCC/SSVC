#  Copyright (c) 2025 Carnegie Mellon University.
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
from random import randint

from pydantic import BaseModel, ValidationError

from ssvc._mixins import (
    _Base,
    _Keyed,
    _Namespaced,
    _Valued,
    _Versioned,
)
from ssvc.namespaces import NameSpace
from ssvc.utils.defaults import DEFAULT_VERSION


class TestMixins(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = _Base(name="foo", definition="baz")

    def test_ssvc_base_create(self):
        obj = _Base(name="foo", definition="baz")
        self.assertEqual(obj.name, "foo")
        self.assertEqual(obj.definition, "baz")

        # empty
        self.assertRaises(ValidationError, _Base)
        # no name
        self.assertRaises(ValidationError, _Base, description="baz")
        # no description
        self.assertRaises(ValidationError, _Base, name="foo")

    def test_json_roundtrip(self):
        obj = self.obj
        json = obj.model_dump_json()
        # is it a string?
        self.assertIsInstance(json, str)
        # does it look right?
        self.assertEqual(json, '{"name":"foo","definition":"baz"}')

        # modify the raw json string
        json = json.replace("foo", "quux")
        self.assertEqual(json, '{"name":"quux","definition":"baz"}')

        # does it load?
        obj2 = _Base.model_validate_json(json)
        self.assertEqual(obj2.name, "quux")
        self.assertEqual(obj2.definition, "baz")

    def test_asdict_roundtrip(self):

        obj = self.obj
        d = obj.model_dump()

        self.assertIsInstance(d, dict)
        self.assertEqual(d["name"], "foo")
        self.assertEqual(d["definition"], "baz")

        # modify the dict
        d["name"] = "quux"

        # does it load?
        obj2 = _Base(**d)
        self.assertEqual(obj2.name, "quux")
        self.assertEqual(obj2.definition, "baz")

    def test_namespaced_create_errors(self):
        # error if no namespace given
        with self.assertRaises(ValidationError):
            _Namespaced()

        # error if namespace is not in the enum
        # and it doesn't start with x_
        self.assertNotIn("quux", NameSpace)
        with self.assertRaises(ValidationError):
            _Namespaced(namespace="quux")

        # error if namespace starts with x_ but is too short
        with self.assertRaises(ValidationError):
            _Namespaced(namespace="x_")

    def test_namespaced_create(self):
        # use the official namespace values
        for ns in NameSpace:
            obj = _Namespaced(namespace=ns)
            self.assertEqual(obj.namespace, ns)

        # custom namespaces are allowed as long as they start with x_
        # and then follow `x-name = reverse-dns  "#" fragment-seg`
        for _ in range(100):
            # we're just fuzzing some random strings here
            ns = f"x_example.test{randint(1000,1000000)}#test"
            obj = _Namespaced(namespace=ns)
            self.assertEqual(obj.namespace, ns)

    def test_versioned_create(self):
        obj = _Versioned()
        self.assertEqual(obj.version, DEFAULT_VERSION)

        obj = _Versioned(version="1.2.3")
        self.assertEqual(obj.version, "1.2.3")

    def test_keyed_create(self):
        obj = _Keyed(key="foo")
        self.assertEqual(obj.key, "foo")

        self.assertRaises(ValidationError, _Keyed)

        good_keys = ["A", "1", "F1", "T*", "Mixed_case_OK", "alph4num3ric"]
        bad_keys = [
            "",  # no empty string
            "foo_",  # no trailing underscore
            "_",  # no solitary underscore
            "_foo",  # no leading underscore
            "A*",  # no trailing asterisk
        ]
        # add other bad keys that contain special characters
        # these should not be allowed in keys
        for char in " ~`!@#$%^&*()-+={}[]|\\:;\"'<>,.?/":
            bad_keys.append(char)
            bad_keys.append("foo" + char)
            bad_keys.append(char + "bar")
            bad_keys.append("foo" + char + "bar")

        for key in good_keys:
            with self.subTest(key=key):
                obj = _Keyed(key=key)
                self.assertEqual(obj.key, key)

        for key in bad_keys:
            with self.subTest(key=key):
                with self.assertRaises(
                    ValidationError, msg=f"Key '{key}' should be invalid"
                ):
                    _Keyed(key=key)

    def test_valued_create(self):
        values = ("foo", "bar", "baz", "quux")

        obj = _Valued(values=values)

        # length
        self.assertEqual(len(obj), len(values))

        # iteration
        for i, v in enumerate(obj):
            self.assertEqual(v, values[i])

        # values
        self.assertEqual(obj.values, values)

        self.assertRaises(ValidationError, _Valued)

    def test_mixin_combos(self):
        # We need to test all the combinations
        mixins = [
            {"class": _Keyed, "args": {"key": "fizz"}, "has_default": False},
            {
                "class": _Namespaced,
                "args": {"namespace": "x_example.test#test"},
                "has_default": False,
            },
            {
                "class": _Versioned,
                "args": {"version": "1.2.3"},
                "has_default": True,
            },
        ]
        keys_with_defaults = [
            x["args"].keys() for x in mixins if x["has_default"]
        ]
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
                class Foo(_Base, *classes, BaseModel):
                    pass

                # make sure it breaks if we leave out a required arg
                for k in args.keys():
                    args_copy = args.copy()
                    del args_copy[k]

                    if k in keys_with_defaults:
                        # expect success
                        obj = Foo(name="foo", definition="baz", **args_copy)
                        # make sure the key is defaulted
                        self.assertIsNotNone(getattr(obj, k))
                    else:
                        self.assertRaises(
                            ValidationError,
                            Foo,
                            name="foo",
                            description="baz",
                            **args_copy,
                        )

                # instantiate the object
                obj = Foo(name="foo", definition="baz", **args)
                self.assertEqual(obj.name, "foo")
                self.assertEqual(obj.definition, "baz")
                # make sure the args are set
                for k, v in args.items():
                    self.assertEqual(getattr(obj, k), v)

                # test json roundtrip
                json = obj.model_dump_json()
                # is it a string?
                self.assertIsInstance(json, str)
                # does it look right?
                self.assertIn('"name":"foo"', json)
                self.assertIn('"definition":"baz"', json)
                for k, v in args.items():
                    self.assertIn(f'"{k}":"{v}"', json)
                # change the name and description
                json = json.replace("foo", "quux")
                json = json.replace("baz", "fizz")
                # does it load?
                obj2 = Foo.model_validate_json(json)
                self.assertEqual(obj2.name, "quux")
                self.assertEqual(obj2.definition, "fizz")
                # make sure the args are set
                for k, v in args.items():
                    self.assertEqual(getattr(obj2, k), v)
                # make sure unchanged attributes match from the original object
                for k in args.keys():
                    self.assertEqual(getattr(obj2, k), getattr(obj, k))


if __name__ == "__main__":
    unittest.main()
