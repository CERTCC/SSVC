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

from ssvc.decision_tables.cvss.equivalence_set_six import V1_0_0 as EQ6


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.eq6 = EQ6

    def test_mapping(self):
        # Table 29: EQ6 - MacroVectors
        #
        # Levels	Constraints	Highest Severity Vector(s)
        # 0	(CR:H and VC:H) or (IR:H and VI:H) or (AR:H and VA:H)	VC:H/VI:H/VA:H/CR:H/IR:H/AR:H
        # 1	not (CR:H and VC:H) and not (IR:H and VI:H) and not (AR:H and VA:H)	VC:H/VI:H/VA:H/CR:M/IR:M/AR:M or VC:H/VI:H/VA:L/CR:M/IR:M/AR:H or VC:H/VI:L/VA:H/CR:M/IR:H/AR:M or VC:H/VI:L/VA:L/CR:M/IR:H/AR:H or VC:L/VI:H/VA:H/CR:H/IR:M/AR:M or VC:L/VI:H/VA:L/CR:H/IR:M/AR:H or VC:L/VI:L/VA:H/CR:H/IR:H/AR:M or VC:L/VI:L/VA:L/CR:H/IR:H/AR:H

        cr = [k for k in self.eq6.decision_points.keys() if "CR" in k][0]
        ir = [k for k in self.eq6.decision_points.keys() if "IR" in k][0]
        ar = [k for k in self.eq6.decision_points.keys() if "AR" in k][0]

        vc = [k for k in self.eq6.decision_points.keys() if "VC" in k][0]
        vi = [k for k in self.eq6.decision_points.keys() if "VI" in k][0]
        va = [k for k in self.eq6.decision_points.keys() if "VA" in k][0]
        out = self.eq6.outcome

        for row in self.eq6.mapping:
            with self.subTest(row=row):
                self.assertIn(cr, row)
                self.assertIn(ir, row)
                self.assertIn(ar, row)
                self.assertIn(out, row)

                if row[cr] == "H" and row[vc] == "H":
                    # level 0
                    self.assertEqual(row[out], "H")
                elif row[ir] == "H" and row[vi] == "H":
                    # level 0
                    self.assertEqual(row[out], "H")
                elif row[ar] == "H" and row[va] == "H":
                    # level 0
                    self.assertEqual(row[out], "H")
                else:
                    # level 1
                    self.assertEqual(row[out], "L")


if __name__ == "__main__":
    unittest.main()
