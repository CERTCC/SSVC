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

from ssvc.decision_points import SsvcDecisionPoint, SsvcDecisionPointValue
from ssvc.doc_helpers import example_block, markdown_table


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.dp = SsvcDecisionPoint(
            namespace="test",
            name="test name",
            description="test description",
            key="TK",
            version="1.0.0",
            values=(
                SsvcDecisionPointValue(name="A", key="A", description="A Definition"),
                SsvcDecisionPointValue(name="B", key="B", description="B Definition"),
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
            "| A | A Definition |\n"
            "| B | B Definition |"
        )

        self.assertEqual(result, expected)

        indented = markdown_table(self.dp, indent=4)

        expected_indented = (
            "    test description\n"
            "\n"
            "    | Value | Definition |\n"
            "    |:-----|:-----------|\n"
            "    | A | A Definition |\n"
            "    | B | B Definition |"
        )

        self.assertEqual(indented, expected_indented)

    def test_example_block(self):

        result = example_block(self.dp)

        self.assertIn("!!! note", result)
        self.assertIn("\n    | Value | Definition |", result)
        self.assertIn("\n    | A | A Definition |", result)
        self.assertIn("\n    | B | B Definition |", result)
        self.assertIn("\n    ??? example", result)
        self.assertIn("\n        ```json", result)

        for value in self.dp.values:
            self.assertIn(value.name, result)
            self.assertIn(value.description, result)


if __name__ == "__main__":
    unittest.main()
