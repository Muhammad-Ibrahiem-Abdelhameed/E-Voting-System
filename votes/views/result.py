from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from votes.models import Result, Supervisor

from .authorization_permission import *

class ResultListView(SupervisorRequiredMixin, ListView):
    model = Result
    template_name = 'result/result_list.html'

    def get_queryset(self):
        print(self.request.user.id)
        return Result.objects.filter(supervisor_id= self.request.user.id)

class ResultCreateView(SupervisorRequiredMixin, CreateView):
    model = Result
    template_name = 'result/result_create.html'
    fields = '__all__'

    success_url = '/result/create'

    def form_valid(self, form):

        return super().form_valid(form)