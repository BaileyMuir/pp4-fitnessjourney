from .models import JournalComment
from django import forms


class JournalCommentForm(forms.ModelForm):
    class Meta:
        model = JournalComment
        fields = ('message_body',)
