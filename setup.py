#!/usr/bin/env python
from setuptools import setup
import mailgun2

try:
    readme = open("README.rst")
    long_description = str(readme.read())
finally:
    readme.close()

download_url = ("https://github.com/albertyw/python-mailgun2/"
                "archive/%s.tar.gz") % mailgun2.__version__

setup(
    name=mailgun2.__title__,
    packages=[mailgun2.__title__],
    version=mailgun2.__version__,
    description='A python client for Mailgun API v2',
    long_description=long_description,
    author=mailgun2.__author__,
    author_email='albertyw@mit.edu',
    url='https://github.com/albertyw/python-mailgun2',
    download_url=download_url,
    keywords=['mailgun', 'email'],
    install_requires=[
        'requests>=2.6',
    ],
    license='Apache',
    test_suite="tests",
    tests_require=[
        'mock>=0.8',
        'codeclimate-test-reporter',
        'tox>=2.3'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Communications :: Email',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ],
)
