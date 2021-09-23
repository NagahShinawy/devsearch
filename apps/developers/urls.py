from django.urls import path
from .views import index, single_profile, edit_profile, add_skill, edit_skill, delete_skill

app_name = "developers"


urlpatterns = [
    path("", index, name="index"),
    path("developers/edit/", edit_profile, name="edit-profile"),
    path("developers/<str:username>/add_skill/", add_skill, name="add_skill"),
    path("developers/<str:username>/edit_skill/<str:skill_title>/", edit_skill, name="edit_skill"),
    path("developers/<str:username>/delete_skill/<str:skill_title>/", delete_skill, name="delete_skill"),
    path("developers/<str:username>/", single_profile, name="profile"),
]
