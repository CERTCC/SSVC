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

from ssvc.namespaces import NS_PATTERN, NameSpace


class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ns_pattern(self):
        should_match = [
            "foo",
            "foo.bar",
            "foo.bar.baz",
            "foo/bar/baz/quux",
            "foo.bar/baz.quux",
        ]
        should_match.extend([f"x_{ns}" for ns in should_match])

        for ns in should_match:
            with self.subTest(ns=ns):
                self.assertTrue(NS_PATTERN.match(ns), ns)

        should_not_match = [
            "",
            "ab",
            ".foo",
            "foo..bar",
            "foo/bar//baz",
            "foo/bar/baz/",
            "(&(&" "foo\\bar",
            "foo|bar|baz",
        ]

        should_not_match.extend([f"_{ns}" for ns in should_not_match])

        for ns in should_not_match:
            with self.subTest(ns=ns):
                self.assertFalse(NS_PATTERN.match(ns))

    def test_namspace_enum(self):
        for ns in NameSpace:
            self.assertEqual(ns.name.lower(), ns.value)

        # make sure we have an SSVC namespace with the correct value
        self.assertIn("SSVC", NameSpace.__members__)
        values = [ns.value for ns in NameSpace]
        self.assertIn("ssvc", values)

    def test_namespace_validator(self):
        for ns in NameSpace:
            self.assertTrue(NameSpace.validate(ns.value))

        for ns in ["foo", "bar", "baz", "quux"]:
            with self.assertRaises(ValueError):
                NameSpace.validate(ns)

        for ns in ["x_foo", "x_bar", "x_baz", "x_quux"]:
            self.assertEqual(ns, NameSpace.validate(ns))


if __name__ == "__main__":
    unittest.main()
