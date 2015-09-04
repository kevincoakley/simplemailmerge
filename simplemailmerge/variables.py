#!/usr/bin/env python

import csv


class Variables:

    def __init__(self, csv_file):
        self.list = Variables.read(csv_file)

    @staticmethod
    def read(csv_file):

        with open(csv_file, 'r') as f:

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

            return csv_list
