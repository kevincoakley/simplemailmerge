import vars
import unittest
from simplemailmerge.template import Template


class TemplateTestCase(unittest.TestCase):
    def setUp(self):
        self.test_json_files = vars.test_json_files
        self.json_template_properties = ["body", "from_address", "subject"]
        self.json_values = {"from_address": "kcoakley@sdsc.edu",
                            "subject": "I have a link for you!",
                            "body": "Hi %%FIRST_NAME%%\n\nI have a link to share with you: "
                                    "%%LINK%%\n\nKevin"}

    # User specifies json file that exists
    def test_json_file_exists(self):
        with self.assertRaises(IOError):
            missing_template = Template(self.test_json_files["missing_json_file"])
            missing_template.read()

        try:
            valid_template = Template(self.test_json_files["valid_json_file"])
            valid_template.read()
        except IOError:
            self.fail("valid_json_file not found: %s" % self.test_json_files["valid_json_file"])

    # User specifies a valid json file
    def test_valid_json_format(self):
        with self.assertRaises(ValueError):
            blank_template = Template(self.test_json_files["blank_json_file"])
            blank_template.read()

        with self.assertRaises(ValueError):
            invalid_template = Template(self.test_json_files["invalid_json_file"])
            invalid_template.read()

        try:
            valid_template = Template(self.test_json_files["valid_json_file"])
            valid_template.read()
        except ValueError:
            self.fail("valid_json_file not valid JSON")

    # The json file has properties: from, subject, body
    def test_json_file_has_correct_properties(self):
        with self.assertRaises(KeyError):
            bad_property_template = Template(self.test_json_files["bad_property_json_file"])
            bad_property_template.read()

        with self.assertRaises(ValueError):
            missing_property_template = Template(self.test_json_files["missing_property_json_file"])
            missing_property_template.read()

        valid_template = Template(self.test_json_files["valid_json_file"])
        valid_template.read()

        for json_template_property in self.json_template_properties:
            self.assertIsNotNone(valid_template.__dict__[json_template_property])

    # Verify the Template object has the correct values for the properties
    def test_for_correct_values(self):
        valid_template = Template(self.test_json_files["valid_json_file"])
        valid_template.read()

        for key, value in self.json_values.iteritems():
            self.assertEqual(valid_template.__dict__[key], value)
