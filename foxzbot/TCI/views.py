from typing import Any
from django.shortcuts import render
from .middleware import tci, StartTciClient
from django.views.generic import TemplateView, ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.apps import apps

class TCIStopView(View):
    template_name = 'TCI/index.html'
    def get(self,request):
        tci.disconnect()
        return render(request,self.template_name)

class TCIStartView(View):
    template_name = 'TCI/index.html'
    def get(self,request):
        tci.connect()
        return render(request,self.template_name)