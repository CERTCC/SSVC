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

import unittest

from fastapi import HTTPException

from ssvc.api.helpers import _404_on_none


class Test404OnNone(unittest.TestCase):
    def test_raises_404_on_none(self):
        with self.assertRaises(HTTPException) as context:
            _404_on_none(None)
        self.assertEqual(context.exception.status_code, 404)
        self.assertEqual(context.exception.detail, "Item not found")

    def test_does_not_raise_on_not_none(self):
        try:
            _404_on_none("not none")
        except HTTPException:
            self.fail(
                "HTTPException should not be raised when obj is not None"
            )


if __name__ == "__main__":
    unittest.main()
