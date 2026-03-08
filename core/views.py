from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, FormView, CreateView, RedirectView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from utils import mixins
from . import forms


# Auth
class Login(mixins.CoreMixin, FormView):
    template_name = 'core/login.html'
    form_class = forms.Login
    success_url = reverse_lazy('schedule')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['headline'] = 'LOGIN FORM'
        context['breadcramps'] = {'log in': reverse_lazy('login')}
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request=request, user=user)
                return HttpResponseRedirect(self.get_success_url())
        return self.form_invalid(form)

class Signin(mixins.CoreMixin, CreateView):
    template_name = 'form.html'
    model = User
    success_url = reverse_lazy('schedule')
    form_class = forms.Create

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['headline'] = 'SIGN IN FORM'
        context['breadcramps'] = {'log in': reverse_lazy('login'), 'sign in': 'signin'}
        return context
    
    def form_valid(self, form):
        password = form.cleaned_data['password']
        user: User = form.save(commit=False)
        user.set_password(make_password(password))
        user.save()
        login(self.request, user)
        return HttpResponseRedirect(self.success_url)

class Logout(mixins.CoreMixin, RedirectView):
    url = reverse_lazy('schedule')

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(self.url)
