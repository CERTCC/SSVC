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

from ssvc.decision_tables.cvss.qualitative_severity import QSR_4
from ._v4expected import V4_EXPECTED

# create a dict of the mapping rows for lookups in tests
_MAPPING = {
    tuple([v for k, v in row.items() if k != QSR_4.outcome]): row
    for row in QSR_4.mapping
}

# create a dict of the expected rows for lookups in tests
_EXPECTED = {
    tuple([v for k, v in row.items() if k != QSR_4.outcome]): row
    for row in V4_EXPECTED
}


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.qsr4 = QSR_4
        self.eq3 = [k for k in self.qsr4.decision_points.keys() if "EQ3" in k][
            0
        ]
        self.eq6 = [k for k in self.qsr4.decision_points.keys() if "EQ6" in k][
            0
        ]

    def test_mapping_for_expected(self):
        for row in V4_EXPECTED:
            key = tuple([v for k, v in row.items() if k != self.qsr4.outcome])
            self.assertIn(key, _MAPPING, f"Could not find {key} in mapping")

    def test_mapping_for_invalids(self):
        """
        Test that the mapping includes the "forbidden" macrovector combinations
        (EQ3="L" and EQ6="H") that are not valid according to the CVSSv4 specification.
        We need them to support full coverage of the MacroVector input space in a DecisionTable object.
        Also confirms that the workaround outcome for these combinations
        is the same as the corresponding valid macrovector combination (where EQ6="L" instead of "H").
        This ensures that the resulting `DecisionTable.mapping` has full coverage of the input space and
        that it will pass topological consistency checks.
        """
        for row in self.qsr4.mapping:
            key = tuple([v for k, v in row.items() if k != self.qsr4.outcome])
            if key in _EXPECTED:
                # skip these, we test them in test_mapping_for_expected
                continue

            # the only things to get here should be (EQ3="L" and EQ6="H")
            self.assertEqual("L", row[self.eq3])
            self.assertEqual("H", row[self.eq6])

            # construct a new key with EQ6="L" instead of "H"
            new_key = list(key)
            new_key[5] = "L"
            new_key = tuple(new_key)
            # make sure that the new key is in expected mapping
            self.assertIn(new_key, _EXPECTED)

            expected_row = _EXPECTED[new_key]
            self.assertEqual(
                expected_row[self.qsr4.outcome], row[self.qsr4.outcome]
            )


if __name__ == "__main__":
    unittest.main()
