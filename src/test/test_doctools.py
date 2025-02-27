#  Copyright (c) 2023-2025 Carnegie Mellon University and Contributors.
#  - see Contributors.md for a full list of Contributors
#  - see ContributionInstructions.md for information on how you can Contribute to this project
#  Stakeholder Specific Vulnerability Categorization (SSVC) is
#  licensed under a MIT (SEI)-style license, please see LICENSE.md distributed
#  with this Software or contact permission@sei.cmu.edu for full terms.
#  Created, in part, with funding and support from the United States Government
#  (see Acknowledgments file). This program may include and/or can make use of
#  certain third party source code, object code, documentation and other files
#  (“Third Party Software”). See LICENSE.md for more details.
#  Carnegie Mellon®, CERT® and CERT Coordination Center® are registered in the
#  U.S. Patent and Trademark Office by Carnegie Mellon University
import json
import logging
import os
import tempfile
import unittest

from ssvc.decision_points import SsvcDecisionPoint
from ssvc.doctools import (
    EnsureDirExists,
    _filename_friendly,
    dump_decision_point,
    dump_json,
    remove_if_exists,
)

_dp_dict = {
    "namespace": "ssvc",
    "version": "1.0.0",
    "key": "DPT",
    "name": "Decision Point Test",
    "description": "This is a test decision point.",
    "values": [
        {"key": "N", "name": "No", "description": "No means no"},
        {"key": "Y", "name": "Yes", "description": "Yes means yes"},
    ],
}


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.dp = SsvcDecisionPoint.model_validate(_dp_dict)

        # create a temp working dir
        self.tempdir = tempfile.TemporaryDirectory()

    def tearDown(self) -> None:
        # remove the temp working dir
        self.tempdir.cleanup()
        self.assertFalse(os.path.exists(self.tempdir.name))

    def test__filename_friendly(self):
        # replace spaces with underscores
        self.assertEqual("foo_bar", _filename_friendly("foo bar"))
        # replace periods with underscores
        self.assertEqual("foo_bar", _filename_friendly("foo.bar"))
        # lowercase the string
        self.assertEqual("foo_bar", _filename_friendly("Foo.Bar"))

    def test_ensure_dir_exists(self):
        path = os.path.join(self.tempdir.name, "foo")
        self.assertFalse(os.path.exists(path))

        with EnsureDirExists(path):
            self.assertTrue(os.path.exists(path))

    def test_remove_if_exists(self):
        path = os.path.join(self.tempdir.name, "foo")
        self.assertFalse(os.path.exists(path))

        # should work without error
        self.assertIsNone(remove_if_exists(path))

        # create the file
        open(path, "w").close()
        self.assertTrue(os.path.exists(path))

        # should work without error
        self.assertIsNone(remove_if_exists(path))

        # should have removed the file
        self.assertFalse(os.path.exists(path))

    def test_dump_decision_point(self):
        jsondir = os.path.join(self.tempdir.name, "json")
        dp = self.dp
        overwrite = False

        # should create the files in the expected places
        self.assertFalse(os.path.exists(jsondir))
        self.assertEqual(0, len(os.listdir(self.tempdir.name)))

        r = dump_decision_point(jsondir, dp, overwrite)

        self.assertTrue(os.path.exists(jsondir))
        self.assertIn("json", os.listdir(self.tempdir.name))
        self.assertEqual(1, len(os.listdir(jsondir)))

        file_created = os.listdir(jsondir)[0]

        for word in dp.name.split():
            self.assertIn(word.lower(), file_created)

        # not checking these thoroughly, just making sure they are there
        # because they are tested elsewhere in dump_markdown and dump_json

    def test_dump_json(self):
        basename = "foo"
        dp = self.dp
        jsondir = self.tempdir.name
        overwrite = False

        _jsonfile = os.path.join(jsondir, f"{basename}.json")
        self.assertFalse(os.path.exists(_jsonfile))

        # should create the file in the expected place
        json_file = dump_json(basename, dp, jsondir, overwrite)
        self.assertEqual(_jsonfile, json_file)
        self.assertTrue(os.path.exists(json_file))

        # file is loadable json
        d = json.load(open(json_file))
        for k, v in dp.model_dump().items():
            self.assertEqual(v, d[k])

        # should not overwrite the file
        overwrite = False
        # capture logger output
        with self.assertLogs() as cm:
            json_file = dump_json(basename, dp, jsondir, overwrite)
        self.assertEqual(_jsonfile, json_file)
        # logger warns that the file exists
        self.assertIn("already exists", cm.output[0])

        # should overwrite the file
        overwrite = True

        dp.name = "Different Decision Point"
        # capture logger output
        with self.assertLogs(level=logging.DEBUG) as cm:
            json_file = dump_json(basename, dp, jsondir, overwrite)

        self.assertEqual(_jsonfile, json_file)
        # logger warns that the file was removed
        self.assertIn("Removed", cm.output[0])

        # the file was overwritten
        d = json.load(open(json_file))
        self.assertEqual(dp.name, d["name"])

    def test_main(self):
        pass


if __name__ == "__main__":
    unittest.main()
