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
import re
import unittest

from ssvc.utils.defaults import MAX_NS_LENGTH, MIN_NS_LENGTH
from ssvc.utils.patterns import (
    BASE_NS_PATTERN,
    BASE_PATTERN,
    EXT_SEGMENT_PATTERN,
    LENGTH_CHECK_PATTERN,
    NS_PATTERN,
)

logger = logging.getLogger(__name__)


class TestNamespacePattern(unittest.TestCase):
    def setUp(self):
        self.expect_success = [
            "ssvc",
            "cisa",
            "custom",  # not in enum, but valid for the pattern
            "abc",  # not in enum, but valid for the pattern
            "x_abc",  # valid namespace with x_ prefix
            "x_custom",  # valid namespace with x_ prefix
            "x_private-test",  # valid namespace with dash
            "x_custom.with.dots",  # valid namespace with x_ prefix and dots
            "x_custom//extension",  # double slash is okay when it's the first segment
            "x_private-test",  # valid namespace with x_ prefix and dash (does not follow reverse domain notation)
            "x_com.example//custom-extension",  # x_prefix, reverse domain notation, double slash, dashes
            "ssvc/de-DE/example.organization#reference-arch-1",  # valid BCP-47 tag, reverse domain notation, hash
            "ssvc//example.organization#model/com.example#foo",  # valid BCP-47 tag, two segments with one hash each
            "ssvc/de-DE/reference-arch-1",  # valid BCP-47 tag with dashes (But doesn't follow reverse domain notation)
            "x_example.test/pl-PL/foo/bar/baz/quux",  # valid BCP-47 tag and multiple segments
            "com.example",  # valid namespace with dots following reverse domain notation
            "x_com.example",  # valid namespace with x_ prefix and dots following reverse domain notation
            "au.com.example",  # valid namespace with dots following reverse domain notation for 2-letter TLD
            "x_au.com.example"  # valid namespace with x_ prefix and dots following reverse domain notation
            "abc//com.example",  # valid namespace with double slash
            "abc//com.au.example",
            "abc//com.example/foo.bar",  # valid namespace with double slash and additional segments
            "abc//com.example-foo.bar",  # valid namespace with double slash and dash
            "foo.bar//baz.quux",
        ]
        self.expect_fail = [
            "999",  # invalid namespace, numeric only
            "99xx",  # invalid namespace, numeric prefix
            "x__invalid",  # invalid namespace, double underscore
            "x_-invalid",  # invalid namespace, dash after x_
            "x_.invalid",  # invalid namespace, dash at end
            "x_/foo",  # invalid namespace, slash after x_, invalid BCP-47 tag
            "x_//foo",  # invalid namespace, double slash after x_
            "x_abc/invalid-bcp-47",  # not a valid BCP-47 tag
            "abc/invalid-bcp-47",  # not in enum (but that's ok for the pattern), not a valid BCP-47 tag
            "abc/invalid",  # not in enum (but that's ok for the pattern), not a valid BCP-47 tag
            "x_custom/extension",  # not a valid BCP-47 tag
            "x_example.test/not-bcp-47",  # not a valid BCP-47 tag
            "x_custom/extension/with/multiple/segments/"
            + "a" * 990,  # exceeds max length
            "ssvc/de-DE/example.organization##reference-arch-1",  # valid BCP-47 tag, reverse domain notation, double hash
            "ssvc/de-DE/example.organization#multi#hash#forbidden",  # valid BCP-47 tag, reverse domain notation, more than one hash per segment
            "x_custom.extension.",  # ends with punctuation
            "x_custom..extension",  # double dot
            "x_custom/",  # ends with slash
            "x_custom/extension//",  # double slash at end
            "x_custom/extension/with//double/slash",  # double slash in middle
            "x_custom/extension/with..double.dot",  # double dot in middle
            "x_custom/extension/with--double-dash",  # double dash in middle
            "ab",  # too short
            "x_",  # too short after prefix
            "x_x_some-weird-private-one",  # double x_ not allowed
            "x_example.test///org.example#fragment", # three slashes in a row (was an mistake in ABNF previously)
        ]

    def test_ns_pattern(self):

        self._test_successes_failures(
            NS_PATTERN.pattern, self.expect_fail, self.expect_success
        )

    def test_base_pattern(self):
        x_success = [
            "abc",
            "contains.dot",
            "contains-dash",
            "contains-dash-and.dot",
            "com.example",  # valid namespace with dots following reverse domain notation
            "au.com.example",  # valid namespace with dots following reverse domain notation
        ]
        x_fail = [
            "a",  # too short
            "9abc",  # starts with a number
            "x_foo",  # no x_ in base pattern
            "com.example#foo",  # no hashes in base
            "com.example##foo",  # double hash
            "com.example#foo#bar",  # multiple hashes not allowed
            "contains..double.dot",  # double dot
            "contains--double-dash",  # double dash
            "contains_underscore",  # underscore not allowed
            "contains/slash",  # slash not allowed
            ".starts.with.dot",  # starts with a dot
            "-starts-with-dash",  # starts with a dash
            "/starts-with-slash",  # starts with a slash
            "_starts-with-underscore",  # starts with an underscore
            "ends-with-dot.",  # ends with a dot
            "ends-with-dash-",  # ends with a dash
            "ends-with-slash/",  # ends with a slash
        ]
        self._test_successes_failures(BASE_PATTERN, x_fail, x_success)

    def test_experimental_base_pattern(self):
        x_success = [
            "x_abc",
            "x_custom",
            "x_custom.with.dots",  # dots are allowed in the base pattern
            "x_custom-with-dashes",  # dashes are allowed in the base pattern
        ]
        x_fail = [
            "9abc",  # does not start with x_
            "x__invalid",  # double underscore
            "x_-invalid",  # dash after x_
            "x_.invalid",  # dash at end
            "x_9abc",  # starts with a number after x_
            "x_abc.",  # ends with a dot
            "x_abc-",  # ends with a dash
            "x_abc/",  # ends with a slash
            "x_/foo",  # slashes aren't part of the base pattern
        ]
        self._test_successes_failures(BASE_NS_PATTERN, x_fail, x_success)

    def test_base_ns_pattern(self):
        x_success = [
            "abc",
            "x_abc",
            "x_custom",
            "x_custom.with.dots",  # dots are allowed in the base pattern
            "x_custom-with-dashes",  # dashes are allowed in the base pattern
        ]
        x_fail = [
            "9abc",  # starts with a number
            "x__invalid",  # double underscore
            "x_-invalid",  # dash after x_
            "x_.invalid",  # dash at end
            "x_9abc",  # starts with a number after x_
            "x_abc.",  # ends with a dot
            "x_abc-",  # ends with a dash
            "x_abc/",  # ends with a slash
            "x_/foo",  # slashes aren't part of the base pattern
        ]
        self._test_successes_failures(BASE_NS_PATTERN, x_fail, x_success)

    def _test_successes_failures(
        self, pattern: str, x_fail: list[str], x_success: list[str]
    ):
        successes = []
        failures = []
        # if pattern is not anchored, anchor it
        if not pattern.startswith("^"):
            pattern = "^" + pattern
        if not pattern.endswith("$"):
            pattern = pattern + "$"

        for ns in x_success:
            expected = f"Should match {ns}"
            if re.match(pattern, ns) is None:
                failures.append(expected)
            else:
                successes.append(expected)
        for ns in x_fail:
            expected = f"Should not match {ns}"
            if re.match(pattern, ns) is not None:
                failures.append(expected)
            else:
                successes.append(expected)
        logger.debug(f"Successes: {successes}")
        self.assertFalse(failures)

    def test_length_check_pattern(self):
        """
        Test the length check pattern for namespaces.
        The pattern should enforce a minimum and maximum length.
        """
        min_length = MIN_NS_LENGTH
        max_length = MAX_NS_LENGTH

        valid_ns = "x_valid_namespace"
        too_short_ns = "x_v"
        too_long_ns = "x_" + "a" * (max_length - 2)

        for i in range(0, MIN_NS_LENGTH):
            # should fail for lengths less than MIN_NS_LENGTH
            ns = "a" * i
            self.assertIsNone(
                re.match(LENGTH_CHECK_PATTERN, ns), f"Should not match: {ns}"
            )

    def test_ext_segment_pattern(self):
        """
        Test the extension segment pattern.
        The pattern should allow valid extension segments and disallow invalid ones.
        """
        valid_segments = [
            "valid",
            "valid.extension",
            "valid-extension",
            "valid#extension",
            "valid.extension#with-hash",
            "com.example#foo",  # valid namespace with hash
        ]
        invalid_segments = [
            "a_bc",  # underscore not allowed
            "invalid..segment",  # double dot
            "invalid--segment",  # double dash
            "invalid.segment.",  # ends with a dot
            "invalid.segment-",  # ends with a dash
            "invalid/segment",  # slash not allowed
            "com.example##foo",  # valid namespace with hash
            "invalid#segment#with#multiple#hashes",  # multiple hashes not allowed
            "invalid/segment/",  # ends with a slash
        ]
        self._test_successes_failures(
            EXT_SEGMENT_PATTERN, invalid_segments, valid_segments
        )


if __name__ == "__main__":
    unittest.main()
