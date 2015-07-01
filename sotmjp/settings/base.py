# -*- coding: utf-8 -*-
#:coding=utf-8:
# base settings - imported by other settings files, then overridden

import os.path
import posixpath

from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

def env_or_default(NAME, default):
    return os.environ.get(NAME, default)


# Top level of our source / repository
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                            os.pardir, os.pardir))
DEBUG = False
TEMPLATE_DEBUG = DEBUG

# tells Pinax to serve media through the staticfiles app.
SERVE_MEDIA = DEBUG

# django-compressor is turned off by default due to deployment overhead for
# most users. See <URL> for more information
COMPRESS = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env_or_default("DB_NAME", "sotmjp2015"),
        "USER": env_or_default("DB_USER", ""),
        "PASSWORD": env_or_default("DB_PASSWORD", ""),
        "HOST": env_or_default("DB_HOST", ""),
        "PORT": env_or_default("DB_PORT", ""),
    }
}

INTERNAL_IPS = [
    "127.0.0.1",
]

ADMINS = [
    # ("Your Name", "your_email@domain.com"),
]

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.

TIME_ZONE = 'Asia/Tokyo'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "ja-jp"

SITE_ID = 1

# Conference ID and any URL prefixes
CONFERENCE_ID = 2
CONFERENCE_URL_PREFIXES = {
    1: "2014",
    2: "2015",
}


# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

gettext = lambda s: s

LANGUAGES = (
    ('en', gettext('English')),
    ('fr', gettext('French')),
    ('ja', gettext('Japanese')),
)

LOCALE_PATHS = [os.path.join(PROJECT_ROOT, "locale")]

# Absolute path to the directory that holds media - this is files uploaded
# by users, such as attachments.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = env_or_default("MEDIA_ROOT", os.path.join(PROJECT_ROOT, "site_media", "media"))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = "/%s/site_media/media/" % CONFERENCE_URL_PREFIXES[CONFERENCE_ID]

# Absolute path to the directory where static files will be gathered
# at deploy time and served from in production.  Should NOT be
# in version control, or contain anything before deploying.
STATIC_ROOT = os.path.join(PROJECT_ROOT, "site_media", "static")

# URL that handles the static files like app media.
# Example: "http://media.lawrence.com"
STATIC_URL = "/%s/site_media/static/" % CONFERENCE_URL_PREFIXES[CONFERENCE_ID]

# Additional directories which hold static files
STATICFILES_DIRS = []

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
]

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = posixpath.join(STATIC_URL, "admin/")

# Subdirectory of COMPRESS_ROOT to store the cached media files in
COMPRESS_OUTPUT_DIR = "cache"

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
]

MIDDLEWARE_CLASSES = [
    "djangosecure.middleware.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    # LocaleMiddleware must follow session middleware, auth middleware,
    # and and cache middleware, and precede commonmiddleware
    "django.middleware.locale.LocaleMiddleware",
    "account.middleware.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    #"django_openid.consumer.SessionConsumer",
    "django.contrib.messages.middleware.MessageMiddleware",
    "reversion.middleware.RevisionMiddleware",
    #"social_auth.middleware.SocialAuthExceptionMiddleware",
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'sotmjp.urls'

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, "sotmjp/templates"),
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "pinax_theme_bootstrap.context_processors.theme",
    #"social_auth.context_processors.social_auth_backends",
    #"pinax_utils.context_processors.settings",
    "account.context_processors.account",
    "symposion.reviews.context_processors.reviews",
    "constance.context_processors.config",
]


INSTALLED_APPS = [
    # Admin UI (WARN: should placed before django.contrib.admin/sites/auth)
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',

    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",

    # theme
    "pinax_theme_bootstrap",
    "django_forms_bootstrap",

    # external
    "account",
    "compressor",
    "mailer",
    "timezones",
    "metron",
    "easy_thumbnails",
    "sitetree",
    "taggit",
    "reversion",
    "pinax.blog",
    #"social_auth",
    "djangosecure",
    "raven.contrib.django",
    "constance",
    "constance.backends.database",
    #"redis_cache",
    "uni_form",
    "gunicorn",
    "selectable",

    # symposion
    "symposion.conference",
    #"symposion.cms", # use restcms
    "symposion.boxes",
    "symposion.speakers",
    "symposion.proposals",
    "symposion.reviews",
    "symposion.teams",
    "symposion.schedule",
    "symposion.sponsorship",

    # custom
    "markedit",
    "sotmjp",
    "restcms",
    "sotmjp.registration",
    "sotmjp.profile",
    "leaflet",
    "osm_field",
]

FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

# for debug
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# for production
#EMAIL_BACKEND = "mailer.backend.DbBackend"
EMAIL_HOST          = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = 'tester@@abcd'
EMAIL_HOST_USER     = 'tester.abcd@gmail.com'
EMAIL_PORT          = 587
EMAIL_USE_TLS       = True

ACCOUNT_OPEN_SIGNUP = True
ACCOUNT_USE_OPENID = False
ACCOUNT_REQUIRED_EMAIL = False
ACCOUNT_EMAIL_VERIFICATION = False
ACCOUNT_EMAIL_AUTHENTICATION = False
ACCOUNT_UNIQUE_EMAIL = EMAIL_CONFIRMATION_UNIQUE_EMAIL = False
ACCOUNT_CREATE_ON_SAVE = True
ACCOUNT_EMAIL_CONFIRMATION_EMAIL = False

ACCOUNT_DELETION_EXPUNGE_CALLBACK = 'sotmjp.account.callbacks.account_delete_expunge'

TWITTER_CONSUMER_KEY         = ''
TWITTER_CONSUMER_SECRET      = ''
FACEBOOK_APP_ID              = ''
FACEBOOK_API_SECRET          = ''
GOOGLE_CONSUMER_KEY          = ''
GOOGLE_CONSUMER_SECRET       = ''
GOOGLE_OAUTH2_CLIENT_ID      = ''
GOOGLE_OAUTH2_CLIENT_SECRET  = ''

AUTHENTICATION_BACKENDS = [
    # Permissions backends
    "symposion.teams.backends.TeamPermissionsBackend",

    # Social Auth Backends
    #'social_auth.backends.twitter.TwitterBackend',
    #'social_auth.backends.facebook.FacebookBackend',
    #'social_auth.backends.google.GoogleOAuth2Backend',
    #'social_auth.backends.google.GoogleBackend',
    #'social_auth.backends.contrib.linkedin.LinkedinBackend',
    #'social_auth.backends.contrib.github.GithubBackend',
    #'social_auth.backends.OpenIDBackend',

    # Django User Accounts
    "account.auth_backends.EmailAuthenticationBackend",
    'django.contrib.auth.backends.ModelBackend',
]

#SOCIAL_AUTH_PIPELINE = [
#    "social_auth.backends.pipeline.social.social_auth_user",
#    "social_auth.backends.pipeline.user.get_username",
#    "symposion.social_auth.pipeline.user.create_user",
#    "social_auth.backends.pipeline.social.associate_user",
#    "social_auth.backends.pipeline.social.load_extra_data",
#    "social_auth.backends.pipeline.user.update_user_details",
#]

LOGIN_URL = reverse_lazy("account_login")

ACCOUNT_SIGNUP_REDIRECT_URL = "dashboard"
ACCOUNT_LOGIN_REDIRECT_URL = "dashboard"
ACCOUNT_LOGOUT_REDIRECT_URL = "home"
ACCOUNT_USER_DISPLAY = lambda user: user.get_full_name()
LOGIN_ERROR_URL = reverse_lazy("account_login")

# Need these to be reversed urls, currently breaks if using reverse_lazy
#SOCIAL_AUTH_LOGIN_REDIRECT_URL = "/%s/dashboard/"% CONFERENCE_URL_PREFIXES[CONFERENCE_ID]
#SOCIAL_AUTH_NEW_USER_REDIRECT_URL = "/%s/dashboard/"% CONFERENCE_URL_PREFIXES[CONFERENCE_ID]

#SOCIAL_AUTH_ASSOCIATE_BY_MAIL = False

# Don't clobber User.email if someone associates a social account that
# happens to have a different email address
# http://django-social-auth.readthedocs.org/en/latest/configuration.html#miscellaneous-settings
#SOCIAL_AUTH_PROTECTED_USER_FIELDS = ['email',]

