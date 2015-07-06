from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Profile(models.Model):

    user = models.OneToOneField(User, related_name="profile",
                                verbose_name=_("User"))
    first_name = models.CharField(max_length=50, blank=True, null=True,
                                  verbose_name=_("First name"))
    last_name = models.CharField(max_length=50, blank=True, null=True,
                                 verbose_name=_("Last name"))
    phone = models.CharField(max_length=20, blank=True, null=True,
                             verbose_name=_("Phone"))
    first_name_ja = models.CharField(max_length=50, blank=True, null=True,
                                     verbose_name=_("First name (Japanese)"))
    last_name_ja = models.CharField(max_length=50, blank=True, null=True,
                                    verbose_name=_("Last name (Japanese)"))

    @property
    def is_complete(self):
        for key in self._meta.get_all_field_names():
            if key != "phone" and not getattr(self, key):
                return False
        return True

    @property
    def display_name(self):
        return " ".join([self.first_name, self.last_name])

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")
