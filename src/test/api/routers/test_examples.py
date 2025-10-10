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
import datetime
import random
import unittest

from fastapi import FastAPI
from fastapi.testclient import TestClient

from ssvc.api.v1.routers import examples
from ssvc.decision_points.base import DecisionPoint, DecisionPointValue
from ssvc.decision_tables.base import DecisionTable
from ssvc.decision_tables.example.to_play import TOPLAY_1
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

        # set up a decision table from which we can derive other objects in post-tests
        self.dt = TOPLAY_1

    def tearDown(self):
        pass

    def _test_get_example(self, endpoint: str, model: type):
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, 200)
        data = response.json()

        self.assertIsInstance(data, dict)

        try:
            model.model_validate(data)
        except Exception as e:
            self.fail(f"Validation failed: {e}")

    def _test_post_example(self, endpoint: str, model: type, obj: object):
        response = self.client.post(endpoint, json=obj.model_dump(mode="json"))
        self.assertEqual(
            200, response.status_code, f"POST to {endpoint} failed: {response}"
        )
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

    def test_post_decision_points(self):
        for dp in self.dt.decision_points.values():
            self._test_post_example(
                "/examples/decision-points", DecisionPoint, dp
            )
        # TODO test bad data

    def test_post_decision_point_values(self):
        for dp in self.dt.decision_points.values():
            for dpv in dp.values:
                self._test_post_example(
                    "/examples/decision-point-values", DecisionPointValue, dpv
                )
        # TODO test bad data

    def test_post_decision_tables(self):
        self._test_post_example(
            "/examples/decision-tables", DecisionTable, self.dt
        )
        # TODO test bad data

    def test_post_minimal_decision_point_values(self):
        for dp in self.dt.decision_points.values():
            for dpv in dp.values:
                mdpv = MinimalDecisionPointValue(
                    key=dpv.key,
                )
                self._test_post_example(
                    "/examples/decision-point-values-minimal",
                    MinimalDecisionPointValue,
                    mdpv,
                )
        # TODO test bad data

    def test_post_selections(self):
        for dp in self.dt.decision_points.values():
            sel = Selection.from_decision_point(dp)
            # randomly sample 1 or more values from the selection
            sample_size = random.randint(1, len(sel.values))
            sel.values = random.sample(sel.values, sample_size)
            self._test_post_example("/examples/selections", Selection, sel)

        # TODO test bad data

    def test_post_selection_lists(self):
        sels = []
        for dp in self.dt.decision_points.values():
            sel = Selection.from_decision_point(dp)
            # randomly sample 1 or more values from the selection
            sample_size = random.randint(1, len(sel.values))
            sel.values = random.sample(sel.values, sample_size)
            sels.append(sel)

        sel_list = SelectionList(
            target_ids=["TK-421", "TK-710"],
            selections=sels,
            timestamp=datetime.datetime.now(),
            references=[
                Reference(
                    uri="https://starwars.fandom.com/wiki/TK-421",
                    summary="Alongside TK-710, TK-421's first security assignment was to guard the Millennium Falcon in Docking Bay 327 after the Death Star captured it.",
                )
            ],
        )
        self._test_post_example(
            "/examples/selection-lists", SelectionList, sel_list
        )
        # TODO test bad data

    def test_post_references(self):
        ref = Reference(
            uri="http://some/reference", summary="An example reference"
        )
        self._test_post_example("/examples/references", Reference, ref)
        # TODO test bad data


if __name__ == "__main__":
    unittest.main()
