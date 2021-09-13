from django.urls import path
from .views import login, logout, signup, forgetpassword


app_name = "accounts"


urlpatterns = [
    path("login/", login, name="login"),
    path("signup/", signup, name="signup"),
    path("logout/", logout, name="logout"),
    path("forgetpassword/", forgetpassword, name="forgetpassword"),
]
