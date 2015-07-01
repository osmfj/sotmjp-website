# :coding=utf-8:

# Staging settings
from .server import *  # NOQA

# From address for staging - use our development list
DEFAULT_FROM_EMAIL = 'sotmjp2014@stateofthemap.jp'
SERVER_EMAIL = DEFAULT_FROM_EMAIL

LOGGING['filters']['static_fields']['fields']['environment'] = 'staging'

ALLOWED_HOSTS = [
    'staging-sotm.openstreetmap.jp',
]
