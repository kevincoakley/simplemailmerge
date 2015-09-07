import vars
import unittest
from simplemailmerge.simplemailmerge import SimpleMailMerge


class MergeTestCase(unittest.TestCase):
    def setUp(self):
        self.test_csv_files = vars.test_csv_files
        self.test_json_files = vars.test_json_files
        self.input_body = "Hi %%FIRST_NAME%%\n\nI have a link to share with you: %%LINK%%\n\nKevin"
        self.variables = {"email": "kcoakley@sdsc.edu",
                          "first_name": "Kevin",
                          "link": "http://www.google.com"}
        self.output_body = "Hi Kevin\n\nI have a link to share with you: " \
                           "http://www.google.com\n\nKevin"

    # The values from the csv file are successfully merged with the json template
    def test_csv_values_merged_with_template(self):
        simplemailmerge = SimpleMailMerge(self.test_csv_files["valid_csv_file"],
                                          self.test_json_files["valid_json_file"])
        self.assertEqual(simplemailmerge.merge(self.variables, self.input_body), self.output_body)
