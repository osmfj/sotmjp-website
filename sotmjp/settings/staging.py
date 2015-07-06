# :coding=utf-8:

# Staging settings
from .server import *  # NOQA

# From address for staging - use our development list
DEFAULT_FROM_EMAIL = 'team@stateofthemap.jp'
SERVER_EMAIL = DEFAULT_FROM_EMAIL

LOGGING['filters']['static_fields']['fields']['environment'] = 'staging'

ALLOWED_HOSTS = [
    'stateofthemap.jp',
    'staging.stateofthemap.jp',
]
