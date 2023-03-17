from typing import Any
from django.forms import formset_factory, modelformset_factory
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, ListView, UpdateView, TemplateView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.apps import apps
from .models import Settings
from .forms import SettingsForm, settingsFormset
from django.views.generic.edit import DeleteView
from django.db import transaction
class HomeView(LoginRequiredMixin, TemplateView):
    template_name: str = 'home/home.html'
    login_url = '/login'

class LoginInterfaceView(LoginView):
    template_name: str = 'home/login.html'
    

class LogoutInterfaceView(LogoutView):
    template_name: str = 'home/home.html'    
  

SUCCESS_URL = '/settings'
CONTEXT_OBJECT = "settings"
FORM_CLASS = SettingsForm
MODEL = Settings
PATH_PREFIX ="settings"

class SettingsListView(LoginRequiredMixin, ListView):
    model = MODEL
    context_object_name = CONTEXT_OBJECT
    template_name: str = f"{PATH_PREFIX}/index.html"
    login_url = '/login'

class SettingsCreationView(LoginRequiredMixin, ListView):
    template_name = f"{PATH_PREFIX}/add.html"
    model = MODEL
    success_url = SUCCESS_URL
    form_class = FORM_CLASS
   
class SettingsUpdateView(LoginRequiredMixin, UpdateView):
    template_name: str = f"{PATH_PREFIX}/edit_form_snip.html"
    model = MODEL
    success_url = SUCCESS_URL
    form_class = FORM_CLASS
    pk=0
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = settingsFormset
        return context
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        err=None
        formset = settingsFormset(self.request.POST, queryset=MODEL.objects.all())
        if formset.is_valid():
            formset.save(commit=False)
            for form in formset:
                if form.is_valid:
                    form.save()
                else:
                    err = form.errors   
       

        return super().post(request, errors=err, *args, **kwargs)
   


   
class SettingsDetailView(LoginRequiredMixin, DetailView):
    template_name = f"{PATH_PREFIX}/details.html"
    model = MODEL
    context_object_name = CONTEXT_OBJECT
    
class SettingsDeleteView(LoginRequiredMixin, DeleteView):
    template_name = f"{PATH_PREFIX}/delete.html"
    model = MODEL
    context_object_name = CONTEXT_OBJECT
    success_url= SUCCESS_URL       