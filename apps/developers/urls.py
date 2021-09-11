from django.urls import path
from .views import index, single_profile

app_name = "developers"


urlpatterns = [
    path("", index, name="index"),
    path("developers/<str:username>/", single_profile, name="profile"),
]
