#  Copyright (c) 2023-2025 Carnegie Mellon University.
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

import pandas as pd

from ssvc import csv_analyzer as acsv


class MyTestCase(unittest.TestCase):
    def test_col_norm(self):
        # col_norm should remove any non-alphanumeric characters and replace them with underscores
        # col_norm should convert all characters to lowercase

        # fold to lowercase
        self.assertEqual(acsv._col_norm("Exploitation"), "exploitation")
        self.assertEqual(
            acsv._col_norm("AbcdEfghIjklmnOpqrstUvwxYz"),
            "abcdefghijklmnopqrstuvwxyz",
        )

        # replace strings of non-alphanumeric characters with underscores
        self.assertEqual(acsv._col_norm("War!"), "war_")
        self.assertEqual(
            acsv._col_norm("Foo!@#$%^&*()- .,/<>;:'\"[]{}+=BAR"), "foo_bar"
        )

    def test_imp_df(self):
        # given a list of column names and a list of feature importances,
        # imp_df should return a dataframe with the column names and feature importances
        # sorted in descending order by feature importance

        column_names = [
            "exploitation",
            "human_impact",
            "automatable",
            "exposure",
        ]
        importances = [0.347222, 0.291667, 0.180556, 0.166667]
        df = acsv._imp_df(column_names, importances)
        self.assertEqual(df["feature"][0], "exploitation")
        self.assertEqual(df["feature_importance"][0], 0.347222)
        self.assertEqual(df["feature"][1], "human_impact")
        self.assertEqual(df["feature_importance"][1], 0.291667)
        self.assertEqual(df["feature"][2], "automatable")
        self.assertEqual(df["feature_importance"][2], 0.180556)
        self.assertEqual(df["feature"][3], "exposure")
        self.assertEqual(df["feature_importance"][3], 0.166667)

    def test_drop_col_feat_imp(self):
        # given a model, two dataframes representing the input and output data, return a dataframe

        # create a model
        model = acsv.DecisionTreeClassifier()
        # create a dataframe representing the input data
        df = pd.DataFrame(
            {
                "color": [1, 1, 1, 1, 2, 2, 2, 2],
                "size": [1, 2, 3, 4, 1, 2, 3, 4],
                "priority": [1, 1, 2, 2, 2, 3, 3, 3],
            }
        )
        x = df.drop("priority", axis=1)
        y = df["priority"]

        # call drop_col_feat_imp
        df = acsv._drop_col_feat_imp(model, x, y)
        # assert that the dataframe returned by drop_col_feat_imp is the same as the dataframe returned by imp_df

        self.assertEqual(df["feature"][0], "color")
        self.assertEqual(df["feature"][1], "size")
        # I don't really know how to test a model fit, so let's just make sure
        # that the column is ordered in descending order
        self.assertGreaterEqual(
            df["feature_importance"][0], df["feature_importance"][1]
        )

    def test_split_data(self):
        df = pd.DataFrame(
            {"A": [1, 2, 3, 4], "B": [5, 6, 7, 8], "C": [9, 10, 11, 12]}
        )
        x, y = acsv._split_data(df, "C")

        self.assertTrue(x.equals(df.drop("C", axis=1)))
        self.assertTrue(y.equals(df["C"]))

    def test_clean_table(self):
        # columns get renamed
        # column named "row" is dropped

        df = pd.DataFrame(
            {
                "row": [1, 2, 3, 4],
                "A!": [1, 2, 3, 4],
                "?B?": [5, 6, 7, 8],
                "C with spaces": [9, 10, 11, 12],
            }
        )
        df = acsv._clean_table(df)
        self.assertNotIn("row", df.columns)
        self.assertEqual(df.columns[0], "a_")
        self.assertEqual(df.columns[1], "_b_")
        self.assertEqual(df.columns[2], "c_with_spaces")

    def test_perm_feat_imp(self):
        model = acsv.DecisionTreeClassifier()
        df = pd.DataFrame(
            {
                "color": [1, 1, 1, 1, 2, 2, 2, 2],
                "size": [1, 2, 3, 4, 1, 2, 3, 4],
                "priority": [1, 1, 2, 2, 2, 3, 3, 3],
            }
        )
        x = df.drop("priority", axis=1)
        y = df["priority"]

        df = acsv._perm_feat_imp(model, x, y)

        self.assertIn("color", df["feature"].values)
        self.assertIn("size", df["feature"].values)
        # I don't really know how to test a model fit, so let's just make sure
        # that the column is ordered in descending order
        self.assertGreaterEqual(
            df["feature_importance"][0], df["feature_importance"][1]
        )

    def test_parse_args(self):
        # given a list of arguments, parse_args should return an argparse.Namespace object
        # with the arguments as attributes
        args = [
            "foo.csv",
            "--outcol",
            "bar",
            "--permutation",
        ]
        args = acsv._parse_args(args)
        self.assertEqual(args.csvfile, "foo.csv")
        self.assertEqual(args.outcol, "bar")
        self.assertTrue(args.permutation)

        args = [
            "foo.csv",
        ]
        args = acsv._parse_args(args)
        self.assertEqual(args.csvfile, "foo.csv")
        self.assertEqual(args.outcol, "priority")
        self.assertFalse(args.permutation)

    def test_prepare_data(self):
        df = pd.DataFrame()
        target = "outcome"

        # key error when target is not in df.columns
        self.assertNotIn(target, df.columns)
        self.assertRaises(KeyError, acsv._prepare_data, df, target)

        df["color"] = [1, 1, 1, 1, 2, 2, 2, 2]
        df["size"] = [1, 2, 3, 4, 1, 2, 3, 4]
        df["outcome"] = [1, 1, 1, 1, 2, 2, 2, 2]

        # create_dt_classifier should return a DecisionTreeClassifier object
        x, y = acsv._prepare_data(df, target)
        self.assertIsInstance(x, pd.DataFrame)
        self.assertIsInstance(y, pd.Series)

        self.assertIn("color_", x.columns)
        self.assertIn("size_", x.columns)


if __name__ == "__main__":
    unittest.main()