EMAIL_CONFIRMATION_DAYS = 2
EMAIL_DEBUG = DEBUG
DEFAULT_FROM_EMAIL = "SotM JP committee <no-reply@stateofthemap.jp>"

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}

CONSTANCE_BACKEND = "constance.backends.database.DatabaseBackend"
CONSTANCE_CONFIG = {
    # "SETTING_NAME": (default_value, "help text")
    "REGISTRATION_URL": ("", _("URL for registration")),
    "SPONSOR_FROM_EMAIL": ("", _("From address for emails to sponsors")),
    "REGISTRATION_STATUS": ("", _("Used in the home page template. Valid values are 'soon', 'open', 'closed' and 'over'")),
    "PROPOSAL_NAME_MAX_LENGTH": (100, _("Maximum length for proposal title")),
    "PROPOSAL_DURATION_CHOICE_COUNT": (2, _("Number of duration choices for talk")),
    "PROPOSAL_DURAION_CHOICE_1": ("I prefer a 15 minute slot", _("Duration choice 1 for talk proposal")),
    "PROPOSAL_DURAION_CHOICE_2": ("I prefer a 20 minute slot", _("Duration choice 2 for talk proposal")),
    "CONFERENCE_NAME": ("State of the Map Japan 2015", _("Conference name (long)")),
    "CONFERENCE_NAME_SHORT": ("SotM JP 15", _("Conference name (short)")),
    "CONFERENCE_LOCALITY": ("Hamamatsu", _("Conference locality place")),
    "CONFERENCE_COUNTRY": ("Japan", _("Conference locality country")),
    "CONFERENCE_START_DATE": ("2015-10-31", _("Conference start date")),
    "CONFERENCE_END_DATE": ("2015-10-31", _("Conference end date")),
    "CONFERENCE_DURATION": ("2015-10-31 ~ 31", _("Conference duration")),
    "CONFERENCE_DAYS": (1, _("How much days for conference(day number)?")),
    "HAVE_TUTORIAL": ("No", _("Conference has tutorial program?(Yes/No)")),
    "TUTORIAL_NAME": ("", _("Tutorial program name")),
    "TUTORIAL_START_DATE": ("", _("Tutorial start date")),
    "TUTORIAL_END_DATE": ("", _("Tutorial end date")),
    "TUTORIAL_DURATION": ("", _("Tutorail duration")),
    "HAVE_HACKATHON": ("No", _("Conference has hackathon program?(Yes/No)")),
    "HACKATHON_NAME": ("", _("Hackathon program name")),
    "HACKATHON_START_DATE": ("", _("Hackathon start date")),
    "HACKATHON_END_DATE": ("", _("Hackathon end date")),
    "HACKATHON_DURATION": ("", _("Hackathon duration")),
}

SYMPOSION_PAGE_REGEX = r"(([\w-]{1,})(/[\w-]{1,})*)/$"

PROPOSAL_FORMS = {
    "talk": "sotmjp.proposals.forms.TalkProposalForm",
    "poster": "sotmjp.proposals.forms.PosterProposalForm",
    "lightning-talk": "sotmjp.proposals.forms.LightningTalkProposalForm",
    "open-space": "sotmjp.proposals.forms.OpenSpaceProposalForm",
}


USE_X_ACCEL_REDIRECT = False

MARKEDIT_DEFAULT_SETTINGS = {
    'preview': 'below',
    'toolbar': {
        'backgroundMode': 'dark',
    }
}

COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Is somebody clobbering this?  We shouldn't have to set it ourselves,
# but if we don't, gunicorn's django_wsgi blows up trying to configure
# logging with an empty dictionary.
from django.utils.log import DEFAULT_LOGGING
LOGGING = DEFAULT_LOGGING

# Add config for Google Analytics
CONSTANCE_CONFIG["GOOGLE_ANALYTICS_TRACKING_ID"] = ("", "The site's Google Analytics Tracking ID.")

# Add config for leaflet
LEAFLET_CONFIG = {
  'TILES': 'http://tile.openstreetmap.jp/{z}/{x}/{y}.png',
  'SPATIAL_EXTENT': (139.665, 35.655, 139.75, 35.6698),
  'DEFAULT_CENTER': (35.662, 139.67771),
  'DEFAULT_ZOOM': 17,
  'MIN_ZOOM': 15,
  'MAX_ZOOM': 19,
}
