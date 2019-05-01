from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.edit import  UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from votes.models import VoterVote, Assistant, Supervisor

from .authorization_permission import *

class VoterVoteListView(AssistantRequiredMixin, ListView):
    model = VoterVote
    template_name = 'votervote/votervote_list.html'


class VoterVoteCreateView(AssistantRequiredMixin, CreateView):
    model = VoterVote
    template_name = 'votervote/votervote_create.html'
    fields = '__all__'

    success_url = '/votervote/list'
    def form_valid(self, form):
        return super().form_valid(form)

class VoterVoteDetailView(DetailView):
    model = VoterVote
    slug_field = 'national_id'
    template_name = 'voter/voter_detail.html'

class VoterUpdateView(UpdateView):
    model = VoterVote
    slug_field = 'national_id'
    template_name = 'voter/voter_update.html'

class VoterDeleteView(DeleteView):
    model = VoterVote
    slug_field = 'national_id'
    template_name = 'voter/voter_delete.html'

