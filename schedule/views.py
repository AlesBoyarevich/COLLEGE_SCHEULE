from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from . import models
from utils import mixins

# Teachers
class Teachers(mixins.TeachersMixin, ListView):
    template_name = 'teachers/list.html'
    model = forms.Teacher
    context_object_name = 'teachers'

    headline = 'TEACHERS'

class TeachersCreate(LoginRequiredMixin, mixins.TeachersMixin, CreateView):
    template_name = 'form.html'
    model = models.Teacher
    form_class = forms.TeacherCreateForm
    success_url = reverse_lazy('teachers')

    headline = 'TEACHERS ADD'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcramps']['create'] = reverse_lazy('teachers create')
        return context

class TeachersDelete(LoginRequiredMixin, mixins.TeachersMixin, DeleteView):
    template_name = 'delete.html'
    model = models.Teacher
    success_url = reverse_lazy('teachers')
    pk_url_kwarg = 'id'
    context_object_name = 'teacher'

    headline = 'TEACHER DELETE CONFIRM'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_object = context[self.context_object_name]
        context.update(
            subheadline=f'of {context_object.lastname} {context_object.name} {context_object.surname}',
            canel_url='teachers',
            )
        context['breadcramps']['delete'] = reverse_lazy('teachers delete', kwargs={'id': context_object.id})
        context['breadcramps'][str.join(' ', [context_object.lastname, context_object.name, context_object.surname])] = context['breadcramps']['delete']
        return context

class TeachersEdit(LoginRequiredMixin, mixins.TeachersMixin, UpdateView):
    template_name = 'form.html'
    model = models.Teacher
    pk_url_kwarg = 'id'
    form_class = forms.TeacherCreateForm
    success_url = reverse_lazy('teachers')
    context_object_name = 'teacher'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_object = context[self.context_object_name]
        context_object_fullname = str.join(' ', [context_object.lastname, context_object.name, context_object.surname])
        context.update(
            headline='TEACHER EDIT FORM',
            subheadline='of ' + context_object_fullname,
            )
        context['breadcramps']['edit'] = reverse_lazy('teachers edit', kwargs={'id': context_object.id})
        context['breadcramps'][context_object_fullname] = context['breadcramps']['edit']

        context_file_name = context['form'].initial['image'].name.split('/')[-1]
        context['form'].fields['image'].label = f'TEACHER IMAGE (now {context_file_name}):'

        return context
    

# Subjects
class Subjects(mixins.SubjectsMixin, ListView):
    template_name = 'subjects/list.html'
    model = models.Subject
    context_object_name = 'subjects'

    headline = 'SUBJECTS'

class SubjectsCreate(LoginRequiredMixin, mixins.SubjectsMixin, CreateView):
    template_name = 'form.html'
    model = models.Subject
    form_class = forms.SubjectCreateForm
    success_url = reverse_lazy('subjects')

    headline = 'SUBJECTS ADD'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcramps']['create'] = reverse_lazy('subjects create')
        return context

class SubjectsDelete(LoginRequiredMixin, mixins.SubjectsMixin, DeleteView):
    template_name = 'delete.html'
    model = models.Subject
    success_url = reverse_lazy('subjects')
    pk_url_kwarg = 'id'
    context_object_name = 'subject'

    headline = 'SUBJECT DELETE CONFIRM'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = context[self.context_object_name]
        context.update(
            subheadline='of ' + obj.title,
            canel_url='subjects',
            )
        context['breadcramps']['delete'] = reverse_lazy('subjects delete', kwargs={'id': obj.id})
        context['breadcramps'][obj.title] = context['breadcramps']['delete']
        return context
    
class SubjectsEdit(LoginRequiredMixin, mixins.SubjectsMixin, UpdateView):
    template_name = 'form.html'
    model = models.Subject
    pk_url_kwarg = 'id'
    form_class = forms.SubjectCreateForm
    success_url = reverse_lazy('subjects')
    context_object_name = 'subject'

    headline = 'SUBJECT EDIT FORM'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = context[self.context_object_name]
        context.update(
            subheadline='of ' + obj.title
            )
        context['breadcramps']['edit'] = reverse_lazy('subjects edit', kwargs={'id': obj.id})
        context['breadcramps'][obj.title] = context['breadcramps']['edit']
        return context


# Groups
class Groups(mixins.GroupsMixin, ListView):
    template_name = 'groups/list.html'
    context_object_name = 'groups'

    headline = 'GROUPS'

    def get_queryset(self):
        groups = models.Group.objects.all()
        group_dict: dict[str:list[str]] = {}

        for group in groups:
            pair = group.get_key_value_pair()
            values: list[str] = group_dict.get(pair[0], [])
            values.append(pair[1])
            group_dict[pair[0]] = values

        return group_dict
    
class GroupsCreate(LoginRequiredMixin, mixins.GroupsMixin, CreateView):
    template_name = 'form.html'
    model = models.Group
    form_class = forms.GroupCreateForm
    success_url = reverse_lazy('groups')

    headline = 'GROUPS ADD'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcramps']['create'] = reverse_lazy('groups create')
        return context
    
