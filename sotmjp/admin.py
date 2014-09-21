from django import forms
from django.contrib import admin

from markedit.admin import MarkEditAdmin

from sotmjp.models import (SotMProposalCategory, SotMSponsorTutorialProposal,
                          SotMTalkProposal, SotMTutorialProposal,
                          SotMPosterProposal, SotMLightningTalkProposal,
                          SotMOpenSpaceProposal)


class ProposalMarkEditAdmin(MarkEditAdmin):
    class MarkEdit:
        fields = ['abstract', 'additional_notes', 'outline', 'more_info']
        options = {
            'preview': 'below'
        }


class TalkAdmin(ProposalMarkEditAdmin):
    list_display = [
        'title',
        'kind',
        'status',
        'duration',
        'submitted',
        'speaker',
        'category',
        'audience_level',
        'cancelled',
    ]


class TutorialAdmin(ProposalMarkEditAdmin):
    list_display = [
        'title',
        'kind',
        'status',
        'submitted',
        'speaker',
        'category',
        'audience_level',
        'domain_level',
        'cancelled',
    ]
    readonly_fields = ['cte_tutorial_id', 'registrants', 'max_attendees']


class LightningTalkAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(LightningTalkAdminForm, self).__init__(*args, **kwargs)
        # TODO: This is a hack to populate the field...
        self.fields['category'].initial = SotMProposalCategory.objects.all()[0]
        self.fields['audience_level'].initial = SotMLightningTalkProposal.AUDIENCE_LEVEL_NOVICE

    class Meta:
        model = SotMLightningTalkProposal
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
        'kind',
        'status',
        'submitted',
        'speaker',
        'cancelled',
    ]


class PosterAdmin(ProposalMarkEditAdmin):
    list_display = [
        'title',
        'kind',
        'status',
        'submitted',
        'speaker',
        'category',
        'audience_level',
        'cancelled',
    ]


class OpenSpaceAdmin(ProposalMarkEditAdmin):
    list_display = [
        'title',
        'kind',
        'status',
        'submitted',
        'speaker',
        'cancelled'
    ]


class SponsorTutorialAdmin(ProposalMarkEditAdmin):
    list_display = [
        'title',
        'kind',
        'status',
        'submitted',
        'speaker',
        'cancelled',
    ]


admin.site.register(SotMProposalCategory)
admin.site.register(SotMTalkProposal, TalkAdmin)
admin.site.register(SotMTutorialProposal, TutorialAdmin)
admin.site.register(SotMPosterProposal, PosterAdmin)
admin.site.register(SotMOpenSpaceProposal, OpenSpaceAdmin)
admin.site.register(SotMSponsorTutorialProposal, SponsorTutorialAdmin)
admin.site.register(SotMLightningTalkProposal, LightningTalkAdmin)


# HACK HACK - monkey patch User because the username field is useless
# when using django-user-accounts
from django.contrib.auth.models import User


def user_unicode(self):
    # Use full name if any, else email
    return self.get_full_name() or self.email
User.__unicode__ = user_unicode

# Also monkey patch the sort order
User._meta.ordering = ['last_name', 'first_name']
