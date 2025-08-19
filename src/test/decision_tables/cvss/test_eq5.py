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

from ssvc.decision_tables.cvss.equivalence_set_five import V1_0_0 as EQ5


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.eq5 = EQ5

    def test_mapping(self):
        # Table 28: EQ5 - MacroVectors
        #
        # Levels	Constraints	Highest Severity Vector(s)
        # 0	E:A	E:A
        # 1	E:P	E:P
        # 2	E:U	E:U

        e = [k for k in self.eq5.decision_points.keys() if "E" in k][0]
        out = self.eq5.outcome

        for row in self.eq5.mapping:
            with self.subTest(row=row):
                self.assertIn(e, row)
                self.assertIn(out, row)

                if row[e] == "A":
                    # level 0
                    self.assertEqual(row[out], "H")
                elif row[e] == "P":
                    # level 1
                    self.assertEqual(row[out], "M")
                elif row[e] == "U":
                    # level 2
                    self.assertEqual(row[out], "L")
                else:
                    self.fail(f"Unexpected value: {row}")


if __name__ == "__main__":
    unittest.main()
