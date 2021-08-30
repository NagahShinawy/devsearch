from django.shortcuts import render
from django.http import HttpResponse


def profile(request):
    return render(request=request, template_name="accounts/profile.html")


def signup(request):
    return render(request=request, template_name="accounts/signup.html")


def login(request):
    return render(request=request, template_name="accounts/login.html")


def logout(request):
    return HttpResponse("You are logged out")


def forgetpassword(request):
    return render(request=request, template_name="accounts/forgetpassword.html")
