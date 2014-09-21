from django import forms
from django.forms import Textarea

from markedit.widgets import MarkEdit

from sotmjp.tutorials.models import SotMTutorialMessage


class TutorialMessageForm(forms.ModelForm):
    class Meta:
        model = PyConTutorialMessage
        fields = [
            "message"
        ]
        widgets = {
            'message': MarkEdit(),
        }


class BulkEmailForm(forms.Form):
    subject = forms.CharField()
    body = forms.CharField(
        widget=Textarea(attrs={'class': 'fullwidth-textarea'})
    )
