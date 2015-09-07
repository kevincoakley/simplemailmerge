#!/usr/bin/env python

import csv
import smtplib
from email.mime.text import MIMEText

from variables import Variables
from template import Template


class SimpleMailMerge:

    def __init__(self, csv_file, json_file):
        self.csv_file = csv_file
        self.json_file = json_file

    def email(self):
        try:
            variables = Variables(self.csv_file)
            variables.read()
        except IOError:
            raise SystemExit("%s not found" % self.csv_file)
        except csv.Error, e:
            raise SystemExit(e.message)
        except ValueError, e:
            raise SystemExit(e.message)

        try:
            template = Template(self.json_file)
            template.read()
        except IOError:
            raise SystemExit("%s not found" % self.json_file)
        except ValueError, e:
            raise SystemExit(e.message)
        except KeyError, e:
            raise SystemExit("Missing template key: %s" % e.message)

        for row in variables.list:
            merged_body = SimpleMailMerge.merge(row, template.body)
            try:
                SimpleMailMerge.send_email(template.from_address,
                                           row["email"],
                                           template.subject,
                                           merged_body,
                                           template.smtp_server,
                                           template.smtp_port,
                                           template.smtp_username,
                                           template.smtp_password)
            except smtplib.SMTPAuthenticationError, e:
                raise SystemExit("Invalid SMTP Username or Password")

    @staticmethod
    def merge(variables, body):

        for key, value in variables.iteritems():
            body = body.replace("%%%%%s%%%%" % key.upper(), value)

        return body

    @staticmethod
    def send_email(from_address, to_address, subject, body, smtp_server, smtp_port, smtp_username,
                   smtp_password):
        # Create the message
        msg = MIMEText(body)
        msg['To'] = to_address
        msg['From'] = from_address
        msg['Subject'] = subject

        # Send the mail
        server = smtplib.SMTP("%s:%s" % (smtp_server, smtp_port), timeout=5)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(from_address, to_address, msg.as_string())
        server.quit()
