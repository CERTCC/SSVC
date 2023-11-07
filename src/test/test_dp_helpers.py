#  Copyright (c) 2023 Carnegie Mellon University and Contributors.
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
from copy import deepcopy

from ssvc.decision_points import SsvcDecisionPoint, SsvcDecisionPointValue
from ssvc.decision_points.helpers import dp_diff


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.dp1 = SsvcDecisionPoint(
            name="Test DP",
            key="test_dp",
            description="This is a test decision point",
            version="1.0.0",
            values=[
                SsvcDecisionPointValue(
                    name="Yes",
                    key="yes",
                    description="Yes",
                ),
                SsvcDecisionPointValue(
                    name="No",
                    key="no",
                    description="No",
                ),
            ],
        )
        self.dp2 = deepcopy(self.dp1)

    def test_maybe_new_obj(self):
        # ### Create a new object when
        # * A different or new concept is being represented

        # if name, key, and description are the same, then it's not a new object
        self.assertEqual(self.dp1.name, self.dp2.name)
        self.assertEqual(self.dp1.key, self.dp2.key)
        self.assertEqual(self.dp1.description, self.dp2.description)

        results = dp_diff(self.dp1, self.dp2)
        text = "\n".join(results)
        self.assertNotIn("new object", text)

        # if name, key, AND description are different, then it is maybe a new object
        self.dp2.name = "New Test DP"
        results = dp_diff(self.dp1, self.dp2)
        text = "\n".join(results)
        self.assertNotIn("new object", text)

        self.dp2.key = "new_test_dp"
        results = dp_diff(self.dp1, self.dp2)
        text = "\n".join(results)
        self.assertNotIn("new object", text)

        self.dp2.description = "This is a new test decision point"
        results = dp_diff(self.dp1, self.dp2)
        text = "\n".join(results)

        # now that all three are different, it should suggest a new object
        self.assertIn("new object", text)

    def test_major_version(self):
        # ### Increment the Major Version when
        #
        # * Criteria for creating a new object are not met, _AND_
        #   * existing values are removed, _OR_
        #   * value semantics change in a way that older answers are no longer usable,
        #     _OR_
        #   * new values are added that divide previous value semantics ambiguously

        # remove one
        self.dp2.values = self.dp2.values[:-1]
        results = dp_diff(self.dp1, self.dp2)
        text = "\n".join(results)
        self.assertIn("major", text)

        # add one
        self.dp2.values = list(self.dp1.values)
        self.dp2.values.append(
            SsvcDecisionPointValue(
                name="Maybe",
                key="maybe",
                description="Maybe",
            )
        )

        results = dp_diff(self.dp1, self.dp2)
        text = "\n".join(results)
        self.assertIn("major", text)

    def test_minor_version_when_new_option_added(self):
        # ### Increment the Minor Version when
        # * Criteria for incrementing the Major Version are not met, _AND_
        #   * new options are added, _OR_
        # add one
        self.dp2.values = list(self.dp1.values)
        self.dp2.values.append(
            SsvcDecisionPointValue(
                name="Maybe",
                key="maybe",
                description="Maybe",
            )
        )

        results = dp_diff(self.dp1, self.dp2)
        text = "\n".join(results)
        self.assertIn("minor", text)

    def test_minor_version_when_value_name_change(self):
        #   * value names or keys are changed, _OR_

        self.dp2.values = deepcopy(self.dp1.values)
        self.dp2.values[0].name = "New Yes"

        results = dp_diff(self.dp1, self.dp2)
        text = "\n".join(results)
        self.assertIn("minor", text)

    def test_minor_version_when_value_key_changes(self):
        self.dp2.values = deepcopy(self.dp1.values)
        self.dp2.values[0].key = "new_yes"
        results = dp_diff(self.dp1, self.dp2)
        text = "\n".join(results)
        self.assertIn("minor", text)

    def test_minor_version_when_decision_point_name_changes(self):
        #   * the decision point name is changed
        self.dp2.name = "New Test DP"
        results = dp_diff(self.dp1, self.dp2)
        text = "\n".join(results)
        self.assertIn("minor", text)

    def test_patch_version_when_typo_fixed(self):
        #   * typo fixes in option names or decision point name, _OR_
        self.dp2.name = "Test Dp"
        results = dp_diff(self.dp1, self.dp2)
        text = "\n".join(results)
        self.assertIn("patch", text)

    def test_patch_version_when_description_changes(self):
        # ### Increment the Patch Version when
        #   * the decision point description changes in a way that does not affect
        #     semantics, _OR_

        self.dp2.description = "This is a new test decision point"
        results = dp_diff(self.dp1, self.dp2)
        text = "\n".join(results)
        self.assertIn("patch", text)

    def test_patch_version_when_value_description_changes(self):
        #   * a value description changes in a way that does not affect semantics
        self.dp2.values = deepcopy(self.dp1.values)
        self.dp2.values[0].description = "New Yes"
        results = dp_diff(self.dp1, self.dp2)
        text = "\n".join(results)
        self.assertIn("patch", text)


if __name__ == "__main__":
    unittest.main()
