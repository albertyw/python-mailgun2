python-mailgun2
===============

|PyPI|

|Codeship Status for albertyw/python-mailgun2|
|Code Climate|
|Code Climate Test Coverage|
|Dependency Status|

Originally at https://github.com/ZeroCater/python-mailgun2

A super simple Python API for interacting with
`Mailgun <http://www.mailgun.com/>`__. Currently only supports sending
messages. Powered by
`Requests <http://docs.python-requests.org/en/latest/>`__.

Works with Python 3!

Installation
------------

.. code:: shell

    pip install mailgun2

Usage
-----

.. code:: python

    from mailgun2 import Mailgun
    mailer = Mailgun('example.mailgun.org', 'public_key', 'private_key')
    mailer.send_message(
        'from@yourdomain.com',
        ['to@you.com', 'others@you.com'],
        subject='Hi!',
        text='Sweet.'
        )

Required arguments:

::

    from_email: string of email address to set as sender
    to: list or string of email address to send to

Optional arguments:

::

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


Contributing
------------
See `Contributing <https://github.com/albertyw/python-mailgun2/blob/master/CONTRIBUTING.rst>`__

Pull requests welcome!



.. |PyPI| image:: https://img.shields.io/pypi/dm/mailgun2.svg
   :target: https://pypi.python.org/pypi?:action=display&name=mailgun2
.. |Codeship Status for albertyw/python-mailgun2| image:: https://codeship.com/projects/ce6c4f80-c4de-0133-efb5-62b97b21679d/status?branch=master
   :target: https://codeship.com/projects/138455
.. |Code Climate| image:: https://codeclimate.com/github/albertyw/python-mailgun2/badges/gpa.svg
   :target: https://codeclimate.com/github/albertyw/python-mailgun2
.. |Code Climate Test Coverage| image:: https://codeclimate.com/github/albertyw/python-mailgun2/badges/coverage.svg
   :target: https://codeclimate.com/github/albertyw/python-mailgun2/coverage
.. |Dependency Status| image:: https://gemnasium.com/albertyw/python-mailgun2.svg
   :target: https://gemnasium.com/albertyw/python-mailgun2
