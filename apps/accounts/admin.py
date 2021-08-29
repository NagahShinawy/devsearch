from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


admin.site.unregister(User)


@admin.register(User)
class UserModelAdmin(UserAdmin):
    list_display = ("id", "username", "email", "is_superuser")
    search_fields = ("id", "username", "email")
    list_editable = ("username",)
    list_per_page = 5
