
from setuptools import setup, find_packages
import sys, os

version = '0.1.0'

setup(
    name = 'XML2Dict',
    version = version,
    description = "XML 2 Dict converter",
    packages = find_packages( exclude = [ 'ez_setup'] ),
    include_package_data = True,
    zip_safe = False,
    author = 'Bence Faludi',
    author_email = 'hello@bfaludi.com',
    license = 'GPL',
    install_requires = [],
    test_suite = "xml2dict.tests",
    url = 'http://bfaludi.com'
)