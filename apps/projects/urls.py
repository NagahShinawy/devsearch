from django.urls import path
from .views import (
    list_projects,
    single_project,
    create_project,
    delete_project,
    update_project,
)


app_name = "projects"


urlpatterns = [
    path("", list_projects, name="projects"),
    path("create/", create_project, name="create"),
    path("<str:uuid>/", single_project, name="project"),
    path("delete/<str:uuid>/", delete_project, name="delete"),
    path("update/<str:uuid>/", update_project, name="update"),
]
