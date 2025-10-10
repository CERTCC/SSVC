#!/usr/bin/env python
"""
SSVC API v1 Examples Router
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

from fastapi import APIRouter

from ssvc.decision_points.base import DecisionPoint, DecisionPointValue
from ssvc.decision_tables.base import DecisionTable
from ssvc.examples import (
    EXAMPLE_DECISION_POINT_1,
    EXAMPLE_DECISION_TABLE,
    EXAMPLE_MINIMAL_DECISION_POINT_VALUE,
    EXAMPLE_SELECTION_1,
    EXAMPLE_SELECTION_LIST,
)
from ssvc.selection import (
    MinimalDecisionPointValue,
    Reference,
    Selection,
    SelectionList,
)

router = APIRouter(prefix="/examples", tags=["Examples"])

# GET to retrieve a sample object
# POST to validate an object against the pydantic model


# Decision Point Values
@router.get(
    "/decision-point-values",
    response_model=DecisionPointValue,
    response_model_exclude_none=True,
    summary="Get a sample Decision Point Value",
    description="Retrieve a sample Decision Point Value object.",
)
def get_example_decision_point_value() -> DecisionPointValue:
    """
    Retrieve a sample Decision Point Value object.
    """
    return EXAMPLE_DECISION_POINT_1.values[0]


@router.post(
    "/decision-point-values",
    response_model=DecisionPointValue,
    response_model_exclude_none=True,
    summary="Validate a Decision Point Value",
    description="Validate a Decision Point Value object against the pydantic model.",
)
def validate_decision_point_value(
    decision_point_value: DecisionPointValue,
) -> DecisionPointValue:
    """
    Validate a Decision Point Value object against the pydantic model.
    """
    return decision_point_value


# Decision Points
@router.get(
    "/decision-points",
    response_model=DecisionPoint,
    response_model_exclude_none=True,
    summary="Get a sample Decision Point",
    description="Retrieve a sample Decision Point object.",
)
def get_example_decision_point() -> DecisionPoint:
    """
    Retrieve a sample Decision Point object.
    """
    return EXAMPLE_DECISION_POINT_1


@router.post(
    "/decision-points",
    response_model=DecisionPoint,
    response_model_exclude_none=True,
    summary="Validate a Decision Point",
    description="Validate a Decision Point object against the pydantic model.",
)
def validate_decision_point(decision_point: DecisionPoint) -> DecisionPoint:
    """
    Validate a Decision Point object against the pydantic model.
    """
    return decision_point


# Decision Tables
@router.get(
    "/decision-tables",
    response_model=DecisionTable,
    response_model_exclude_none=True,
    summary="Get a sample Decision Table",
    description="Retrieve a sample Decision Table object.",
)
def get_example_decision_table() -> DecisionTable:
    """
    Retrieve a sample Decision Table object.
    """
    return EXAMPLE_DECISION_TABLE


@router.post(
    "/decision-tables",
    response_model=DecisionTable,
    response_model_exclude_none=True,
    summary="Validate a Decision Table",
    description="Validate a Decision Table object against the pydantic model.",
)
def validate_decision_table(decision_table: DecisionTable) -> DecisionTable:
    """
    Validate a Decision Table object against the pydantic model.
    """
    return decision_table


# minimal decision point values
@router.get(
    "/decision-point-values-minimal",
    response_model=MinimalDecisionPointValue,
    response_model_exclude_none=True,
    summary="Get a minimal Decision Point Value",
    description="Retrieve a minimal Decision Point Value object.",
)
def get_minimal_decision_point_value() -> MinimalDecisionPointValue:
    """
    Retrieve a minimal Decision Point Value object.
    """
    return EXAMPLE_MINIMAL_DECISION_POINT_VALUE


@router.post(
    "/decision-point-values-minimal",
    response_model=MinimalDecisionPointValue,
    response_model_exclude_none=True,
    summary="Validate a minimal Decision Point Value",
    description="Validate a minimal Decision Point Value object against the pydantic model.",
)
def validate_minimal_decision_point_value(
    minimal_decision_point_value: MinimalDecisionPointValue,
) -> MinimalDecisionPointValue:
    """
    Validate a minimal Decision Point Value object against the pydantic model.
    """
    return minimal_decision_point_value


# selection
@router.get(
    "/selections",
    response_model=Selection,
    response_model_exclude_none=True,
    summary="Get a sample Selection",
    description="Retrieve a sample Selection object.",
)
def get_example_selection() -> Selection:
    """
    Retrieve a sample Selection object.
    """
    return EXAMPLE_SELECTION_1


@router.post(
    "/selections",
    response_model=Selection,
    response_model_exclude_none=True,
    summary="Validate a Selection",
    description="Validate a Selection object against the pydantic model.",
)
def validate_selection(selection: Selection) -> Selection:
    """
    Validate a Selection object against the pydantic model.
    """
    return selection


# Selection lists
@router.get(
    "/selection-lists",
    response_model=SelectionList,
    response_model_exclude_none=True,
    summary="Get a sample Selection List",
    description="Retrieve a sample Selection List object.",
)
def get_example_selection_list() -> SelectionList:
    """
    Retrieve a sample Selection List object.
    """
    return EXAMPLE_SELECTION_LIST


@router.post(
    "/selection-lists",
    response_model=SelectionList,
    response_model_exclude_none=True,
    summary="Validate a Selection List",
    description="Validate a Selection List object against the pydantic model.",
)
def validate_selection_list(selection_list: SelectionList) -> SelectionList:
    """
    Validate a Selection List object against the pydantic model.
    """
    return selection_list


# references
@router.get(
    "/references",
    response_model=Reference,
    response_model_exclude_none=True,
    summary="Get sample References",
    description="Retrieve a list of sample Reference URIs.",
)
def get_example_references() -> Reference:
    """
    Retrieve a list of sample Reference URIs.
    """
    return EXAMPLE_SELECTION_LIST.references[0]


@router.post(
    "/references",
    response_model=Reference,
    response_model_exclude_none=True,
    summary="Validate a Reference",
    description="Validate a Reference object against the pydantic model.",
)
def validate_reference(reference: Reference) -> Reference:
    """
    Validate a Reference object against the pydantic model.
    """
    return reference
