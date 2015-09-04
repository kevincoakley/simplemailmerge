import unittest
from simplemailmerge.template import Template


class TemplateTestCase(unittest.TestCase):
    def setUp(self):
        self.blank_json_file = "tests/json/blank_json_file.json"
        self.invalid_json_file = "tests/json/invalid_json_file.json"
        self.missing_json_file = "tests/json/missing_json_file.json"
        self.valid_json_file = "tests/json/valid_json_file.json"

    # User specifies json file that exists
    def test_json_file_exists(self):
        self.assertRaises(IOError, Template, self.missing_json_file)

        try:
            self.assertIsInstance(Template(self.valid_json_file), Template)
        except IOError:
            self.fail("valid_csv_file not found: %s" % self.valid_json_file)

    # User specifies a valid json file
    def test_valid_json_format(self):
        self.assertRaises(ValueError, Template, self.blank_json_file)
        self.assertRaises(ValueError, Template, self.invalid_json_file)
        self.assertIsInstance(Template(self.valid_json_file), Template)

    # The json file has variables: from, subject, body

    # The values from the csv file are successfully merged with the json template
