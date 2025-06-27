#!/usr/bin/env python
"""
file: registry
author: adh
created_at: 6/26/25 10:31 AM
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

from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)


class Registry(BaseModel):
    """
    A simple registry for storing key-value pairs of BaseModel objects.
    This registry allows for idempotent registration of key-value pairs,
    where the key is a string and the value is a BaseModel object.
    """

    registry: dict[str, BaseModel] = Field(default_factory=dict)

    def __iter__(self) -> object:
        return iter(self.registry.values())

    def __getitem__(self, key: str) -> object:
        return self.registry[key]

    def register(self, key: str, value: BaseModel) -> None:
        """
        Idempotently register a key-value pair in the registry.
        If the key does not exist, it is added to the registry.
        If the key already exists, and the value is the same, it is ignored.
        If the key already exists with a different value, a KeyError is raised.

        Args:
            key: The key to register.
            value: The object to register under the key.

        Returns:
            None

        Raises:
            KeyError: If the key already exists with a different value.

        """
        if key in self.registry:
            # are the values the same?
            registered = self.registry[key].model_dump_json()
            value_dumped = value.model_dump_json()
            if registered == value_dumped:
                logger.debug(f"Duplicate key {key} with the same value, ignoring.")
                return

            logger.warning(f"Duplicate key {key}:")
            logger.warning(f"\t{registered}")
            logger.warning(f"\t{value_dumped}")
            raise KeyError(f"Duplicate key {key}")

        self.registry[key] = value

    def __contains__(self, key: str) -> bool:
        return key in self.registry

    def reset_registry(self) -> None:
        self.registry = {}

    # convenience alias
    def clear(self) -> None:
        self.reset_registry()


def main():
    pass


if __name__ == "__main__":
    main()
