from django.shortcuts import render
from .models import Profile


def index(request):
    profiles = Profile.objects.all()
    return render(request, "developers/profiles.html", {"profiles": profiles})
