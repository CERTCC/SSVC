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
import math
from collections import Counter
from functools import partial
from typing import Any, Callable, Dict, List, Optional, Tuple

import colorcet as cc
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

from ssvc.decision_tables.base import DecisionTable
from ssvc.utils.toposort import graph_from_dplist


def draw_hasse(
    G: nx.DiGraph,
    ax: Optional[plt.Axes] = None,
    use_graphviz: bool = True,
    node_size: int = 500,
    node_color_attr: str = "color",
    figsize: Tuple[int, int] = (18, 16),
) -> plt.Axes:
    """
    Draw a Hasse-like diagram for a DAG. Returns the axes containing the plot.
    Per-node colors are read from node attribute `node_color_attr` when
    `node_color` is None.
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)

    pos: Optional[Dict[Any, Tuple[float, float]]] = None

    if use_graphviz:
        pos = layout_graphviz(G)

    if pos is None:
        pos = layout_deterministic(G)

    nx_node_color = [G.nodes[n].get(node_color_attr, "skyblue") for n in G.nodes()]

    nx.draw(
        G,
        pos=pos,
        with_labels=True,
        node_size=node_size,
        node_color=nx_node_color,
        edge_color="gray",
        font_size=10,
        ax=ax,
    )
    ax.margins(0.2)
    return ax


def layout_deterministic(G: nx.DiGraph) -> dict[Any, tuple[
    float, float]] | None:
    # Deterministic level layout (longest distance from minimal nodes)
    min_nodes = [n for n in G.nodes if G.in_degree(n) == 0] or list(G.nodes)
    levels: Dict[Any, int] = {n: 0 for n in min_nodes}
    for n in nx.topological_sort(G):
        base = levels.get(n, 0)
        for s in G.successors(n):
            levels[s] = max(levels.get(s, 0), base + 1)

    level_groups: Dict[int, List[Any]] = {}
    for n, lvl in levels.items():
        level_groups.setdefault(lvl, []).append(n)

    pos = {}
    for lvl in sorted(level_groups):
        nodes = sorted(level_groups[lvl], key=lambda x: str(x))
        count = len(nodes)
        xs = [i - (count - 1) / 2.0 for i in range(count)]
        y = float(lvl)
        for x, n in zip(xs, nodes):
            pos[n] = (x, y)

    remaining = [n for n in G.nodes if n not in pos]
    if remaining:
        count = len(remaining)
        xs = [i - (count - 1) / 2.0 for i in range(count)]
        for x, n in zip(xs, remaining):
            pos[n] = (x, 0.0)
    return pos


def layout_graphviz(G: nx.DiGraph) -> dict[Any, tuple[float, float]] | None:
    pos = None

    try:
        from networkx.drawing.nx_agraph import graphviz_layout  # type: ignore

        pos = graphviz_layout(G, prog="dot", args="-Grankdir=BT")
    except Exception:
        try:
            from networkx.drawing.nx_pydot import graphviz_layout  # type: ignore

            pos = graphviz_layout(G, prog="dot", args="-Grankdir=BT")
        except Exception:
            pass

    return pos


def write_graph(filename: str, G: nx.DiGraph, figsize: Tuple[int, int] = (24, 20),svg:bool=False,png:bool=True) -> None:
    """Render `G` and write PNG and SVG files named `filename`.png / .svg."""
    if not (png or svg):
        raise ValueError("At least one of png or svg must be True")

    ax = draw_hasse(G, figsize=figsize)

    if png:
        ax.figure.savefig(f"{filename}.png", dpi=300, bbox_inches="tight")
    if svg:
        ax.figure.savefig(f"{filename}.svg", bbox_inches="tight")

    plt.close(ax.figure)

# define partial functions for different norms
l1_magnitudes: Callable[[np.ndarray], np.ndarray] = partial(np.linalg.norm, ord=1, axis=1)
l2_magnitudes: Callable[[np.ndarray], np.ndarray] = partial(np.linalg.norm, ord=2, axis=1)
linf_magnitudes: Callable[[np.ndarray], np.ndarray] = partial(np.linalg.norm, ord=np.inf, axis=1)

manhattan_distances = l1_magnitudes
euclidean_distances = l2_magnitudes
max_distances = linf_magnitudes

def normalize_columns(arr: np.ndarray[tuple[Any, ...], np.dtype[Any]]) -> np.ndarray[tuple[Any, ...], np.dtype[Any]]:
    """Normalize each column of `arr` to the range [0, 1].

    Args:
        arr: 2D numpy array to normalize. All columns must have minimum 0 and positive maximum.
    Returns:
        Normalized 2D numpy array with same shape as `arr`. All columns are scaled to [0, 1].
    Raises:
        ValueError: If any column does not have minimum 0 or has non-positive maximum.
    """
    maxs = arr.max(axis=0)

    if np.any(maxs <= 0):
        # throw an error if maxs are not positive
        raise ValueError("All columns must have a positive maximum value for normalization.")

    # we're just going to scale from 0 to max
    # so we can use min as 0 for all columns
    mins = np.zeros_like(maxs)
    ranges = maxs - mins
    arr_norm = np.zeros_like(arr)

    nonzero = ranges != 0.0
    if np.any(nonzero):
        arr_norm[:, nonzero] = (arr[:, nonzero] - mins[nonzero]) / ranges[nonzero]
    return arr_norm


def magnitude_quantile_labels_from_graph(
    G: nx.DiGraph,
    K: int,
    norm_func: Optional[Callable[[np.ndarray], np.ndarray]] = euclidean_distances,
) -> Dict[Any, int]:
    """
    More sophisticated magnitude-quantile labeling that normalizes per-dimension
    then computes magnitudes and forms clump-safe quantile bins.

    This function now accepts a dependency (norm_func) that computes magnitudes
    from the normalized array. For backward compatibility, a legacy `norm`
    spec (string/number) is still accepted and mapped once to an appropriate
    norm_func before use.
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

    arr_norm = normalize_columns(arr)

    # Compute magnitudes by calling dependency
    mags = norm_func(arr_norm)

    unique_mags = np.unique(mags)
    um_list = unique_mags.tolist()

    probs = [i / K for i in range(K + 1)]
    try:
        raw_cuts = np.quantile(mags, probs, method="linear")
    except TypeError:
        raw_cuts = np.quantile(mags, probs, interpolation="linear")  # type: ignore

    def first_strictly_greater(val: float) -> float:
        idx = bisect.bisect_right(um_list, val)
        return float(um_list[idx]) if idx < len(um_list) else float(um_list[-1])

    adjusted: List[float] = [0.0] * (K + 1)
    adjusted[0] = float(um_list[0])
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
            adjusted[j] = float(um_list[idx]) if idx < len(um_list) else float(um_list[-1])

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



