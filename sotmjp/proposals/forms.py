from django import forms
from django.utils.translation import ugettext_lazy as _

from markedit.widgets import MarkEdit

from .models import (ProposalCategory, TalkProposal,
                     PosterProposal, LightningTalkProposal,
                     OpenSpaceProposal)


class ProposalForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProposalForm, self).__init__(*args, **kwargs)
        queryset = ProposalCategory.objects.order_by("name")
        self.fields["category"].queryset = queryset

    def clean_description(self):
        value = self.cleaned_data["description"]
        if len(value) > 400:
            raise forms.ValidationError(
                _(u"The description must be less than 400 characters")
            )
        return value


class TalkProposalForm(ProposalForm):

    class Meta:
        model = TalkProposal
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


class LightningTalkProposalForm(ProposalForm):

    def __init__(self, *args, **kwargs):
        super(LightningTalkProposalForm, self).__init__(*args, **kwargs)
        self.fields['audience_level'].widget = forms.HiddenInput()
        initial_level = LightningTalkProposal.AUDIENCE_LEVEL_NOVICE
        self.fields['audience_level'].initial = initial_level

    class Meta:
        model = LightningTalkProposal
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


class PosterProposalForm(ProposalForm):

    class Meta:
        model = PosterProposal
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


class OpenSpaceProposalForm(ProposalForm):

    class Meta:
        model = OpenSpaceProposal
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
        super(ProposalForm, self).__init__(*args, **kwargs)
        self.fields['audience_level'].widget = forms.HiddenInput()
        initial_level = LightningTalkProposal.AUDIENCE_LEVEL_NOVICE
        self.fields['audience_level'].initial = initial_level

    def clean_description(self):
        value = self.cleaned_data["description"]
        return value
