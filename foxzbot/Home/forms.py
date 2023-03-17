from dataclasses import fields
from django import forms
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError
from .models import Settings
class SettingsForm(forms.ModelForm):
    
    class Meta:
        model = Settings
        fields = ('__all__')

settingsFormset = forms.modelformset_factory(Settings, SettingsForm, extra=0)
    