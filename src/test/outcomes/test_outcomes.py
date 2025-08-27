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

from ssvc.outcomes.base import OutcomeGroup, OutcomeValue

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


class MyTestCase(unittest.TestCase):
    def test_outcome_value(self):
        for x in ALPHABET:
            ov = OutcomeValue(key=x, name=x, definition=x)
            self.assertEqual(ov.key, x)
            self.assertEqual(ov.name, x)
            self.assertEqual(ov.definition, x)

    def test_outcome_group(self):
        values = []
        for x in ALPHABET:
            values.append(OutcomeValue(key=x, name=x, definition=x))

        og = OutcomeGroup(
            name="Outcome Group",
            key="OGX",
            definition="an outcome group",
            namespace="test",
            values=tuple(values),
        )

        self.assertEqual(og.name, "Outcome Group")
        self.assertEqual(og.key, "OGX")
        self.assertEqual(og.definition, "an outcome group")

        self.assertEqual(len(og), len(ALPHABET))

        og_outcomes = list(og.values)
        for i, letter in enumerate(ALPHABET):
            self.assertEqual(og_outcomes[i].key, letter)
            self.assertEqual(og_outcomes[i].name, letter)
            self.assertEqual(og_outcomes[i].definition, letter)


if __name__ == "__main__":
    unittest.main()
