#!/usr/bin/env python

import json


class Template:

    def __init__(self, json_file):
        self.from_address = None
        self.subject = None
        self.body = None

        Template.read(self, json_file)

    def read(self, json_file):
        with open(json_file, 'r') as f:
            template_json = json.load(f)

        self.from_address = template_json["from_address"]
        self.subject = template_json["subject"]
        self.body = template_json["body"]
