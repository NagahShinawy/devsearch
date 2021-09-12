from importlib import import_module
from django.apps import AppConfig


class ProjectsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.projects"

    def ready(self):
        import_module("apps.core.signals")
        import_module("apps.projects.signals")
