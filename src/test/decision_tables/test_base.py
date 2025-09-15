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
import json
import os
import tempfile
import unittest
from unittest.mock import Mock, patch

import pandas as pd

from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_tables.base import (
    DecisionTable,
    decision_table_to_csv,
    decision_table_to_df,
    decision_table_to_longform_df,
    dpdict_to_combination_list,
)
from ssvc.dp_groups.base import DecisionPoint
from ssvc.outcomes.base import OutcomeGroup


class TestDecisionTableBase(unittest.TestCase):
    def setUp(self):
        # create a temporary directory for testing
        self.tmpdir = tempfile.TemporaryDirectory()

        # Create dummy decision point values
        self.dp1v1 = DecisionPointValue(
            name="a", key="a", definition="A value"
        )
        self.dp1v2 = DecisionPointValue(
            name="b", key="b", definition="B value"
        )

        self.dp2v1 = DecisionPointValue(
            name="x", key="x", definition="X value"
        )
        self.dp2v2 = DecisionPointValue(
            name="y", key="y", definition="Y value"
        )
        self.dp2v3 = DecisionPointValue(
            name="z", key="z", definition="Z value"
        )
        self.dp2v4 = DecisionPointValue(
            name="w", key="w", definition="W value"
        )

        # Create dummy decision points and group
        self.dp1 = DecisionPoint(
            name="dp1",
            definition="description for dp1",
            version="1.0.0",
            namespace="test",
            key="dp1",
            values=(self.dp1v1, self.dp1v2),
        )
        self.dp2 = DecisionPoint(
            name="dp2",
            definition="description for dp2",
            version="1.0.0",
            namespace="test",
            key="dp2",
            values=(self.dp2v1, self.dp2v2, self.dp2v3, self.dp2v4),
        )
        # Create dummy outcome group
        self.ogv1 = DecisionPointValue(
            name="o1", key="o1", definition="Outcome 1"
        )
        self.ogv2 = DecisionPointValue(
            name="o2", key="o2", definition="Outcome 2"
        )
        self.ogv3 = DecisionPointValue(
            name="o3", key="o3", definition="Outcome 3"
        )

        self.og = OutcomeGroup(
            name="outcome",
            definition="description for outcome",
            version="1.0.0",
            namespace="test",
            key="outcome",
            values=(self.ogv1, self.ogv2, self.ogv3),
        )

        self.dplist = [self.dp1, self.dp2, self.og]
        self.dpdict = {dp.id: dp for dp in self.dplist}

        self.dt = DecisionTable(
            key="TEST",
            namespace="test",
            name="Test Table",
            definition="Describes the test table",
            decision_points=self.dpdict,
            outcome=self.og.id,
        )

    def tearDown(self):
        # clean up the temporary directory
        self.tmpdir.cleanup()

    def test_init(self):
        dt = self.dt

        self.assertEqual(dt.outcome, self.og.id)

        # default should be to populate mapping if not provided
        self.assertIsNotNone(dt.mapping)
        # mapping length should match product of decision point values
        expected_length = len(self.dp1.values) * len(self.dp2.values)

        self.assertEqual(len(dt.mapping), expected_length),
        # Check if mapping is a list of dicts
        for row in dt.mapping:
            self.assertIsInstance(row, dict)
        # We aren't testing the actual values here, just that they are created
        # correctly. The mappings will be tested in more detail in other tests.

    def test_decision_table_to_csv(self):
        dt = self.dt

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

        expected_columns = set(self.dpdict.keys())
        colset = set(df.columns)

        # everything in expected_columns should be in colset
        # (colset might have more columns, like a row index, but that's okay)
        self.assertTrue(
            expected_columns.issubset(colset),
            "Expected columns are not a subset of DataFrame columns",
        )

    def test_model_dump_json(self):
        dt = self.dt

        json_str = dt.model_dump_json()

        self.assertIn("decision_points", json_str)
        self.assertIn("outcome", json_str)
        self.assertIn("mapping", json_str)

        # load it as a dict to check structure
        d = json.loads(json_str)
        self.assertIn("decision_points", d)
        self.assertIn("outcome", d)
        self.assertIn("mapping", d)
        # check that outcome is a string corresponding to a key in decsion point group
        self.assertIsInstance(d["outcome"], str)
        self.assertIn(d["outcome"], d["decision_points"])
        # Check if mapping is a list of dicts
        self.assertIsInstance(d["mapping"], list)
        self.assertTrue(
            all(isinstance(row, dict) for row in d["mapping"]),
        )
        # and that the keys of each dict match the keys of decision points
        expect_keys = set(d["decision_points"].keys())
        for row in d["mapping"]:
            row_keys = set(row.keys())
            self.assertEqual(
                row_keys,
                expect_keys,
                "Row keys do not match expected decision points",
            )

    def test_populate_mapping_if_none(self):
        dt = self.dt

        # Set an empty list to simulate no mapping
        dt.mapping = ["a", "b", "c"]
        dt.populate_mapping_if_empty()
        self.assertEqual(
            ["a", "b", "c"],
            dt.mapping,
            "Mapping should not change if already populated",
        )

        # Now set mapping to None to trigger population
        dt.mapping = None

        # Populate the mapping
        dt.populate_mapping_if_empty()

        # Check if mapping is populated
        self.assertIsNotNone(dt.mapping)
        self.assertGreater(len(dt.mapping), 0)

        # Check if each MappingRow has an outcome assigned
        for row in dt.mapping:
            self.assertIsNotNone(
                row[dt.outcome], "Outcome should not be None after population"
            )

    def test_distribute_outcomes_evenly_function(self):
        from ssvc.decision_tables.base import distribute_outcomes_evenly

        dt = self.dt

        # Distribute outcomes evenly
        outcome_key = dt.outcome
        og = dt.decision_points[outcome_key]
        outcome_values = [v.key for v in og.values]

        # unset the mapping to test distribution
        for row in dt.mapping:
            row[outcome_key] = None

        self.assertTrue(all(row[outcome_key] is None for row in dt.mapping))

        new_mapping = distribute_outcomes_evenly(dt.mapping, og)

        # Check if the new mapping has outcomes assigned
        for row in new_mapping:
            self.assertIsNotNone(
                row[outcome_key],
                "Outcome should not be None after distribution",
            )

        # Check if the length of new mapping matches original mapping
        self.assertEqual(len(new_mapping), len(dt.mapping))
        # first outcome should be assigned to first mapping row
        self.assertEqual(new_mapping[0][outcome_key], outcome_values[0])
        # last outcome should be assigned to last mapping row
        self.assertEqual(new_mapping[-1][outcome_key], outcome_values[-1])

    def test_decision_table_to_longform_df(self):
        dt = self.dt

        df = decision_table_to_longform_df(dt)
        self.assertIsInstance(df, pd.DataFrame)
        # Should have as many rows as mapping
        self.assertEqual(len(df), len(dt.mapping))
        # Should have as many columns as decision points (including outcome)
        expected_num_cols = len(self.dplist)
        self.assertEqual(len(df.columns), expected_num_cols)
        # All values should be lowercase strings
        for col in df.columns:
            for val in df[col]:
                if isinstance(val, str):
                    self.assertEqual(val, val.lower())
        # Column names should contain decision point names and version
        for dp in self.dplist:
            self.assertTrue(any(dp.name in c for c in df.columns))
        self.assertTrue(any(self.og.name in c for c in df.columns))

    @patch("ssvc.decision_tables.base.decision_table_to_longform_df")
    @patch("ssvc.decision_tables.base.decision_table_to_shortform_df")
    def test_decision_table_to_df(self, mock_shortform, mock_longform):
        mock_df = pd.DataFrame(
            [
                {"dp1": 0, "dp2": 0, "outcome": 0},
                {"dp1": 0, "dp2": 1, "outcome": 1},
                {"dp1": 1, "dp2": 0, "outcome": 1},
                {"dp1": 1, "dp2": 1, "outcome": 2},
            ],
        )
        mock_longform.return_value = mock_df
        mock_shortform.return_value = mock_df
        # Create a DecisionTable instance for testing
        dt = Mock()

        # default should be shortform
        # reset mocks
        mock_longform.reset_mock()
        mock_shortform.reset_mock()

        df_default = decision_table_to_df(dt)

        self.assertTrue(df_default.equals(mock_df))
        mock_shortform.assert_called_with(dt)
        mock_longform.assert_not_called()

        # Test longform
        df_long = decision_table_to_df(dt, longform=True)
        self.assertTrue(df_long.equals(mock_df))
        mock_longform.assert_called_with(dt)
        mock_shortform.assert_called_with(dt)

        # Test shortform
        mock_longform.reset_mock()
        mock_shortform.reset_mock()

        df_short = decision_table_to_df(dt, longform=False)
        self.assertTrue(df_short.equals(mock_df))
        mock_shortform.assert_called_once_with(dt)
        mock_longform.assert_not_called()

    def test_combo_strings(self):
        dps = dict(self.dpdict)  # copy the decision points
        del [dps[self.og.id]]  # remove outcome group from decision points

        # get all the combinations
        combos = dpdict_to_combination_list(dps)

        # assert that the number of combinations is the product of the number of values
        # for each decision point
        n_combos = 1
        for dp in dps.values():
            n_combos *= len(dp.values)
        self.assertEqual(n_combos, len(combos))

        counter = {}
        for dp in dps.values():
            for v in dp.values:
                counter[v.key] = 0

        # assert that each combination is a tuple
        for combo in combos:
            self.assertEqual(len(dps), len(combo))
            self.assertIsInstance(combo, dict)
            # assert that each value in the combination is a string
            print(combo)
            for value in combo.values():
                print(value)
                self.assertIn(value, counter)
                counter[value] += 1

        for k, count in counter.items():
            # each count should be greater than or equal to 0
            self.assertGreaterEqual(count, 0)
            # # each count should be less than or equal to the length of the combination
            self.assertLessEqual(count, len(combos))

    def test_single_dp_dt(self):
        # Create a DecisionTable with a single DecisionPoint
        dp_in = DecisionPoint(
            name="dp_in",
            definition="A single decision point",
            version="1.0.0",
            namespace="test",
            key="dp",
            values=(self.dp1v1, self.dp1v2),
            registered=False,
        )
        dp_out = DecisionPoint(
            namespace="test",
            key="outcome",
            name="Outcome",
            definition="Outcome for single DP test",
            version="1.0.0",
            values=(self.ogv1, self.ogv2, self.ogv3),
            registered=False,
        )

        single_dt = DecisionTable(
            key="SINGLE_TEST",
            namespace="test",
            name="Single DP Test Table",
            definition="Describes the single DP test table",
            decision_points={dp.id: dp for dp in [dp_in, dp_out]},
            outcome=dp_out.id,
            registered=False,
        )

        # Check if mapping is populated correctly
        self.assertIsNotNone(single_dt.mapping)
        self.assertEqual(len(single_dt.mapping), len(dp_in.values))

        # Check if the mapping contains the correct outcomes
        for row in single_dt.mapping:
            self.assertIn(single_dt.outcome, row)
            self.assertIn(
                row[single_dt.outcome], [v.key for v in self.og.values]
            )

    def test_should_reject_duplicate_conflicting_mappings(self):
        dt = self.dt

        # dt already has a mapping, so we can just append to it
        self.assertGreater(len(dt.mapping), 0, "Mapping should not be empty")

        new_row = dict(dt.mapping[0])  # copy the first row
        self.assertEqual(
            new_row[dt.outcome],
            self.ogv1.key,
            "First row should have outcome o1",
        )
        new_row[dt.outcome] = self.ogv2.key  # change the outcome to o2
        # insert it at position 1
        dt.mapping.insert(1, new_row)

        with self.assertRaises(ValueError) as context:
            dt.remove_duplicate_mapping_rows()

        self.assertIn("Conflicting mappings found", str(context.exception))

    def test_should_warn_duplicate_nonconflicting_mappings(self):
        dt = self.dt

        # dt already has a mapping, so we can just append to it
        self.assertGreater(len(dt.mapping), 0, "Mapping should not be empty")

        new_row = dict(dt.mapping[0])  # copy the first row
        self.assertEqual(
            new_row[dt.outcome],
            self.ogv1.key,
            "First row should have outcome o1",
        )
        # do not change the outcome, just duplicate the row
        # insert it at position 1
        dt.mapping.insert(1, new_row)

        with self.assertLogs(level="WARNING") as log:
            dt.remove_duplicate_mapping_rows()

        self.assertIn("Duplicate mapping found", log.output[0])

    def test_should_fail_on_incomplete_mapping(self):
        dt = self.dt

        # dt already has a mapping, so we can just remove something from it
        self.assertGreater(len(dt.mapping), 0, "Mapping should not be empty")
        dt.mapping = dt.mapping[:-1]  # remove the last row

        with self.assertRaises(ValueError) as context:
            dt.check_mapping_coverage()

        self.assertIn("Mapping is incomplete", str(context.exception))


if __name__ == "__main__":
    unittest.main()
