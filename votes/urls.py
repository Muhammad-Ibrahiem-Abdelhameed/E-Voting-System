from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from datetime import datetime

from .views import *
from .forms import *

import votes.aviews

urlpatterns = [

    path('dashboard/', votes.aviews.dashboard_view, name='dashboard_view'),

    path('', VoterListView.as_view() ),

    path('user/create', UserCreateView.as_view() ),


    path('voter/list', VoterListView.as_view() ),
    path('voter/create', VoterCreateView.as_view() ),

    path('vote/list', VoteListView.as_view() ),
    path('vote/create', VoteCreateView.as_view() ),

    path('votervote/list', VoterVoteListView.as_view() ),
    path('votervote/create', VoterVoteCreateView.as_view() ),

    path('candidate/create', CandidateCreateView.as_view(), name='candidate_create' ),
    path('candidate/list', CandidateListView.as_view(), name='candidate_list' ),
    path('candidate/update/<int:pk>', CandidateUpdateView.as_view(), name='candidate_update'),
    #path('candidate/create', create_book_normal ),
    #path('candidate/create', create_book_normal ),
    #path('votervote/create', VoterVoteCreateView.as_view() ),

    #path('votervote/list', VoterVoteListView.as_view() ),
    path('result/create', ResultCreateView.as_view() ),

    #path('phase/edit/<int:id>', PhaseUpdateView.as_view(), name='phase-edit'),

    path('accounts/login/',
        auth_views.LoginView.as_view(template_name='user/login.html'),
        {
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    path('logout', votes.aviews.logout_view, name='logout_view'),

    path('api/mobile/login', votes.aviews.mobile_login),
    path('api/mobile/votemobile', votes.aviews.get_votes_from_mobile),
    path('api/mobile/sampleapi', votes.aviews.get_votes),

]