###############
simplemailmerge
###############

************
Installation
************

Install via pip:

::

    $ pip install git+https://github.com/kevincoakley/simplemailmerge.git

Install from source:

::

    $ git clone https://github.com/kevincoakley/simplemailmerge.git
    $ cd UCSD_BigData_Scripts
    $ python setup.py install

*******
Removal
*******

Remove via pip:

::

    $ pip uninstall simplemailmerge -y

****************
Example Template
****************

* Use %%COLUMN_NAME%% for the column names that will be merged from the variables CSV file.

::

    {
      "smtp_server": "smtp.server.com",
      "smtp_port": "587",
      "smtp_username": "username",
      "smtp_password": "password",
      "from_address": "from@email.com",
      "subject": "This is my subject",
      "body": "Use the variables CSV file to replace %%COLUMN_ONE%% and %%COLUMN_TWO%%\n\nKevin"
    }


*****************
Example Variables
*****************

* The first line is the header.
* One header column must be name email.
* Column names will replace %%COLUMN_NAME%% in the body section of the template JSON file.

::

    email,column_one,column_two
    one@emailaddress.com,var_one_one,var_two_one
    two@emailaddress.com,var_one_two,var_two_two
    three@emailaddress.com,var_one_three,var_two_three
