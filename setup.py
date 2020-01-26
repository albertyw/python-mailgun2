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
    author_email='git@albertyw.com',
    url='https://github.com/albertyw/python-mailgun2',
    download_url=download_url,
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
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Communications :: Email',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ],
)
