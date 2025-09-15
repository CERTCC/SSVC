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
from unittest import expectedFailure

from ssvc import selection
from ssvc.selection import MinimalDecisionPointValue, SelectionList
from ssvc.utils.patterns import NS_PATTERN, VERSION_PATTERN


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.s1 = selection.Selection(
            namespace="test",
            key="test_key_1",
            version="1.0.0",
            values=[{"key": "value11"}, {"key": "value12"}],
        )
        self.s2 = selection.Selection(
            namespace="test",
            key="test_key_2",
            version="1.0.0",
            values=[{"key": "value21"}, {"key": "value22"}],
        )
        self.selections = SelectionList(
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
            self.assertTrue(
                hasattr(self.s1, attr), f"Attribute {attr} is missing"
            )
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
            # enable re.ASCII so that `\d` is interpreted like in Javascript
            "(?a:" + VERSION_PATTERN + ")",
            "Version does not match the required pattern",
        )

        # values is list of strings'
        self.assertIsInstance(self.s1.values, tuple)
        for value in self.s1.values:
            self.assertIsInstance(
                value,
                MinimalDecisionPointValue,
                f"Value {value} is not a MinimalDecisionPoint",
            )
            self.assertTrue(
                hasattr(value, "key"),
                f"Attribute 'key' is missing from {value}",
            )
            self.assertIsInstance(value.key, str)

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

        # selections is a list of Selection objects
        self.assertIsInstance(self.selections.selections, list)
        for sel in self.selections.selections:
            self.assertIsInstance(sel, selection.Selection)

        # timestamp is a datetime object
        self.assertIsInstance(self.selections.timestamp, datetime)

    def test_minimal_decision_point_value_validators(self):
        """Test the model validators for MinimalDecisionPointValue."""
        # Test set_optional_fields validator
        value = MinimalDecisionPointValue(key="test_key")
        self.assertIsNone(value.name)
        self.assertIsNone(value.definition)

        # Test with empty strings
        value_empty = MinimalDecisionPointValue(
            key="test_key", name="", definition=""
        )
        self.assertIsNone(value_empty.name)
        self.assertIsNone(value_empty.definition)

    def test_selection_validators(self):
        """Test the model validators for Selection."""
        # Test with minimal data
        selection_minimal = selection.Selection(
            namespace="test",
            key="test_key",
            version="1.0.0",
            values=[{"key": "value1"}],
        )
        self.assertIsNone(selection_minimal.name)
        self.assertIsNone(selection_minimal.definition)

        # Test with empty strings
        selection_empty = selection.Selection(
            namespace="test",
            key="test_key",
            version="1.0.0",
            values=[{"key": "value1"}],
            name="",
            definition="",
        )
        self.assertIsNone(selection_empty.name)
        self.assertIsNone(selection_empty.definition)

    def test_from_decision_point(self):
        """Test converting a decision point to a selection."""
        from ssvc.decision_points.ssvc.automatable import LATEST as dp

        selection_obj = selection.Selection.from_decision_point(dp)

        self.assertEqual(selection_obj.namespace, dp.namespace)
        self.assertEqual(selection_obj.key, dp.key)
        self.assertEqual(selection_obj.version, dp.version)
        self.assertEqual(len(selection_obj.values), len(dp.values))

        for sel_val, dp_val in zip(selection_obj.values, dp.values):
            self.assertEqual(sel_val.key, dp_val.key)

    def test_reference_model(self):
        """Test the Reference model."""
        uris = [
            "https://example.com",
            "http://example.org/path",
            "ftp://ftp.example.com/file.txt",
            "mailto:someone@example.com",
            "tel:+1-555-555-5555",
            "https://example.com:8080/path/to/resource?query=string#fragment",
            "http://localhost:3000/api/v1/users",
            "https://127.0.0.1/",
            "https://user:pass@example.com",
            "ftp://anonymous:anon@example.com/resource.txt",
            "http://192.168.1.1/",
            "https://[2001:db8::1]/",
            "urn:isbn:8675309#page=42",
            "data:text/plain;base64,SGVsbG8sIFdvcmxkIQ%3D%3D",
            "custom-scheme://host/resource",
            "blob:https://example.com/550e8400-e29b-41d4-a716-446655440000",
        ]

        for uri in uris:
            ref = selection.Reference(uri=uri, summary="Test description")

            self.assertIn(uri, str(ref.uri))
            self.assertEqual(ref.summary, "Test description")

    @expectedFailure
    def test_reference_model_without_summary(self):
        """Test the Reference model."""
        uris = [
            "https://example.com",
            "http://example.org/path",
            "ftp://ftp.example.com/file.txt",
            "mailto:someone@example.com",
            "tel:+1-555-555-5555",
            "https://example.com:8080/path/to/resource?query=string#fragment",
            "http://localhost:3000/api/v1/users",
            "https://127.0.0.1/",
            "https://user:pass@example.com",
            "ftp://anonymous:anon@example.com/resource.txt",
            "http://192.168.1.1/",
            "https://[2001:db8::1]/",
            "urn:isbn:8675309#page=42",
            "data:text/plain;base64,SGVsbG8sIFdvcmxkIQ%3D%3D",
            "custom-scheme://host/resource",
            "blob:https://example.com/550e8400-e29b-41d4-a716-446655440000",
        ]

        for uri in uris:
            ref = selection.Reference(
                uri=uri,
            )

            self.assertIn(uri, str(ref.uri))

    def test_selection_list_validators(self):
        """Test SelectionList validators."""
        # Test schema version is set automatically
        sel_list = SelectionList(
            selections=[self.s1],
            timestamp=datetime.now(),
        )
        self.assertEqual(sel_list.schemaVersion, selection.SCHEMA_VERSION)

    def test_target_ids_validation(self):
        """Test target_ids field validation."""
        # Test empty list throws ValueError
        with self.assertRaises(ValueError):
            SelectionList(
                selections=[self.s1],
                timestamp=datetime.now(),
                target_ids=[],
            )

        # Test None throws ValueError
        with self.assertRaises(ValueError):
            SelectionList(
                selections=[self.s1],
                timestamp=datetime.now(),
                target_ids=None,
            )

        # absent target_ids leads to empty list
        sel_list = SelectionList(
            selections=[self.s1],
            timestamp=datetime.now(),
        )
        self.assertEqual(sel_list.target_ids, [])

        # Test valid target_ids
        sel_list_valid = SelectionList(
            selections=[self.s1],
            timestamp=datetime.now(),
            target_ids=["CVE-1900-0001"],
        )
        self.assertEqual(sel_list_valid.target_ids, ["CVE-1900-0001"])

        # Test invalid target_ids (non-string)
        with self.assertRaises(ValueError):
            SelectionList(
                selections=[self.s1],
                timestamp=datetime.now(),
                target_ids=[123],  # Invalid: not a string
            )

        # Test invalid target_ids (duplicate items)
        with self.assertRaises(ValueError):
            SelectionList(
                selections=[self.s1],
                timestamp=datetime.now(),
                # Invalid: due to duplicates
                target_ids=["CVE-1900-1234", "CVE-1900-1234"],
            )

    def test_add_selection_method(self):
        """Test the add_selection method."""
        initial_count = len(self.selections.selections)
        new_selection = selection.Selection(
            namespace="test",
            key="new_key",
            version="1.0.0",
            values=[{"key": "new_value"}],
        )

        self.selections.add_selection(new_selection)
        self.assertEqual(len(self.selections.selections), initial_count + 1)
        self.assertEqual(self.selections.selections[-1], new_selection)

    def test_selection_list_optional_fields(self):
        """Test SelectionList with optional fields."""
        ref = selection.Reference(
            uri="https://example.com/resource", summary="Test resource"
        )

        sel_list = SelectionList(
            selections=[self.s1, self.s2],
            timestamp=datetime.now(),
            target_ids=["CVE-1900-0001"],
            decision_point_resources=[ref],
            references=[ref],
        )

        self.assertEqual(len(sel_list.decision_point_resources), 1)
        self.assertEqual(len(sel_list.references), 1)
        self.assertEqual(sel_list.decision_point_resources[0].uri, ref.uri)

    def test_model_json_schema_customization(self):
        """Test that JSON schema is properly customized."""
        schema = SelectionList.model_json_schema()

        # Check schema metadata
        self.assertIn("title", schema)
        self.assertEqual(
            schema["$schema"], "https://json-schema.org/draft/2020-12/schema"
        )
        self.assertIn("$id", schema)
        self.assertIn("description", schema)

        # Check that optional fields are not in required list
        required_fields = schema.get("required", [])
        optional_fields = [
            "name",
            "description",
            "target_ids",
            "decision_point_resources",
            "references",
        ]
        for field in optional_fields:
            self.assertNotIn(field, required_fields)

    def test_selection_values_validation(self):
        """Test that Selection requires at least one value."""
        with self.assertRaises(ValueError):
            selection.Selection(
                namespace="test",
                key="test_key",
                version="1.0.0",
                values=[],  # Empty values should raise error
            )

    def test_selection_list_minimum_selections(self):
        """Test that SelectionList requires at least one selection."""
        with self.assertRaises(ValueError):
            SelectionList(
                selections=[],  # Empty selections should raise error
                timestamp=datetime.now(),
            )


if __name__ == "__main__":
    unittest.main()
