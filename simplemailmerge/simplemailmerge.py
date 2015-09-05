#!/usr/bin/env python

from variables import Variables
from template import Template


class SimpleMailMerge:

    def __init__(self, csv_file, json_file):
        self.template = Template(json_file)
        self.variables = Variables(csv_file).list

    @staticmethod
    def merge(variables, body):

        for key, value in variables.iteritems():
            body = body.replace("%%%%%s%%%%" % key.upper(), value)

        return body
