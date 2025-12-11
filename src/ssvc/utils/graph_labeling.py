#!/usr/bin/env python


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

import bisect
import logging
import math
from functools import partial
from itertools import product
from typing import Any, Callable, Dict, List, Tuple

# import colorcet as cc
import networkx as nx
import numpy as np

from ssvc.decision_points.base import DecisionPoint

logger = logging.getLogger(__name__)


# define partial functions for different norms
l1_magnitudes: Callable[[np.ndarray], np.ndarray] = partial(
    np.linalg.norm, ord=1, axis=1
)
l2_magnitudes: Callable[[np.ndarray], np.ndarray] = partial(
    np.linalg.norm, ord=2, axis=1
)
linf_magnitudes: Callable[[np.ndarray], np.ndarray] = partial(
    np.linalg.norm, ord=np.inf, axis=1
)

# convenience aliases
manhattan_distances = l1_magnitudes
euclidean_distances = l2_magnitudes
max_distances = linf_magnitudes


def _normalize_columns(
    arr: np.ndarray[tuple[Any, ...], np.dtype[Any]],
) -> np.ndarray[tuple[Any, ...], np.dtype[Any]]:
    """Normalize each column of `arr` to the range [0, 1].

    Args:
        arr: 2D numpy array to normalize. All columns must have minimum 0 and positive maximum.
    Returns:
        Normalized 2D numpy array with same shape as `arr`. All columns are scaled to [0, 1].
    Raises:
        ValueError: If any column does not have minimum 0 or has non-positive maximum.
    """
    # ensure that arr is all floats
    arr = arr.astype(float)

    maxs = arr.max(axis=0)

    if np.any(maxs <= 0):
        # throw an error if maxs are not positive
        raise ValueError(
            "All columns must have a positive maximum value for normalization."
        )

    # we're just going to scale from 0 to max
    # so we can use min as 0 for all columns
    mins = np.zeros_like(maxs)
    ranges = maxs - mins
    arr_norm = np.zeros_like(arr)

    nonzero = ranges != 0.0
    if np.any(nonzero):
        arr_norm[:, nonzero] = (arr[:, nonzero] - mins[nonzero]) / ranges[
            nonzero
        ]
    return arr_norm


def _magnitude_quantile_labels_from_graph(
    G: nx.DiGraph,
    K: int,
    norm_func: Callable[[np.ndarray], np.ndarray] = euclidean_distances,
) -> Dict[Any, int]:
    """
    Assign labels to graph nodes based on quantiles of their vector magnitudes.
    Args:
        G: Input graph with nodes as integer tuples representing vectors.
        K: Number of quantile-based labels to assign (must be >= 2).
        norm_func: Function to compute vector magnitudes (default: Euclidean aka L2 norm).
    """
    if K < 2:
        raise ValueError("K must be >= 2")

    node_iterable = list(G.nodes())
    if not node_iterable:
        raise ValueError("Graph has no nodes")

    node_vectors: List[Tuple[int, ...]] = []

    for n in node_iterable:
        vec = n
        node_vectors.append(tuple(int(x) for x in vec))

    dim = len(node_vectors[0])
    for v in node_vectors:
        if len(v) != dim:
            raise ValueError("All node vectors must have the same length")

    # normalize per-dimension to [0,1]
    arr = np.array(node_vectors, dtype=float)

    arr_norm = _normalize_columns(arr)

    # Compute magnitudes by calling dependency
    mags = norm_func(arr_norm)

    # here is where we start the quantile labeling
    unique_mags = np.unique(mags)
    um_list = unique_mags.tolist()

    # Compute raw quantile cut values
    probs = [i / K for i in range(K + 1)]
    try:
        raw_cuts = np.quantile(mags, probs, method="linear")
    except TypeError:
        raw_cuts = np.quantile(mags, probs, interpolation="linear")  # type: ignore

    def first_strictly_greater(val: float) -> float:
        idx = bisect.bisect_right(um_list, val)
        return (
            float(um_list[idx]) if idx < len(um_list) else float(um_list[-1])
        )

    # create adjusted cut values
    adjusted: List[float] = [0.0] * (K + 1)
    # the min and max cuts are fixed
    # lowest cut is min magnitude
    adjusted[0] = float(um_list[0])
    # highest cut is max magnitude
    adjusted[-1] = float(um_list[-1])

    # Adjust cut values to avoid clumps
    for j in range(1, K):
        c = float(raw_cuts[j])
        if np.any(np.isclose(unique_mags, c)):
            adjusted[j] = first_strictly_greater(c)
        else:
            adjusted[j] = c

    # Ensure strictly increasing cut values
    for j in range(1, K + 1):
        prev = adjusted[j - 1]
        cur = adjusted[j]
        if cur <= prev or math.isclose(cur, prev):
            idx = bisect.bisect_right(um_list, prev)
            adjusted[j] = (
                float(um_list[idx])
                if idx < len(um_list)
                else float(um_list[-1])
            )

    # Assign labels based on adjusted cut values
    adj_list = adjusted
    labels_list: List[int] = []
    for m in mags:
        pos = bisect.bisect_right(adj_list, float(m)) - 1
        if pos < 0:
            pos = 0
        if pos >= K:
            pos = K - 1
        labels_list.append(int(pos))

    return {node: label for node, label in zip(node_iterable, labels_list)}


def graph_from_dplist(decision_points: list[DecisionPoint]) -> nx.DiGraph:
    logger.debug(
        f"Creating graph from dplist: {[dp.id for dp in decision_points]}"
    )
    value_lookup = dplist_to_value_lookup(decision_points)
    value_tuples = [tuple(v.keys()) for v in value_lookup]
    logger.debug(f"Value tuples: {value_tuples}")

    return graph_from_value_tuples(value_tuples)


def graph_from_value_tuples(value_tuples: list[tuple[int, ...]]) -> nx.DiGraph:
    logger.debug(f"Creating graph from value_tuples: {value_tuples}")
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
