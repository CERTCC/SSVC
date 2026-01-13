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

import logging
import math
from functools import partial
from itertools import product
from typing import Any, Callable, Dict, List

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


def _normalize_columns(arr: np.ndarray) -> np.ndarray:
    """
    Normalize each column of `arr` to the range [0, 1].

    This computes per-column min and max and scales each column as:
        (col - min) / (max - min)

    Raises:
        ValueError: if any column has zero range (max == min).
    """
    arr = np.asarray(arr, dtype=float)
    if arr.ndim != 2:
        raise ValueError("Input must be a 2D array")

    mins = arr.min(axis=0)
    maxs = arr.max(axis=0)
    ranges = maxs - mins

    if np.any(ranges == 0.0):
        # Explicitly fail for zero-range columns to avoid division-by-zero ambiguity.
        zero_cols = np.where(ranges == 0.0)[0].tolist()
        raise ValueError(
            f"Columns with zero range cannot be normalized: {zero_cols}"
        )

    arr_norm = (arr - mins) / ranges
    return arr_norm


def _magnitude_quantile_labels_from_graph(
    G: nx.DiGraph,
    K: int,
    norm_func: Callable[[np.ndarray], np.ndarray] = None,
) -> Dict[Any, int]:
    """
    Assign labels to graph nodes based on quantiles of their vector magnitudes.

    Notes:
     - norm_func defaults to L2 if not provided by the caller.
     - Uses numpy searchsorted on the sorted unique magnitudes to make tie-handling explicit.
    """
    if norm_func is None:
        # but keep compatibility with callers that pass no norm_func
        from functools import partial

        norm_func = partial(np.linalg.norm, ord=2, axis=1)

    if K < 2:
        raise ValueError("K must be >= 2")

    node_iterable = list(G.nodes())
    if not node_iterable:
        raise ValueError("Graph has no nodes")

    node_vectors: List[tuple] = [
        tuple(int(x) for x in n) for n in node_iterable
    ]

    dim = len(node_vectors[0])
    for v in node_vectors:
        if len(v) != dim:
            raise ValueError("All node vectors must have the same length")

    arr = np.array(node_vectors, dtype=float)
    arr_norm = _normalize_columns(arr)

    mags = norm_func(arr_norm)
    unique_mags = np.unique(mags)
    if unique_mags.size == 0:
        raise ValueError("No magnitudes computed")

    probs = np.linspace(0.0, 1.0, K + 1)
    try:
        raw_cuts = np.quantile(mags, probs, method="linear")
    except TypeError:
        raw_cuts = np.quantile(mags, probs, interpolation="linear")  # type: ignore

    # helper: next unique magnitude strictly greater than val (or last if none)
    def next_strictly_greater(val: float) -> float:
        idx = np.searchsorted(unique_mags, val, side="right")
        return (
            float(unique_mags[idx])
            if idx < unique_mags.size
            else float(unique_mags[-1])
        )

    # build adjusted cuts ensuring strictly increasing sequence from unique_mags
    adjusted = [0.0] * (K + 1)
    adjusted[0] = float(unique_mags[0])
    adjusted[-1] = float(unique_mags[-1])

    for j in range(1, K):
        c = float(raw_cuts[j])
        # if the cut equals an existing magnitude, move to the next strictly greater unique mag
        if np.any(np.isclose(unique_mags, c)):
            adjusted[j] = next_strictly_greater(c)
        else:
            adjusted[j] = c

    # enforce strictly increasing using unique_mags when needed
    for j in range(1, K + 1):
        prev = adjusted[j - 1]
        cur = adjusted[j]
        if cur <= prev or math.isclose(cur, prev):
            # pick the next unique magnitude after prev
            idx = np.searchsorted(unique_mags, prev, side="right")
            adjusted[j] = (
                float(unique_mags[idx])
                if idx < unique_mags.size
                else float(unique_mags[-1])
            )

    adj_array = np.array(adjusted, dtype=float)

    # assign labels using searchsorted (right) then clamp to [0, K-1]
    labels_list: List[int] = []
    for m in mags:
        pos = int(np.searchsorted(adj_array, float(m), side="right") - 1)
        pos = max(0, min(pos, K - 1))
        labels_list.append(pos)

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
    decision_points: List[DecisionPoint],
) -> List[Dict[int, Any]]:
    """
    Convert a list of DecisionPoint objects into a list of index->value-key mappings.
    Each entry corresponds to one DecisionPoint and maps the value index to the value key.
    """
    value_lookup: List[Dict[int, Any]] = [
        {i: v.key for i, v in enumerate(dp.values)} for dp in decision_points
    ]
    return value_lookup
