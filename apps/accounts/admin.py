from django.contrib import admin
from django.contrib.auth.models import User

admin.site.unregister(User)


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "is_superuser")
    search_fields = ("id", "username", "email")
    list_editable = ("username", )
    list_per_page = 5
