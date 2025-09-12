#!/usr/bin/env python
"""
Provides example decision point for weather forecast
"""
#  Copyright (c) 2024-2025 Carnegie Mellon University.
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

from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_points.helpers import print_versions_and_diffs
from ssvc.decision_points.ssvc.base import SsvcDecisionPoint

SUNNY = DecisionPointValue(
    name="Sunny",
    key="S",
    definition="Weather is sunny."
)

OVERCAST = DecisionPointValue(
    name="Overcast",
    key="O",
    definition="Weather is overcast."
)

RAIN = DecisionPointValue(
    name="Rain",
    key="R",
    definition="Weather is rainy."
)

WEATHER_FORECAST_1 = SsvcDecisionPoint(
    name="Weather Forecast",
    namespace="x_example.test#forecast",
    definition="Weather is the forecast that describes general weather patterns ",
    key="W",
    version="1.0.0",
    values=(
        RAIN,
        OVERCAST,
        SUNNY,
    ),
)

VERSIONS = (WEATHER_FORECAST_1,)
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
