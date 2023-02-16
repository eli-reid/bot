from typing import Any
from django.shortcuts import render
from django import http
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.apps import apps

class StreamTimerSettingsView(LoginRequiredMixin, ListView):
    template_name = "streamtimer/index.html"
    settings = apps.get_app_config('Home').get_model('Settings')
    model = settings
    context_object_name = "streamtimer"

class StreamTimerView(ListView):
    template_name="streamtimer/streamtimer.html"
    settings = apps.get_app_config('Home').get_model('Settings')
    model = settings
    context_object_name = "streamtimer"

    def get(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:
        if kwargs["key"] != "edog":
            raise http.Http404()
        return super().get(request, *args, **kwargs)


  