def spectrum(n, cmap="rainbow"):
    base = cc.cm[cmap]
    return [base(i / (n - 1)) for i in range(n)]

class DecisionTableGraph:
    def __init__(self,decision_table: DecisionTable, norm_func: Callable[[np.ndarray],np.ndarray] = euclidean_distances) -> None:
        self.dt = decision_table
        self.norm_func = norm_func
        self.cmap = "bmy"
        self.pos = None

        self.G = graph_from_dplist(
            decision_points=[
                dp
                for dp in self.dt.decision_points.values()
                if dp.id != self.dt.outcome
            ]
        )
        # number of outcome labels
        self.K = len(self.dt.decision_points[self.dt.outcome].values)

    def layout(self,redraw: bool = False) -> dict[Any, tuple[float, float]]:
        """
        Compute or return cached layout for the graph.
        Args:
            redraw: If True, recompute the layout even if cached.

        Returns:
            Dictionary mapping nodes to (x, y) positions.
        """
        if self.pos is not None and not redraw:
            return self.pos
        # try graphviz layout first, fall back to deterministic layout
        pos = layout_graphviz(self.G)

        if pos is not None:
            self.pos = pos
            return pos

        self.pos = layout_deterministic(self.G)
        return self.pos

    def draw(self):
        return draw_hasse(self.G)

    def labels(self):
        return magnitude_quantile_labels_from_graph(self.G, K=self.K, norm_func=self.norm_func)

    def colorize(self):
        # generate RGBA tuples from spectrum, then convert to hex strings for Graphviz/pygraphviz
        raw_colors = spectrum(self.K, cmap=self.cmap)
        color_list = [mcolors.to_hex(tuple(float(c) for c in col), keep_alpha=False) for col in raw_colors]

        for node, i in self.labels().items():
            self.G.nodes[node]["color"] = color_list[i]

    def draw(self, figsize: Tuple[int, int] = (24, 20)) -> plt.Axes:
        return draw_hasse(self.G, figsize=figsize)

    def write_graph(self, filename: str, figsize: Tuple[int, int] = (24, 20)) -> None:
        write_graph(filename, self.G, figsize=figsize)

def main() -> None:
    """Main entry: build graphs from decision tables, color nodes, draw and write outputs."""

    from ssvc.decision_tables.aivss.execution_power import LATEST as DT_AIVSS
    from ssvc.decision_tables.ssvc.deployer_dt import LATEST as DT_DEPLOYER
    from ssvc.decision_tables.ssvc.coord_triage import LATEST as DT_COORD_TRIAGE
    from ssvc.decision_tables.ssvc.supplier_dt import LATEST as DT_SUPPLIER

    for j,normfunc in enumerate([manhattan_distances, euclidean_distances, max_distances]):
        for dt in [("aivss", DT_AIVSS), ("deployer", DT_DEPLOYER),("coord_triage", DT_COORD_TRIAGE), ("supplier", DT_SUPPLIER)]:


            dtg = DecisionTableGraph(dt[1], normfunc)
            dtg.norm_func = normfunc
            dtg.colorize()
            dtg.layout()

            G = dtg.G
            # scale the graph to fit in the figure
            # how many layers in the graph?
            height = 0
            width = 0
            for l in nx.topological_generations(G):
                height += 1
                width = max(width, len(list(l)))
            figsize = (max(24, width * 3), max(20, height * 3))

            dtg.write_graph(filename=f"hasse_vector_magnitude_quantiles_3_{dt[0]}_norm_{j+1}", figsize=figsize)
            write_graph(f"hasse_vector_magnitude_quantiles_3_{dt[0]}_norm_{j+1}", G)
            print(figsize)
            print(f"{dt[0].upper()} color counts (norm {j+1}):", Counter([G.nodes[n]["color"] for n in G.nodes()]))

if __name__ == "__main__":
    main()
