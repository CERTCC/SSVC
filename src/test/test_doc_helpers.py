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

from ssvc.decision_points.base import DecisionPoint, DecisionPointValue
from ssvc.doc_helpers import example_block, markdown_table


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.dp = DecisionPoint(
            namespace="test",
            name="test name",
            definition="test description",
            key="TK",
            version="1.0.0",
            values=(
                DecisionPointValue(
                    name="A", key="A", definition="A Definition"
                ),
                DecisionPointValue(
                    name="B", key="B", definition="B Definition"
                ),
            ),
        )

    def tearDown(self):
        pass

    def test_markdown_table(self):
        result = markdown_table(self.dp)

        expected = (
            "test description\n"
            "\n"
            "| Value | Definition |\n"
            "|:-----|:-----------|\n"
            "| A (A) | A Definition |\n"
            "| B (B) | B Definition |"
        )

        self.assertEqual(result, expected)

        indented = markdown_table(self.dp, indent=4)

        expected_indented = (
            "    test description\n"
            "\n"
            "    | Value | Definition |\n"
            "    |:-----|:-----------|\n"
            "    | A (A) | A Definition |\n"
            "    | B (B) | B Definition |"
        )

        self.assertEqual(indented, expected_indented)

    def test_example_block(self):

        result = example_block(self.dp)

        self.assertIn("!!! note", result)
        self.assertIn("\n    | Value | Definition |", result)
        self.assertIn("\n    | A (A) | A Definition |", result)
        self.assertIn("\n    | B (B) | B Definition |", result)
        self.assertIn("\n    ??? example", result)
        self.assertIn("\n        ```json", result)

        for value in self.dp.values:
            self.assertIn(value.name, result)
            self.assertIn(value.definition, result)


if __name__ == "__main__":
    unittest.main()
