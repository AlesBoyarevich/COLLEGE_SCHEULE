from django import forms
from django.contrib.auth.models import User


class Login(forms.Form):
    username = forms.CharField(label='USERNAME:', widget=forms.TextInput(attrs={
        'class': 'form___field-name',
        'placeholder': 'Enter a username, for example: SashaTopchic2010'
    }))
    password = forms.CharField(label='PASSWORD:', widget=forms.PasswordInput(attrs={
        'class': 'form___field-password',
        'placeholder': 'Enter a password'
    }))


class Create(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form___field-name',
                'placeholder': 'Enter a username, for example: SashaTopchic2010'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form___field-name',
                'placeholder': 'Enter a first name, for example: Sasha'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form___field-name',
                'placeholder': 'Enter a last name, for example: Dedov'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form___field-email',
                'placeholder': 'Enter a email, for example: sashadedov@gmail.com'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form___field-password',
                'placeholder': 'Enter a password'
            }),
        }
        labels = {
            'username': 'USERNAME:',
            'first_name': 'FIRSTNAME:',
            'last_name': 'LASTNAME:',
            'email': 'EMAIL:',
            'password': 'PASSWORD:'
        }
