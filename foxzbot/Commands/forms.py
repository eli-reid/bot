from dataclasses import fields
from django import forms
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError
from .models import Command

class CommandForm(forms.ModelForm):
    
    class Meta:
        model = Command
        fields = ('__all__')
    
    