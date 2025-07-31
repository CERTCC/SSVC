#!/usr/bin/env python
"""
file: toposort
author: adh
created_at: 7/30/25 12:45 PM
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

import logging
from itertools import product

import networkx as nx

from ssvc.decision_points.base import DecisionPoint

logger = logging.getLogger(__name__)


def diff(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:

    if len(a) != len(b):
        raise ValueError("Tuples must be of the same length")

    d = [x - y for x, y in zip(a, b)]
    return tuple(d)


def all_but_one_zero(t: tuple[int, ...]) -> bool:
    """
    Check if all elements in the tuple are zero except for one element.
    """
    non_zero_count = sum(1 for x in t if x != 0)
    return non_zero_count == 1 and len(t) > 1


def exactly_one_one(t: tuple[int, ...]) -> bool:
    """
    Check if exactly one element in the tuple is one.
    """
    one_count = sum(1 for x in t if x == 1)
    return one_count == 1 and len(t) > 1


def off_by_one(t: tuple[int, ...]) -> bool:
    """
    Returns true if exactly one element in the tuple is one and all others are zero.
    Args:
        t: the tuple to check

    Returns:
        bool: True if the tuple is off by one, False otherwise

    """
    if not all_but_one_zero(t):
        return False
    if not exactly_one_one(t):
        return False
    return True


def graph_from_dplist(decision_points: list[DecisionPoint]) -> nx.DiGraph:

    dp_lookup = dplist_to_lookup(decision_points)

    value_lookup = dplist_to_value_lookup(decision_points)

    logger.debug(f"dp_lookup: {dp_lookup}")
    logger.debug(f"value_lookup: {value_lookup}")

    value_tuples = [tuple(v.keys()) for v in value_lookup]

    return graph_from_value_tuples(value_tuples)


def graph_from_value_tuples(value_tuples: list[tuple[int, ...]]) -> nx.DiGraph:
    G = nx.DiGraph()

    # add nodes to the graph
    nodes = list(product(*value_tuples))
    G.add_nodes_from(nodes)

    # add edges to the graph

    # For each node, try to increment one coordinate by one step
    for node in nodes:
        for i, val in enumerate(node):
            axis = value_tuples[i]
            idx = axis.index(val)
            if idx + 1 < len(axis):
                # Create a new node with i-th coordinate incremented
                neighbor = list(node)
                neighbor[i] = axis[idx + 1]
                neighbor = tuple(neighbor)
                if neighbor in G:
                    G.add_edge(node, neighbor)
    return G


def dplist_to_value_lookup(
    decision_points: list[DecisionPoint],
) -> list[dict[int, str]]:
    value_lookup = [
        {i: v.key for i, v in enumerate(dp.values)} for dp in decision_points
    ]
    return value_lookup


def dplist_to_lookup(decision_points: list[DecisionPoint]) -> dict[int, str]:
    dp_lookup = {i: dp.id for i, dp in enumerate(decision_points)}
    return dp_lookup


def lookup_value(t: tuple[int, ...], lookup: list[dict[int, str]]) -> tuple[str, ...]:
    #     given
    # t = (0, 0, 0)
    # lookup = [{0: 'V', 1: 'R', 2: 'S', 3: 'HS'}, {0: 'H', 1: 'S', 2: 'B', 3: 'N'}, {0: 'F', 1: 'R', 2: 'B', 3: 'N'}]
    # return (V,H,F
    l = [lookup[i][t[i]] for i in range(len(t))]
    return tuple(l)


def tuple_to_dict(t: tuple[str, ...], lookup: dict[int, str]) -> dict[str, str]:
    #     given
    # t = ('V', 'H', 'F')
    # return {'ER': 'V', 'GM': 'H', 'RC': 'F'}
    return {lookup[i]: t[i] for i in range(len(t))}


def dplist_to_toposort(decision_points: list[DecisionPoint]) -> list[dict[str, str]]:
    logger.debug("Creating graph from list of decision points")
    G = graph_from_dplist(decision_points)
    dp_lookup = dplist_to_lookup(decision_points)
    value_lookup = dplist_to_value_lookup(decision_points)
    logger.debug(
        "Graph created, performing topological sort over decision points graph"
    )
    sorted_nodes = nx.topological_sort(G)
    sorted_list = []
    logger.debug("Topological sort completed, converting graph nodes to dictionaries")
    for node in sorted_nodes:
        vals = lookup_value(node, value_lookup)
        sorted_list.append(tuple_to_dict(vals, dp_lookup))
    return sorted_list


def main():
    from ssvc.decision_points.cvss.attack_vector import LATEST as AT
    from ssvc.decision_points.cvss.attack_complexity import LATEST as AC
    from ssvc.decision_points.cvss.privileges_required import LATEST as PR

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    dps = [AT, AC, PR]

    print("mapping order:")
    print("===========================")
    for row in dplist_to_toposort(dps):
        print(row)


if __name__ == "__main__":
    main()
