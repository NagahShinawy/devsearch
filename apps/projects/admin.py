from django.contrib import admin
from .models import Project, Tag, Review


@admin.register(Project)
class ProjectModelAdmin(admin.ModelAdmin):
    date_hierarchy = "created"

    list_display = ("uuid", "title", "slug", "tags_list", "created", "updated")
    list_display_links = ("uuid", "title", "slug")
    search_fields = ("uuid", "title", "description", "tags__name", "reviews__body")
    readonly_fields = ("uuid", "slug")

    list_per_page = 10


@admin.register(Review)
class ReviewModelAdmin(admin.ModelAdmin):
    date_hierarchy = "created"

    list_display = ("uuid", "content", "value", "project", "created")
    search_fields = ("uuid", "body", "value")
    readonly_fields = ("uuid",)

    list_per_page = 10


@admin.register(Tag)
class TagModelAdmin(admin.ModelAdmin):
    date_hierarchy = "created"

    list_display = ("uuid", "name", "projects_list", "created")
    search_fields = ("uuid", "name")
    readonly_fields = ("uuid",)

    list_per_page = 10
