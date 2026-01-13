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

"""
Provides TODO writeme
"""
from typing import Callable

import numpy as np

from ssvc.decision_points.base import DecisionPoint
from ssvc.utils.graph_labeling import (
    _magnitude_quantile_labels_from_graph,
    euclidean_distances,
    graph_from_dplist,
)


class DtGraph:
    """Helper class to represent the decision table as a graph to facilitate mapping generation."""

    def __init__(
        self,
        decision_points: dict[str, DecisionPoint],
        outcome_id: str,
        norm_func: Callable[[np.ndarray], np.ndarray] = euclidean_distances,
    ) -> None:
        """
        Initialize the DtGraph.

        Args:
            decision_points: dict[str, DecisionPoint]: The decision points in the decision table.
            outcome_id: str: The ID of the outcome decision point. Must be a key in decision_points.
            norm_func: Callable[[np.ndarray], np.ndarray]: A normalization function to apply to the distance matrix. Defaults to euclidean_distances.
        Raises:
            ValueError: If the outcome_id is not found in decision_points.
        """
        self.decision_points = decision_points
        self.outcome_id = outcome_id
        self.norm_func = norm_func

        if self.outcome_id not in self.decision_points:
            raise ValueError(
                f"Outcome ID '{self.outcome_id}' not found in decision points."
            )

        self._input_points = {
            k: v
            for k, v in self.decision_points.items()
            if k != self.outcome_id
        }
        self._outcome_point = self.decision_points[self.outcome_id]

        # G is an integer-labeled directed graph representing the decision table
        self.G = graph_from_dplist(
            decision_points=list(self._input_points.values())
        )

        self.K = len(self._outcome_point.values)

    def _int_labels(self):
        return _magnitude_quantile_labels_from_graph(
            G=self.G, K=self.K, norm_func=self.norm_func
        )

    def mapping(self) -> list[dict[str, str]]:
        """
        Generate the mapping from the graph with integer labels to decision point value keys.

        Returns:
            list[dict[str, str]]: The mapping as a list of dictionaries.
        """
        int_labels = self._int_labels()
        mapping = []
        input_dps = list(self._input_points.values())
        outcome_dp = self._outcome_point

        for node in self.G.nodes:
            row = {}
            for i, dp in enumerate(input_dps):
                value_idx = node[i]
                value_key = dp.values[value_idx].key
                row[dp.id] = value_key
            outcome_idx = int_labels[node]
            outcome_value_key = outcome_dp.values[outcome_idx].key
            row[self.outcome_id] = outcome_value_key
            mapping.append(row)

        return mapping
