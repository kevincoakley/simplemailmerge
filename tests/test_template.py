import unittest
from simplemailmerge.template import Template


class TemplateTestCase(unittest.TestCase):
    def setUp(self):
        self.bad_property_json_file = "tests/json/bad_property_json_file.json"
        self.blank_json_file = "tests/json/blank_json_file.json"
        self.invalid_json_file = "tests/json/invalid_json_file.json"
        self.missing_json_file = "tests/json/missing_json_file.json"
        self.missing_property_json_file = "tests/json/missing_property_json_file.json"
        self.valid_json_file = "tests/json/valid_json_file.json"

        self.json_template_properties = ["body", "from_address", "subject"]
        self.json_values = {"from_address": "kcoakley@sdsc.edu",
                            "subject": "I have a link for you!",
                            "body": "Hi %%FIRST_NAME%%\n\nI have a link to share with you: "
                                    "%%LINK%%\n\nKevin"}

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

    # The json file has properties: from, subject, body
    def test_json_file_has_correct_properties(self):
        self.assertRaises(KeyError, Template, self.bad_property_json_file)
        self.assertRaises(ValueError, Template, self.missing_property_json_file)

        template = Template(self.valid_json_file)

        self.assertListEqual(template.__dict__.keys(), self.json_template_properties)

        for json_template_property in self.json_template_properties:
            self.assertIsNotNone(template.__dict__[json_template_property])

    # Verify the Template object has the correct values for the properties
    def test_for_correct_values(self):
        template = Template(self.valid_json_file)

        for key, value in self.json_values.iteritems():
            self.assertEqual(template.__dict__[key], value)
