# python-mailgun2

[![PyPI](https://img.shields.io/pypi/v/mailgun2)](https://pypi.org/project/mailgun2/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mailgun2)
![PyPI - License](https://img.shields.io/pypi/l/mailgun2)

[![Build Status](https://drone.albertyw.com/api/badges/albertyw/python-mailgun2/status.svg)](https://drone.albertyw.com/albertyw/python-mailgun2)
[![Dependency Status](https://pyup.io/repos/github/albertyw/python-mailgun2/shield.svg)](https://pyup.io/repos/github/albertyw/python-mailgun2/)
[![Code Climate](https://codeclimate.com/github/albertyw/python-mailgun2/badges/gpa.svg)](https://codeclimate.com/github/albertyw/python-mailgun2)
[![Test Coverage](https://codeclimate.com/github/albertyw/python-mailgun2/badges/coverage.svg)](https://codeclimate.com/github/albertyw/python-mailgun2/coverage)

Originally at <https://github.com/ZeroCater/python-mailgun2>

A super simple Python API for interacting with [Mailgun](https://www.mailgun.com/). Currently
only supports sending messages. Powered by [Requests](https://docs.python-requests.org/en/latest/).

## Installation

```shell
pip install mailgun2
```

## Usage

```python
from mailgun2 import Mailgun
mailer = Mailgun('example.mailgun.org', 'public_key', 'private_key')
mailer.send_message(
    'from@yourdomain.com',
    ['to@you.com', 'others@you.com'],
    subject='Hi!',
    text='Sweet.'
    )
```

Required arguments:

```
from_email: string of email address to set as sender
to: list or string of email address to send to
```

Optional arguments:

```
subject: string subject of the email
text: string body of the email. Either text or html is required.
html: string HTML of the email. Either text or html is required.
cc: list of cc addresses.
bcc: list of bcc addresses.
tags: list of mailgun tags to associate with the email.
reply_to: Convenience argument for setting the Reply-To header
headers: Extra headers for messages
inlines: List of file paths to attach inline to the message
attachments: List of (file name, content type, file handle) as a multipart attachment
```

## Contributing

See [Contributing](https://github.com/albertyw/python-mailgun2/blob/master/CONTRIBUTING.md)

Pull requests welcome!
