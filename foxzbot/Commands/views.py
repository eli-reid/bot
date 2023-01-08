from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommandForm
from .models import Command
SUCCESS_URL = '/commands/'
CONTEXT_OBJECT = "commands"
FORM_CLASS = CommandForm
MODEL = Command
PATH_PREFIX ="commands"

class CommandListView(LoginRequiredMixin, ListView):
    model = MODEL
    context_object_name = CONTEXT_OBJECT
    template_name: str = f"{PATH_PREFIX}/index.html"
    login_url = '/login'

class CommandCreationView(LoginRequiredMixin, CreateView):
    template_name = f"{PATH_PREFIX}/add.html"
    model = MODEL
    success_url = SUCCESS_URL
    form_class = FORM_CLASS

class CommandUpdateView(LoginRequiredMixin, UpdateView):
    template_name: str = f"{PATH_PREFIX}/edit.html"
    model = MODEL
    success_url = SUCCESS_URL
    form_class = FORM_CLASS
   
class CommandDetailView(LoginRequiredMixin, DetailView):
    template_name = f"{PATH_PREFIX}/details.html"
    model = MODEL
    context_object_name = CONTEXT_OBJECT
    
class CommandDeleteView(LoginRequiredMixin, DeleteView):
    template_name = f"{PATH_PREFIX}/delete.html"
    model = MODEL
    context_object_name = CONTEXT_OBJECT
    success_url= SUCCESS_URL