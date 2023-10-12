import json
import unittest

import jsonschema

import ssvc.decision_points  # noqa F401
from ssvc.decision_points.base import REGISTERED_DECISION_POINTS


class MyTestCase(unittest.TestCase):
    def test_validation(self):
        schema = json.load(open("../../data/schema/Decision_Point.schema.json"))
        import logging

        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        hdlr = logging.StreamHandler()
        logger.addHandler(hdlr)

        # importing these causes the decision points to register themselves
        from ssvc.dp_groups.v1 import SSVCv1  # noqa
        from ssvc.dp_groups.v2 import SSVCv2  # noqa
        from ssvc.dp_groups.v2_1 import SSVCv2_1  # noqa
        from ssvc.dp_groups.cvss.v1 import CVSSv1  # noqa
        from ssvc.dp_groups.cvss.v2 import CVSSv2  # noqa
        from ssvc.dp_groups.cvss.v3 import CVSSv3  # noqa

        for dp in REGISTERED_DECISION_POINTS:
            exp = None
            as_json = dp.to_json()
            loaded = json.loads(as_json)

            try:
                jsonschema.validate(loaded, schema)
            except jsonschema.exceptions.ValidationError as e:
                exp = e

            self.assertIsNone(exp, f"Validation failed for {dp.name} {dp.version}")
            logger.debug(
                f"Validation passed for ({dp.namespace}) {dp.name} v{dp.version}"
            )


if __name__ == "__main__":
    unittest.main()
