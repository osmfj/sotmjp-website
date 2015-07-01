# HACK HACK - monkey patch User because the username field is useless
# when using django-user-accounts
from django.contrib.auth.models import User


def user_unicode(self):
    # Use full name if any, else email
    return self.get_full_name() or self.email
User.__unicode__ = user_unicode

# Also monkey patch the sort order
User._meta.ordering = ['last_name', 'first_name']
