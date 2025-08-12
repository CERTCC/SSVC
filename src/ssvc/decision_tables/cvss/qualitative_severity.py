#!/usr/bin/env python
"""
Models the CVSS v4.0 Qualitative Severity Ratings from Equivalency Set 1-6
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
#Exploitation,Automatable,TechnicalImpact,HumanImpact,Decision
from ssvc.decision_points.cvss.equivalence_set_1 import LATEST as EQ1
from ssvc.decision_points.cvss.equivalence_set_2 import LATEST as EQ2
from ssvc.decision_points.cvss.equivalence_set_3 import LATEST as EQ3
from ssvc.decision_points.cvss.equivalence_set_4 import LATEST as EQ4
from ssvc.decision_points.cvss.equivalence_set_5 import LATEST as EQ5
from ssvc.decision_points.cvss.equivalence_set_6 import LATEST as EQ6
from ssvc.outcomes.cvss.lmhc import LATEST as LMHC
import pandas as pd
from ssvc.decision_tables.base import DecisionTable, dpdict_to_combination_list
from ssvc.decision_tables.helpers import write_csv

dp_array = [EQ1,EQ2,EQ3,EQ4,EQ5,EQ6,LMHC]

dp_dict = {dp.id: dp for dp in dp_array}


LMHC_1 = DecisionTable(
        name = "CVSS v4.0 Qualitative Severity Ratings",
        key="CVSS4_QSR",
        version="1.0.0",
        namespace = "cvss",
        description = "CVSS v4.0  using MacroVectors and Interpolation. See https://www.first.org/cvss/specification-document#New-Scoring-System-Development for details",
        decision_points = {dp.id: dp for dp in dp_array},
        outcome = LMHC.id,
        mapping = [
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "L",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "M",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "L",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "L"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "L",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "M",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "M"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "L",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "H"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "M",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "L",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "M",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "L",
          "cvss:CVSS:1.0.0": "C"
     },
     {
          "cvss:EQ1:1.0.0": "H",
          "cvss:EQ2:1.0.0": "H",
          "cvss:EQ3:1.0.0": "H",
          "cvss:EQ4:1.0.0": "H",
          "cvss:EQ5:1.0.0": "H",
          "cvss:EQ6:1.0.0": "H",
          "cvss:CVSS:1.0.0": "C"
     }
]

)

VERSIONS = [LMHC_1,]
LATEST = LMHC_1

def main():

    print(LMHC_1.model_dump_json(indent=2))


if __name__ == '__main__':
    main()
