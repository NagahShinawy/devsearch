from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth, messages
from apps.core.constants.messages import InvalidCredentialsMessage


def signup(request):
    return render(request=request, template_name="accounts/signup.html")


def login(request):
    if request.method != 'POST':
        return render(request=request, template_name="accounts/login.html")
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = auth.authenticate(request, username=username, password=password)
    if user:
        auth.login(request, user)
        return redirect("developers:index")
    else:
        messages.error(request, InvalidCredentialsMessage.text)
        return render(request=request, template_name="accounts/login.html")



def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect("accounts:login")


def forgetpassword(request):
    return render(request=request, template_name="accounts/forgetpassword.html")
