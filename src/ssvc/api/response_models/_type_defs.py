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

# simple stuff first
StringsListType = list[str]
"""A list of strings, used for various purposes in the API."""

DecisionPointValuesListType = list[DecisionPointValue]
"""A list of decision point values."""

DecisionPointDictType = dict[str, DecisionPoint]
"""A dictionary mapping decision point IDs to their corresponding DecisionPoint objects."""

DecisionTableDictType = dict[str, DecisionTable]
"""A dictionary mapping decision table IDs to their corresponding DecisionTable objects."""


# more complex types
TypesDictType = dict[
    str,  # "types"
    list[str],  # list of object types
]
"""A dictionary containing a list of object types."""

NamespaceDictType = dict[
    str,  # "types"
    dict[
        str,  # specific type
        dict[
            str, StringsListType  # "namespaces"  # list of namespace strings
        ],
    ],
]
"""A nested dictionary mapping object types to lists of namespaces for each type."""

KeyDictType = dict[
    str,  # "types"
    dict[
        str,  # specific type
        dict[
            str,  # "namespaces"
            dict[
                str,  # specific namespace
                dict[str, StringsListType],  # "keys"  # list of keys
            ],
        ],
    ],
]
"""A nested dictionary mapping object types to namespaces and keys for each type."""

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
                            StringsListType,  # list of version strings
                        ],
                    ],
                ],
            ],
        ],
    ],
]
"""A nested dictionary mapping object types to namespaces, keys, and versions for each type."""
