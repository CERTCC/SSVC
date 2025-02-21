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

import json
import logging
import os
import unittest

import jsonschema
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

import ssvc.decision_points  # noqa F401
from ssvc.decision_points.base import REGISTERED_DECISION_POINTS

# importing these causes the decision points to register themselves
from ssvc.decision_points.critical_software import CRITICAL_SOFTWARE_1  # noqa
from ssvc.decision_points.high_value_asset import HIGH_VALUE_ASSET_1  # noqa
from ssvc.decision_points.in_kev import IN_KEV_1
from ssvc.dp_groups.cvss.collections import (
    CVSSv1,
    CVSSv2,
    CVSSv3,
    CVSSv4,
)  # noqa

# importing these causes the decision points to register themselves
from ssvc.dp_groups.ssvc.collections import SSVCv1, SSVCv2, SSVCv2_1  # noqa


def retrieve_local(uri: str) -> Resource:
    # retrieve_local gets called anytime we're trying to get a schema.
    # Because our schemas refer to each other by https: uris, we need this function
    # to load the schema from a local file instead of trying to download it from the internet

    # here we compute the path to the data directory where the schemas are stored
    my_file_path = os.path.abspath(__file__)
    my_dir = os.path.dirname(my_file_path)
    data_path = os.path.join(my_dir, "..", "..", "data")
    data_path = os.path.abspath(data_path)

    fileuri = uri.replace("https://certcc.github.io/SSVC/data", data_path)

    with open(fileuri) as fh:
        schema = json.load(fh)
    return Resource.from_contents(schema)


registry = Registry(retrieve=retrieve_local)


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        hdlr = logging.StreamHandler()
        logger.addHandler(hdlr)
        self.logger = logger

        self.dpgs = [SSVCv1, SSVCv2, SSVCv2_1, CVSSv1, CVSSv2, CVSSv3, CVSSv4]

    def test_confirm_registered_decision_points(self):
        dps = list(REGISTERED_DECISION_POINTS)
        self.assertGreater(len(dps), 0)

        for dpg in self.dpgs:
            for dp in dpg:
                self.assertIn(dp, REGISTERED_DECISION_POINTS)

        extras = [CRITICAL_SOFTWARE_1, HIGH_VALUE_ASSET_1, IN_KEV_1]
        for dp in extras:
            self.assertIn(dp, REGISTERED_DECISION_POINTS)

    def test_decision_point_validation(self):
        # path relative to top level of repo
        schema_url = "https://certcc.github.io/SSVC/data/schema/current/Decision_Point.schema.json"

        decision_points = list(REGISTERED_DECISION_POINTS)
        self.assertGreater(len(decision_points), 0)

        for dp in decision_points:
            exp = None
            as_json = dp.model_dump_json()
            loaded = json.loads(as_json)

            try:
                Draft202012Validator(
                    {"$ref": schema_url}, registry=registry
                ).validate(loaded)
            except jsonschema.exceptions.ValidationError as e:
                exp = e

            self.assertIsNone(
                exp, f"Validation failed for {dp.name} {dp.version}"
            )
            self.logger.debug(
                f"Validation passed for Decision Point ({dp.namespace}) {dp.name} v{dp.version}"
            )

    def test_decision_point_group_validation(self):
        schema_url = "https://certcc.github.io/SSVC/data/schema/current/Decision_Point_Group.schema.json"
        for dpg in self.dpgs:
            exp = None
            as_json = dpg.model_dump_json()
            loaded = json.loads(as_json)

            try:
                Draft202012Validator(
                    {"$ref": schema_url}, registry=registry
                ).validate(loaded)
            except jsonschema.exceptions.ValidationError as e:
                exp = e

            self.assertIsNone(
                exp, f"Validation failed for {dpg.name} {dpg.version}"
            )
            self.logger.debug(
                f"Validation passed for Decision Point Group {dpg.name} v{dpg.version}"
            )

    @unittest.skip("Test not implemented")
    def test_outcome_group_schema_validation(self):
        # TODO: Implement test
        self.fail()


if __name__ == "__main__":
    unittest.main()
