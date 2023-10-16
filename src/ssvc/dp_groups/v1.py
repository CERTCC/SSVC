#!/usr/bin/env python
"""
file: v1
author: adh
created_at: 9/21/23 9:52 AM
"""
from ssvc.dp_groups.base import SsvcDecisionPointGroup, get_all_decision_points_from

# convenience imports
from ssvc.dp_groups.deployer import PATCH_APPLIER_1  # noqa
from ssvc.dp_groups.supplier import PATCH_DEVELOPER_1  # noqa

GROUPS = [PATCH_APPLIER_1, PATCH_DEVELOPER_1]

SSVCv1 = SsvcDecisionPointGroup(
    name="SSVCv1",
    description="The first version of the SSVC.",
    version="1.0.0",
    decision_points=get_all_decision_points_from(GROUPS),
)


def main():
    print(SSVCv1.to_json(indent=2))


if __name__ == "__main__":
    main()
