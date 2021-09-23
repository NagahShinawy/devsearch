from django.urls import path

from .views import forgetpassword, login, logout, signup

app_name = "accounts"


urlpatterns = [
    path("login/", login, name="login"),
    path("signup/", signup, name="signup"),
    path("logout/", logout, name="logout"),
    path("forgetpassword/", forgetpassword, name="forgetpassword"),
]
