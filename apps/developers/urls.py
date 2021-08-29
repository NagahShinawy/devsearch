from django.urls import path
from .views import index

app_name = "developers"


urlpatterns = [
    path("", index, name="index"),
]
