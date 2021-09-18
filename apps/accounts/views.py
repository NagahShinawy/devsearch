from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from apps.core.constants.messages import InvalidCredentialsMessage, AlreadyExistMessage
from .forms import ProfileCreationForm


def signup(request):
    form = ProfileCreationForm()
    if request.method == "POST":
        form = ProfileCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if User.objects.filter(username__iexact=user.username).exists():
                messages.error(request, AlreadyExistMessage.text)
                return render(request=request, template_name="accounts/signup.html")
            user.save()
            auth.login(request, user=form.instance)
            return redirect("developers:index")
    return render(request=request, template_name="accounts/signup.html", context={"form": form})


def login(request):
    if request.user.is_authenticated:
        return redirect("developers:index")

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
    auth.logout(request)
    return redirect("accounts:login")


def forgetpassword(request):
    return render(request=request, template_name="accounts/forgetpassword.html")
