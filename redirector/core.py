# -*- coding: utf-8 -*-

"""
redirector.core
~~~~~~~~~~~~~~~

This module provides the core redirector experience.

The redirection destination is configured with the REDIRECTOR_LOCATION
environment variable.
"""

import os

from werkzeug.wsgi import responder
from werkzeug.utils import redirect

DEFAULT = 'https://github.com/kennethreitz/redirector'


# ------
# Routes
# ------

def get_destination():
    """Gets configured redirection location."""

    return os.environ.get('REDIRECTOR_LOCATION', DEFAULT)


@responder
def app(*args):
    return redirect(get_destination())


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 4000, app)