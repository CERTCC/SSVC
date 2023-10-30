#  Copyright (c) 2023 Carnegie Mellon University and Contributors.
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

from ssvc.outcomes.base import OutcomeGroup, OutcomeValue

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


class MyTestCase(unittest.TestCase):
    def test_outcome_value(self):
        for x in ALPHABET:
            ov = OutcomeValue(key=x, name=x, description=x)
            self.assertEqual(ov.key, x)
            self.assertEqual(ov.name, x)
            self.assertEqual(ov.description, x)

    def test_outcome_group(self):
        ALPHABET

        values = []
        for x in ALPHABET:
            values.append(OutcomeValue(key=x, name=x, description=x))

        og = OutcomeGroup(
            name="og", description="an outcome group", outcomes=tuple(values)
        )

        self.assertEqual(og.name, "og")
        self.assertEqual(og.description, "an outcome group")

        self.assertEqual(len(og), len(ALPHABET))

        for i, letter in enumerate(ALPHABET):
            self.assertEqual(og.outcomes[i].key, letter)
            self.assertEqual(og.outcomes[i].name, letter)
            self.assertEqual(og.outcomes[i].description, letter)


if __name__ == "__main__":
    unittest.main()
