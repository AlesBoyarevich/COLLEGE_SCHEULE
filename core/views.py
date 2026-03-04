from django.shortcuts import render
from django.http import request, HttpResponse
from django.views.generic import View, TemplateView

# Create your views here.
class Index(TemplateView):
    template_name = 'index.html'
