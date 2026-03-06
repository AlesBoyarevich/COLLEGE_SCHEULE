from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, DetailView, CreateView, ListView, DeleteView, UpdateView
from . import forms
from . import models

# Teachers
class Teachers(ListView):
    template_name = 'teachers/list.html'
    model = forms.Teacher
    context_object_name = 'teachers'

class TeachersCreate(CreateView):
    template_name = 'form.html'
    model = models.Teacher
    form_class = forms.TeacherCreateForm
    success_url = reverse_lazy('teachers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            headline='TEACHERS CREATE FORM'
            )
        return context

class TeachersDelete(DeleteView):
    template_name = 'delete.html'
    model = models.Teacher
    success_url = reverse_lazy('teachers')
    pk_url_kwarg = 'id'
    context_object_name = 'teacher'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_object = context[self.context_object_name]
        context.update(
            object_name=f'{context_object.lastname} {context_object.name} {context_object.surname}',
            canel_url='teachers',
            )
        return context

class TeachersEdit(UpdateView):
    template_name = 'form.html'
    model = models.Teacher
    pk_url_kwarg = 'id'
    form_class = forms.TeacherCreateForm
    success_url = reverse_lazy('teachers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            headline='TEACHERS EDIT FORM'
            )
        return context
        

# Subjects
class Subjects(ListView):
    template_name = 'subjects/list.html'
    model = models.Subject
    context_object_name = 'subjects'

class SubjectsCreate(CreateView):
    template_name = 'form.html'
    model = models.Subject
    form_class = forms.SubjectCreateForm
    success_url = reverse_lazy('subjects')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            headline='SUBJECT CREATE FORM'
            )
        return context

class SubjectsDelete(DeleteView):
    template_name = 'delete.html'
    model = models.Subject
    success_url = reverse_lazy('subjects')
    pk_url_kwarg = 'id'
    context_object_name = 'subject'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            object_name=context[self.context_object_name].title,
            canel_url='subjects',
            )
        return context
    
class SubjectsEdit(UpdateView):
    template_name = 'form.html'
    model = models.Subject
    pk_url_kwarg = 'id'
    form_class = forms.SubjectCreateForm
    success_url = reverse_lazy('subjects')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            headline='SUBJECT EDIT FORM'
            )
        return context


# Groups
class Groups(ListView):
    template_name = 'groups/list.html'
    context_object_name = 'groups'

    def get_queryset(self):
        groups = models.Group.objects.all()
        group_dict: dict[str:list[str]] = {}

        for group in groups:
            pair = group.get_key_value_pair()
            values: list[str] = group_dict.get(pair[0], [])
            values.append(pair[1])
            group_dict[pair[0]] = values

        return group_dict
    
class GroupsCreate(CreateView):
    template_name = 'form.html'
    model = models.Group
    form_class = forms.GroupCreateForm
    success_url = reverse_lazy('groups')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            headline='GROUP CREATE FORM'
            )
        return context
    
class GroupsEdit(UpdateView):
    template_name = 'groups/form.html'
    model = models.Group
    form_class = forms.GroupCreateForm
    success_url = reverse_lazy('groups')


    def get_object(self):
        return get_object_or_404(models.Group, name=self.kwargs['group_name'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            headline='GROUP EDIT FORM'
            )
        return context
    
class GroupsDelete(DeleteView):
    template_name = 'delete.html'
    success_url = reverse_lazy('groups')
    context_object_name = 'group'
    
    def get_object(self):
        return get_object_or_404(models.Group, name=self.kwargs['group_name'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            canel_url='groups',
            object_name=f'{context[self.context_object_name].name}'
        )
        return context


# Schedule
class Schedule(TemplateView):
    template_name = 'schedule.html'


#TODO Object_name for edit form
#TODO Form validation