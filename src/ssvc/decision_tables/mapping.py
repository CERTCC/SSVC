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

from datetime import datetime
from typing import List

from pydantic import BaseModel, Field, validator


class SsvcDecisionPointSelection(BaseModel):
    name: str = Field(..., min_length=1, description="Name of the decision point")
    namespace: str = Field(
        ..., min_length=1, description="Namespace of the decision point"
    )
    version: str = Field(..., min_length=1, description="Version of the decision point")
    values: List[str] = Field(
        ..., min_items=1, description="Selected values for the decision point"
    )

    @validator("values")
    def check_values_not_empty(cls, v):
        if not v or len(v) < 1:
            raise ValueError("At least one value must be specified")
        return v


class DecisionPointValueSelection(BaseModel):
    id: str = Field(
        ...,
        min_length=1,
        description="Identifier for the vulnerability (e.g., CVE, VU#, GHSA, etc.)",
    )
    role: str = Field(
        ...,
        min_length=1,
        description="Stakeholder role (Supplier, Deployer, Coordinator, etc.)",
    )
    timestamp: datetime = Field(
        ..., description="RFC 3339 timestamp for the evaluation"
    )
    schemaVersion: str = Field(
        ...,
        min_length=1,
        description="Schema version used for the decision point evaluation",
    )
    selections: List[SsvcDecisionPointSelection] = Field(
        ..., min_items=1, description="Evaluated decision points"
    )

    @validator("selections")
    def check_selections_not_empty(cls, v):
        if not v or len(v) < 1:
            raise ValueError("At least one decision point selection must be provided")
        return v
