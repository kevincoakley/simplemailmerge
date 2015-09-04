#!/usr/bin/env python

import json


class Template:

    def __init__(self, json_file):
        self.json = Template.read(json_file)

    @staticmethod
    def read(json_file):
        with open(json_file, 'r') as f:
            template_json = json.load(f)

        return None
