#!/usr/bin/env python

import json


class Template:

    def __init__(self, json_file):
        self.json_file = json_file
        self.from_address = None
        self.subject = None
        self.body = None

    def read(self):
        with open(self.json_file, 'r') as f:
            template_json = json.load(f)

        self.from_address = template_json["from_address"]
        self.subject = template_json["subject"]
        self.body = template_json["body"]
