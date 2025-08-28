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

from ssvc.api.routers import decision_tables
from ssvc.decision_points.base import DecisionPoint, DecisionPointValue
from ssvc.decision_tables.base import DecisionTable
from ssvc.registry.base import SsvcObjectRegistry


class TestDecisionTablesRouter(unittest.TestCase):
    def setUp(self):
        self.app = FastAPI()
        self.app.include_router(decision_tables.router)
        self.client = TestClient(self.app)

        # create a new registry for testing
        self.r = SsvcObjectRegistry(
            name="test registry", definition="test registry"
        )
        self.r.reset(force=True)
        # make sure it's empty
        self.assertEqual(0, len(self.r.types))

        decision_tables.r = self.r

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

    @patch("ssvc.api.routers.decision_tables.lookup_objtype")
    def test_get_all_decision_tables_success(self, mock_lookup):
        result_mock = MagicMock()
        result_mock.namespaces = {
            self.dt.namespace: MagicMock(
                keys={
                    self.dt.key: MagicMock(
                        versions={self.dt.version: MagicMock(obj=self.dt)}
                    )
                }
            )
        }
        mock_lookup.return_value = result_mock
        response = self.client.get("/decision_tables/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.dt.id, response.json())

    @patch("ssvc.api.routers.decision_tables.lookup_objtype")
    def test_get_all_decision_tables_not_found(self, mock_lookup):
        mock_lookup.return_value = None
        response = self.client.get("/decision_tables/")
        self.assertEqual(response.status_code, 404)

    @patch("ssvc.api.routers.decision_tables.lookup_namespace")
    def test_get_decision_tables_for_namespace_success(self, mock_lookup):
        ns_mock = MagicMock()
        ns_mock.keys = {
            self.dt.key: MagicMock(
                versions={self.dt.version: MagicMock(obj=self.dt)}
            )
        }
        mock_lookup.return_value = ns_mock
        response = self.client.get(f"/decision_tables/{self.dt.namespace}")
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.dt.id, response.json())

    @patch("ssvc.api.routers.decision_tables.lookup_namespace")
    def test_get_decision_tables_for_namespace_not_found(self, mock_lookup):
        mock_lookup.return_value = None
        response = self.client.get(f"/decision_tables/{self.dt.namespace}")
        self.assertEqual(response.status_code, 404)

    @patch("ssvc.api.routers.decision_tables.lookup_key")
    def test_get_decision_tables_for_key_success(self, mock_lookup):
        key_mock = MagicMock()
        key_mock.versions = {self.dt.version: MagicMock(obj=self.dt)}
        mock_lookup.return_value = key_mock
        response = self.client.get(
            f"/decision_tables/{self.dt.namespace}/{self.dt.key}"
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.dt.id, response.json())

    @patch("ssvc.api.routers.decision_tables.lookup_key")
    def test_get_decision_tables_for_key_not_found(self, mock_lookup):
        mock_lookup.return_value = None
        response = self.client.get(
            f"/decision_tables/{self.dt.namespace}/{self.dt.key}"
        )
        self.assertEqual(response.status_code, 404)

    @patch("ssvc.api.routers.decision_tables.lookup_latest")
    def test_get_latest_decision_table_for_key_success(self, mock_lookup):
        latest_dt = self.dt
        mock_lookup.return_value = latest_dt
        response = self.client.get(
            f"/decision_tables/{latest_dt.namespace}/{latest_dt.key}/latest"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["namespace"], latest_dt.namespace)
        self.assertEqual(response.json()["key"], latest_dt.key)
        self.assertEqual(response.json()["version"], latest_dt.version)
        self.assertEqual(response.json()["name"], latest_dt.name)

    @patch("ssvc.api.routers.decision_tables.lookup_latest")
    def test_get_latest_decision_table_for_key_not_found(self, mock_lookup):
        mock_lookup.return_value = None
        response = self.client.get(f"/decision_tables/test/key1/latest")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
