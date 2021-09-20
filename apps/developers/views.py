from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile


def index(request):
    profiles = Profile.objects.all()
    return render(request, "developers/profiles.html", {"profiles": profiles})


@login_required
def single_profile(request, username):
    try:
        profile = Profile.objects.get(user__username__iexact=username)
    except ObjectDoesNotExist:
        return HttpResponse("Profile Not Created Yet")
    context = {
        "profile": profile,
    }
    return render(request=request, template_name="developers/account.html", context=context)