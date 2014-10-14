
from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(
    name = 'xmlsquash',
    version = version,
    description = "XML 2 Dict converter",
    packages = find_packages( exclude = [ 'ez_setup'] ),
    include_package_data = True,
    zip_safe = False,
    author = 'Bence Faludi',
    author_email = 'b.faludi@mito.hu',
    license = 'GPL',
    install_requires = [],
    test_suite = "xmlsquash.tests",
    url = 'http://bfaludi.com'
)