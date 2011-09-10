# -*- coding: utf-8 -*-

"""
redirector.core
~~~~~~~~~~~~~~~

This module provides the core redirector experience.

The redirection destination is configured with the REDIRECTOR_LOCATION
environment variable.
"""

import os

from werkzeug.wrappers import Request
from werkzeug.utils import redirect

DEFAULT = 'https://github.com/kennethreitz/redirector'


# ------
# Routes
# ------

def get_destination():
    """Gets configured redirection location."""

    return os.environ.get('REDIRECTOR_LOCATION', DEFAULT)


@Request.application
def application(request):
    return redirect(get_destination())


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 4000, application)