from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'access_token', 'refresh_token')


admin.site.register(User, UserAdmin)

admin.site.unregister(Group)
