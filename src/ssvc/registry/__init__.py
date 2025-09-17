"""
Provides an object registry for SSVC.
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

from ssvc.registry.events import add_registration_hook

logger = logging.getLogger(__name__)

# create an empty registry
_REGISTRY = None


def get_registry() -> "SsvcObjectRegistry":
    """Create and return a new SSVC object registry."""
    from ssvc.registry.base import SsvcObjectRegistry

    global _REGISTRY

    if _REGISTRY is None:
        _REGISTRY = SsvcObjectRegistry(
            name="SSVC Object Registry",
            definition="A registry for SSVC objects organized by type, namespace, key, and version.",
        )

    return _REGISTRY


def _handle_registration(obj):
    """Handle object registration with type checking."""
    registry = get_registry()

    # Import here to avoid circular imports
    try:
        from ssvc.decision_points.base import DecisionPoint, DecisionPointValue
        from ssvc.decision_tables.base import DecisionTable

        if isinstance(obj, (DecisionPoint, DecisionPointValue, DecisionTable)):
            registry.register(obj)
            logger.debug(
                "Registered object %s of type %s", obj.id, type(obj).__name__
            )
        else:
            logger.warning(
                f"Object {obj.id} is not a recognized SSVC type: {type(obj)}"
            )
            raise TypeError(f"Object {obj.id} is not a valid SSVC type.")

    except ImportError:
        # Fallback registration without type checking
        logger.debug(f"Handling registration for {obj.id} of type {type(obj)}")
        registry.register(obj)


# Set up the hook
add_registration_hook(_handle_registration)
