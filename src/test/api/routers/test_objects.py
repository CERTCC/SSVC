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
from unittest.mock import MagicMock, patch

from fastapi import FastAPI
from fastapi.testclient import TestClient

from ssvc.api.routers import objects
from ssvc.decision_points.base import DecisionPoint, DecisionPointValue
from ssvc.decision_tables.base import DecisionTable


class TestObjectsRouter(unittest.TestCase):
    def setUp(self):
        self.app = FastAPI()
        self.app.include_router(objects.router)
        self.client = TestClient(self.app)

        objects.r.reset(force=True)

        self.dp1 = DecisionPoint(
            namespace="test",
            key="key1",
            version="1.0.0",
            name="Test DP 1",
            definition="desc1",
            values=(
                DecisionPointValue(
                    key="value1",
                    name="Value 1",
                    definition="Description for value 1",
                ),
                DecisionPointValue(
                    key="value2",
                    name="Value 2",
                    definition="Description for value 2",
                ),
            ),
        )
        self.dp2 = DecisionPoint(
            namespace="test",
            key="key2",
            version="1.0.0",
            name="Test DP 2",
            definition="desc2",
            values=(
                DecisionPointValue(
                    key="value1",
                    name="Value 1",
                    definition="Description for value 1",
                ),
                DecisionPointValue(
                    key="value2",
                    name="Value 2",
                    definition="Description for value 2",
                ),
            ),
        )
        self.dp3 = DecisionPoint(
            namespace="test",
            key="key3",
            version="1.0.0",
            name="Test DP 3",
            definition="desc3",
            values=(
                DecisionPointValue(
                    key="value1",
                    name="Value 1",
                    definition="Description for value 1",
                ),
                DecisionPointValue(
                    key="value2",
                    name="Value 2",
                    definition="Description for value 2",
                ),
                DecisionPointValue(
                    key="value3",
                    name="Value 3",
                    definition="Description for value 3",
                ),
            ),
        )
        self.dt = DecisionTable(
            namespace="test",
            key="key2",
            version="2.0.0",
            name="Test DT",
            definition="desc",
            decision_points={
                dp.id: dp for dp in (self.dp1, self.dp2, self.dp3)
            },
            outcome=self.dp3.id,
        )

    @patch("ssvc.api.routers.objects.lookup_by_id")
    def test_get_decision_point_success(self, mock_lookup):
        dp = self.dp1
        ver_obj = MagicMock(obj=dp)
        mock_lookup.return_value = ver_obj
        response = self.client.get("/objects/DecisionPoint/ns1/key1/1.0.0")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["namespace"], dp.namespace)
        self.assertEqual(response.json()["key"], dp.key)
        self.assertEqual(response.json()["version"], dp.version)
        self.assertEqual(response.json()["name"], dp.name)

    @patch("ssvc.api.routers.objects.lookup_by_id")
    def test_get_decision_point_not_found(self, mock_lookup):
        mock_lookup.return_value = None
        response = self.client.get("/objects/DecisionPoint/ns1/key1/1.0.0")
        self.assertEqual(response.status_code, 404)

    @patch("ssvc.api.routers.objects.lookup_by_id")
    def test_get_decision_table_success(self, mock_lookup):
        dt = self.dt
        ver_obj = MagicMock(obj=dt)
        mock_lookup.return_value = ver_obj
        response = self.client.get("/objects/DecisionTable/ns2/key2/2.0.0")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["namespace"], dt.namespace)
        self.assertEqual(response.json()["key"], dt.key)
        self.assertEqual(response.json()["version"], dt.version)
        self.assertEqual(response.json()["name"], dt.name)
        self.assertEqual(response.json()["definition"], dt.definition)

    @patch("ssvc.api.routers.objects.lookup_by_id")
    def test_get_decision_table_not_found(self, mock_lookup):
        mock_lookup.return_value = None
        response = self.client.get("/objects/DecisionTable/ns2/key2/2.0.0")
        self.assertEqual(response.status_code, 404)

    def test_get_object_invalid_params(self):
        # Missing version param
        response = self.client.get("/objects/DecisionPoint/ns1/key1/")
        self.assertEqual(
            response.status_code, 404
        )  # FastAPI returns 404 for missing path param


if __name__ == "__main__":
    unittest.main()
