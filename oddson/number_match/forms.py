from django import forms


class AttemptForm(forms.Form):
    """(AttemptForm description)"""
    number = forms.IntegerField()
