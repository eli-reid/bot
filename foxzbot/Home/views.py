from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.apps import apps
from .models import Settings
class HomeView(LoginRequiredMixin, TemplateView):
    template_name: str = 'home/home.html'
    login_url = '/login'

class LoginInterfaceView(LoginView):
    template_name: str = 'home/login.html'
    

class LogoutInterfaceView(LogoutView):
    template_name: str = 'home/home.html'

class SettingsView(LoginRequiredMixin, TemplateView):
    template_name = "home/settings.html"
    model = Settings
    
  
   
    
        