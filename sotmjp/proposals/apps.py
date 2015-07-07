from __future__ import unicode_literals
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ProposalsConfig(AppConfig):
    name = "proposals"
    verbose_name = _("Proposals")
    label = "proposals"
