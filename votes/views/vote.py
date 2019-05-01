from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from votes.models import Vote, Supervisor

from .authorization_permission import *


class VoteListView(SupervisorRequiredMixin, ListView):
    model = Vote
    template_name = 'vote/vote_list.html'

    def get_queryset(self):
        print(self.request.user.id)
        return Vote.objects.filter(supervisor_id= self.request.user.id)


class VoteCreateView(SupervisorRequiredMixin, CreateView):
    model = Vote
    template_name = 'vote/vote_create.html'
    fields = ['title', 'status', 'description','type_of_vote', 'start_date', 'end_date', 'devices' ]

    success_url = '/vote/list'

    def form_valid(self, form):
        form.instance.supervisor_id = self.request.user.id
        return super().form_valid(form)