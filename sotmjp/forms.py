from django import forms
from django.utils.translation import ugettext_lazy as _

from markedit.widgets import MarkEdit

from symposion.proposals.models import ProposalBase


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
        model = ProposalBase
        fields = [
            "title",
            "description",
            "abstract",
        ]
        widgets = {
            "title": forms.TextInput(attrs={'class': 'fullwidth-input'}),
            "description": forms.Textarea(attrs={'rows': '3'}),
            "abstract": MarkEdit(),
        }


class LightningTalkProposalForm(ProposalForm):

    class Meta:
        model = ProposalBase
        fields = [
            "title",
        ]
        widgets = {
            "title": forms.TextInput(attrs={'class': 'fullwidth-input'}),
        }


class PosterProposalForm(ProposalForm):

    def __init__(self, *args, **kwargs):
        super(PosterProposalForm, self).__init__(*args, **kwargs)
        self.fields['additional_requirement'].widget = forms.HiddenInput()

    class Meta:
        model = ProposalBase
        fields = [
            "title",
            "description",
            "abstract",
        ]
        widgets = {
            "title": forms.TextInput(attrs={'class': 'fullwidth-input'}),
            "description": forms.Textarea(attrs={'rows': '3'}),
            "abstract": MarkEdit(),
        }


class OpenSpaceProposalForm(ProposalForm):

    class Meta:
        model = ProposalBase
        fields = [
            "title",
            "description",
        ]
        widgets = {
            "title": forms.TextInput(attrs={'class': 'fullwidth-input'}),
            "description": forms.Textarea(attrs={'rows': '3'}),
        }
