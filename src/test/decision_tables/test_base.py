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
import os
import tempfile
import unittest

import pandas as pd

from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_tables.base import (
    DecisionTable,
    MappingRow,
    decision_table_to_csv,
    generate_full_mapping,
)
from ssvc.dp_groups.base import DecisionPoint, DecisionPointGroup
from ssvc.outcomes.base import OutcomeGroup


class TestDecisionTableBase(unittest.TestCase):
    def setUp(self):
        # create a temporary directory for testing
        self.tmpdir = tempfile.TemporaryDirectory()

        # Create dummy decision point values
        self.dp1v1 = DecisionPointValue(name="a", key="a", description="A value")
        self.dp1v2 = DecisionPointValue(name="b", key="b", description="B value")
        self.dp2v1 = DecisionPointValue(name="x", key="x", description="X value")
        self.dp2v2 = DecisionPointValue(name="y", key="y", description="Y value")

        # Create dummy decision points and group
        self.dp1 = DecisionPoint(
            name="dp1",
            description="",
            version="1.0",
            namespace="x_test",
            key="dp1",
            values=(self.dp1v1, self.dp1v2),
        )
        self.dp2 = DecisionPoint(
            name="dp2",
            description="",
            version="1.0",
            namespace="x_test",
            key="dp2",
            values=(self.dp2v1, self.dp2v2),
        )
        self.dpg = DecisionPointGroup(
            name="dpg",
            description="",
            version="1.0",
            namespace="x_test",
            decision_points=(self.dp1, self.dp2),
        )
        # Create dummy outcome group
        self.ogv1 = DecisionPointValue(name="o1", key="o1", description="Outcome 1")
        self.ogv2 = DecisionPointValue(name="o2", key="o2", description="Outcome 2")
        self.og = OutcomeGroup(
            name="outcome",
            description="",
            version="1.0",
            namespace="x_test",
            key="outcome",
            values=(self.ogv1, self.ogv2),
        )

    def tearDown(self):
        # clean up the temporary directory
        self.tmpdir.cleanup()

    def test_init(self):
        dt = DecisionTable(
            name="Test Table",
            namespace="x_test",
            description="",
            decision_point_group=self.dpg,
            outcome_group=self.og,
            mapping=None,
        )
        self.assertEqual(dt.decision_point_group, self.dpg)
        self.assertEqual(dt.outcome_group, self.og)

        # default should be to populate mapping if not provided
        self.assertIsNotNone(dt.mapping)
        # mapping length should match product of decision point values
        expected_length = len(self.dp1.values) * len(self.dp2.values)
        self.assertEqual(len(dt.mapping), expected_length)
        # Check if mapping is a list of MappingRow objects
        for row in dt.mapping:
            self.assertIsInstance(row, MappingRow)
        # We aren't testing the actual values here, just that they are created
        # correctly. The mappings will be tested in more detail in other tests.

    def test_to_csv(self):
        dt = DecisionTable(
            name="Test Table",
            namespace="x_test",
            description="",
            decision_point_group=self.dpg,
            outcome_group=self.og,
            mapping=None,
        )
        csv_str = decision_table_to_csv(dt=dt)

        # write csv to a temporary file
        csvfile = os.path.join(self.tmpdir.name, "test_table.csv")
        with open(csvfile, "w") as f:
            f.write(csv_str)

        # read the csv file into a DataFrame
        # using pandas
        df = pd.read_csv(csvfile)

        # does line count match expected?
        expected_lines = len(dt.mapping)  # for header
        self.assertEqual(len(df), expected_lines)
        # Check if the DataFrame has the expected columns

        expected_columns = [dp.id for dp in self.dpg.decision_points] + [self.og.id]
        for expected in expected_columns:
            self.assertIn(expected, df.columns, f"Expected column {expected} not found")

    def test_model_dump_json(self):
        dt = DecisionTable(
            name="Test Table",
            namespace="x_test",
            description="",
            decision_point_group=self.dpg,
            outcome_group=self.og,
            mapping=None,
        )
        json_str = dt.model_dump_json()
        self.assertIn("decision_point_group", json_str)
        self.assertIn("outcome_group", json_str)
        self.assertIn("mapping", json_str)

    def test_generate_full_mapping_object_method(self):
        dt = DecisionTable(
            name="Test Table",
            namespace="x_test",
            description="",
            decision_point_group=self.dpg,
            outcome_group=self.og,
            mapping=None,
        )
        mapping = generate_full_mapping(dt=dt)
        # length should match product of decision point values
        expected_length = len(self.dp1.values) * len(self.dp2.values)
        self.assertEqual(len(mapping), expected_length)

        # ensure each row is a  MappingRow
        for row in mapping:
            self.assertIsInstance(row, MappingRow)
            # ensure each row has the correct number of decision point values
            self.assertEqual(
                len(row.decision_point_values), len(dt.decision_point_group)
            )
            # ensure outcome is None
            self.assertIsNone(row.outcome, "Outcome should be None after generation")

    def test_generate_full_mapping_function(self):
        from ssvc.decision_tables.base import generate_full_mapping

        dt = DecisionTable(
            name="Test Table",
            namespace="x_test",
            description="",
            decision_point_group=self.dpg,
            outcome_group=self.og,
            mapping=None,
        )
        mapping = generate_full_mapping(dt)
        # length should match product of decision point values
        expected_length = len(self.dp1.values) * len(self.dp2.values)
        self.assertEqual(len(mapping), expected_length)

        # ensure each row is a  MappingRow
        for row in mapping:
            self.assertIsInstance(row, MappingRow)
            # ensure each row has the correct number of decision point values
            self.assertEqual(
                len(row.decision_point_values), len(dt.decision_point_group)
            )
            self.assertIsNone(row.outcome, "Outcome should be None before distribution")

    def test_populate_mapping_if_none(self):
        dt = DecisionTable(
            name="Test Table",
            namespace="x_test",
            description="",
            decision_point_group=self.dpg,
            outcome_group=self.og,
            mapping=None,
        )

        # Set an empty list to simulate no mapping
        dt.mapping = []
        dt.populate_mapping_if_none()
        self.assertEqual(
            [], dt.mapping, "Mapping should not change if already populated"
        )

        # Now set mapping to None to trigger population
        dt.mapping = None

        # Populate the mapping
        dt.populate_mapping_if_none()

        # Check if mapping is populated
        self.assertIsNotNone(dt.mapping)
        self.assertGreater(len(dt.mapping), 0)

        # Check if each MappingRow has an outcome assigned
        for row in dt.mapping:
            self.assertIsNotNone(
                row.outcome, "Outcome should not be None after population"
            )

    def test_distribute_outcomes_evenly_function(self):
        from ssvc.decision_tables.base import distribute_outcomes_evenly

        dt = DecisionTable(
            name="Test Table",
            namespace="x_test",
            description="",
            decision_point_group=self.dpg,
            outcome_group=self.og,
            mapping=None,
        )
        mapping = generate_full_mapping(dt=dt)

        # Distribute outcomes evenly
        outcome_values = self.og.value_summaries
        new_mapping = distribute_outcomes_evenly(mapping, outcome_values)

        # Check if the new mapping has outcomes assigned
        for row in new_mapping:
            self.assertIsNotNone(
                row.outcome, "Outcome should not be None after distribution"
            )

        # Check if the length of new mapping matches original mapping
        self.assertEqual(len(new_mapping), len(mapping))
        # first outcome should be assigned to first mapping row
        self.assertEqual(new_mapping[0].outcome, outcome_values[0])
        # last outcome should be assigned to last mapping row
        self.assertEqual(new_mapping[-1].outcome, outcome_values[-1])


if __name__ == "__main__":
    unittest.main()
