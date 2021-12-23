from .models import BlogComment
from django import forms


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ('message',)