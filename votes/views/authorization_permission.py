from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from votes.models import VoterVote, Assistant, Supervisor

class SupervisorRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        is_staff = self.request.user.is_superuser or self.request.user.is_staff
        is_supervisor = Supervisor.objects.filter(user_id=self.request.user.id).exists()
        return is_staff or is_supervisor

class AssistantRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        is_staff = self.request.user.is_superuser or self.request.user.is_staff
        is_supervisor = Supervisor.objects.filter(user_id=self.request.user.id).exists()
        is_assistant = Assistant.objects.filter(user_id=self.request.user.id).exists()
        return is_staff or is_supervisor or is_assistant

