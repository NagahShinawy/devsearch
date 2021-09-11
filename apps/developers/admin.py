from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ("uuid", "get_username", "get_email", "github", "linkedin", "short_intro", "location")
    list_display_links = ("uuid", "get_username", "get_email", "linkedin")
    list_editable = ("short_intro", "location")
    list_select_related = ("user", )

    def get_username(self, obj):
        return obj.user.username

    def get_email(self, obj):
        return obj.user.email

    # get_username.admin_order_field = 'author'  # Allows column order sorting
    get_username.short_description = 'username'  # Renames column head
    get_email.short_description = 'email'  # Renames column head
