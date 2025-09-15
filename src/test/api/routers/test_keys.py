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

from ssvc.api.routers import keys


class TestKeysRouter(unittest.TestCase):
    def setUp(self):
        self.app = FastAPI()
        self.app.include_router(keys.router)
        self.client = TestClient(self.app)
        self.registry_patch = patch.object(keys, "r", autospec=True)
        self.mock_registry = self.registry_patch.start()
        self.addCleanup(self.registry_patch.stop)

    def test_get_key_dict(self):
        # Setup mock registry
        ns_mock1 = MagicMock(keys={"k1": None, "k2": None})
        ns_mock2 = MagicMock(keys={"k3": None})
        type_mock = MagicMock(namespaces={"ns1": ns_mock1, "ns2": ns_mock2})
        self.mock_registry.types = {"TypeA": type_mock}
        response = self.client.get("/keys/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "types": {
                    "TypeA": {
                        "namespaces": {
                            "ns1": {"keys": ["k1", "k2"]},
                            "ns2": {"keys": ["k3"]},
                        }
                    }
                }
            },
        )

    @patch("ssvc.api.routers.keys._404_on_none")
    def test_get_key_dict_for_type(self, mock_404):
        ns_mock1 = MagicMock(keys={"k1": None})
        type_mock = MagicMock(namespaces={"ns1": ns_mock1})
        self.mock_registry.types = {"TypeA": type_mock}
        response = self.client.get("/keys/TypeA")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {"types": {"TypeA": {"namespaces": {"ns1": {"keys": ["k1"]}}}}},
        )
        mock_404.assert_called_once()

    @patch("ssvc.api.routers.keys.lookup_namespace")
    @patch("ssvc.api.routers.keys._404_on_none")
    def test_get_key_dict_for_type_and_namespace(self, mock_404, mock_lookup):
        ns_mock = MagicMock(keys={"k1": None, "k2": None})
        mock_lookup.return_value = ns_mock
        mock_404.return_value = None
        response = self.client.get("/keys/TypeA/ns1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "types": {
                    "TypeA": {"namespaces": {"ns1": {"keys": ["k1", "k2"]}}}
                }
            },
        )
        mock_lookup.assert_called_once_with(
            objtype="TypeA", namespace="ns1", registry=self.mock_registry
        )
        mock_404.assert_called_once()

    @patch("ssvc.api.routers.keys.lookup_namespace")
    @patch("ssvc.api.routers.keys._404_on_none")
    def test_get_key_list_for_type_and_namespace(self, mock_404, mock_lookup):
        ns_mock = MagicMock(keys={"k1": None, "k2": None})
        mock_lookup.return_value = ns_mock
        mock_404.return_value = None
        response = self.client.get("/keys/TypeA/ns1/list")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(sorted(response.json()), ["k1", "k2"])
        mock_lookup.assert_called_once_with(
            objtype="TypeA", namespace="ns1", registry=self.mock_registry
        )
        mock_404.assert_called_once()

    def test_get_key_dict_for_type_not_found(self):
        self.mock_registry.types = {}

        response = self.client.get("/keys/TypeA")
        self.assertEqual(response.status_code, 404)  # Exception raised


if __name__ == "__main__":
    unittest.main()
