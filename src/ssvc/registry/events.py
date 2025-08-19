#!/usr/bin/env python
"""
Provides an event system for SSVC object registration.
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

logger = logging.getLogger(__name__)

_registration_hooks = []


def add_registration_hook(hook_func):
    """Add a function to be called when objects are registered."""
    logger.debug(f"Adding registration hook: {hook_func.__name__}")
    _registration_hooks.append(hook_func)


def notify_registration(obj):
    """Notify all hooks about a new registration."""
    for hook in _registration_hooks:
        try:
            logger.debug(
                f"Notifying {hook.__name__} about registration of {obj.id}"
            )
            hook(obj)
        except Exception as e:
            logger.warning(f"Registration hook failed: {e}")
            raise
