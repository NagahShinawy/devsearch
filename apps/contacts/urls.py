from django.urls import path
from .views import inbox, message


app_name = "contacts"


urlpatterns = [
    path("", inbox, name="inbox"),
    path("message/", message, name="message"),
]
