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

expect_track = {
    ("N", "Y", "NC", "O", "A", "E", "S"): "T",
    ("N", "Y", "NC", "O", "A", "S", "S"): "T",
    ("N", "Y", "NC", "O", "U", "E", "S"): "T",
    ("N", "Y", "NC", "O", "U", "S", "S"): "T",
    ("N", "Y", "NC", "M", "A", "L", "S"): "T",
    ("N", "Y", "NC", "M", "A", "E", "S"): "T",
    ("N", "Y", "NC", "M", "A", "S", "M"): "T",
    ("N", "Y", "NC", "M", "U", "L", "S"): "T",
    ("N", "Y", "NC", "M", "U", "E", "S"): "T",
    ("N", "Y", "NC", "M", "U", "S", "M"): "T",
    ("N", "Y", "C", "O", "A", "E", "S"): "T",
    ("N", "Y", "C", "O", "A", "S", "S"): "T",
    ("N", "Y", "C", "O", "U", "L", "M"): "T",
    ("N", "Y", "C", "M", "A", "L", "S"): "T",
    ("N", "Y", "C", "M", "A", "E", "S"): "T",
}

expect_coord = {
    ("N", "Y", "NC", "M", "A", "S", "S"): "C",
    ("N", "Y", "NC", "M", "U", "S", "S"): "C",
    ("N", "Y", "C", "O", "U", "L", "S"): "C",
    ("N", "Y", "C", "O", "U", "E", "M"): "C",
    ("N", "Y", "C", "O", "U", "E", "S"): "C",
    ("N", "Y", "C", "O", "U", "S", "M"): "C",
    ("N", "Y", "C", "O", "U", "S", "S"): "C",
    ("N", "Y", "C", "M", "A", "S", "M"): "C",
    ("N", "Y", "C", "M", "A", "S", "S"): "C",
    ("N", "Y", "C", "M", "U", "L", "M"): "C",
    ("N", "Y", "C", "M", "U", "L", "S"): "C",
    ("N", "Y", "C", "M", "U", "E", "M"): "C",
    ("N", "Y", "C", "M", "U", "E", "S"): "C",
    ("N", "Y", "C", "M", "U", "S", "M"): "C",
    ("N", "Y", "C", "M", "U", "S", "S"): "C",
    ("Y", "Y", "NC", "M", "A", "S", "S"): "C",
    ("Y", "Y", "NC", "M", "U", "S", "S"): "C",
    ("Y", "Y", "C", "M", "A", "S", "S"): "C",
    ("Y", "Y", "C", "M", "U", "S", "S"): "C",
    ("Y", "N", "NC", "M", "A", "S", "S"): "C",
    ("Y", "N", "NC", "M", "U", "S", "S"): "C",
    ("Y", "N", "C", "M", "A", "S", "S"): "C",
    ("Y", "N", "C", "M", "U", "S", "S"): "C",
    ("N", "N", "NC", "M", "A", "S", "S"): "C",
    ("N", "N", "NC", "M", "U", "S", "S"): "C",
    ("N", "N", "C", "M", "A", "S", "S"): "C",
    ("N", "N", "C", "M", "U", "S", "S"): "C",
}


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.ct: "DecisionTable" = CT
        self.rp: str = [k for k in self.ct.decision_points if "RP" in k][0]
        self.scon: str = [k for k in self.ct.decision_points if "SCON" in k][0]
        self.rc: str = [k for k in self.ct.decision_points if "RC" in k][0]
        self.sc: str = [
            k for k in self.ct.decision_points if "SC" in k and "SCON" not in k
        ][0]
        self.se: str = [k for k in self.ct.decision_points if "SE" in k][0]
        self.u: str = [k for k in self.ct.decision_points if "U" in k][0]
        self.psi: str = [k for k in self.ct.decision_points if "PSI" in k][0]
        self.outcome: str = self.ct.outcome

    def test_mapping_basics(self):
        self.assertIsNotNone(self.ct.mapping)
        self.assertGreater(len(self.ct.mapping), 0)

        for row in self.ct.mapping:
            with self.subTest(row=row):
                for x in [
                    self.rp,
                    self.scon,
                    self.rc,
                    self.sc,
                    self.se,
                    self.u,
                    self.psi,
                    self.outcome,
                ]:
                    self.assertIn(x, row)

    # @unittest.expectedFailure
    def test_mapping(self):

        for row in self.ct.mapping:
            with self.subTest(row=row):

                multiparty_supereffective_safety_impact = (
                    row[self.sc] == "M" and row[self.u] == "S" and row[self.psi] == "S"
                )

                # Report Public: If a report is already public,
                # OR If no suppliers have been contacted,
                # then CERT/CC will decline the case unless
                # there are multiple suppliers,
                # super effective Utility,
                # and significant Public Safety Impact.
                if row[self.rp] == "Y" or row[self.scon] == "N":
                    if row[self.rc] == "NC":
                        self.assertEqual("D", row[self.outcome])

                    if not multiparty_supereffective_safety_impact:
                        self.assertEqual("D", row[self.outcome])
                else:
                    if row[self.rc] == "NC":
                        # Report Credibility: If the report is not credible,
                        # then CERT/CC will decline the case.
                        self.assertEqual("D", row[self.outcome])

    @unittest.expectedFailure
    def test_mapping_expected(self):

        matches = []
        anomalies = []

        for row in self.ct.mapping:
            with self.subTest(row=row):

                val_tup = tuple([v for k, v in row.items() if k != self.outcome])

                if val_tup in expect_track:
                    if row[self.outcome] != "T":
                        anomalies.append(f"Unexpected outcome {val_tup} should be T ")
                    else:
                        matches.append(val_tup)
                elif val_tup in expect_coord:
                    if row[self.outcome] != "C":
                        anomalies.append(f"Unexpected outcome {val_tup} should be C")
                    else:
                        matches.append(val_tup)
                else:
                    if row[self.outcome] != "D":
                        anomalies.append(f"Unexpected outcome {val_tup} should be D")
                    else:
                        matches.append(val_tup)

        if matches:
            print()
            print("### Matches ###")
            for match in matches:
                print(match)

        if anomalies:
            print()
            print("### Anomalies ###")
            for anomaly in anomalies:
                print(anomaly)
            self.fail("See anomalies")


if __name__ == "__main__":
    unittest.main()
