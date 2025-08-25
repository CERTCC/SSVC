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

from fastapi.testclient import TestClient

from ssvc.api.main import app


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def tearDown(self):
        pass

    def test_expected_routers(self):
        # Check if the expected routers are included in the app
        expected_routers = [
            "decision_point",
            "decision_points",
            "decision_table",
            "decision_tables",
            "types",
            "namespaces",
            "keys",
            "versions",
        ]
        routes = [r.path for r in app.routes]
        for expected in expected_routers:
            self.assertTrue(
                any([expected in route for route in routes]),
                "Expected router '{}' not found in app routes.".format(
                    expected
                ),
            )

    def test_root_redirects_to_docs(self):
        # disable redirect
        response = self.client.get("/", follow_redirects=False)
        self.assertIn(response.status_code, [302, 307])
        self.assertEqual("/docs", response.headers["location"])


if __name__ == "__main__":
    unittest.main()
