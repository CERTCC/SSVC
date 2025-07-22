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
from datetime import datetime

from ssvc import selection
from ssvc.selection import MinimalSelectionList
from ssvc.utils.patterns import NS_PATTERN, VERSION_PATTERN


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.s1 = selection.MinimalSelection(
            namespace="x_example.test",
            key="test_key_1",
            version="1.0.0",
            values=["value11", "value12"],
        )
        self.s2 = selection.MinimalSelection(
            namespace="x_example.test",
            key="test_key_2",
            version="1.0.0",
            values=["value21", "value22"],
        )
        self.selections = MinimalSelectionList(
            selections=[self.s1, self.s2],
            timestamp=datetime.now(),
            target_ids=["target_id_1", "target_id_2"],
        )

    def test_minimal_selection_init(self):
        required_attrs = [
            "namespace",
            "key",
            "version",
            "values",
        ]
        for attr in required_attrs:
            self.assertTrue(hasattr(self.s1, attr), f"Attribute {attr} is missing")
        # namespace is a valid NamespaceString
        self.assertIsInstance(self.s1.namespace, str)
        self.assertRegex(
            self.s1.namespace,
            NS_PATTERN,
            "Namespace does not match the required pattern",
        )

        # key is a string
        self.assertIsInstance(self.s1.key, str)
        self.assertGreater(len(self.s1.key), 0, "Key should not be empty")
        # version is a valid VersionString
        self.assertIsInstance(self.s1.version, str)
        self.assertRegex(
            self.s1.version,
            VERSION_PATTERN,
            "Version does not match the required pattern",
        )

        # values is list of strings
        self.assertIsInstance(self.s1.values, list)
        for value in self.s1.values:
            self.assertIsInstance(value, str, f"Value {value} is not a string")

    def test_minimal_selection_list_init(self):
        required_attrs = [
            "schemaVersion",
            "selections",
            "timestamp",
        ]
        for attr in required_attrs:
            self.assertTrue(
                hasattr(self.selections, attr), f"Attribute {attr} is missing"
            )

        # schemaVersion is a string
        self.assertIsInstance(self.selections.schemaVersion, str)
        self.assertEqual(
            self.selections.schemaVersion,
            selection.SCHEMA_VERSION,
            "Schema version does not match the expected value",
        )
        self.assertRegex(self.selections.schemaVersion, VERSION_PATTERN)

        self.assertIsInstance(self.selections.target_ids, (list, type(None)))
        for target_id in self.selections.target_ids:
            self.assertIsInstance(
                target_id, str, f"Target ID {target_id} is not a string"
            )

        # selections is a list of MinimalSelection objects
        self.assertIsInstance(self.selections.selections, list)
        for sel in self.selections.selections:
            self.assertIsInstance(sel, selection.MinimalSelection)

        # timestamp is a datetime object
        self.assertIsInstance(self.selections.timestamp, datetime)


if __name__ == "__main__":
    unittest.main()
