#  Copyright (c) 2026 Carnegie Mellon University.
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

from ssvc.decision_tables.base import ascii_tree as base_ascii_tree
from ssvc.decision_tables.example.to_play import LATEST as EXAMPLE_DT
from ssvc.decision_tables.helpers import (
    ascii_tree,
    decision_table_to_longform_df,
)


class TestAsciiTree(unittest.TestCase):
    def setUp(self) -> None:
        self.dt = EXAMPLE_DT

    def test_df_omitted(self) -> None:
        # The path every caller in the repository takes.
        self.assertGreater(len(ascii_tree(self.dt).splitlines()), 0)

    def test_df_supplied(self) -> None:
        # Passing the frame is what the signature invites, and `df == None`
        # made it raise ValueError from DataFrame.__bool__ for every frame.
        df = decision_table_to_longform_df(self.dt)
        self.assertEqual(ascii_tree(self.dt, df), ascii_tree(self.dt))

    def test_df_supplied_via_base(self) -> None:
        # base re-exports the helper, so the same call has two public routes.
        df = decision_table_to_longform_df(self.dt)
        self.assertEqual(
            base_ascii_tree(self.dt, df), base_ascii_tree(self.dt)
        )

    def test_caller_frame_is_not_modified(self) -> None:
        # The "row" column was dropped in place. That only ever touched the
        # frame this function built itself while `df` could not be supplied;
        # once it can, an in-place drop takes a column off the caller's object.
        df = decision_table_to_longform_df(self.dt)
        df.insert(0, "row", range(len(df)))
        columns_before = list(df.columns)

        ascii_tree(self.dt, df)

        self.assertEqual(list(df.columns), columns_before)

    def test_row_column_is_excluded_from_the_tree(self) -> None:
        # Dropping "row" must still happen, just not on the caller's frame.
        df = decision_table_to_longform_df(self.dt)
        without_row = ascii_tree(self.dt, df)

        df_with_row = decision_table_to_longform_df(self.dt)
        df_with_row.insert(0, "row", range(len(df_with_row)))

        self.assertEqual(ascii_tree(self.dt, df_with_row), without_row)


if __name__ == "__main__":
    unittest.main()
