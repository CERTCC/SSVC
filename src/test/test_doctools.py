#  Copyright (c) 2023-2025 Carnegie Mellon University.
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
import json
import logging
import os
import tempfile
import unittest

from ssvc.decision_points.base import DecisionPoint
from ssvc.doctools import (
    EnsureDirExists,
    dump_decision_point,
    dump_json,
    filename_friendly as _filename_friendly,
    remove_if_exists,
)

_dp_dict = {
    "namespace": "ssvc",
    "version": "1.0.0",
    "key": "DPT",
    "name": "Decision Point Test",
    "definition": "This is a test decision point.",
    "values": (
        {"key": "N", "name": "No", "definition": "No means no"},
        {"key": "Y", "name": "Yes", "definition": "Yes means yes"},
    ),
}


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.dp = DecisionPoint.model_validate(_dp_dict)

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

        nsdir = os.path.join(jsondir, dp.namespace)
        self.assertTrue(os.path.exists(nsdir))
        self.assertEqual(1, len(os.listdir(nsdir)))

        file_created = os.listdir(nsdir)[0]

        for word in dp.name.split():
            self.assertIn(word.lower(), file_created)

        # not checking these thoroughly, just making sure they are there
        # because they are tested elsewhere in dump_markdown and dump_json

    def test_dump_json(self):
        basename = "foo"
        dp = self.dp
        jsondir = self.tempdir.name
        overwrite = False
        nsdir = os.path.join(jsondir, dp.namespace)

        _jsonfile = os.path.join(nsdir, f"{basename}.json")
        self.assertFalse(os.path.exists(_jsonfile))

        # should create the file in the expected place
        json_file = dump_json(basename, dp, jsondir, overwrite)

        self.assertEqual(_jsonfile, json_file)
        self.assertTrue(os.path.exists(json_file))

        # file is loadable json
        d = json.load(open(json_file))
        for k, v in dp.model_dump().items():
            # on reload, the tuples are lists, but they should be the same
            reloaded_value = d[k]
            if isinstance(reloaded_value, list):
                reloaded_value = tuple(reloaded_value)

            self.assertEqual(v, reloaded_value)

        # should not overwrite the file
        overwrite = False
        # capture logger output
        with self.assertLogs() as cm:
            json_file = dump_json(basename, dp, jsondir, overwrite)
            self.assertEqual(_jsonfile, json_file)
            # logger warns that the file exists
            found = False
            for line in cm.output:
                if not "WARNING" in line:
                    continue
                # it's a warning log
                if "already exists" in line:
                    found = True
                    break
            self.assertTrue(
                found, "Expected warning about existing file not found"
            )

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

    def test_dump_schema(self):
        schemafile = os.path.join(self.tempdir.name, "dummy_schema.json")
        self.assertFalse(os.path.exists(schemafile))
        from ssvc.doctools import dump_schema
        from pydantic import BaseModel

        class Dummy(BaseModel):
            name: str = "Name"
            description: str = "Description"

        dump_schema(filepath=schemafile, schema=Dummy.model_json_schema())
        self.assertTrue(os.path.exists(schemafile))

        # file is loadable json
        d = json.load(open(schemafile))
        self.assertIn("title", d)
        self.assertEqual("Dummy", d["title"])
        self.assertIn("type", d)
        self.assertEqual(d["type"], "object")


if __name__ == "__main__":
    unittest.main()