class GroupsEdit(LoginRequiredMixin, mixins.GroupsMixin, UpdateView):
    template_name = 'form_and_delete.html'
    model = models.Group
    form_class = forms.GroupCreateForm
    success_url = reverse_lazy('groups')
    context_object_name = 'group'

    headline = 'GROUP EDIT FORM'


    def get_object(self):
        return get_object_or_404(models.Group, name=self.kwargs['group_name'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = context[self.context_object_name]
        context.update(
            subheadline='of ' + obj.name,
            )
        context['breadcramps']['edit'] = reverse_lazy('groups edit', kwargs={'group_name': obj.name})
        context['breadcramps'][obj.name] = context['breadcramps']['edit']
        context['delete_url'] = reverse_lazy('groups delete', kwargs={'group_name': obj.name})
        return context
    
class GroupsDelete(LoginRequiredMixin, mixins.GroupsMixin, DeleteView):
    template_name = 'delete.html'
    success_url = reverse_lazy('groups')
    context_object_name = 'group'

    headline = 'GROUP DELETE CONFIRM'
    
    def get_object(self):
        return get_object_or_404(models.Group, name=self.kwargs['group_name'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = context[self.context_object_name]
        context.update(
            canel_url='groups',
            subheadline=f'of {obj.name}'
        )
        context['breadcramps']['edit'] = reverse_lazy('groups edit', kwargs={'group_name': obj.name})
        context['breadcramps']['delete'] = reverse_lazy('groups delete', kwargs={'group_name': obj.name})
        context['breadcramps'][obj.name] = context['breadcramps']['delete']
        return context


# Schedule
class Schedule(mixins.ScheduleMixin, ListView):
    template_name = 'schedule/list.html'
    context_object_name = 'schedule'

    headline = 'SCHEDULE'

    def get_queryset(self):
        schedule: dict[str: dict[str: dict[str: Schedule]]] = {}
        days = models.Schedule.Day.choices
        times = models.Schedule.Time.choices
        if models.Group.objects.filter(name=self.request.GET.get('group')):
            groups = models.Group.objects.filter(name=self.request.GET['group'])
        else:
            groups = models.Group.objects.values_list('name', flat=True)

        schedules = models.Schedule.objects.all()

        for day in days:
            schedule[day[1]] = {}
            for group in groups:
                schedule[day[1]][group] = {}
                for time in times:
                    schedule[day[1]][group][time[1]] = schedules.filter(day=day[0], group__name=group, time=time[0]).first()

        return schedule

    def get_context_data(self, **kwargs):
        group =  self.request.GET.get('group')
        context = super().get_context_data(**kwargs)
        context['active'] = 'schedule'
        context['times'] = models.Schedule.Time.labels
        context['canel_filter'] = group != None
        if context['canel_filter']:
            context['breadcramps'][group] = reverse_lazy('schedule') + '?group=' + group
        return context

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class ScheduleCreate(LoginRequiredMixin, mixins.ScheduleMixin, CreateView):
    template_name = 'form.html'
    model = Schedule
    form_class = forms.ScheduleCreateForm
    success_url = reverse_lazy('schedule')

    headline = 'SCHEDULE ENTRY ADD'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcramps']['create'] = reverse_lazy('schedule create')

        return context
    
    def post(self, request, *args, **kwargs):
        self.object = None

        form = self.get_form()
        obj:models.Schedule = form.save(commit=False)

        query_1 = models.Schedule.objects.filter(group=obj.group, day=obj.day, time=obj.time).first()
        query_2 = models.Schedule.objects.filter(teacher=obj.teacher, day=obj.day, time=obj.time).first()
        if query_1 != None:
            form.add_error('group', error='This time is booked for this group')
        if query_2 != None:
            form.add_error('teacher', error='This time is booked for this teacher')
        
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ScheduleEdit(LoginRequiredMixin, mixins.ScheduleMixin, UpdateView):
    template_name = 'form_and_delete.html'
    model = models.Schedule
    form_class = forms.ScheduleCreateForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('schedule')
    context_object_name = 'schedule'

    headline = 'SCHEDULE ENTRY EDIT FORM'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj:models.Schedule = context[self.context_object_name]
        context['subheadline'] = 'of ' + obj.__str__()
        context['breadcramps']['edit'] = reverse_lazy('schedule edit', kwargs={'id': obj.id})
        context['breadcramps'][obj.__str__()] = context['breadcramps']['edit']
        context['delete_url'] = reverse_lazy('schedule delete', kwargs={'id': obj.id})
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        form = self.get_form()
        obj:models.Schedule = form.save(commit=False)

        query_1 = models.Schedule.objects.filter(group=obj.group, day=obj.day, time=obj.time).first()
        query_2 = models.Schedule.objects.filter(teacher=obj.teacher, day=obj.day, time=obj.time).first()
        if query_1 != None and query_1 != obj:
            form.add_error('group', error='This time is booked for this group')
        if query_2 != None and query_2 != obj:
            form.add_error('teacher', error='                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 This time is booked for this teacher')
        
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    
class ScheduleDelete(LoginRequiredMixin, mixins.ScheduleMixin, DeleteView):
    template_name = 'delete.html'
    model = models.Schedule
    success_url = reverse_lazy('schedule')
    pk_url_kwarg = 'id'
    context_object_name = 'schedule'

    headline = 'SCHEDULE DELETE CONFIRM'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = context[self.context_object_name]
        context.update(
            subheadline='of ' + obj.__str__(),
            canel_url='schedule',
            )
        context['breadcramps']['delete'] = reverse_lazy('schedule delete', kwargs={'id': obj.id})
        context['breadcramps'][obj] = context['breadcramps']['delete']
        return context
