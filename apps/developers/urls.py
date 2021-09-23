from django.urls import path

from .views import (add_skill, delete_skill, edit_profile, edit_skill, index,
                    single_profile)

app_name = "developers"


urlpatterns = [
    path("", index, name="index"),
    path("developers/edit/", edit_profile, name="edit-profile"),
    path("developers/<str:username>/add_skill/", add_skill, name="add_skill"),
    path("developers/<str:username>/edit_skill/<str:slug>/", edit_skill, name="edit_skill"),
    path("developers/<str:username>/delete_skill/<str:slug>/", delete_skill, name="delete_skill"),
    path("developers/<str:username>/", single_profile, name="profile"),
]
