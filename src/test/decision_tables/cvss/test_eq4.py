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

from ssvc.decision_tables.cvss.equivalence_set_four import V1_0_0 as EQ4


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.eq4 = EQ4

    def test_mapping(self):
        msi = [k for k in self.eq4.decision_points.keys() if "MSI" in k][0]
        msa = [k for k in self.eq4.decision_points.keys() if "MSA" in k][0]
        sc = [k for k in self.eq4.decision_points.keys() if "SC" in k][0]
        out = self.eq4.outcome

        for row in self.eq4.mapping:
            self.assertIn(msi, row)
            self.assertIn(msa, row)
            self.assertIn(sc, row)
            self.assertIn(out, row)

            # Levels	Constraints	Highest Severity Vector(s)
            # 0	MSI:S or MSA:S	SC:H/SI:S/SA:S
            # 1	not (MSI:S or MSA:S) and (SC:H or SI:H or SA:H)	SC:H/SI:H/SA:H
            # 2	not (MSI:S or MSA:S) and not (SC:H or SI:H or SA:H)	SC:L/SI:L/SA:L
            if row[msi] == "S" or row[msa] == "S":
                # level 0
                self.assertEqual(row[out], "H")
            else:
                # level 1
                if row[msi] == "H":
                    self.assertEqual(row[out], "M")
                elif row[msa] == "H":
                    self.assertEqual(row[out], "M")
                elif row[sc] == "H":
                    self.assertEqual(row[out], "M")
                else:
                    # level 2
                    self.assertEqual(row[out], "L")


if __name__ == "__main__":
    unittest.main()
