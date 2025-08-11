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

from ssvc.decision_tables.cvss.equivalence_set_two import V1_0_0 as EQ2


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.eq2 = EQ2

    def test_mapping(self):
        #     Table 25: EQ2 - MacroVectors
        #
        # Levels	Constraints	Highest Severity Vector(s)
        # 0	AC:L and AT:N	AC:L/AT:N
        # 1	not (AC:L and AT:N)	AC:L/AT:P or AC:H/AT:N
        ac = [k for k in self.eq2.decision_points.keys() if "AC" in k][0]
        at = [k for k in self.eq2.decision_points.keys() if "AT" in k][0]
        out = self.eq2.outcome

        for row in self.eq2.mapping:
            with self.subTest(row=row):
                self.assertIn(ac, row)
                self.assertIn(at, row)
                self.assertIn(out, row)

                if row[ac] == "L" and row[at] == "N":
                    # level 0
                    self.assertEqual(row[out], "H")
                else:
                    # level 1
                    self.assertEqual(row[out], "L")


if __name__ == "__main__":
    unittest.main()
