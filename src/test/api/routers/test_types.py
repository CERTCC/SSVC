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
from unittest.mock import patch

from fastapi import FastAPI
from fastapi.testclient import TestClient

from ssvc.api.routers import types


class TestTypesRouter(unittest.TestCase):
    def setUp(self):
        # Create FastAPI app and include the router
        self.app = FastAPI()
        self.app.include_router(types.router)
        self.client = TestClient(self.app)
        # Patch the registry
        self.registry_patch = patch.object(types, "r", autospec=True)
        self.mock_registry = self.registry_patch.start()
        self.addCleanup(self.registry_patch.stop)

    def test_get_object_types(self):
        self.mock_registry.types = {"A": None, "B": None}
        response = self.client.get("/objtypes/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"types": ["A", "B"]})

    def test_get_object_type_list(self):
        self.mock_registry.types = {"X": None, "Y": None}
        response = self.client.get("/objtypes/list")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), ["X", "Y"])


if __name__ == "__main__":
    unittest.main()
