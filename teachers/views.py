from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import request, HttpResponse

# Create your views here.
class Index(TemplateView):
    template_name = 'teachers/index.html'