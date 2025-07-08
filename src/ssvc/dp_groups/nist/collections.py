#!/usr/bin/env python
"""
Provides a collection of decision points based on NIST SP 800-30 Revision 1.
"""

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

from ssvc.decision_points.nist.adversarial_initiation_likelihood import (
    ADVERSARIAL_INITIATION_LIKELIHOOD,
)
from ssvc.decision_points.nist.adversary_capability import ADVERSARY_CAPABILITY
from ssvc.decision_points.nist.adversary_intent import ADVERSARY_INTENT
from ssvc.decision_points.nist.adversary_targeting import ADVERSARY_TARGETING
from ssvc.decision_points.nist.adverse_impact_likelihood import (
    ADVERSE_IMPACT_LIKELIHOOD,
)
from ssvc.decision_points.nist.condition_pervasiveness import CONDITION_PERVASIVENESS
from ssvc.decision_points.nist.nonadversarial_occurrence_likelihood import (
    NONADVERSARIAL_OCCURRENCE_LIKELIHOOD,
)
from ssvc.decision_points.nist.range_of_effects import RANGE_OF_EFFECTS
from ssvc.decision_points.nist.threat_event_impact import THREAT_EVENT_IMPACT
from ssvc.decision_points.nist.threat_event_relevance import THREAT_EVENT_RELEVANCE
from ssvc.decision_points.nist.vulnerability_severity import VULNERABILITY_SEVERITY
from ssvc.dp_groups.base import DecisionPointGroup

NIST_800_30 = DecisionPointGroup(
    name="NIST SP 800-30 Revision 1",
    description="Decision points based on NIST SP 800-30 Revision 1",
    version="1.0.0",
    decision_points=(
        ADVERSARY_CAPABILITY,
        ADVERSARY_INTENT,
        ADVERSARY_TARGETING,
        THREAT_EVENT_RELEVANCE,
        ADVERSARIAL_INITIATION_LIKELIHOOD,
        NONADVERSARIAL_OCCURRENCE_LIKELIHOOD,
        ADVERSE_IMPACT_LIKELIHOOD,
        VULNERABILITY_SEVERITY,
        CONDITION_PERVASIVENESS,
        RANGE_OF_EFFECTS,
        THREAT_EVENT_IMPACT,
    ),
)


def main():
    for group in [
        NIST_800_30,
    ]:
        print(f"## {group.name} v{group.version}")
        print(group.model_dump_json(indent=2))
        print()


if __name__ == "__main__":
    main()
