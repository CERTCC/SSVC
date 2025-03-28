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
