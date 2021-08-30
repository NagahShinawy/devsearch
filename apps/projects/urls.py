from django.urls import path

from apps.projects.views import projects

app_name = "projects"

urlpatterns = [
    path("", projects, name="projects"),
]