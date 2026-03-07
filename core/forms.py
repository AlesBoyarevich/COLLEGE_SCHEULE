from django import forms
from django.contrib.auth.models import User


class Login(forms.Form):
    username = forms.CharField(max_length=100, label='USERNAME:', widget=forms.TextInput(attrs={
        'class': 'form-name'
    }))
    password = forms.CharField(max_length=100, label='PASSWORD:', widget=forms.PasswordInput(attrs={
        'class': 'form-password'
    }))


class Create(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-name'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-email'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-password'
            }),
        }
        labels = {
            'username': 'USERNAME:',
            'first_name': 'FIRSTNAME:',
            'last_name': 'LASTNAME:',
            'email': 'EMAIL:',
            'password': 'PASSWORD:'
        }
