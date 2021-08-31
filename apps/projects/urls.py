from django.urls import path
from .views import projects, project


app_name = "projects"


urlpatterns = [
    path("", projects, name="projects"),
    path("<int:uuid>/", project, name="project"),
]
