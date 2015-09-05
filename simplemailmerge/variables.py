#!/usr/bin/env python

import csv


class Variables:

    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.list = None

    def read(self):

        with open(self.csv_file, 'r') as f:

            dialect = csv.Sniffer().sniff(f.read())
            f.seek(0)

            if not csv.Sniffer().has_header(f.read()):
                raise ValueError("CSV header not found")
            f.seek(0)

            reader = csv.reader(f, dialect)

            csv_list = list(reader)

            if len(csv_list) < 2:
                raise ValueError("CSV only contains the header")

            if "email" not in csv_list[0]:
                raise ValueError("CSV header does not contain \"email\" column")

            csv_list_of_dict = []

            for row in csv_list:
                # Skip the csv header
                if row != csv_list[0]:
                    dict_row = dict()

                    for column_index, value in enumerate(row):
                        dict_row.update({csv_list[0][column_index]: value})

                    csv_list_of_dict.append(dict_row)

            self.list = csv_list_of_dict
