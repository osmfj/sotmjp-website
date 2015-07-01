from django import forms
from django.contrib import admin

from markedit.admin import MarkEditAdmin

from .models import (ProposalCategory, SponsorTutorialProposal,
                     TalkProposal, TutorialProposal,
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
        initial_category = ProposalCategory.objects.all()[0]
        initial_level = LightningTalkProposal.AUDIENCE_LEVEL_NOVICE
        self.fields['category'].initial = initial_category
        self.fields['audience_level'].initial = initial_level

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


admin.site.register(ProposalCategory)
admin.site.register(TalkProposal, TalkAdmin)
admin.site.register(TutorialProposal, TutorialAdmin)
admin.site.register(PosterProposal, PosterAdmin)
admin.site.register(OpenSpaceProposal, OpenSpaceAdmin)
admin.site.register(SponsorTutorialProposal, SponsorTutorialAdmin)
admin.site.register(LightningTalkProposal, LightningTalkAdmin)
