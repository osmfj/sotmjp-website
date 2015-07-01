from django import forms
from django.utils.translation import ugettext_lazy as _

from markedit.widgets import MarkEdit

from .models import (SotMProposalCategory, SotMTalkProposal,
                     SotMTutorialProposal, SotMPosterProposal,
                     SotMLightningTalkProposal, SotMSponsorTutorialProposal,
                     SotMOpenSpaceProposal)


class SotMProposalForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SotMProposalForm, self).__init__(*args, **kwargs)
        self.fields["category"].queryset = SotMProposalCategory.objects.order_by("name")

    def clean_description(self):
        value = self.cleaned_data["description"]
        if len(value) > 400:
            raise forms.ValidationError(
                _(u"The description must be less than 400 characters")
            )
        return value


class SotMTalkProposalForm(SotMProposalForm):

    class Meta:
        model = SotMTalkProposal
        fields = [
            "title",
            "category",
            "language",
            "duration",
            "description",
            "audience",
            "audience_level",
            "perceived_value",
            "abstract",
            "outline",
            "additional_notes",
            "additional_requirements",
            "recording_release",
        ]
        widgets = {
            "title": forms.TextInput(attrs={'class': 'fullwidth-input'}),
            "description": forms.Textarea(attrs={'rows': '3'}),
            "audience": forms.TextInput(attrs={'class': 'fullwidth-input'}),
            "perceived_value": forms.Textarea(attrs={'rows': '3'}),
            "abstract": MarkEdit(),
            "outline": MarkEdit(),
            "additional_notes": MarkEdit(attrs={'rows': '3'}),
            "additional_requirements": forms.Textarea(attrs={'rows': '3'}),
        }


class SotMLightningTalkProposalForm(SotMProposalForm):

    def __init__(self, *args, **kwargs):
        super(SotMLightningTalkProposalForm, self).__init__(*args, **kwargs)
        self.fields['audience_level'].widget = forms.HiddenInput()
        self.fields['audience_level'].initial = SotMLightningTalkProposal.AUDIENCE_LEVEL_NOVICE

    class Meta:
        model = SotMLightningTalkProposal
        fields = [
            "title",
            "category",
            "description",
            "additional_notes",
            "additional_requirements",
            "audience_level",
            "recording_release",
        ]
        widgets = {
            "title": forms.TextInput(attrs={'class': 'fullwidth-input'}),
            "description": forms.Textarea(attrs={'rows': '3'}),
            "additional_notes": MarkEdit(attrs={'rows': '3'}),
            "additional_requirements": forms.Textarea(attrs={'rows': '3'}),
        }


#class SotMTutorialProposalForm(SotMProposalForm):
#
#    class Meta:
#        model = SotMTutorialProposal
#        fields = [
#            "title",
#            "category",
#            "audience_level",
#            "domain_level",
#            "description",
#            "audience",
#            "perceived_value",
#            "abstract",
#            "outline",
#            "more_info",
#            "additional_notes",
#            "additional_requirements",
#            "handout",
#            "recording_release",
#        ]
#        widgets = {
#            "title": forms.TextInput(attrs={'class': 'fullwidth-input'}),
#            "description": forms.Textarea(attrs={'rows': '3'}),
#            "audience": forms.TextInput(attrs={'class': 'fullwidth-input'}),
#            "perceived_value": forms.Textarea(attrs={'rows': '3'}),
#            "abstract": MarkEdit(),
#            "outline": MarkEdit(),
#            "more_info": MarkEdit(),
#            "additional_notes": MarkEdit(attrs={'rows': '3'}),
#            "additional_requirements": forms.Textarea(attrs={'rows': '3'}),
#        }
#

class SotMPosterProposalForm(SotMProposalForm):

    class Meta:
        model = SotMPosterProposal
        fields = [
            "title",
            "category",
            "audience_level",
            "description",
            "abstract",
            "additional_notes",
            "additional_requirements",
            "recording_release",
        ]
        widgets = {
            "title": forms.TextInput(attrs={'class': 'fullwidth-input'}),
            "description": forms.Textarea(attrs={'rows': '3'}),
            "abstract": MarkEdit(),
            "additional_notes": MarkEdit(attrs={'rows': '3'}),
            "additional_requirements": forms.Textarea(attrs={'rows': '3'}),
        }


class SotMOpenSpaceProposalForm(SotMProposalForm):

    class Meta:
        model = SotMOpenSpaceProposal
        fields = [
            "title",
            "description",
            "additional_notes",
            "additional_requirements",
            "audience_level",
            "category",
        ]
        widgets = {
            "title": forms.TextInput(attrs={'class': 'fullwidth-input'}),
            "description": forms.Textarea(attrs={'rows': '3'}),
            "additional_notes": MarkEdit(attrs={'rows': '3'}),
            "additional_requirements": forms.Textarea(attrs={'rows': '3'}),
        }

    def __init__(self, *args, **kwargs):
        super(SotMProposalForm, self).__init__(*args, **kwargs)
        self.fields['audience_level'].widget = forms.HiddenInput()
        self.fields['audience_level'].initial = SotMLightningTalkProposal.AUDIENCE_LEVEL_NOVICE

    def clean_description(self):
        value = self.cleaned_data["description"]
        return value


class SotMSponsorTutorialForm(SotMProposalForm):

    class Meta:
        model = SotMSponsorTutorialProposal
        fields = [
            "title",
            "description",
            "abstract",
            "additional_notes",
        ]
        widgets = {
            "title": forms.TextInput(attrs={'class': 'fullwidth-input'}),
            "description": forms.Textarea(attrs={'rows': '3'}),
            "abstract": MarkEdit(),
            "additional_notes": MarkEdit(attrs={'rows': '3'}),
        }



