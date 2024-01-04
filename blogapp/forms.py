from django import forms

from .models import comment


class CommentForms(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['text']
