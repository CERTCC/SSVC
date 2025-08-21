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

"""Type definitions for use in response models and API endpoints."""
from ssvc.decision_points.base import DecisionPoint, DecisionPointValue
from ssvc.decision_tables.base import DecisionTable

ListOfStringsType = list[str]
DecisionPointValuesListType = list[DecisionPointValue]

NamespaceDictType = dict[
    str,  # "types"
    dict[
        str,  # specific type
        dict[
            str, ListOfStringsType  # "namespaces"  # list of namespace strings
        ],
    ],
]
KeyDictType = dict[
    str,  # "types"
    dict[
        str,  # specific type
        dict[
            str,  # "namespaces"
            dict[
                str,  # specific namespace
                dict[str, ListOfStringsType],  # "keys"  # list of keys
            ],
        ],
    ],
]
VersionDictType = dict[
    #   types     type      namespaces namespace keys
    str,  # "types"
    dict[
        str,  # specific type
        dict[
            str,  # "namespaces"
            dict[
                str,  # specific namespace
                dict[
                    str,  # "keys"
                    dict[
                        str,  # specific key
                        dict[
                            str,  # "versions"
                            ListOfStringsType,  # list of version strings
                        ],
                    ],
                ],
            ],
        ],
    ],
]
DecisionPointDictType = dict[str, DecisionPoint]
DecisionTableDictType = dict[str, DecisionTable]
