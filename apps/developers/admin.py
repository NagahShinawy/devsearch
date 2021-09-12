from django.contrib import admin
from .models import Profile, Skill


@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ("uuid", "get_username", "get_email", "github", "linkedin", "short_intro", "location")
    list_display_links = ("uuid", "get_username", "get_email", "linkedin")
    list_editable = ("short_intro", "location")
    search_fields = ("uuid", "user__username", "user__first_name", "user__last_name", "user__email")
    list_select_related = ("user", )

    def get_username(self, obj):
        return obj.user.username

    def get_email(self, obj):
        return obj.user.email

    # get_username.admin_order_field = 'author'  # Allows column order sorting
    get_username.short_description = 'username'  # Renames column head
    get_email.short_description = 'email'  # Renames column head


@admin.register(Skill)
class SkillModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created", "updated", "description")
    list_editable = ("title", "description")