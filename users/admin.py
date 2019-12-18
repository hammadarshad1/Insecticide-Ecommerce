from django.contrib import admin
from django.contrib.auth.models import User
from .models import *

admin.site.register(Profile)
admin.site.register(Gender)