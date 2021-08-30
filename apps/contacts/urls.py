from django.urls import path
from .views import inbox


app_name = "contacts"


urlpatterns = [
    path("", inbox, name="inbox"),
]