#:coding=utf-8:

from pycon.settings.base import *  # NOQA

INSTALLED_APPS.append('sotmjp')
INSTALLED_APPS.append('sotmjp.account')
INSTALLED_APPS.append('restcms')
INSTALLED_APPS.remove('symposion.cms')

ROOT_URLCONF = 'sotmjp.urls'

TIME_ZONE = 'Asia/Tokyo'

LANGUAGES = (
    ('en', 'English'),
    ('ja', 'Japanese'),
)

BIBLION_SECTIONS = [
    ("ja", u"Japanese/日本語"),
    ("en", u"English/英語"),
]

# Add config for Google Analytics
CONSTANCE_CONFIG["GOOGLE_ANALYTICS_TRACKING_ID"] = ("", "The site's Google Analytics Tracking ID.")

PROPOSAL_FORMS['talk'] = 'sotmjp.forms.SotMJPTalkProposalForm'
TEMPLATE_DIRS.insert(0, os.path.join(PROJECT_ROOT, "sotmjp/templates"))

ACCOUNT_DELETION_EXPUNGE_CALLBACK = 'sotmjp.account.callbacks.account_delete_expunge'
