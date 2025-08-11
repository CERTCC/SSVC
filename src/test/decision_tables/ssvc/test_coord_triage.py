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

from ssvc.decision_tables.ssvc.coord_triage import LATEST as CT


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.ct = CT

    def test_mapping(self):
        rp = [k for k in self.ct.decision_points if "RP" in k][0]
        scon = [k for k in self.ct.decision_points if "SCON" in k][0]
        rc = [k for k in self.ct.decision_points if "RC" in k][0]
        sc = [k for k in self.ct.decision_points if "SC" in k and "SCON" not in k][0]
        se = [k for k in self.ct.decision_points if "SE" in k][0]
        u = [k for k in self.ct.decision_points if "U" in k][0]
        psi = [k for k in self.ct.decision_points if "PSI" in k][0]
        outcome = self.ct.outcome

        for row in self.ct.mapping:
            with self.subTest(row=row):
                self.assertIn(rp, row)
                self.assertIn(scon, row)
                self.assertIn(rc, row)
                self.assertIn(sc, row)
                self.assertIn(se, row)
                self.assertIn(u, row)
                self.assertIn(psi, row)
                self.assertIn(outcome, row)

                multiparty_supereffective_safety_impact = (
                    row[sc] == "M" and row[u] == "SE" and row[psi] == "S"
                )

                # Report Public: If a report is already public,
                # OR If no suppliers have been contacted,
                # then CERT/CC will decline the case unless
                # there are multiple suppliers,
                # super effective Utility,
                # and significant Public Safety Impact.
                if row[rp] == "Y" or row[scon] == "N":
                    if not multiparty_supereffective_safety_impact:
                        self.assertEqual("D", row[outcome])
                else:
                    if row[rc] == "NC":
                        # Report Credibility: If the report is not credible,
                        # then CERT/CC will decline the case.
                        self.assertEqual("D", row[outcome])


if __name__ == "__main__":
    unittest.main()
