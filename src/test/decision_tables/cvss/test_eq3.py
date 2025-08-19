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

from ssvc.decision_tables.cvss.equivalence_set_three import V1_0_0 as EQ3


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.eq3 = EQ3

    def test_mapping(self):
        #         Table 26: EQ3 - MacroVectors
        #
        # Levels	Constraints	Highest Severity Vector(s)
        # 0	VC:H and VI:H	VC:H/VI:H/VA:H
        # 1	not (VC:H and VI:H) and (VC:H or VI:H or VA:H)	VC:L/VI:H/VA:H or VC:H/VI:L/VA:H
        # 2	not (VC:H or VI:H or VA:H)	VC:L/VI:L/VA:L
        vc = [k for k in self.eq3.decision_points.keys() if "VC" in k][0]
        vi = [k for k in self.eq3.decision_points.keys() if "VI" in k][0]
        va = [k for k in self.eq3.decision_points.keys() if "VA" in k][0]
        out = self.eq3.outcome

        for row in self.eq3.mapping:
            with self.subTest(row=row):
                self.assertIn(vc, row)
                self.assertIn(vi, row)
                self.assertIn(va, row)
                self.assertIn(out, row)

                if row[vc] == "H" and row[vi] == "H":
                    # level 0
                    self.assertEqual(row[out], "H")
                elif row[vc] == "H" or row[vi] == "H" or row[va] == "H":
                    # level 1
                    self.assertFalse(row[vc] == "H" and row[vi] == "H")
                    self.assertEqual(row[out], "M")
                else:
                    # level 2
                    self.assertNotEqual(row[vc], "H")
                    self.assertNotEqual(row[vi], "H")
                    self.assertNotEqual(row[va], "H")
                    self.assertEqual(row[out], "L")


if __name__ == "__main__":
    unittest.main()
