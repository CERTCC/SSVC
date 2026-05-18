"""Spec registry for ``specs/*.yaml`` structured requirement files."""


#  Copyright (c) 2026 Carnegie Mellon University.
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

import warnings

from ssvc.metadata.specs.registry import SpecRegistry, load_registry


class UnknownSpecIdWarning(UserWarning):
    """Warning emitted when a test references a spec ID not in the registry.

    Emitted (non-blocking) by ``pytest_collection_modifyitems`` when a
    ``@pytest.mark.spec`` marker references an ID that cannot be found in the
    loaded :class:`SpecRegistry`.
    """


def warn_unknown_spec_id(spec_id: str, registry: SpecRegistry) -> None:
    """Emit :class:`UnknownSpecIdWarning` if ``spec_id`` is not in registry.

    Args:
        spec_id: The spec ID string to validate.
        registry: The loaded :class:`SpecRegistry` to check against.
    """
    try:
        registry.get(spec_id)
    except KeyError:
        warnings.warn(
            f"Unknown spec ID referenced in test marker: {spec_id!r}",
            UnknownSpecIdWarning,
            stacklevel=2,
        )


__all__ = [
    "SpecRegistry",
    "UnknownSpecIdWarning",
    "load_registry",
    "warn_unknown_spec_id",
]
