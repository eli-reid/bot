from django.shortcuts import render
from TCI.middleware import tci
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.apps import apps

class StreamTimerSettingsView(LoginRequiredMixin,ListView):
    template_name = "streamtimer/index.html"
    settings = apps.get_app_config('Home').get_model('Settings')
    model = settings
    context_object_name = "streamtimer"

class StreamTimerView(ListView):
    template_name="streamtimer/streamTimer.html"
    settings = apps.get_app_config('Home').get_model('Settings')
    model = settings
    context_object_name = "streamtimer"
