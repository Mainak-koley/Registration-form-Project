from django.contrib import admin

from .models import registration, login

admin.site.register(registration)

admin.site.register(login)
