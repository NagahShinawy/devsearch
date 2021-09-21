from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile
from .forms import ProfileModelForm


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
    if profile.user == request.user:
        return render(request=request, template_name="developers/account.html", context=context)
    return render(request=request, template_name="developers/profile.html", context=context)


@login_required
def edit_profile(request):
    profile = request.user.profile
    form = ProfileModelForm(instance=profile)
    if request.method != "POST":
        return render(request=request, template_name="developers/profile_form.html", context={"form": form})

    form = ProfileModelForm(data=request.POST, instance=profile, files=request.FILES)
    if form.is_valid():
        form.save()
    return render(request=request, template_name="developers/account.html", context={"profile": profile})

