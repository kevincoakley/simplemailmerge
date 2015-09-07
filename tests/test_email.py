import vars
import unittest
import smtplib
from simplemailmerge.simplemailmerge import SimpleMailMerge


class EmailTestCase(unittest.TestCase):
    def setUp(self):
        self.test_csv_files = vars.test_csv_files
        self.test_json_files = vars.test_json_files

    # The values from the csv file are successfully merged with the json template
    def test_send_email(self):

        for key in self.test_csv_files.iterkeys():
            with self.assertRaises(SystemExit):
                simplemailmerge = SimpleMailMerge(self.test_csv_files[key],
                                                  self.test_json_files["valid_json_file"])
                simplemailmerge.email()

        for key in self.test_json_files.iterkeys():
            with self.assertRaises(SystemExit):
                simplemailmerge = SimpleMailMerge(self.test_csv_files["valid_csv_file"],
                                                  self.test_json_files[key])
                simplemailmerge.email()
