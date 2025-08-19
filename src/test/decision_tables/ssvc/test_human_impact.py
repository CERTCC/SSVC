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

from ssvc.decision_tables.ssvc.human_impact import HUMAN_IMPACT_1 as HI


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.hi: "DecisionTable" = HI
        self.si: str = [
            k for k in self.hi.decision_points.keys() if "SI" in k
        ][0]
        self.mi: str = [
            k for k in self.hi.decision_points.keys() if "MI" in k
        ][0]
        self.outcome: str = self.hi.outcome

    def test_mapping(self):
        for i, row in enumerate(self.hi.mapping):
            with self.subTest(row=row):
                self.assertIn(self.si, row)
                self.assertIn(self.mi, row)
                self.assertIn(self.outcome, row)

        if row[self.si] == "N" and row[self.mi] in ["D", "MSC"]:
            # Low	Safety Impact:(Negligible) AND Mission Impact:(Degraded OR Crippled)
            self.assertEqual(row[self.outcome], "L", f"row {i}: {row}")
        elif row[self.si] == "N" and row[self.mi] == "MEF":
            # Medium	(Safety Impact:Negligible AND Mission Impact:MEF Failure)
            self.assertEqual(row[self.outcome], "M", f"row {i}: {row}")
        elif row[self.si] == "M" and row[self.mi] in ["D", "MSC"]:
            # Medium	OR (Safety Impact:Marginal AND Mission Impact:(Degraded OR Crippled))
            self.assertEqual(row[self.outcome], "M", f"row {i}: {row}")
        elif row[self.si] == "C" and row[self.mi] in ["D", "MSC"]:
            # High	(Safety Impact:Critical AND Mission Impact:(Degraded OR Crippled))
            self.assertEqual(row[self.outcome], "H", f"row {i}: {row}")
        elif row[self.si] == "M" and row[self.mi] == "MEF":
            # OR (Safety Impact:Marginal AND Mission Impact:MEF Failure)
            self.assertEqual(row[self.outcome], "H", f"row {i}: {row}")
        elif row[self.si] == "C":
            # Very High	Safety Impact:Catastrophic
            self.assertEqual(row[self.outcome], "VH", f"row {i}: {row}")
        elif row[self.mi] == "MF":
            # OR Mission Impact:Mission Failure
            self.assertEqual(row[self.outcome], "VH", f"row {i}: {row}")
        else:
            self.fail(f"Unhandled combination row {i}: {row}")


if __name__ == "__main__":
    unittest.main()
