from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django import forms
from votes.models import Result, Supervisor
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .authorization_permission import *

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserCreateView(AssistantRequiredMixin, CreateView):
    model = User
    template_name = 'user/user_create.html'
    #fields = ['username', 'password', 'email' ]
    form_class = UserRegisterForm
    success_url = '/user/create'

    def form_valid(self, form):
        return super().form_valid(form)  

"""
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserCreateForm
    template_name = 'user/user_create.html'
    
"""
