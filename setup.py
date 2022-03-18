#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from codecs import open
from os import path
from typing import Dict


# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

about: Dict[str, str] = {}
with open(path.join(here, 'mailgun2', '__version__.py')) as f:
    exec(f.read(), about)


setup(
    name='mailgun2',
    packages=find_packages(exclude=['tests']),
    version=about['__version__'],
    description='A python client for Mailgun API v2',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Albert Wang',
    author_email='git@albertyw.com',
    url='https://github.com/albertyw/python-mailgun2',
    keywords=['mailgun', 'email'],
    install_requires=[
        'requests>=2.6,<3.0',
    ],
    license='Apache',
    test_suite="mailgun2.tests",
    # testing requires flake8 and coverage but they're listed separately
    # because they need to wrap setup.py
    extras_require={
        'dev': [],
        'test': [],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Communications :: Email',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ],
)
