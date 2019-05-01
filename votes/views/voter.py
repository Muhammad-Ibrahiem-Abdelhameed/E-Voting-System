from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.edit import  UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from votes.models import Voter

from .authorization_permission import *

class VoterListView(AssistantRequiredMixin, ListView):
    model = Voter
    template_name = 'voter/voter_list.html'

class VoterDetailView(AssistantRequiredMixin, DetailView):
    model = Voter
    slug_field = 'national_id'
    template_name = 'voter/voter_detail.html'

class VoterCreateView(AssistantRequiredMixin, CreateView):
    model = Voter
    template_name = 'voter/voter_create.html'
    fields = '__all__'

    success_url = '/voter/list'
    def form_valid(self, form):
        return super().form_valid(form)

class VoterUpdateView(AssistantRequiredMixin, UpdateView):
    model = Voter
    slug_field = 'national_id'
    template_name = 'voter/voter_update.html'

class VoterDeleteView(AssistantRequiredMixin, DeleteView):
    model = Voter
    slug_field = 'national_id'
    template_name = 'voter/voter_delete.html'

"""
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class AdminStaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

class AdminView(AdminStaffRequiredMixin, generic.ListView):
    model = get_user_model()
    fields = ['first_name', 'username', 'is_active']
    template_name = 'users/admin.html'

class AdminUpdateView(AdminStaffRequiredMixin, UpdateView):
    model = get_user_model()
    fields = ['is_active']
    template_name = 'users/user_update.html'
    success_url = reverse_lazy('users:admin')

"""