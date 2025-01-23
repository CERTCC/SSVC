#  Copyright (c) 2023-2025 Carnegie Mellon University and Contributors.
#  - see Contributors.md for a full list of Contributors
#  - see ContributionInstructions.md for information on how you can Contribute to this project
#  Stakeholder Specific Vulnerability Categorization (SSVC) is
#  licensed under a MIT (SEI)-style license, please see LICENSE.md distributed
#  with this Software or contact permission@sei.cmu.edu for full terms.
#  Created, in part, with funding and support from the United States Government
#  (see Acknowledgments file). This program may include and/or can make use of
#  certain third party source code, object code, documentation and other files
#  (“Third Party Software”). See LICENSE.md for more details.
#  Carnegie Mellon®, CERT® and CERT Coordination Center® are registered in the
#  U.S. Patent and Trademark Office by Carnegie Mellon University

import unittest

import ssvc.decision_points.cvss.helpers as h
from ssvc.decision_points import SsvcDecisionPointValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint


def fake_ms_impacts() -> list[CvssDecisionPoint]:
    dps = []
    for key in ["MSC", "MSI", "MSA"]:
        dp = CvssDecisionPoint(
            name=f"{key} test",
            description=f"{key} test",
            version="1.0.0",
            key=key,
            values=(
                SsvcDecisionPointValue(
                    name="None",
                    key="N",
                    description="No impact",
                ),
                SsvcDecisionPointValue(
                    name="Low",
                    key="L",
                    description="Low impact",
                ),
                SsvcDecisionPointValue(
                    name="High",
                    key="H",
                    description="High impact",
                ),
            ),
        )
        dps.append(dp)
    return dps


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.dps = []
        for i in range(3):
            dp = CvssDecisionPoint(
                name=f"test_{i}",
                description=f"test_{i}",
                version="1.0",
                key=f"TDP{i}",
                values=(
                    SsvcDecisionPointValue(
                        name=f"yes_{i}",
                        description=f"yes_{i}",
                        key=f"Y{i}",
                    ),
                    SsvcDecisionPointValue(
                        name=f"no_{i}",
                        description=f"no_{i}",
                        key=f"N{i}",
                    ),
                ),
            )
            self.dps.append(dp)

    def test_modify_3(self):
        # version 3 just added "Modified" and "M" to the name and key
        # and adds a "Not Defined" value with key "X"
        for dp in self.dps:
            modified = h.modify_3(dp)
            self.assertTrue(modified.key.startswith("M"))
            self.assertTrue(modified.name.startswith("Modified"))

            self.assertIn("Not Defined", [v.name for v in modified.values])
            self.assertIn("X", [v.key for v in modified.values])

    def test_modify_4(self):
        # _modify 4 assumes you've already done the Modify 3 step
        # changes MSC, MSI, MSA "None" to "Negligible"

        dps = fake_ms_impacts()

        for dp in dps:
            modified = h._modify_4(dp)

            self.assertIn("Negligible", [v.name for v in modified.values])
            self.assertNotIn("None", [v.name for v in modified.values])

        # MSI should add "Safety" as the highest value
        _msi = dps[1]
        msi = h._modify_4(_msi)

        self.assertEqual("Safety", msi.values[-1].name)

    def test_modify_4_full(self):
        self.test_modify_3()
        self.test_modify_4()


if __name__ == "__main__":
    unittest.main()
