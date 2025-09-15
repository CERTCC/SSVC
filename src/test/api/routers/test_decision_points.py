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

from ssvc.api.routers import decision_points
from ssvc.decision_points.base import DecisionPoint, DecisionPointValue


class TestDecisionPointsRouter(unittest.TestCase):
    def setUp(self):
        self.app = FastAPI()
        self.app.include_router(decision_points.router)
        self.client = TestClient(self.app)
        self.dp = DecisionPoint(
            namespace="test",
            key="key1",
            version="1.0.0",
            name="Test DP",
            definition="desc",
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

    @patch("ssvc.api.routers.decision_points.lookup_objtype")
    def test_get_all_decision_points_success(self, mock_lookup):
        dp = self.dp
        result_mock = MagicMock()
        result_mock.namespaces = {
            "ns1": MagicMock(
                keys={"key1": MagicMock(versions={"1.0.0": MagicMock(obj=dp)})}
            )
        }
        mock_lookup.return_value = result_mock
        response = self.client.get("/decision_points/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(dp.id, response.json())

    @patch("ssvc.api.routers.decision_points.lookup_objtype")
    def test_get_all_decision_points_not_found(self, mock_lookup):
        mock_lookup.return_value = None
        response = self.client.get("/decision_points/")
        self.assertEqual(response.status_code, 404)

    @patch("ssvc.api.routers.decision_points.lookup_namespace")
    def test_get_all_decision_points_for_namespace_success(self, mock_lookup):
        dp = self.dp
        result_mock = MagicMock()
        result_mock.keys = {
            "key1": MagicMock(versions={"1.0.0": MagicMock(obj=dp)})
        }
        mock_lookup.return_value = result_mock
        response = self.client.get("/decision_points/ns1")
        self.assertEqual(response.status_code, 200)
        self.assertIn(dp.id, response.json())

    @patch("ssvc.api.routers.decision_points.lookup_namespace")
    def test_get_all_decision_points_for_namespace_not_found(
        self, mock_lookup
    ):
        mock_lookup.return_value = None
        response = self.client.get("/decision_points/ns1")
        self.assertEqual(response.status_code, 404)

    @patch("ssvc.api.routers.decision_points.lookup_key")
    def test_get_all_versions_of_decision_points_for_key_success(
        self, mock_lookup
    ):
        dp = self.dp
        result_mock = MagicMock()
        result_mock.versions = {"1.0.0": MagicMock(obj=dp)}
        mock_lookup.return_value = result_mock
        response = self.client.get("/decision_points/ns1/key1")
        self.assertEqual(response.status_code, 200)
        self.assertIn(dp.id, response.json())

    @patch("ssvc.api.routers.decision_points.lookup_key")
    def test_get_all_versions_of_decision_points_for_key_not_found(
        self, mock_lookup
    ):
        mock_lookup.return_value = None
        response = self.client.get("/decision_points/ns1/key1")
        self.assertEqual(response.status_code, 404)

    @patch("ssvc.api.routers.decision_points.lookup_latest")
    def test_get_latest_decision_point_for_key_success(self, mock_lookup):
        dp = self.dp
        mock_lookup.return_value = dp
        response = self.client.get("/decision_points/test/key1/latest")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["namespace"], dp.namespace)
        self.assertEqual(response.json()["key"], dp.key)
        self.assertEqual(response.json()["version"], dp.version)
        self.assertEqual(response.json()["name"], dp.name)

    @patch("ssvc.api.routers.decision_points.lookup_latest")
    def test_get_latest_decision_point_for_key_not_found(self, mock_lookup):
        mock_lookup.return_value = None
        response = self.client.get("/decision_points/ns1/key1/latest")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
