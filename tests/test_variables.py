import csv
import vars
import unittest
from simplemailmerge.variables import Variables


class VariablesTestCase(unittest.TestCase):

    def setUp(self):
        self.test_csv_files = vars.test_csv_files
        self.valid_csv_file_values = [{"email": "kcoakley@sdsc.edu",
                                       "first_name": "Kevin",
                                       "link": "http://www.google.com"},
                                      {"email": "kcoakley@ucsd.edu",
                                       "first_name": "Nivek",
                                       "link": "http://www.github.com"},
                                      {"email": "kcoakley@eng.ucsd.edu",
                                       "first_name": "KEVIN",
                                       "link": "http://www.python.org"}]

    # User specifies csv file that exists
    def test_csv_file_exists(self):
        with self.assertRaises(IOError):
            missing_variables = Variables(self.test_csv_files["missing_csv_file"])
            missing_variables.read()

        try:
            valid_variables = Variables(self.test_csv_files["valid_csv_file"])
            valid_variables.read()
        except IOError:
            self.fail("valid_csv_file not found: %s" % self.test_csv_files["valid_csv_file"])

    # User specifies a valid csv file
    def test_valid_csv_format(self):
        with self.assertRaises(csv.Error):
            blank_variables = Variables(self.test_csv_files["blank_csv_file"])
            blank_variables.read()

        with self.assertRaises(csv.Error):
            invalid_variables = Variables(self.test_csv_files["invalid_csv_file"])
            invalid_variables.read()

        try:
            valid_variables = Variables(self.test_csv_files["valid_csv_file"])
            valid_variables.read()
        except csv.Error:
            self.fail("valid_csv_file is invalid format")

    # The csv file has a header row
    def test_for_csv_header(self):
        with self.assertRaisesRegexp(ValueError, "CSV header not found"):
            no_header_variables = Variables(self.test_csv_files["no_header_csv_file"])
            no_header_variables.read()

        try:
            valid_variables = Variables(self.test_csv_files["valid_csv_file"])
            valid_variables.read()
        except ValueError as e:
            if e.message == "CSV header not found":
                self.fail("valid_csv_file does not have a header")
            else:
                self.fail("Unknown Value error")

    # The csv file has at least one variable row
    def test_for_multiple_rows(self):
        with self.assertRaisesRegexp(ValueError, "CSV only contains the header"):
            only_header_variables = Variables(self.test_csv_files["only_header_csv_file"])
            only_header_variables.read()

        try:
            valid_variables = Variables(self.test_csv_files["valid_csv_file"])
            valid_variables.read()
        except ValueError as e:
            if e.message == "CSV only contains the header":
                self.fail("valid_csv_file only contains the header")
            else:
                self.fail("Unknown Value error")

    # The csv file has at least one header column name email
    def test_for_email_column_in_header(self):
        with self.assertRaisesRegexp(ValueError, "CSV header does not contain \"email\" column"):
            no_email_header_variables = Variables(self.test_csv_files["no_email_header_csv_file"])
            no_email_header_variables.read()

        try:
            valid_variables = Variables(self.test_csv_files["valid_csv_file"])
            valid_variables.read()
        except ValueError as e:
            if e.message == "CSV header does not contain \"email\" column":
                self.fail("valid_csv_file header does not contain email")
            else:
                self.fail("Unknown Value error")

    # Verify Variables.list returns the expected values
    def test_for_list_output(self):
        valid_variables = Variables(self.test_csv_files["valid_csv_file"])
        valid_variables.read()

        self.assertListEqual(valid_variables.list, self.valid_csv_file_values)
