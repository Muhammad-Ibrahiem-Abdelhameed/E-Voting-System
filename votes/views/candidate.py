from django.views.generic import DetailView, ListView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.forms import modelformset_factory

from votes.models import Candidate, Supervisor, Assistant
from django.shortcuts import render, redirect
from django import forms
from django.forms import formset_factory

from .authorization_permission import *

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['vote_id', 'name', 'number_in_list', 'image']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('userid', None)
        super().__init__(*args, **kwargs)
        # restrict the queryset of 'Turma'
        self.fields['vote_id'].queryset = self.fields['vote_id'].queryset.filter(
            supervisor_id=user)



class CandidateListView(AssistantRequiredMixin, ListView):
    model = Candidate
    template_name = 'candidate/candidate_list.html'

    def get_queryset(self):
        print(self.request.user.id)
        return Candidate.objects.filter(vote_id__supervisor_id= self.request.user.id)


class CandidateCreateView(SupervisorRequiredMixin, CreateView):
    #model = Candidate
    template_name = 'candidate/candidate_create.html'
    #fields = ['vote_id', 'name', 'number_in_list', 'image']
    form_class = CandidateForm
    success_url = '/candidate/list'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['userid'] = self.request.user.id
        return kwargs
    def form_valid(self, form):
        return super().form_valid(form)

class CandidateUpdateView(SupervisorRequiredMixin, UpdateView):
    model = Candidate
    fields = ['vote_id', 'name', 'number_in_list', 'image']
    template_name = 'candidate/candidate_update.html'
    paginate_by = 1
    success_url = '/candidate/list'
    

"""
class CandidateForm(forms.Form):
    vote_id = forms.ChoiceField(
        label='Name',
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': 'Vote_id'
        })
    )
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Name here'
        })
    )
    
    number_in_list = forms.CharField(
        label='Number in List',
        widget=forms.CharField(attrs={})
    )

    image = forms.CharField(
        label='Image',
        widget=forms.ImageField(attrs={})
    )
    

CandidateFormset = formset_factory(CandidateForm, extra=1)


def create_book_normal(request):
    template_name = 'candidate/candidate_create.html'
    heading_message = 'Formset Demo'
    if request.method == 'GET':
        formset = CandidateFormset(request.GET or None)
    elif request.method == 'POST':
        formset = CandidateFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                # extract name from each form and save
                vote_id = form.cleaned_data.get('vote_id')
                name = form.cleaned_data.get('name')
                number_in_list = form.cleaned_data.get('number_in_list')
                image = form.cleaned_data.get('image')
                # save book instance
                if name:
                    Candidate(vote_id=vote_id, name= name, number_in_list=number_in_list, image=image ).save()
            # once all books are saved, redirect to book list view
            return redirect('/candidate/candidate_list')
    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
    })
"""
"""
class CreateAddView(FormView):
    success_url = reverse_lazy('candidate/list')
    form_class = modelformset_factory(
        Candidate,
        fields=[ 'vote_id','name', 'number_in_list', 'image'],
        extra=3
    )
    template_name = 'candidate/candidate_create.html'

    def get_form_kwargs(self):
        kwargs = super(CreateAddView, self).get_form_kwargs()
        kwargs["queryset"] = Candidate.objects.none()
        return kwargs

    def form_valid(self, form):
        for sub_form in form:
            if sub_form.has_changed():
                sub_form.save()

        return super(CreateAddView, self).form_valid(form)

"""