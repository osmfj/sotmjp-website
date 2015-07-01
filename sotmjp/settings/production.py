# :coding=utf-8:

# Production settings
from .server import *  # NOQA

# From address for production
DEFAULT_FROM_EMAIL = "State of the Map JP 2014 <no-reply@stateofthemap.jp>"
SERVER_EMAIL = DEFAULT_FROM_EMAIL

LOGGING['filters']['static_fields']['fields']['environment'] = 'production'

ALLOWED_HOSTS = [
    'stateofthemap.jp',
]

LANGUAGE_CODE = "ja-jp"

import logging
logging.basicConfig(level=logging.DEBUG)
