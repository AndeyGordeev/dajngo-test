from django import forms

from . import models


class ThoughtForm(forms.ModelForm):
    class Meta:
        fields = ('conditions', 'notes')
        model = models.Thought
