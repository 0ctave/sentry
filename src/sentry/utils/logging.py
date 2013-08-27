"""
sentry.utils.logging
~~~~~~~~~~~~~~~~~

:copyright: (c) 2010-2013 by the Sentry Team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""
from __future__ import absolute_import, print_function

import logging

from functools import wraps


def log_exceptions(func=None):
    cm = WithoutRavenManager()
    if not func:
        return cm

    @wraps(func)
    def wrapped(*args, **kwargs):
        with cm:
            return func(*args, **kwargs)
    return wrapped


class WithoutRavenManager(object):
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if all([exc_type, exc_value, exc_traceback]):
            logger = logging.getLogger('sentry.errors')
            logger.exception(unicode(exc_value))
        return True