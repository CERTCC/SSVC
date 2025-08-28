#  Copyright (c) 2023-2025 Carnegie Mellon University.
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

import ssvc.decision_points.cvss.helpers as h
from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint
from ssvc.registry import get_registry


def fake_ms_impacts() -> list[CvssDecisionPoint]:
    dps = []
    for key in ["MSC", "MSI", "MSA"]:
        dp = CvssDecisionPoint(
            name=f"{key} test",
            definition=f"{key} test",
            version="1.0.0",
            key=key,
            values=(
                DecisionPointValue(
                    name="None",
                    key="N",
                    definition="No impact",
                ),
                DecisionPointValue(
                    name="Low",
                    key="L",
                    definition="Low impact",
                ),
                DecisionPointValue(
                    name="High",
                    key="H",
                    definition="High impact",
                ),
            ),
        )
        dps.append(dp)
    return dps


class TestCvssHelpers(unittest.TestCase):
    def setUp(self) -> None:
        # reset the registry

        registry = get_registry()
        registry.reset(force=True)

        self.dps = []
        for i in range(3):
            dp = CvssDecisionPoint(
                name=f"test_{i}",
                definition=f"test_{i}",
                version="1.0.0",
                key=f"TDP{i}",
                values=(
                    DecisionPointValue(
                        name=f"yes_{i}",
                        definition=f"yes_{i}",
                        key=f"Y{i}",
                    ),
                    DecisionPointValue(
                        name=f"no_{i}",
                        definition=f"no_{i}",
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
