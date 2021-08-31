from django.contrib import admin
from .models import Car, Make


@admin.register(Car)
class CarModelAdmin(admin.ModelAdmin):
    date_hierarchy = "date_added"

    list_display = ("id", "name", "price", "date_added", "make")
    list_display_links = ("id", "name")
    search_fields = ("id", "name", "price")
    readonly_fields = ("id", )

    list_per_page = 10


@admin.register(Make)
class MakeModelAdmin(admin.ModelAdmin):

    list_display = ("id", "name", "factory_address", "email")
    list_per_page = 10
