#!/usr/bin/env python

import json


class Template:

    def __init__(self, json_file):
        self.json_file = json_file
        self.smtp_server = None
        self.smtp_port = None
        self.smtp_username = None
        self.smtp_password = None
        self.from_address = None
        self.subject = None
        self.body = None

    def read(self):
        with open(self.json_file, 'r') as f:
            template_json = json.load(f)

        self.smtp_server = template_json["smtp_server"]
        self.smtp_port = template_json["smtp_port"]
        self.smtp_username = template_json["smtp_username"]
        self.smtp_password = template_json["smtp_password"]
        self.from_address = template_json["from_address"]
        self.subject = template_json["subject"]
        self.body = template_json["body"]
