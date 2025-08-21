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

from ssvc.api.routers import namespaces


class TestNamespacesRouter(unittest.TestCase):
    def setUp(self):
        self.app = FastAPI()
        self.app.include_router(namespaces.router)
        self.client = TestClient(self.app)
        self.registry_patch = patch.object(namespaces, "r", autospec=True)
        self.mock_registry = self.registry_patch.start()
        self.addCleanup(self.registry_patch.stop)

    def test_get_object_type_namespaces(self):
        # Setup mock registry
        self.mock_registry.types = {
            "TypeA": MagicMock(namespaces={"ns1": None, "ns2": None}),
            "TypeB": MagicMock(namespaces={"ns3": None}),
        }
        response = self.client.get("/namespaces/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "types": {
                    "TypeA": {"namespaces": ["ns1", "ns2"]},
                    "TypeB": {"namespaces": ["ns3"]},
                }
            },
        )

    def test_get_namespace_list(self):
        self.mock_registry.types = {
            "TypeA": MagicMock(namespaces={"ns1": None, "ns2": None}),
            "TypeB": MagicMock(namespaces={"ns3": None}),
        }
        response = self.client.get("/namespaces/list")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(sorted(response.json()), ["ns1", "ns2", "ns3"])

    @patch("ssvc.api.routers.namespaces.lookup_objtype")
    @patch("ssvc.api.routers.namespaces._404_on_none")
    def test_get_namespace_list_for_type(self, mock_404, mock_lookup):

        self.mock_registry.types = {
            "TypeA": MagicMock(namespaces={"ns1": None, "ns2": None}),
            "TypeB": MagicMock(namespaces={"ns3": None}),
        }
        mock_404.return_value = None
        response = self.client.get("/namespaces/TypeA")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {"types": {"TypeA": {"namespaces": ["ns1", "ns2"]}}},
        )
        mock_lookup.assert_called_once_with(
            objtype="TypeA", registry=self.mock_registry
        )
        mock_404.assert_called_once()


if __name__ == "__main__":
    unittest.main()
