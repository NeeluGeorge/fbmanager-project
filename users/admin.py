#django
from django.contrib import admin

# local
from .models import User

admin.site.register(User)