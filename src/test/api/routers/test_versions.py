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

from ssvc.api.routers import versions


class TestVersionsRouter(unittest.TestCase):
    def setUp(self):
        self.app = FastAPI()
        self.app.include_router(versions.router)
        self.client = TestClient(self.app)

    @patch("ssvc.api.routers.versions.lookup_key")
    def test_get_version_dict_for_key_success(self, mock_lookup):
        key_mock = MagicMock()
        key_mock.versions = {"1.0.0": None, "2.0.0": None}
        mock_lookup.return_value = key_mock
        response = self.client.get("/versions/TypeA/ns1/key1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "types": {
                    "TypeA": {
                        "namespaces": {
                            "ns1": {
                                "keys": {
                                    "key1": {"versions": ["1.0.0", "2.0.0"]}
                                }
                            }
                        }
                    }
                }
            },
        )

    @patch("ssvc.api.routers.versions.lookup_key")
    def test_get_version_dict_for_key_not_found(self, mock_lookup):
        mock_lookup.return_value = None
        response = self.client.get("/versions/TypeA/ns1/key1")
        self.assertEqual(response.status_code, 404)

    @patch("ssvc.api.routers.versions.lookup_key")
    def test_get_version_dict_for_key_empty_versions(self, mock_lookup):
        key_mock = MagicMock()
        key_mock.versions = {}
        mock_lookup.return_value = key_mock
        response = self.client.get("/versions/TypeA/ns1/key1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "types": {
                    "TypeA": {
                        "namespaces": {
                            "ns1": {"keys": {"key1": {"versions": []}}}
                        }
                    }
                }
            },
        )

    @patch("ssvc.api.routers.versions.lookup_key")
    def test_get_version_list_for_key_success(self, mock_lookup):
        key_mock = MagicMock()
        key_mock.versions = {"1.0.0": None, "2.0.0": None}
        mock_lookup.return_value = key_mock
        response = self.client.get("/versions/TypeA/ns1/key1/list")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(sorted(response.json()), ["1.0.0", "2.0.0"])

    @patch("ssvc.api.routers.versions.lookup_key")
    def test_get_version_list_for_key_not_found(self, mock_lookup):
        mock_lookup.return_value = None
        response = self.client.get("/versions/TypeA/ns1/key1/list")
        self.assertEqual(response.status_code, 404)

    @patch("ssvc.api.routers.versions.lookup_key")
    def test_get_version_list_for_key_empty_versions(self, mock_lookup):
        key_mock = MagicMock()
        key_mock.versions = {}
        mock_lookup.return_value = key_mock
        response = self.client.get("/versions/TypeA/ns1/key1/list")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])


if __name__ == "__main__":
    unittest.main()
