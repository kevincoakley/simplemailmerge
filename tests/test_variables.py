import csv
import unittest
from simplemailmerge.variables import Variables


class VariablesTestCase(unittest.TestCase):

    def setUp(self):
        self.blank_csv_file = "tests/csv/blank_csv_file.csv"
        self.invalid_csv_file = "tests/csv/invalid_csv_file.csv"
        self.no_header_csv_file = "tests/csv/no_header_csv_file.csv"
        self.no_email_header_csv_file = "tests/csv/no_email_header_csv_file.csv"
        self.missing_csv_file = "tests/csv/missing_csv_file.csv"
        self.only_header_csv_file = "tests/csv/only_header_csv_file.csv"
        self.valid_csv_file = "tests/csv/valid_csv_file.csv"

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
        self.assertRaises(IOError, Variables, self.missing_csv_file)

        try:
            self.assertIsInstance(Variables(self.valid_csv_file), Variables)
        except IOError:
            self.fail("valid_csv_file not found: %s" % self.valid_csv_file)

    # User specifies a valid csv file
    def test_valid_csv_format(self):
        self.assertRaises(csv.Error, Variables, self.blank_csv_file)
        self.assertRaises(csv.Error, Variables, self.invalid_csv_file)
        self.assertIsInstance(Variables(self.valid_csv_file), Variables)

    # The csv file has a header row
    def test_for_csv_header(self):
        self.assertRaisesRegexp(ValueError,
                                "CSV header not found",
                                Variables,
                                self.no_header_csv_file)
        self.assertIsInstance(Variables(self.valid_csv_file), Variables)

    # The csv file has at least one variable row
    def test_for_multiple_rows(self):
        self.assertRaisesRegexp(ValueError,
                                "CSV only contains the header",
                                Variables,
                                self.only_header_csv_file)
        self.assertIsInstance(Variables(self.valid_csv_file), Variables)

    # The csv file has at least one header column name email
    def test_for_email_column_in_header(self):
        self.assertRaisesRegexp(ValueError,
                                "CSV header does not contain \"email\" column",
                                Variables,
                                self.no_email_header_csv_file)
        self.assertIsInstance(Variables(self.valid_csv_file), Variables)

    # Verify Variables.list returns the expected values
    def test_for_list_output(self):
        self.assertListEqual(Variables(self.valid_csv_file).list, self.valid_csv_file_values)
