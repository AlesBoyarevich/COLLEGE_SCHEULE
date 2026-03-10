from django.core.exceptions import ValidationError
from django import forms
from .models import *


class TeacherCreateForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('name', 'lastname', 'surname', 'image')
        labels = {
            'name': 'TEACHER NAME:',
            'lastname': 'TEACHER LASTNAME:',
            'surname': 'SURNAME:',
            'image': 'TEACHER IMAGE:',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-name',
            }),
            'lastname': forms.TextInput(attrs={
                'class': 'form-lastname'
            }),
            'surname': forms.TextInput(attrs={
                'class': 'form-surname'
            }),
            "image": forms.FileInput(attrs={
                'class': 'form-file'
            }),
        }

class SubjectCreateForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('title', )
        labels = {
            'title': 'SUBJECT TITLE:',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-name'
            })
        }

class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name', )
        labels = {
            'name': 'GROUP NAME:',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-name'
            })
        }


class ScheduleCreateForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ('group', 'subject', 'teacher', 'day', 'time')
        labels = {
            'group': 'GROUP:',
            'subject': 'SUBJECT:',
            'teacher': 'TEACHER:',
            'day': 'DAY:',
            'time': 'TIME:'
        }
        widgets = {
            'group': forms.Select(attrs={
                'class': 'form-select'
            }),
            'subject': forms.Select(attrs={
                'class': 'form-select'
            }),
            'teacher': forms.Select(attrs={
                'class': 'form-select'
            }),
            'day': forms.Select(attrs={
                'class': 'form-select'
            }),
            'time': forms.Select(attrs={
                'class': 'form-select'
            })
        }
