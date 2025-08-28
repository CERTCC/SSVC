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
import math
import random
import unittest
from unittest.mock import Mock, patch

import semver

import ssvc.registry.base as base
from ssvc.decision_points.base import DecisionPoint
from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_tables.base import DecisionTable
from ssvc.registry import get_registry


class RegistryTestCase(unittest.TestCase):
    def setUp(self):
        self.registry = base.SsvcObjectRegistry(
            name="test_registry", definition="A test registry"
        )
        main_reg = get_registry()
        main_reg.reset(
            force=True
        )  # reset the main registry to ensure a clean state

    def tearDown(self):
        pass

    def test_empty_init(self):
        self.assertEqual(self.registry.name, "test_registry")
        self.assertEqual(self.registry.definition, "A test registry")
        self.assertFalse(self.registry.types)

    def test_lookup_type(self):
        type_name = "RegistryTestCase"
        module_name = "test.registry.test_base"

        result = base.lookup_type(module_name, type_name)
        # we expect to find ourselves
        self.assertEqual(result, self.__class__)

        result = base.lookup_type("foo.bar", "NonExistent")
        self.assertIsNone(result)

    def test_get_obj_type(self):
        class Dummy:
            pass

        dummy = Dummy()
        obj_type = base._get_obj_type(dummy)
        # anything outside of recognized types should be "other"
        self.assertEqual("other", obj_type)

        # test with a known type
        obj = DecisionPoint(
            name="TestDP",
            definition="A test decision point",
            namespace="test",
            key="TEST",
            values=[
                DecisionPointValue(key="A", name="AAA", definition="Option A"),
                DecisionPointValue(key="B", name="BBB", definition="Option B"),
            ],
            registered=False,
        )
        self.assertEqual("DecisionPoint", base._get_obj_type(obj))

        class DpSubclass(DecisionPoint):
            pass

        obj2 = DpSubclass(
            name="TestDP2",
            definition="Another test decision point",
            namespace="test",
            key="TEST2",
            values=[
                DecisionPointValue(key="A", name="AAA", definition="Option A"),
                DecisionPointValue(key="B", name="BBB", definition="Option B"),
                DecisionPointValue(key="C", name="CCC", definition="Option C"),
            ],
            registered=False,
        )
        self.assertEqual("DecisionPoint", base._get_obj_type(obj2))

    def test_valued_version(self):
        # test with a known type

        dp = DecisionPoint(
            name="TestDP",
            definition="A test decision point",
            namespace="test",
            version="2.0.0",
            key="TEST",
            values=[
                DecisionPointValue(key="A", name="AAA", definition="Option A"),
                DecisionPointValue(key="B", name="BBB", definition="Option B"),
            ],
            registered=False,
        )

        ver = base._ValuedVersion(version=dp.version, obj=dp)
        self.assertEqual(dp.version, ver.version)
        self.assertEqual(dp, ver.obj)
        self.assertEqual(2, len(ver.values))

    def test_nonvalued_version(self):
        # test with a known type

        dp1 = DecisionPoint(
            namespace="test",
            key="TEST",
            version="2.0.0",
            name="TestDP",
            definition="A test decision point",
            values=(
                DecisionPointValue(key="A", name="AAA", definition="Option A"),
                DecisionPointValue(key="B", name="BBB", definition="Option B"),
                DecisionPointValue(key="C", name="CCC", definition="Option C"),
                DecisionPointValue(key="D", name="DDD", definition="Option D"),
                DecisionPointValue(key="E", name="EEE", definition="Option E"),
            ),
            registered=False,
        )
        dp2 = DecisionPoint(
            namespace="test",
            key="TEST2",
            version="2.0.0",
            name="TestDP",
            definition="A test decision point",
            values=(
                DecisionPointValue(key="A", name="AAA", definition="Option A"),
                DecisionPointValue(key="B", name="BBB", definition="Option B"),
                DecisionPointValue(key="C", name="CCC", definition="Option C"),
            ),
            registered=False,
        )

        dp3 = DecisionPoint(
            namespace="test",
            key="TEST3",
            version="2.0.0",
            name="TestDP2",
            definition="A test decision point",
            values=(
                DecisionPointValue(key="A", name="A", definition="Outcome A"),
                DecisionPointValue(key="B", name="B", definition="Outcome B"),
            ),
            registered=False,
        )

        dt = DecisionTable(
            namespace="test",
            key="TEST_DT",
            version="2.0.0",
            name="TestDT",
            definition="A test decision table",
            decision_points={dp.id: dp for dp in [dp1, dp2, dp3]},
            outcome=dp3.id,
        )

        ver = base._NonValuedVersion(version=dt.version, obj=dt)
        self.assertEqual(dt.version, ver.version)
        self.assertEqual(dt, ver.obj)
        # even though we didn't specify a mapping
        # it should be created automatically
        # and populated into the object
        self.assertIsNotNone(ver.obj.mapping)

        self.assertEqual(
            math.prod(len(dp.values) for dp in [dp1, dp2]),
            len(ver.obj.mapping),
        )

    @patch("ssvc.registry.base._NonValuedVersion")
    @patch("ssvc.registry.base._ValuedVersion")
    def test_key(self, mock_valued_version, mock_nonvalued_version):
        mockobj1 = Mock()
        mockobj1.schemaVersion = "2.0.0"
        mockobj1.key = "TEST"
        mockobj1.namespace = "test"
        mockobj1.version = "1.0.0"
        mockobj1.name = "Test Object"
        mockobj1.definition = "A test object"
        mockobj1.id = "test-id"
        mockobj1.model_dump_json.return_value = "{}"
        mockobj1.values = []
        mockobj1.decision_points = {}
        mockobj1.outcome = ""

        mockobj2 = Mock()
        mockobj2.schemaVersion = "2.0.0"
        mockobj2.key = "TEST2"
        mockobj2.version = "2.0.0"
        mockobj2.namespace = "test"
        mockobj2.name = "Test Object"
        mockobj2.definition = "A test object"
        mockobj2.id = "test-id"
        mockobj2.model_dump_json.return_value = "{}"
        mockobj2.values = []
        mockobj2.decision_points = {}
        mockobj2.outcome = ""

        mock_valued_version.return_value = mockobj1
        mock_nonvalued_version.return_value = mockobj1

        keyobj = base._Key(
            key="FOO",
            versions={
                "1.0.0": {"obj": mockobj1.__dict__, "version": "1.0.0"},
                "2.0.0": {"obj": mockobj2.__dict__, "version": "2.0.0"},
            },
        )
        self.assertEqual("FOO", keyobj.key)
        self.assertEqual(2, len(keyobj.versions))

        self.assertIn("1.0.0", keyobj.versions)
        self.assertIn("2.0.0", keyobj.versions)

    def test__insert(self):
        # test with a known type

        dp = DecisionPoint(
            name="TestDP",
            definition="A test decision point",
            namespace="test",
            key="TEST",
            values=[
                DecisionPointValue(key="A", name="AAA", definition="Option A"),
                DecisionPointValue(key="B", name="BBB", definition="Option B"),
            ],
            registered=False,
        )

        self.assertIsNone(
            base.lookup_by_id(
                objtype="DecisionPoint", objid=dp.id, registry=self.registry
            )
        )

        # insert the object into the registry
        base._insert(dp, registry=self.registry)

        result = base.lookup_by_id(
            objtype="DecisionPoint", objid=dp.id, registry=self.registry
        )
        self.assertIsNotNone(result)
        self.assertEqual(dp, result.obj)

    def test__compare(self):
        # test with a known type

        dp1 = DecisionPoint(
            name="TestDP",
            definition="A test decision point",
            namespace="test",
            key="TEST",
            values=[
                DecisionPointValue(key="A", name="AAA", definition="Option A"),
                DecisionPointValue(key="B", name="BBB", definition="Option B"),
            ],
            registered=False,
        )

        dp2 = DecisionPoint(
            name="TestDP2",
            definition="A test decision point",
            namespace="test",
            key="TEST",
            values=[
                DecisionPointValue(
                    key="AA", name="AAAA", definition="Option A"
                ),
                DecisionPointValue(key="B", name="BBB", definition="Option B"),
            ],
            registered=False,
        )
        main_reg = get_registry()
        self.assertIsNone(base.lookup_by_id("DecisionPoint", dp1.id, main_reg))
        self.assertIsNone(base.lookup_by_id("DecisionPoint", dp2.id, main_reg))

        # no diffs
        result = base._compare(dp1, dp1)
        self.assertIsNone(result)

        # different values raise ValueError
        with self.assertRaises(ValueError):
            base._compare(dp1, dp2)

    def test_lookup_latest(self):
        dps = []
        for v in range(1, 100):
            version = str(
                semver.Version(
                    major=v,
                    minor=random.randint(0, 20),
                    patch=random.randint(0, 50),
                )
            )

            dp = DecisionPoint(
                name="TestDP",
                definition="A test decision point",
                namespace="test",
                key="TEST",
                version=version,
                values=[
                    DecisionPointValue(
                        key="A", name=f"AAA{v}", definition="Option A"
                    ),
                    DecisionPointValue(
                        key="B", name="BBB", definition="Option B"
                    ),
                ],
                registered=False,
            )
            dps.append(dp)

        # the highest version will be the last one added
        expect_latest = dps[-1]

        # shuffle to change the order of insertion
        # this is to ensure that the lookup_latest function
        # correctly identifies the latest version regardless of insertion order
        random.shuffle(dps)

        for dp in dps:
            self.registry.register(dp)

        latest = base.lookup_latest(
            objtype="DecisionPoint",
            namespace="test",
            key="TEST",
            registry=self.registry,
        )
        self.assertIsNotNone(latest)
        self.assertEqual(expect_latest, latest)


if __name__ == "__main__":
    unittest.main()
