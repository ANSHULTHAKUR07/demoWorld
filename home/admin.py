from django.contrib import admin
from .models import *
from django.contrib.sessions.models import Session



admin.site.register(ContactData)
admin.site.register(Session)
# Register your models here.
