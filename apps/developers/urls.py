from django.urls import path
from .views import index, single_profile, edit_profile

app_name = "developers"


urlpatterns = [
    path("", index, name="index"),
    path("developers/edit/", edit_profile, name="edit-profile"),
    path("developers/<str:username>/", single_profile, name="profile"),
]
