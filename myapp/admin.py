from django.contrib import admin
from .models import User,Video,UserPassword

admin.site.register([User,Video,UserPassword])
