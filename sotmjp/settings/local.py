# :coding=utf-8:

# ローカル開発用の settings.py
# この設定はデフォルトで sqlite を使います。
# DB バックエンドは DB_ENGINE の環境変数で設定できます。
# 例: DB_ENGINE=postgresql_psycopg2 python manage.py runserver

# 設定できる環境変数
# DEBUG
# DB_ENGINE
# DB_NAME
# DB_HOST
# DB_PORT
# DB_USER
# DB_PASSWORD

from .dev import *  # NOQA


def env_var(var, var_type=None, *args, **kwargs):
    u"""
    環境変数の値を返す

    例: env_var("HOGE_SETTING", int, default=123)
    """
    try:
        val = os.environ[var]
    except KeyError:
        if not args and 'default' not in kwargs:
            raise ImproperlyConfigured(
                'The environment variable "%s" is required.' % var)
        elif args:
            val = args[0]
        else:
            val = kwargs['default']

    if var_type:
        try:
            val = var_type(val)
        except ValueError, e:
            raise ImproperlyConfigured(
                'Invalid setting for "%s": "%s"' % (var, e))

    return val

DEBUG = env_var('DEBUG', bool, default=True)

_db_engine = env_var('DB_ENGINE',
                     default='sqlite3' if DEBUG else 'postgresql_psycopg2')
if _db_engine == 'sqlite3':
    _basedir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    _db_name = os.path.join(_basedir, 'sotmjp2015.sqlite')
else:
    _db_name = 'sotmjp2015_staging'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.%s' % _db_engine,
        'NAME': env_var('DB_NAME', default=_db_name),
        'USER': env_var('DB_USER', default=''),
        'PASSWORD': env_var('DB_PASSWORD', default=''),
        'HOST': env_var('DB_HOST', default=''),
        'PORT': env_var('DB_PORT', default=''),
    }
}

LANGUAGE_CODE = "ja-jp"

INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE_CLASSES += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
