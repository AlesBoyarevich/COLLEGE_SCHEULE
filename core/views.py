from django.shortcuts import render
from django.http import request, HttpResponse
from django.views.generic import View, TemplateView
from utils import mixins

# Create your views here.
class Index(mixins.CoreMixin, TemplateView):
    template_name = 'core/index.html'
