from dataclasses import fields
from django import forms
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError
from .models import Quotes
class QuoteForm(forms.ModelForm):
    
    class Meta:
        model = Quotes
        fields = ('__all__')
    
    