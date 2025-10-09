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

from fastapi import FastAPI
from fastapi.testclient import TestClient

from ssvc.api.v1.routers import examples
from ssvc.decision_points.base import DecisionPoint, DecisionPointValue
from ssvc.decision_tables.base import DecisionTable
from ssvc.selection import (
    MinimalDecisionPointValue,
    Reference,
    Selection,
    SelectionList,
)


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = FastAPI()
        self.app.include_router(examples.router)
        self.client = TestClient(self.app)

    def tearDown(self):
        pass

    def _test_get_example(self, endpoint: str, model: type):
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, 200)
        data = response.json()

        try:
            model.model_validate(data)
        except Exception as e:
            self.fail(f"Validation failed: {e}")

    def test_get_decision_point_values(self):
        self._test_get_example(
            "/examples/decision-point-values", DecisionPointValue
        )

    def test_get_decision_points(self):
        self._test_get_example("/examples/decision-points", DecisionPoint)

    def test_get_decision_tables(self):
        self._test_get_example("/examples/decision-tables", DecisionTable)

    def test_get_minimal_decision_point_values(self):
        self._test_get_example(
            "/examples/decision-point-values-minimal",
            MinimalDecisionPointValue,
        )

    def test_get_selections(self):
        self._test_get_example("/examples/selections", Selection)

    def test_get_selection_lists(self):
        self._test_get_example("/examples/selection-lists", SelectionList)

    def test_get_references(self):
        self._test_get_example("/examples/references", Reference)


if __name__ == "__main__":
    unittest.main()
