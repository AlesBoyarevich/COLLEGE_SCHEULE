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
                'class': 'form___field-name',
                'placeholder': 'Enter a name, for example: Olga'
            }),
            'lastname': forms.TextInput(attrs={
                'class': 'form___field-name',
                'placeholder': 'Enter a last name, for example: Krutko'
            }),
            'surname': forms.TextInput(attrs={
                'class': 'form___field-name',
                'placeholder': 'Enter a surname, for example: Vladimirovna'
            }),
            "image": forms.FileInput(attrs={
                'class': 'form___field-file',
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
                'class': 'form___field-name',
                'placeholder': 'Enter a title, for example: Math'
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
                'class': 'form___field-name',
                'placeholder': 'Enter a name (on any language and registr), for example: 5K9791 or 2к9394'
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
                'class': 'form___field-select',
            }),
            'subject': forms.Select(attrs={
                'class': 'form___field-select'
            }),
            'teacher': forms.Select(attrs={
                'class': 'form___field-select'
            }),
            'day': forms.Select(attrs={
                'class': 'form___field-select'
            }),
            'time': forms.Select(attrs={
                'class': 'form___field-select'
            })
        }
