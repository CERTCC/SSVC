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
import json
import unittest

from fastapi import HTTPException
from fastapi.testclient import TestClient

from ssvc.api.routers import decision_table
from ssvc.decision_points.base import DecisionPoint, DecisionPointValue
from ssvc.decision_tables.base import DecisionTable
from ssvc.registry.base import SsvcObjectRegistry


class TestDecisionPointAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(decision_table.router)

        # create a new registry for testing
        self.r = SsvcObjectRegistry(
            name="test registry", definition="test registry"
        )
        self.r.reset(force=True)
        # make sure it's empty
        self.assertEqual(0, len(self.r.types))

        decision_table.r = self.r

        # now add a decision table
        self.dp1 = DecisionPoint(
            namespace="test",
            key="A",
            version="1.0.0",
            name="Test Decision Point",
            definition="This is a test decision point.",
            values=(
                DecisionPointValue(name="value1", definition=".", key="K1"),
                DecisionPointValue(name="value2", definition=".", key="K2"),
                DecisionPointValue(name="value3", definition=".", key="K3"),
            ),
            registered=False,
        )
        self.dp2 = DecisionPoint(
            namespace="test",
            key="B",
            version="1.0.0",
            name="Test Decision Point",
            definition="This is a test decision point.",
            values=(
                DecisionPointValue(name="value1", definition=".", key="K1"),
                DecisionPointValue(name="value2", definition=".", key="K2"),
            ),
            registered=False,
        )
        self.dt = DecisionTable(
            namespace="test",
            key="DT_1",
            version="1.0.0",
            name="Test Decision Table",
            definition="This is a test decision table.",
            decision_points={dp.id: dp for dp in (self.dp1, self.dp2)},
            outcome=self.dp2.id,
            registered=False,
        )

    def test_get_decision_point_by_id_success(self):
        r = self.r
        response = self.client.get("/decision_point/test:A:1.0.0")
        # should 404 because we have no registry entries
        self.assertEqual(
            404,
            response.status_code,
        )

        r.register(self.dt)
        # ensure it's added to the registry

        self.assertEqual(1, len(r.types))
        self.assertEqual(
            self.dt,
            r.types["DecisionTable"]
            .namespaces["test"]
            .keys["DT_1"]
            .versions["1.0.0"]
            .obj,
        )
        response = self.client.get("/decision_table?id=test:DT_1:1.0.0")
        self.assertEqual(
            200,
            response.status_code,
        )
        # we need to do this because JSON doesn't do tuples
        expected = json.loads(self.dt.model_dump_json())
        self.assertEqual(expected, response.json())

    def test_get_decision_point_by_id_bad_id(self):
        with self.assertRaises(HTTPException):
            self.client.get("/decision_table?id=bad_id_format")


if __name__ == "__main__":
    unittest.main()
