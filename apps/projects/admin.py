from django.contrib import admin
from .models import Project, Task


@admin.register(Project)
class ProjectModelAdmin(admin.ModelAdmin):
    date_hierarchy = "created"

    list_display = ("uuid", "title", "slug", "created", "updated")
    list_display_links = ("uuid", "title", "slug")
    search_fields = ("uuid", "title", "description")
    readonly_fields = ("uuid", "slug")

    list_per_page = 10


admin.site.register(Task)
