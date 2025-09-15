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

import json
import logging
import os
import unittest

import jsonschema
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

import ssvc.decision_points  # noqa F401
# importing these causes the decision points to register themselves
from ssvc.dp_groups.ssvc.collections import SSVCv1, SSVCv2, SSVCv2_1  # noqa
from ssvc.registry import get_registry
from ssvc.registry.base import get_all


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


_schema_registry = Registry(retrieve=retrieve_local)


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        hdlr = logging.StreamHandler()
        logger.addHandler(hdlr)
        self.logger = logger

        self.registry = get_registry()
        self.registered_dps = list(
            get_all("DecisionPoint", registry=self.registry)
        )

        my_file_path = os.path.abspath(__file__)
        my_dir = os.path.dirname(my_file_path)

        self.schema_dir = os.path.join(
            my_dir, "..", "..", "data", "schema", "v2"
        )

    def test_confirm_registered_decision_points(self):
        self.assertGreater(
            len(self.registered_dps), 0, "No decision points registered"
        )

    def test_decision_point_validation(self):
        schema_path = os.path.join(
            self.schema_dir, "DecisionPoint_2_0_0.schema.json"
        )
        schema_path = os.path.abspath(schema_path)

        with open(schema_path, "r") as f:
            schema = json.load(f)

        for dp in self.registered_dps:
            exp = None
            as_json = dp.model_dump_json()
            loaded = json.loads(as_json)

            try:
                Draft202012Validator(
                    schema, registry=_schema_registry
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
        schema_path = os.path.join(
            self.schema_dir, "DecisionPointGroup_2_0_0.schema.json"
        )
        schema_path = os.path.abspath(schema_path)

        with open(schema_path, "r") as f:
            schema = json.load(f)

        for dp_group in [SSVCv1, SSVCv2, SSVCv2_1]:
            exp = None
            as_json = dp_group.model_dump_json()
            loaded = json.loads(as_json)

            try:
                Draft202012Validator(
                    schema, registry=_schema_registry
                ).validate(loaded)
            except jsonschema.exceptions.ValidationError as e:
                exp = e

            self.assertIsNone(
                exp,
                f"Validation failed for {dp_group.name} {dp_group.version}",
            )
            self.logger.debug(
                f"Validation passed for Decision Point Group {dp_group.name} v{dp_group.version}"
            )


if __name__ == "__main__":
    unittest.main()
