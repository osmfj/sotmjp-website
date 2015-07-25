from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _

from symposion.proposals.models import ProposalBase


class Proposal(ProposalBase):

    recording_release = models.BooleanField(
        _("Recording Release"),
        default=True,
        help_text=_("By submitting your talk proposal, you agree to give "
                    "permission to the Organization Team to record, edit, "
                    "and release audio and/or video of your presentation. "
                    "If you do not agree to this, please uncheck this box.")
    )
    additional_requirements = models.TextField(
        _("Additional requirements"),
        blank=True,
        help_text=_("Please let us know if you have any specific needs"
                    "(A/V requirements, multiple microphones, a table, etc)."
                    "Note for example that 'audio out' is not provided"
                    "for your computer unless you tell us in advance.")
    )

    class Meta:
        abstract = True


class TalkProposal(Proposal):

    DURATION_CHOICES = [
        (0, _("No preference")),
        (1, _("10min")),
        (2, _("20min")),
    ]

    duration = models.IntegerField(choices=DURATION_CHOICES,
                                   verbose_name=_("Duration"))

    class Meta:
        verbose_name = _("Talk proposal")
        verbose_name_plural = _("Talk proposals")


class LightningTalkProposal(Proposal):

    class Meta:
        verbose_name = _("Lightning talk proposal")
        verbose_name_plural = _("Lightning talk proposals")


class PosterProposal(Proposal):
    class Meta:
        verbose_name = _("Poster proposal")
        verbose_name_plural = _("Poster proposals")


class OpenSpaceProposal(Proposal):
    class Meta:
        verbose_name = _("Open Space proposal")
        verbose_name_plural = _("Open Space proposals")
