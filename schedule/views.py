from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView
from . import forms
from . import models
from utils import mixins

# Teachers
class Teachers(mixins.TeachersMixin, ListView):
    template_name = 'teachers/list.html'
    model = forms.Teacher
    context_object_name = 'teachers'

class TeachersCreate(mixins.TeachersMixin, CreateView):
    template_name = 'form.html'
    model = models.Teacher
    form_class = forms.TeacherCreateForm
    success_url = reverse_lazy('teachers')
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            headline='TEACHERS CREATE FORM'
            )
        context['breadcramps']['create'] = reverse_lazy('teachers create')
        return context

class TeachersDelete(mixins.TeachersMixin, DeleteView):
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
        context['breadcramps']['delete'] = reverse_lazy('teachers delete', kwargs={'id': context_object.id})
        context['breadcramps'][str.join(' ', [context_object.lastname, context_object.name, context_object.surname])] = context['breadcramps']['delete']
        return context

class TeachersEdit(mixins.TeachersMixin, UpdateView):
    template_name = 'form.html'
    model = models.Teacher
    pk_url_kwarg = 'id'
    form_class = forms.TeacherCreateForm
    success_url = reverse_lazy('teachers')
    context_object_name = 'teacher'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            headline='TEACHERS EDIT FORM'
            )
        context_object = context[self.context_object_name]
        context['breadcramps']['edit'] = reverse_lazy('teachers edit', kwargs={'id': context_object.id})
        context['breadcramps'][str.join(' ', [context_object.lastname, context_object.name, context_object.surname])] = context['breadcramps']['edit']
        return context
        

# Subjects
class Subjects(mixins.SubjectsMixin, ListView):
    template_name = 'subjects/list.html'
    model = models.Subject
    context_object_name = 'subjects'

class SubjectsCreate(mixins.SubjectsMixin, CreateView):
    template_name = 'form.html'
    model = models.Subject
    form_class = forms.SubjectCreateForm
    success_url = reverse_lazy('subjects')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            headline='SUBJECT CREATE FORM'
            )
        context['breadcramps']['create'] = reverse_lazy('subjects create')
        return context

class SubjectsDelete(mixins.SubjectsMixin, DeleteView):
    template_name = 'delete.html'
    model = models.Subject
    success_url = reverse_lazy('subjects')
    pk_url_kwarg = 'id'
    context_object_name = 'subject'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = context[self.context_object_name]
        context.update(
            object_name=obj.title,
            canel_url='subjects',
            )
        context['breadcramps']['delete'] = reverse_lazy('subjects delete', kwargs={'id': obj.id})
        context['breadcramps'][obj.title] = context['breadcramps']['delete']
        return context
    
class SubjectsEdit(mixins.SubjectsMixin, UpdateView):
    template_name = 'form.html'
    model = models.Subject
    pk_url_kwarg = 'id'
    form_class = forms.SubjectCreateForm
    success_url = reverse_lazy('subjects')
    context_object_name = 'subject'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            headline='SUBJECT EDIT FORM'
            )
        obj = context[self.context_object_name]
        context['breadcramps']['edit'] = reverse_lazy('subjects edit', kwargs={'id': obj.id})
        context['breadcramps'][obj.title] = context['breadcramps']['edit']
        return context


# Groups
class Groups(mixins.GroupsMixin, ListView):
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
    
class GroupsCreate(mixins.GroupsMixin, CreateView):
    template_name = 'form.html'
    model = models.Group
    form_class = forms.GroupCreateForm
    success_url = reverse_lazy('groups')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            headline='GROUP CREATE FORM'
            )
        context['breadcramps']['create'] = reverse_lazy('groups create')
        return context
    
class GroupsEdit(mixins.GroupsMixin, UpdateView):
    template_name = 'groups/form.html'
    model = models.Group
    form_class = forms.GroupCreateForm
    success_url = reverse_lazy('groups')
    context_object_name = 'group'


    def get_object(self):
        return get_object_or_404(models.Group, name=self.kwargs['group_name'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = context[self.context_object_name]
        context.update(
            headline='GROUP EDIT FORM'
            )
        context['breadcramps']['edit'] = reverse_lazy('groups edit', kwargs={'group_name': obj.name})
        context['breadcramps'][obj.name] = context['breadcramps']['edit']
        return context
    
class GroupsDelete(mixins.GroupsMixin, DeleteView):
    template_name = 'delete.html'
    success_url = reverse_lazy('groups')
    context_object_name = 'group'
    
    def get_object(self):
        return get_object_or_404(models.Group, name=self.kwargs['group_name'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = context[self.context_object_name]
        context.update(
            canel_url='groups',
            object_name=f'{obj.name}'
        )
        context['breadcramps']['edit'] = reverse_lazy('groups edit', kwargs={'group_name': obj.name})
        context['breadcramps']['delete'] = reverse_lazy('groups delete', kwargs={'group_name': obj.name})
        context['breadcramps'][obj.name] = context['breadcramps']['delete']
        return context


# Schedule
class Schedule(mixins.ScheduleMixin, TemplateView):
    template_name = 'schedule.html'


#TODO Object_name for edit form
#TODO Form validation