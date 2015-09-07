#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
    extra = dict(install_requires=[
    ],
        include_package_data=True,
        test_suite="tests.suite.load_tests",
    )
except ImportError:
    from distutils.core import setup
    extra = {}


def readme():
    with open("README.rst") as f:
        return f.read()


setup(name="simplemailmerge",
      version="1.0.0",
      description="Simple mail merge using CSV and JSON",
      long_description=readme(),
      author="Kevin Coakley",
      author_email="kcoakley@sdsc.edu",
      scripts=[
          "bin/simplemailmerge",
      ],
      url="",
      packages=[
          "simplemailmerge",
      ],
      platforms="Posix; MacOS X",
      classifiers=[
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
      ],
      **extra
      )
