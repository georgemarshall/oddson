from django import forms
from django.utils.translation import ugettext_lazy as _

class AttemptForm(forms.Form):
    """(AttemptForm description)"""
    number = forms.IntegerField(label=_('number'))
