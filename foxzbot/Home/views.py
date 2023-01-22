from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.apps import apps
from .models import Settings
from .forms import SettingsForm
from django.views.generic.edit import DeleteView
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

class SettingsCreationView(LoginRequiredMixin, CreateView):
    template_name = f"{PATH_PREFIX}/add.html"
    model = MODEL
    success_url = SUCCESS_URL
    form_class = FORM_CLASS
   
class SettingsUpdateView(LoginRequiredMixin, UpdateView):
    template_name: str = f"{PATH_PREFIX}/edit.html"
    model = MODEL
    success_url = SUCCESS_URL
    form_class = FORM_CLASS
   
class SettingsDetailView(LoginRequiredMixin, DetailView):
    template_name = f"{PATH_PREFIX}/details.html"
    model = MODEL
    context_object_name = CONTEXT_OBJECT
    
class SettingsDeleteView(LoginRequiredMixin, DeleteView):
    template_name = f"{PATH_PREFIX}/delete.html"
    model = MODEL
    context_object_name = CONTEXT_OBJECT
    success_url= SUCCESS_URL       