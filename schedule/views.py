from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Teachers(TemplateView):
    template_name = 'teachers.html'


class Subjects(TemplateView):
    template_name = 'subjects.html'


class Groups(TemplateView):
    template_name = 'groups.html'


class Schedule(TemplateView):
    template_name = 'schedule.html'