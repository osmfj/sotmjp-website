from django import forms
from django.contrib import admin

from markedit.admin import MarkEditAdmin

from .models import (TalkProposal,
                     PosterProposal, LightningTalkProposal,
                     OpenSpaceProposal)


class ProposalMarkEditAdmin(MarkEditAdmin):
    class MarkEdit:
        fields = ['abstract', 'additional_notes', 'outline', 'more_info']
        options = {
            'preview': 'below'
        }


class TalkAdmin(ProposalMarkEditAdmin):
    list_display = [
        'title',
        'duration',
        'submitted',
        'speaker',
        'cancelled',
    ]


class LightningTalkAdminForm(forms.ModelForm):

    class Meta:
        model = LightningTalkProposal
        exclude = ['abstract']


class LightningTalkAdmin(MarkEditAdmin):
    class MarkEdit:
        fields = ['additional_notes']
        options = {
            'preview': 'below'
        }

    form = LightningTalkAdminForm
    list_display = [
        'title',
        'submitted',
        'speaker',
        'cancelled',
    ]


class PosterAdmin(ProposalMarkEditAdmin):
    list_display = [
        'title',
        'submitted',
        'speaker',
        'cancelled',
    ]


class OpenSpaceAdmin(ProposalMarkEditAdmin):
    list_display = [
        'title',
        'submitted',
        'speaker',
        'cancelled'
    ]


admin.site.register(TalkProposal, TalkAdmin)
admin.site.register(PosterProposal, PosterAdmin)
admin.site.register(OpenSpaceProposal, OpenSpaceAdmin)
admin.site.register(LightningTalkProposal, LightningTalkAdmin)
