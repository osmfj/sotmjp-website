from django import forms
from django.utils.translation import ugettext_lazy as _

from markedit.widgets import MarkEdit

from .models import (TalkProposal,
                     PosterProposal, LightningTalkProposal,
                     OpenSpaceProposal)


class ProposalForm(forms.ModelForm):

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
            "duration",
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


class LightningTalkProposalForm(ProposalForm):

    class Meta:
        model = LightningTalkProposal
        fields = [
            "title",
            "additional_notes",
            "recording_release",
        ]
        widgets = {
            "title": forms.TextInput(attrs={'class': 'fullwidth-input'}),
            "additional_notes": MarkEdit(attrs={'rows': '3'}),
        }


class PosterProposalForm(ProposalForm):

    def __init__(self, *args, **kwargs):
        super(LightningTalkProposalForm, self).__init__(*args, **kwargs)
        self.fields['additional_requirement'].widget = forms.HiddenInput()

    class Meta:
        model = PosterProposal
        fields = [
            "title",
            "description",
            "abstract",
            "additional_notes",
            "recording_release",
        ]
        widgets = {
            "title": forms.TextInput(attrs={'class': 'fullwidth-input'}),
            "description": forms.Textarea(attrs={'rows': '3'}),
            "abstract": MarkEdit(),
            "additional_notes": MarkEdit(attrs={'rows': '3'}),
        }


class OpenSpaceProposalForm(ProposalForm):

    class Meta:
        model = OpenSpaceProposal
        fields = [
            "title",
            "description",
            "additional_notes",
        ]
        widgets = {
            "title": forms.TextInput(attrs={'class': 'fullwidth-input'}),
            "description": forms.Textarea(attrs={'rows': '3'}),
            "additional_notes": MarkEdit(attrs={'rows': '3'}),
        }
