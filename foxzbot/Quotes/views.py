from django.shortcuts import render
from .models import Quotes
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import QuoteForm
SUCCESS_URL = '/quotes'
CONTEXT_OBJECT = "Quotes"
FORM_CLASS = QuoteForm
MODEL = Quotes
PATH_PREFIX ="quotes"

class QuotesListView(LoginRequiredMixin, ListView):
    model = MODEL
    context_object_name = CONTEXT_OBJECT
    template_name: str = f"{PATH_PREFIX}/index.html"
    login_url = '/login'

class QuotesCreationView(LoginRequiredMixin, CreateView):
    template_name = f"{PATH_PREFIX}/add.html"
    model = MODEL
    success_url = SUCCESS_URL
    form_class = FORM_CLASS
   
class QuotesUpdateView(LoginRequiredMixin, UpdateView):
    template_name: str = f"{PATH_PREFIX}/edit.html"
    model = MODEL
    success_url = SUCCESS_URL
    form_class = FORM_CLASS
   
class QuotesDetailView(LoginRequiredMixin, DetailView):
    template_name = f"{PATH_PREFIX}/details.html"
    model = MODEL
    context_object_name = CONTEXT_OBJECT
    
class QuotesDeleteView(LoginRequiredMixin, DeleteView):
    template_name = f"{PATH_PREFIX}/delete.html"
    model = MODEL
    context_object_name = CONTEXT_OBJECT
    success_url= SUCCESS_URL