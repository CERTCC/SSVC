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

import ssvc.registry.base as base


class RegistryTestCase(unittest.TestCase):
    def setUp(self):
        self.registry = base.SsvcObjectRegistry(
            name="test_registry", description="A test registry"
        )

    def tearDown(self):
        pass

    def test_empty_init(self):
        self.assertEqual(self.registry.name, "test_registry")
        self.assertEqual(self.registry.description, "A test registry")
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
        from ssvc.decision_points.base import DecisionPoint
        from ssvc.decision_points.base import DecisionPointValue

        obj = DecisionPoint(
            name="TestDP",
            description="A test decision point",
            namespace="x_test",
            key="TEST",
            values=[
                DecisionPointValue(key="A", name="AAA", description="Option A"),
                DecisionPointValue(key="B", name="BBB", description="Option B"),
            ],
        )
        self.assertEqual("DecisionPoint", base._get_obj_type(obj))

        class DpSubclass(DecisionPoint):
            pass

        obj2 = DpSubclass(
            name="TestDP2",
            description="Another test decision point",
            namespace="x_test",
            key="TEST2",
            values=[
                DecisionPointValue(key="A", name="AAA", description="Option A"),
                DecisionPointValue(key="B", name="BBB", description="Option B"),
                DecisionPointValue(key="C", name="CCC", description="Option C"),
            ],
        )
        self.assertEqual("DecisionPoint", base._get_obj_type(obj2))

    @unittest.expectedFailure
    def test_version(self):
        # test with a known type
        from ssvc.decision_points.base import DecisionPoint
        from ssvc.decision_points.base import DecisionPointValue

        obj = DecisionPoint(
            name="TestDP",
            description="A test decision point",
            namespace="x_test",
            version="2.0.0",
            key="TEST",
            values=[
                DecisionPointValue(key="A", name="AAA", description="Option A"),
                DecisionPointValue(key="B", name="BBB", description="Option B"),
            ],
        )
        self.assertEqual("DecisionPoint", base._get_obj_type(obj))

        ver = base._Version(version=obj.version, obj=obj)
        self.assertEqual(obj.version, ver.version)
        self.assertEqual(obj, ver.obj)


if __name__ == "__main__":
    unittest.main()
