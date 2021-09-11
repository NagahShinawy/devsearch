from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import Profile
from apps.core import utils


def index(request):
    profiles = Profile.objects.all()
    return render(request, "developers/profiles.html", {"profiles": profiles})


def single_profile(request, username):
    profile = Profile.objects.get(user__username__iexact=username)
    if profile is False:
        return HttpResponseNotFound("Not Found")

    return render(request=request, template_name="developers/profile.html", context={"profile": profile})