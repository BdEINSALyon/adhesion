"""
For managing databases
"""
from django.contrib import admin
from .models import Membre, Depart

admin.site.register(Membre)
admin.site.register(Depart)