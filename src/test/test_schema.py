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

import json
import logging
import unittest

import jsonschema

import ssvc.decision_points  # noqa F401
from ssvc.decision_points.base import REGISTERED_DECISION_POINTS
from ssvc.decision_points.critical_software import CRITICAL_SOFTWARE_1  # noqa
from ssvc.decision_points.high_value_asset import HIGH_VALUE_ASSET_1  # noqa
from ssvc.decision_points.in_kev import IN_KEV_1
# importing these causes the decision points to register themselves
from ssvc.dp_groups.v1 import SSVCv1  # noqa
from ssvc.dp_groups.v2 import SSVCv2  # noqa
from ssvc.dp_groups.v2_1 import SSVCv2_1  # noqa


def find_schema(basepath: str) -> str:
    import os

    for pfx in (".", "..", "../.."):
        path = os.path.join(pfx, basepath)
        if os.path.exists(path):
            return path
    raise FileNotFoundError(f"Could not find {basepath}")


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        hdlr = logging.StreamHandler()
        logger.addHandler(hdlr)
        self.logger = logger

    def test_confirm_registered_decision_points(self):
        dps = list(REGISTERED_DECISION_POINTS)
        self.assertGreater(len(dps), 0)

        extras = [CRITICAL_SOFTWARE_1, HIGH_VALUE_ASSET_1, IN_KEV_1]
        for dpg in [SSVCv1, SSVCv2, SSVCv2_1, extras]:
            for dp in dpg:
                self.assertIn(dp, REGISTERED_DECISION_POINTS)

    def test_decision_point_validation(self):
        # path relative to top level of repo
        schema_file = find_schema("data/schema/Decision_Point.schema.json")
        schema = json.load(open(schema_file))

        decision_points = list(REGISTERED_DECISION_POINTS)
        self.assertGreater(len(decision_points), 0)

        for dp in decision_points:
            exp = None
            as_json = dp.to_json()
            loaded = json.loads(as_json)

            try:
                jsonschema.validate(loaded, schema)
            except jsonschema.exceptions.ValidationError as e:
                exp = e

            self.assertIsNone(exp, f"Validation failed for {dp.name} {dp.version}")
            self.logger.debug(
                f"Validation passed for ({dp.namespace}) {dp.name} v{dp.version}"
            )

    def test_decision_point_group_validation(self):
        schema_file = find_schema("data/schema/Decision_Point_Group.schema.json")
        schema = json.load(open(schema_file))

        for dpg in (SSVCv1, SSVCv2, SSVCv2_1):
            exp = None
            as_json = dpg.to_json()
            loaded = json.loads(as_json)

            try:
                jsonschema.validate(loaded, schema)
            except jsonschema.exceptions.ValidationError as e:
                exp = e

            self.assertIsNone(exp, f"Validation failed for {dpg.name} {dpg.version}")
            self.logger.debug(f"Validation passed for {dpg.name} v{dpg.version}")


if __name__ == "__main__":
    unittest.main()
