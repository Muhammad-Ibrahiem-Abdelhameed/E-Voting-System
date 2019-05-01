from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

from .models import Voter, VoterVote, Candidate, Vote


def dashboard_view(request):
    return render(request, template_name='dashboard_home.html')

def logout_view(request):
    logout(request)
    return redirect('/accounts/login')


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def mobile_login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    national_id = request.data.get("national_id")

    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)

    votes = VoterVote.objects.filter(voter__national_id=national_id)
    content ={}
    for vote in votes:
        vote_info = Vote.objects.get(id=vote.id)
        candidates = Candidate.objects.filter(vote_id=vote.id).values('id', 'name', 'number_in_list', 'image')
        content[vote.id] = { 'title': vote_info.title, 'status' : vote_info.status ,
         'candidates' : [cand for cand in candidates]}
    return Response({'token': token.key, 'votes': content},
                    status=HTTP_200_OK)


@csrf_exempt
@api_view(["Post"])
@permission_classes((IsAuthenticated,))
def get_votes_from_mobile(request):

    
    return Response(data, status=HTTP_200_OK)

@csrf_exempt
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_votes(request):

    data = {
        'sample_data': 123
        }
    return Response(data, status=HTTP_200_OK)
