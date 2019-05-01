from djongo import models
import djongo
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, Group, PermissionsMixin
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from django.contrib.auth.models import User

from .managers import *

# Inspector    
class Supervisor(models.Model):
    # id
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, db_column='user_id' )
    national_id = models.CharField(max_length=14, unique=True)

    class Meta:
        db_table = 'Supervisors'

    def __str__(self):
        return self.national_id


class Vote(models.Model):
    # id
    TYPES_CHOICES = (
    ('Election','Election'),
    ('Vote', 'Vote'),
    )

    DEVICES_CHOICES = (
    ('Phone','Phone'),
    ('Rasb', 'Rasb'),
    ('Phone and Rasb', 'Phone and Rasb'),
    )

    title = models.CharField(max_length=254)
    type_of_vote = models.CharField(max_length=10, choices=TYPES_CHOICES, default='Election')
    description = models.TextField()
    supervisor = djongo.models.ForeignKey(
        to= Supervisor,
        on_delete= models.CASCADE
    )
    status = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    devices = models.CharField(max_length=16, choices=DEVICES_CHOICES, default='Phone and Rasb')
    #objects = models.Manager()
    #objects = VoteManager()
    class Meta:
        db_table = 'Votes'

    def __str__(self):
        return self.title

# Admin
class Assistant(models.Model):

    user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, db_column='user_id' )
    national_id = models.CharField(max_length=14, unique=True)
    supervisor = models.ForeignKey(
        to= Supervisor,
        on_delete=models.CASCADE
    )
    votes = models.ArrayReferenceField(
        to=Vote
    )
    class Meta:
        db_table = 'Assistants'

    def __str__(self):
        return self.national_id

class Voter(models.Model):
    # id
    user_id = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True, db_column='user_id' )
    national_id = models.CharField(max_length=14, unique=True)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=14, blank=True)
    fingerprint = models.ImageField(null=True, blank=True)
    allow_phone = models.BooleanField(blank=True, null=True)

    region = models.CharField(max_length=20)

    #objects = models.Manager()
    
    class Meta:
        db_table = 'Voters'

    def __str__(self):
        return self.national_id

class VoterVote(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    #user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, db_column='user_id' )
    is_voted = models.BooleanField(default=False)
    class Meta:
        db_table = 'Voters_Votes'

class Candidate(models.Model):

    #candidate_id = models.IntegerField
    vote_id = models.ForeignKey(Vote, on_delete=models.CASCADE, db_column='vote_id' )
    name = models.CharField(max_length=40)
    number_in_list = models.IntegerField()
    image = models.ImageField(blank=True, null=True)

    result = models.IntegerField()
    class Meta:
        db_table = 'Candidates'

class Result(models.Model):

    vote_id = models.OneToOneField(Vote, on_delete=models.CASCADE, primary_key=True, db_column='vote_id' )
    result = models.TextField(null=True, blank=True)

    supervisor = djongo.models.ForeignKey(
        to= Supervisor,
        on_delete= models.CASCADE
    )

    class Meta:
        db_table = 'Results'

    def __str__(self):
        return self.result