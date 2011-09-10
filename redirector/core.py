# -*- coding: utf-8 -*-

"""
redirector.core
~~~~~~~~~~~~~~~

This module provides the core redirector experience.

The redirection destination is configured with the REDIRECTOR_LOCATION
environment variable.
"""

import os

from flask import Flask, redirect


DEFAULT = 'https://github.com/kennethreitz/redirector'

app = Flask(__name__)


# ------
# Routes
# ------

def get_destination():
    """Gets configured redirection location."""

    return os.environ.get('REDIRECTOR_LOCATION', DEFAULT)


@app.errorhandler(404)
def redirect_to_destination(args):
    """Redirects to destination."""

    return redirect(get_destination())


if __name__ == '__main__':
    app.run()
