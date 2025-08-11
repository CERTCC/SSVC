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

from ssvc.decision_tables.cvss.equivalence_set_one import V1_0_0 as EQ1


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.eq1 = EQ1

    def test_mapping(self):
        #     Levels	Constraints	Highest Severity Vector(s)
        # 0	AV:N and PR:N and UI:N	AV:N/PR:N/UI:N
        # 1	(AV:N or PR:N or UI:N) and not (AV:N and PR:N and UI:N) and not AV:P	AV:A/PR:N/UI:N or AV:N/PR:L/UI:N or AV:N/PR:N:/UI:P
        # 2	AV:P or not(AV:N or PR:N or UI:N)	AV:P/PR:N/UI:N or AV:A/PR:L/UI:P

        av = [k for k in self.eq1.decision_points.keys() if "AV" in k][0]
        pr = [k for k in self.eq1.decision_points.keys() if "PR" in k][0]
        ui = [k for k in self.eq1.decision_points.keys() if "UI" in k][0]
        out = self.eq1.outcome
        for row in self.eq1.mapping:
            with self.subTest(row=row):
                self.assertIn(av, row)
                self.assertIn(pr, row)
                self.assertIn(ui, row)
                self.assertIn(out, row)
                if row[av] == "N" and row[pr] == "N" and row[ui] == "N":
                    # level 0
                    self.assertEqual(row[out], "H")
                elif row[av] == "N" and row[av] != "P":
                    # level 1
                    self.assertEqual(row[out], "M")
                elif row[pr] == "N" and row[av] != "P":
                    self.assertEqual(row[out], "M")
                elif row[ui] == "N" and row[av] != "P":
                    self.assertEqual(row[out], "M")
                elif row[av] == "P":
                    # level 2
                    self.assertEqual(row[out], "L")
                else:
                    self.assertNotEqual(row[av], "N")
                    self.assertNotEqual(row[pr], "N")
                    self.assertNotEqual(row[ui], "N")
                    self.assertEqual(row[out], "L")


if __name__ == "__main__":
    unittest.main()
