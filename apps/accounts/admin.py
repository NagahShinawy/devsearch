from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


admin.site.unregister(User)


@admin.register(User)
class UserModelAdmin(UserAdmin):
    list_display = ("id", "username", "email", "is_superuser", "is_staff")
    search_fields = ("id", "username", "email")
    list_editable = ("username", "is_superuser", "is_staff")
    list_per_page = 5