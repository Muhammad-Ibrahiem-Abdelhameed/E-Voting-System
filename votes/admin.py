from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Supervisor)
admin.site.register(Assistant)
admin.site.register(Vote)
admin.site.register(Result)
admin.site.register(Voter)