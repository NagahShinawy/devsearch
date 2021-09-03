from django.urls import path
from .views import projects, project, create_project


app_name = "projects"


urlpatterns = [
    path("", projects, name="projects"),
    path("create/", create_project, name="create_project"),
    path("<str:uuid>/", project, name="project"),
]
