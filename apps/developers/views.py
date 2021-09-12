from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile


def index(request):
    profiles = Profile.objects.all()
    return render(request, "developers/profiles.html", {"profiles": profiles})


def single_profile(request, username):
    if request.user.is_anonymous:
        return redirect("accounts:login")
    try:
        profile = Profile.objects.get(user__username__iexact=username)
    except ObjectDoesNotExist:
        return HttpResponse("Profile Not Created Yet")
    return render(request=request, template_name="developers/profile.html", context={"profile": profile})