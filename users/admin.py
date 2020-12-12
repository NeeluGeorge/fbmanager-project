#django
from django.contrib import admin
# local
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
    # list_display = ('username', )
    # fieldsets = ((None, {
    #     "fields": ('fb_id', 'name', 'fb_token'),
    # }), )
